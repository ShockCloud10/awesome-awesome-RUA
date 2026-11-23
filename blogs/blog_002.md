# How Should We Use LLMs for Robot Control?

[原始来源](https://www.withplayground.ai/research/how-should-we-use-llms-for-robot-control)

- 作者：Playground research
- 首次发布日期：2026-11-12
- 收集日期：2026-11-23
- 模型：Claude Fable 5.2、GPT-6 Astra
- 机器人：LIBERO 仿真机械臂
- 控制层：代码策略 / 手写网络权重 / 逐步闭环动作
- 场景：simulation
- 访问状态：page_read
- 来源类型：一手作者或团队

## 中文摘要

在十项 LIBERO 操作任务上对比三种控制方式，展示相同基模因控制接口而表现不同。Fable 的代码策略在严格成功判据下优于在线逐步控制；Astra 写策略更快。

## 解释边界

只评测十项任务，每种策略生成仅一次；实机泛化未经该实验验证，π0.5 是论文参考分而非同场复测。

## 来源

- [原文](https://www.withplayground.ai/research/how-should-we-use-llms-for-robot-control)

本地保存的是摘要与元数据，未复制完整原文或视频；page_read 仅表示读取成功，不表示独立复现了实验。

