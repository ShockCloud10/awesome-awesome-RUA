# X 机器人控制帖子索引

收集日期：2026-11-23。收录 15 条 X 帖子，覆盖 Astra、Opus、Fable、Claude Code、ENPIRE 和机器人评测。包含同一 ENPIRE 演示的两位作者帖子，已以 experiment_cluster 标注，不能视为两次独立实验。

X 原站在本次读取中均返回 403。因此此文件夹是可离线阅读的中文摘要和链接档案，不是原帖全文或视频备份。技术内容优先使用作者项目页、官方报告交叉核对。公开镜像只说明帖子文字的可读性，不证明视频真实性。

## 证据状态

- primary_project_crosschecked：X 原文不可读，相关技术内容已由作者项目页或官方报告核对。
- mirror_post_read_and_primary_crosschecked：已读公开镜像中的帖子文字，同时核对原始报告。
- mirror_post_read：在公开镜像中读取到帖子文字。
- secondary_page_read：只读到聚合页面内容，技术细节尚缺直接原文核验。
- snippet_only：只有检索摘要和索引线索，未读取完整帖子；不要作为独立证据。

- `primary_project_crosschecked`：6 条
- `mirror_post_read_and_primary_crosschecked`：1 条
- `secondary_page_read`：1 条
- `snippet_only`：5 条
- `mirror_post_read`：2 条

## 帖子

| 笔记 | 模型 | 证据状态 |
|---|---|---|
| [x001 Fable 5.2 官方实机机器人演示](x001.md) | Claude Fable 5.2 | primary_project_crosschecked |
| [x002 Opus 5.5 与 Astra 用同一机械臂写字](x002.md) | Claude Opus 5.5, GPT-6 Astra | mirror_post_read_and_primary_crosschecked |
| [x003 Astra 与 Fable 的方块入碗评测](x003.md) | GPT-6 Astra, Claude Fable 5, Claude Fable 5.1 | primary_project_crosschecked |
| [x004 StationeryBench 双臂文具操作](x004.md) | GPT-6 Astra, MolmoAct2 | primary_project_crosschecked |
| [x005 Agent as Policy 实机操作发布](x005.md) | GPT-6 Astra, Codex CLI | primary_project_crosschecked |
| [x006 Phillip Isola 讨论 Robot Use Agents](x006.md) | Claude, Fable, Astra | primary_project_crosschecked |
| [x007 Sonnet 5.5 直接输出关节角触碰靶心](x007.md) | Claude Sonnet 5.5, Claude Code | secondary_page_read |
| [x008 Astra 用实体键盘学习打字](x008.md) | GPT-6 Astra | snippet_only |
| [x009 Astra 插入网线的人工介入记录](x009.md) | GPT-6 Astra | mirror_post_read |
| [x010 ENPIRE 机器人上下文学习演示](x010.md) | GPT-6 Astra | mirror_post_read |
| [x011 Vitrus OS 上适应新机器人](x011.md) | GPT-6 Astra | snippet_only |
| [x012 Astra 从视频迁移移动操作行为](x012.md) | GPT-6 Astra | snippet_only |
| [x013 Astra 机械臂绘制金门大桥](x013.md) | GPT-6 Astra | snippet_only |
| [x014 Wenli Xiao 的视频条件机器人模仿](x014.md) | GPT-6 Astra, Codex | snippet_only |
| [x015 RoboHarm 具身 agent 指令拒绝评测](x015.md) | GPT-6 Astra, Claude Fable 5.1, MolmoAct2 | primary_project_crosschecked |

机器可读数据：[records.json](records.json)。检索记录：[search_log.json](search_log.json)。待核验与排除线索：[candidates.json](candidates.json)。
