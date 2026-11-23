# Reddit 上的 agent 与基模控制机器人案例

收集日期：2026-11-23，Asia/Hong_Kong。共收录 **16 条去重案例与技术讨论**，均已读取可访问的 Reddit 正文；模型、演示成果与性能说法保持原作者归属，未做硬件复现。交叉帖合并到同一案例，避免把转发数量当成独立实验数量。

重点覆盖 Astra、Fable、Opus、Claude Code、Gemini，以及 MCP／ROS 接入实体机械臂、移动机器人和 CNC。没有把仅仅聊天、音频触发表情、CAD 设计或普通 computer-use 当作模型控制机器人的核心证据。

## 优先阅读

- [Opus 5.5 对齐 SO-101 积木](reddit-001.md)：视觉观察、工具调用、可复用技能。
- [Astra 与 Fable 5.1 工业工作站](reddit-002.md)：三维重建、自动编程与人工监督。
- [Fable 5.2 自画像](reddit-004.md)：控制器、标定、失败恢复的第一手叙述。
- [Astra 绘画工作室](reddit-011.md)：明确区分模型规划和底层执行器。
- [Franka Panda MCP](reddit-006.md) 与 [ROS MCP Server](reddit-013.md)：有开源实现线索。
- [Gemini 清桌](reddit-009.md)：逐动作视觉反馈，不是实时 VLA。

## 全部条目

| 编号 | 内容 | 模型或 agent | 日期 | 来源类型 |
|---|---|---|---|---|
| reddit-001 | [Opus 5.5 通过工具调用控制 SO-101 对齐积木](reddit-001.md) | Claude Code / Opus 5.5 | 2026-10-27 | first_party_demo |
| reddit-002 | [Astra 与 Fable 5.1 工业机械臂工作站](reddit-002.md) | Astra / Fable 5.1 / Claude | 2026-09-12 | first_party_demo |
| reddit-003 | [Dum-E 机械臂技能覆盖诊断 调参与动作编排](reddit-003.md) | Claude Code | 2026-06-22 | first_party_demo |
| reddit-004 | [Fable 5.2 自行编写控制器并用机械臂画自画像](reddit-004.md) | Fable 5.2 | 2026-11-13 | first_party_demo |
| reddit-005 | [Fable 5.2 自编程序完成工厂机械臂任务](reddit-005.md) | Claude Fable 5.2 | 2026-11-17 | demo_claim |
| reddit-006 | [Claude Code 通过 MCP 控制 Franka Panda](reddit-006.md) | Claude Code | 2026-02-08 | first_party_demo |
| reddit-007 | [同一 SO-101 上比较 Fable 5.1 与 Astra 涂色](reddit-007.md) | Claude Fable 5.1 / GPT 6 Astra | 2026-09-14 | first_party_comparison |
| reddit-008 | [Fable 5 通过 API 控制树莓派机器人身体](reddit-008.md) | Claude Fable 5 | 未确认 | first_party_demo |
| reddit-009 | [Gemini 3.0 通过逐步视觉观察完成清桌抓放](reddit-009.md) | Gemini 3.0 / Gemini 1.5 ER（原帖称呼） | 2025-12-14 | first_party_demo |
| reddit-010 | [Fable 5.2 机器人演示的社区技术质疑](reddit-010.md) | Fable 5.2 | 2026-11-09 | secondary_discussion |
| reddit-011 | [Astra 规划绘画并编排整套机械臂工作室](reddit-011.md) | GPT-6 Astra / Codex / Claude | 2026-10-28 | first_party_demo |
| reddit-012 | [LLM 通过 MCP 和 ROS2 控制 Unitree Go2](reddit-012.md) | LLM（未指定） | 2025-05-09 | first_party_release |
| reddit-013 | [ROS MCP Server 连接 Claude GPT Gemini 与实体机器人](reddit-013.md) | Claude / GPT / Gemini | 2025-09-10 | first_party_release |
| reddit-014 | [OpenAI agent SDK 通过 ROS2 控制实体 CNC 绘图机](reddit-014.md) | LLM（未指定） / OpenAI agent SDK | 2026-02-16 | first_party_demo |
| reddit-015 | [Astra 机械臂画金门桥的 Reddit 转发](reddit-015.md) | Astra | 2026-09-08 | secondary_repost |
| reddit-016 | [AgenticROS 连接 Claude 与 RealSense 轮式机器人](reddit-016.md) | OpenClaw / Claude AI Agents | 2026-07-02 | first_party_demo |

## 机器可读文件

- [records.json](records.json)：标题、作者、日期、模型、机器人、控制层、中文摘要、证据状态和原始链接。
- [search_log.json](search_log.json)：检索词、读取页面、访问问题与日期口径。
- [candidates.json](candidates.json)：12 条交叉贴、待核实或因范围原因未进入主表的线索。

## 证据与日期口径

`page_read` 表示读取了公开页面文本，不代表复现实验、检查所有折叠评论或验证视频真实性。本批 16 条均为 page_read，核心表没有 snippet_only 条目。视频和外链仓库仅保留链接。

具体发帖日期优先取搜索索引展示的绝对日期，并在每条记录中注明来源。部分 Reddit 页面显示的缓存相对时间与其不一致，不以相对时间反推发布日期；未确认的日期保留 null。模型名称按帖子原文记录，不将帖中名称自动当作官方型号事实。

保存的是中文研究笔记与原始链接，不是整页或整段评论的版权全文镜像。

