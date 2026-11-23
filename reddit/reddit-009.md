# Gemini 3.0 通过逐步视觉观察完成清桌抓放

原帖：[Robotic Arm Controlled By Gemini 3.0](https://www.reddit.com/r/GeminiAI/comments/1pms77x/robotic_arm_controlled_by_gemini_30/)

- 作者：u/ReflectionLarge6439
- 发帖日期：2025-12-14
- 日期依据：search_index_explicit_date
- 收集日期：2026-11-23（Asia/Hong_Kong）
- 来源类型：first_party_demo
- 证据状态：page_read，已读取可访问正文和相关评论；未独立观看或下载视频。
- 模型或 agent：Gemini 3.0、Gemini 1.5 ER（原帖称呼）
- 机器人：自制 3D 打印机械臂、深度相机、Arduino 夹爪
- 控制层：VLM 逐动作观察与高层抓放选择
- 标签：Gemini、VLM、pick-and-place、closed-loop

## 内容摘要

作者用 Gemini 分析深度相机图像，把清理桌面分解为抓取、放入袋中、重新观察等步骤。评论确认图像发送给 Gemini API，每完成一步才再次观察；机械臂和齿轮箱由作者自制，电脑软件控制机械臂。

## 证据边界

并非持续视频下的实时运动闭环；原帖将 VLA 作为后续升级方案，不能把此实现记为 VLA。

模型名称沿用原帖；本文未独立验证模型官方命名、硬件性能或演示成功率。索引中的明确日期与打开页的缓存相对时间可能不同，按日期依据字段理解。

## 来源与延伸链接

- [Reddit 原帖](https://www.reddit.com/r/GeminiAI/comments/1pms77x/robotic_arm_controlled_by_gemini_30/)
- [关联材料 1](https://youtu.be/UOc8WNjLqPs)

关联材料可能是正文提供的仓库、视频或交叉帖子；出现链接不代表本次已运行代码或观看视频。阅读范围及访问失败见 [search_log.json](search_log.json)。

