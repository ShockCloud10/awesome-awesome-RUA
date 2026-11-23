#!/usr/bin/env python3
"""Build local navigation and validate collected records and note links."""
import collections
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
GROUPS = [("github", "GitHub awesome repositories"), ("x", "X / Twitter posts"), ("reddit", "Reddit posts"), ("zhihu", "Zhihu articles and discussions"), ("blogs", "Technical blogs and research articles")]
PLATFORM_LABELS = {"x": "X", "reddit": "Reddit", "zhihu": "Zhihu", "blogs": "Blog"}


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
    titles_en = json.loads((ROOT / "scripts" / "readme_titles_en.json").read_text())
    lines = [
        "# awesome-awesome-RUA", "",
        "A curated collection of awesome lists, community posts, and research blogs about **Robot-Use Agents (RUA)**: coding agents and foundation models that control robots through perception, planning, tools, and execution feedback.", "",
        "This homepage is in English; the individual research notes and category indexes are currently in Chinese.", "",
        "## Browse the collection", "",
        "| Category | Entries | Index |", "| --- | ---: | --- |",
    ]
    for group, label in GROUPS:
        lines.append(f"| {label} | {count[group]} | [{group}/README.md]({group}/README.md) |")
    lines += [
        "", f"**{len(catalog)} entries in total.** Upstream repositories are pinned as Git submodules. Posts and blogs have source links, Chinese summaries, model and robot details, control interfaces, and evidence status. Videos are not archived, and reported demonstrations have not been independently reproduced.", "",
        "**Access limitations:** All 15 X posts were inaccessible on X itself; their records rely on project pages, public mirrors, aggregation pages, or search snippets. Nine of the 10 Zhihu entries were available only through search snippets. Each record identifies its evidence level.", "",
        "## Start here", "",
        "1. [Awesome Robot Use Agent](github/repos/kairunwen__Awesome-Robot-Use-Agent/README.md): an overview of RUA papers, tools, benchmarks, and community demonstrations.",
        "2. [Awesome Astra Embodied AI](github/repos/zjwzcx__Awesome-Astra-Embodied-AI/README.md): Astra workflows across physical robots, simulation, policy calls, and training.",
        "3. [Coding Agents for Robot Learning](github/repos/harooos__awesome-coding-agents-for-robot-learning/README.md) and [BenchFlow Embodied Agents](github/repos/benchflow-ai__awesome-embodied-agents/README.md): how coding agents connect to robot execution interfaces.",
        "4. [Research blogs](blogs/README.md): first-party methods and project reports, complemented by demonstrations and discussions on [X](x/README.md), [Reddit](reddit/README.md), and [Zhihu](zhihu/README.md).", "",
        "## Browse by model and interface", "",
        "Model names follow the sources. Astra, Opus, and Fable are kept as separate keywords; unspecified model versions are not inferred from shorthand names.", "",
    ]
    for label, pattern in [("Astra", r"astra"), ("Opus", r"opus"), ("Fable", r"fable"), ("Gemini", r"gemini"), ("Robot interfaces and tool use", r"mcp|tool.use|ros|harness")]:
        selected = [r for r in catalog if r["platform"] != "github" and re.search(pattern, " ".join([r["title"], *r["models"], *r["tags"]]), re.I)]
        lines += [f"### {label}", ""]
        for r in selected:
            title = titles_en.get(r["id"], r["title"]).replace("[", "(").replace("]", ")")
            if re.search(r"[\u3400-\u9fff]", title):
                raise ValueError(f"English README title missing for {r['id']}")
            lines.append(f"- [{title}]({r['local_note']}) · {PLATFORM_LABELS[r['platform']]}")
        if not selected:
            lines.append("See the model fields in each category index.")
        lines.append("")
    lines += [
        "## Reading the evidence", "",
        "Physical robot experiments, simulated tasks, high-level planning, tool calls, and learned vision-language-action (VLA) policies describe different forms of control. Generating a robot control program does not imply that the model issues commands at motor servo frequency. Check each record's `control_layer` and `limitations` fields for the actual setup.", "",
        "Evidence labels describe source access, not independent validation of experimental results:", "",
        "- `page_read`: the page text was accessible and read.",
        "- `primary_project_crosschecked`: related technical claims were checked against the author's project page or an official report.",
        "- `mirror_post_read`: the post text was read through a public mirror.",
        "- `mirror_post_read_and_primary_crosschecked`: both mirror text and a primary report were consulted.",
        "- `secondary_page_read`: only an aggregation page was read.",
        "- `snippet_only`: only search-index snippets were available.", "",
        "Access restrictions and unsuccessful searches do not establish that relevant work is absent. Unconfirmed or excluded candidates are stored in each category's `candidates.json` and are not included in the entry counts. Search queries and source trails are recorded in `search_log.json`. Main records are deduplicated by URL within each platform; posts about the same project may appear across platforms, so entry counts are not counts of independent projects.", "",
        "## Files and maintenance", "",
        "- `records.json` in each category: complete structured records.",
        "- [catalog.json](catalog.json): a cross-platform directory with local note paths, models, and tags.",
        "- [collection_stats.json](collection_stats.json): entry counts and validation results.",
        "- [github/metadata/](github/metadata/): upstream commits, remotes, README SHA256 hashes, and license information.",
        "- [scripts/index_github.py](scripts/index_github.py): check downloaded repositories and rebuild their index.",
        "- [scripts/build_catalog.py](scripts/build_catalog.py): regenerate this English homepage and validate records and local note paths.",
        "- [scripts/readme_titles_en.json](scripts/readme_titles_en.json): English navigation labels for community posts.", "",
        "Full articles and media are not reproduced here; follow the source links in each note to access the originals. Third-party repositories retain their own licenses. Missing upstream license declarations are recorded in the metadata.", "",
        "## Download the complete collection", "",
        "The 11 upstream awesome repositories are Git submodules pinned to specific commits. Clone the project with its submodules:", "",
        "```bash", "git clone --recurse-submodules https://github.com/ShockCloud10/awesome-awesome-RUA.git", "```", "",
        "If you have already cloned the main repository, run this from its root:", "",
        "```bash", "git submodule update --init --recursive", "```", "",
        "GitHub ZIP downloads exclude submodule contents. The research notes, indexes, and JSON records are stored directly in the main repository.", "",
    ]
    text = "\n".join(lines)
    for r in json.loads((ROOT / "github" / "records.json").read_text()):
        text = text.replace(f"({r['readme_path']})", f"({r['url']}/blob/{r['commit']}/README.md)")
    (ROOT / "README.md").write_text(text)
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
