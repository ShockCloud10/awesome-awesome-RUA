# Dum-E 机械臂技能覆盖诊断 调参与动作编排

原帖：[Weekend build: an SO-101 arm + a Claude Code skill that handles the whole loop — servo diagnostics, motion tuning, and the video edit.](https://www.reddit.com/r/claude/comments/1ud1b38/weekend_build_an_so101_arm_a_claude_code_skill/)

- 作者：u/KamalSingh10
- 发帖日期：2026-06-22
- 日期依据：search_index_explicit_date
- 收集日期：2026-11-23（Asia/Hong_Kong）
- 来源类型：first_party_demo
- 证据状态：page_read，已读取可访问正文和相关评论；未独立观看或下载视频。
- 模型或 agent：Claude Code
- 机器人：SO-101 机械臂与腕部相机
- 控制层：agent 辅助硬件调试、寄存器调参、运动脚本执行
- 标签：SO-101、Claude-Code、skills、diagnostics

## 内容摘要

作者将 Claude Code 与 SO-101 封装为可复用技能，描述了舵机故障诊断、单关节校准、低速抖动调参，以及经安全层执行的平滑动作脚本。项目同时自动录制腕部相机并剪辑视频，提供 dummie 开源仓库。

## 证据边界

人工负责部分现场观察和操作；这是软硬件工作流及动作脚本演示，不等于通用自主抓取。

模型名称沿用原帖；本文未独立验证模型官方命名、硬件性能或演示成功率。索引中的明确日期与打开页的缓存相对时间可能不同，按日期依据字段理解。

## 来源与延伸链接

- [Reddit 原帖](https://www.reddit.com/r/claude/comments/1ud1b38/weekend_build_an_so101_arm_a_claude_code_skill/)
- [关联材料 1](https://github.com/kamalkantsingh10/dummie)

关联材料可能是正文提供的仓库、视频或交叉帖子；出现链接不代表本次已运行代码或观看视频。阅读范围及访问失败见 [search_log.json](search_log.json)。

