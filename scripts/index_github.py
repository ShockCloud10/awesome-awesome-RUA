#!/usr/bin/env python3
"""Index already cloned awesome repositories without executing their code."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-11-23"
SELECTED = [
    ("kairunwen/Awesome-Robot-Use-Agent", "核心 RUA", "MIT", "直接围绕 Robot Use Agent 汇集论文、博客、工具、基准和社交演示，是本次资料的首要入口。"),
    ("zjwzcx/Awesome-Astra-Embodied-AI", "核心 Astra", None, "聚焦 GPT-6 Astra 的具身工作流，区分真机、仿真、策略调用、数据回放和训练环境。"),
    ("harooos/awesome-coding-agents-for-robot-learning", "核心 coding agent", "MIT", "围绕 coding agent 操作机器人、生成策略代码、构建环境、评估和改进策略组织资料。"),
    ("benchflow-ai/awesome-embodied-agents", "核心 agent policy", "CC0-1.0", "覆盖 agent 作为机器人策略的执行接口、模型与评测；条目附有评测条件和实现链接。"),
    ("chonghanqin/Awesome-Agentic-Robots", "核心 agentic robotics", "MIT", "Towards Agentic Robots 综述配套仓库，按模型、数据、环境和执行框架组织研究。"),
    ("Lin-Murphy/Awesome-Robot-Agents", "核心机械臂 agent", "MIT", "聚焦机器人操作，记录模型决策、执行接口、实现和演示的来源，包含 Astra 实机项目。"),
    ("GT-RIPL/Awesome-LLM-Robotics", "基础 LLM robotics", "BSD-3-Clause", "汇总语言与多模态模型在机器人推理、规划、操作、导航及强化学习中的研究。"),
    ("zchoi/Awesome-Embodied-Robotics-and-Agent", "扩展 embodied agents", "Apache-2.0", "覆盖 VLM、LLM、VLA、规划、导航及自演化等具身研究，也包含部分游戏和数字环境工作。"),
    ("Neal2020GitHub/awesome-embodied-agents", "扩展 embodied agents", "MIT", "从记忆、推理、规划、主动感知、导航和操作等维度整理 VLM/LLM 具身 agent。"),
    ("cagbal/awesome-foundation-models-for-robotics", "基础模型", None, "按模型整理机器人基础模型及输入输出模态，便于补充 VLA 与通用 agent 的技术背景。维护者提示条目可能含 AI 辅助整理错误。"),
    ("keon/awesome-physical-ai", "基础模型与 Physical AI", "CC0-1.0", "覆盖 VLA、世界模型、动作表示和机器人基础模型，用作相邻技术路线的文献入口。"),
]


def git(path, *args):
    return subprocess.check_output(["git", "-C", str(path), *args], text=True).strip()


def main():
    records = []
    for i, (name, category, license_id, summary) in enumerate(SELECTED, 1):
        path = ROOT / "github" / "repos" / name.replace("/", "__")
        readme = path / "README.md"
        if not readme.is_file():
            raise RuntimeError(f"Clone missing README: {name}")
        remote = git(path, "remote", "get-url", "origin")
        if remote.removesuffix(".git").lower() != f"https://github.com/{name}".lower():
            raise RuntimeError(f"Unexpected remote: {name}")
        status = git(path, "status", "--porcelain")
        if status:
            raise RuntimeError(f"Working tree changed: {name}")
        rec = dict(id=f"github-{i:03}", title=name, url=f"https://github.com/{name}",
                   platform="github", author=name.split("/")[0], accessed_at=DATE,
                   category=category, summary_zh=summary, evidence_status="local_clone_readme_verified",
                   evidence_urls=[f"https://github.com/{name}"],
                   local_path=str(path.relative_to(ROOT)), readme_path=str(readme.relative_to(ROOT)),
                   clone_type=("shallow" if git(path, "rev-parse", "--is-shallow-repository") == "true" else "full"), commit=git(path, "rev-parse", "HEAD"),
                   commit_date=git(path, "log", "-1", "--format=%cI"),
                   branch=git(path, "branch", "--show-current"), remote=remote,
                   license=license_id, license_files=[p.name for p in path.iterdir() if p.is_file() and p.name.lower().startswith(("license", "copying"))],
                   readme_sha256=hashlib.sha256(readme.read_bytes()).hexdigest(),
                   limitations="仓库清单中的每项研究未逐一复现；仓库下载成功与其研究结果得到独立验证是不同事项。" + (" 未在仓库根目录发现许可证文件。" if license_id is None else ""))
        records.append(rec)
        (ROOT / "github" / "metadata" / (name.replace("/", "__") + ".json")).write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "github" / "records.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    lines = ["# RUA 相关 awesome 仓库", "", f"采集日期：{DATE}。收录 {len(records)} 个仓库，按相关性排列。上游以 Git 子模块固定版本，首次采集使用 depth 1 浅克隆。在线链接指向所记录提交的 README，本地文件在下表所示目录。", "", "| 仓库固定版本 | 本地目录 | 范围 | 用途 |", "| --- | --- | --- | --- |"]
    for r in records:
        local = Path(r["local_path"]).relative_to("github").as_posix()
        snapshot = f"{r['url']}/blob/{r['commit']}/README.md"
        lines.append(f"| [{r['title']}]({snapshot}) · [上游]({r['url']}) | `{local}` | {r['category']} | {r['summary_zh']} |")
    lines += ["", "## 快照与使用", "", "records.json 和 metadata/ 保存 remote、commit、提交时间、README SHA256 与许可证信息。仓库提交时间和本次采集时间分别保留，不互相替代；研究发布日期请查看上游条目。", "", "在资料库根目录执行 `git submodule update --init --recursive`，即可取得当前固定版本的全部上游仓库。每个仓库的 README.md 可在对应本地目录打开。", "", "这里只下载和阅读资料；没有安装依赖、运行仓库程序或下载模型权重。第三方仓库保留各自许可证。", "", "主动更新上游时，在该子模块目录切换到所需分支并拉取；然后返回资料库根目录，依次运行 `python3 scripts/index_github.py` 和 `python3 scripts/build_catalog.py`，并将子模块的新提交指针与索引一起提交。", ""]
    (ROOT / "github" / "README.md").write_text("\n".join(lines))
    print(f"Indexed {len(records)} clean shallow clones")


if __name__ == "__main__":
    main()
