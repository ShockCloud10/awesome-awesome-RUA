# Claude as a Robot Teacher

[原始来源](https://irvin.quest/distilling-zero-shot-control/)

- 作者：Irvin Hwang
- 首次发布日期：2026-05-30
- 收集日期：2026-11-23
- 模型：Claude Opus、Claude Code
- 机器人：带相机的实体机械臂
- 控制层：世界模型候选预测 + Claude 选择 + 行为克隆
- 场景：physical
- 访问状态：page_read
- 来源类型：一手作者或团队

## 中文摘要

作者先让 Claude 比较世界模型预测的候选动作，再以其生成的数据训练快速控制器，实现将物体居中。也尝试让智能体组织采集、训练与验证流程。

## 解释边界

任务限于物体居中；作者报告慢控制器受环境变化影响，最终快速控制由蒸馏模型完成。

## 来源

- [原文](https://irvin.quest/distilling-zero-shot-control/)

本地保存的是摘要与元数据，未复制完整原文或视频；page_read 仅表示读取成功，不表示独立复现了实验。

