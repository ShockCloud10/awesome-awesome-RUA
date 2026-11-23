#!/usr/bin/env python3
"""Build local navigation and validate collected records and note links."""
import collections
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
GROUPS = [("github", "GitHub awesome 仓库"), ("x", "X 与 Twitter 帖子"), ("reddit", "Reddit 帖子"), ("zhihu", "知乎文章与帖子"), ("blogs", "技术博客与研究文章")]


def normalized_url(url):
    p = urlsplit(url)
    host = p.netloc.lower().removeprefix("www.")
    if host == "twitter.com":
        host = "x.com"
    return urlunsplit(("https", host, p.path.rstrip("/"), "", ""))


def note_path(group, record):
    if group == "github":
        return record["readme_path"]
    for key in ("note_file", "local_file", "local_path", "file"):
        value = record.get(key)
        if value and str(value).endswith(".md"):
            path = Path(value)
            if (ROOT / path).is_file():
                return path.as_posix()
            if (ROOT / group / path).is_file():
                return (Path(group) / path).as_posix()
    matches = [p for p in (ROOT / group).rglob("*.md") if p.stem == record["id"] or p.stem.startswith(record["id"] + "-") or p.stem.startswith(record["id"] + "_")]
    if len(matches) != 1:
        raise ValueError(f"Cannot identify note for {group}/{record['id']}: {matches}")
    return matches[0].relative_to(ROOT).as_posix()


def main():
    catalog = []
    count = {}
    evidence = {}
    ids = set()
    for group, label in GROUPS:
        records = json.loads((ROOT / group / "records.json").read_text())
        assert isinstance(records, list), group
        count[group] = len(records)
        evidence[group] = dict(collections.Counter(r["evidence_status"] for r in records))
        urls = set()
        for r in records:
            assert r["id"] not in ids, r["id"]
            ids.add(r["id"])
            url = normalized_url(r["url"])
            assert url not in urls, f"Duplicate URL in {group}: {url}"
            urls.add(url)
            assert r["summary_zh"] and r["evidence_urls"], r["id"]
            local = note_path(group, r)
            assert (ROOT / local).is_file(), local
            catalog.append(dict(id=r["id"], title=r.get("title_zh") or r["title"], url=r["url"],
                                platform=group, local_note=local, models=r.get("models", []),
                                tags=r.get("tags", []), evidence_status=r["evidence_status"]))
    (ROOT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    stats = dict(accessed_at="2026-11-23", timezone="Asia/Hong_Kong", counts=count,
                 total=len(catalog), evidence_status_counts=evidence,
                 checks=["JSON 可解析", "条目 ID 唯一", "每平台主链接去重", "本地笔记存在", "每条都有摘要与证据链接"])
    (ROOT / "collection_stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n")
    lines = ["# RUA 机器人控制资料库", "", "围绕 Robot Use Agent（RUA）、coding agent 以及基础模型控制机器人，收集 GitHub awesome 清单、X、Reddit、知乎和技术博客。采集日期：2026 年 11 月 23 日（Asia/Hong_Kong）。", "", "## 分类入口", "", "| 资料类别 | 数量 | 本地入口 |", "| --- | ---: | --- |"]
    for group, label in GROUPS:
        lines.append(f"| {label} | {count[group]} | [{group}/README.md]({group}/README.md) |")
    lines += ["", "GitHub 保存的是实际仓库浅克隆；帖子和博客保存的是原始链接、中文摘要、模型与机器人信息、控制方式及来源核实状态。视频没有下载，也没有把演示视频视为已独立复现的实验。", "", "访问限制：15 条 X 原帖均未直接读取，分别通过项目页、公开镜像、聚合页或搜索摘要收集；10 条知乎资料中 9 条仅获得搜索索引摘要。每条记录保留具体证据等级。", "", "## 建议阅读顺序", "", "1. [Awesome Robot Use Agent](github/repos/kairunwen__Awesome-Robot-Use-Agent/README.md)：从 RUA 总览进入论文、工具、基准和社区演示。", "2. [Awesome Astra Embodied AI](github/repos/zjwzcx__Awesome-Astra-Embodied-AI/README.md)：聚焦 Astra，区分真机、仿真、策略调用和训练工作流。", "3. [Coding Agents for Robot Learning](github/repos/harooos__awesome-coding-agents-for-robot-learning/README.md) 与 [BenchFlow Embodied Agents](github/repos/benchflow-ai__awesome-embodied-agents/README.md)：追踪 agent 与机器人执行接口。", "4. [博客索引](blogs/README.md)：阅读一手研究文章和项目方法说明；再结合 [X](x/README.md)、[Reddit](reddit/README.md) 和 [知乎](zhihu/README.md) 查看演示与讨论。", "", "## 关键词导航", "", "模型名称沿用来源中的写法。Astra、Opus、Fable 作为不同关键词保留，不根据简称推断未明确披露的型号或版本。", ""]
    for label, pattern in [("Astra", r"astra"), ("Opus", r"opus"), ("Fable", r"fable"), ("Gemini", r"gemini"), ("机器人接口与工具调用", r"mcp|tool.use|ros|harness")]:
        selected = [r for r in catalog if r["platform"] != "github" and re.search(pattern, " ".join([r["title"], *r["models"], *r["tags"]]), re.I)]
        lines += [f"### {label}", ""]
        for r in selected:
            title = r["title"].replace("[", "(").replace("]", ")")
            lines.append(f"- [{title}]({r['local_note']}) · {r['platform']}")
        if not selected:
            lines.append("详见各平台索引中的模型字段。")
        lines.append("")
    lines += ["## 如何理解资料", "", "真机操作、仿真任务、高层规划、工具调用和学习到的 VLA 策略处于不同层次。某个模型能生成机械臂控制程序，并不表示它直接在电机伺服频率下输出控制信号；具体以每条记录的 control_layer 和 limitations 为准。", "", "page_read 等状态表示读取到网页内容；project_crosschecked 或 mirror_post_read 表示使用项目页或公开镜像辅助核对；snippet_only 表示只获得搜索索引摘要。它们描述来源可见性，不代表独立验证作者的实验结论。不同目录的状态细分见各自 README。", "", "搜索未找到或访问受限不等于相关工作不存在。未确认候选保留在各目录的 candidates.json，未计入主条目数；检索关键词与来源线索保留在 search_log.json。主记录按 URL 去重，同一项目在不同平台的帖子仍分别保存，数量不等于独立项目数量。", "", "## 文件与后续整理", "", "- 每类 records.json：完整结构化记录。", "- catalog.json：跨平台链接目录，包含本地笔记路径、模型和标签。", "- collection_stats.json：条目统计与检查结果。", "- github/metadata/：每个仓库的 commit、remote、README SHA256 和许可证信息。", "- scripts/index_github.py：重新检查已经下载的仓库并生成索引。", "- scripts/build_catalog.py：重新生成总导航并检查记录及本地链接。", "", "网页全文和媒体未批量转载，原始内容请通过每条笔记的来源链接访问。第三方仓库保留原许可证；上游未注明许可证的仓库已在元数据中注明。", ""]
    lines += ["## 下载全部资料", "", "本项目使用 Git 子模块记录 11 个上游 awesome 仓库及其固定提交。完整下载命令：", "", "```bash", "git clone --recurse-submodules https://github.com/ShockCloud10/awesome-awesome-RUA.git", "```", "", "已经克隆主仓库时，在根目录执行 `git submodule update --init --recursive`。GitHub 下载 ZIP 不包含子模块内容；独立笔记、索引和 JSON 保存在主仓库。", ""]
    text = "\n".join(lines)
    for r in json.loads((ROOT / "github" / "records.json").read_text()):
        text = text.replace(f"({r['readme_path']})", f"({r['url']}/blob/{r['commit']}/README.md)")
    (ROOT / "README.md").write_text(text)
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
