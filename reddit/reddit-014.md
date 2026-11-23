# OpenAI agent SDK 通过 ROS2 控制实体 CNC 绘图机

原帖：[I built a ROS2-controlled CNC plotter that takes natural language commands via an LLM Agent (w/ RViz Digital Twin)](https://www.reddit.com/r/ROS/comments/1r67511/i_built_a_ros2controlled_cnc_plotter_that_takes/)

- 作者：u/Purple_Fee6414
- 发帖日期：2026-02-16
- 日期依据：reddit_page_top_posts_date
- 收集日期：2026-11-23（Asia/Hong_Kong）
- 来源类型：first_party_demo
- 证据状态：page_read，已读取可访问正文和相关评论；未独立观看或下载视频。
- 模型或 agent：LLM（未指定）、OpenAI agent SDK
- 机器人：双轴 CNC 绘图机、Raspberry Pi、Arduino GRBL
- 控制层：agent draw_shape 工具 → 路径坐标 → ROS2 GRBL driver
- 标签：ROS2、OpenAI-Agent-SDK、CNC、GRBL、tool-use

## 内容摘要

作者回收光驱步进电机构建双轴绘图机，以 Raspberry Pi 运行 ROS2、Arduino 运行 GRBL。自定义 llm_commander 节点注册 draw_shape 工具，把自然语言画方形等请求转换为坐标，通过驱动节点执行，并在 RViz 中同步状态。

## 证据边界

任务范围主要是预定义几何形状与工具调用；不是任意视觉操作；RViz 是状态可视化而非已证明的动力学仿真。

模型名称沿用原帖；本文未独立验证模型官方命名、硬件性能或演示成功率。索引中的明确日期与打开页的缓存相对时间可能不同，按日期依据字段理解。

## 来源与延伸链接

- [Reddit 原帖](https://www.reddit.com/r/ROS/comments/1r67511/i_built_a_ros2controlled_cnc_plotter_that_takes/)
- [关联材料 1](https://github.com/yacin-hamdi/ros-pi-cnc)
- [关联材料 2](https://www.reddit.com/r/robotics/comments/1r67684/i_built_a_ros2controlled_cnc_plotter_that_takes/)

关联材料可能是正文提供的仓库、视频或交叉帖子；出现链接不代表本次已运行代码或观看视频。阅读范围及访问失败见 [search_log.json](search_log.json)。

