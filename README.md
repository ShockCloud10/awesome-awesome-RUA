# RUA 机器人控制资料库

围绕 Robot Use Agent（RUA）、coding agent 以及基础模型控制机器人，收集 GitHub awesome 清单、X、Reddit、知乎和技术博客。采集日期：2026 年 11 月 23 日（Asia/Hong_Kong）。

## 分类入口

| 资料类别 | 数量 | 本地入口 |
| --- | ---: | --- |
| GitHub awesome 仓库 | 11 | [github/README.md](github/README.md) |
| X 与 Twitter 帖子 | 15 | [x/README.md](x/README.md) |
| Reddit 帖子 | 16 | [reddit/README.md](reddit/README.md) |
| 知乎文章与帖子 | 10 | [zhihu/README.md](zhihu/README.md) |
| 技术博客与研究文章 | 18 | [blogs/README.md](blogs/README.md) |

GitHub 保存的是实际仓库浅克隆；帖子和博客保存的是原始链接、中文摘要、模型与机器人信息、控制方式及来源核实状态。视频没有下载，也没有把演示视频视为已独立复现的实验。

访问限制：15 条 X 原帖均未直接读取，分别通过项目页、公开镜像、聚合页或搜索摘要收集；10 条知乎资料中 9 条仅获得搜索索引摘要。每条记录保留具体证据等级。

## 建议阅读顺序

1. [Awesome Robot Use Agent](https://github.com/kairunwen/Awesome-Robot-Use-Agent/blob/566ed8a2a874694e8034004ca5466a28ff9a657f/README.md)：从 RUA 总览进入论文、工具、基准和社区演示。
2. [Awesome Astra Embodied AI](https://github.com/zjwzcx/Awesome-Astra-Embodied-AI/blob/5f7aa7bcded315d05dfb9d4d473024648bc6cf94/README.md)：聚焦 Astra，区分真机、仿真、策略调用和训练工作流。
3. [Coding Agents for Robot Learning](https://github.com/harooos/awesome-coding-agents-for-robot-learning/blob/7b3505e73983a58260658e39908d0847a7264c6f/README.md) 与 [BenchFlow Embodied Agents](https://github.com/benchflow-ai/awesome-embodied-agents/blob/ba7d64b9d17fa39ce71d249ec8f54891ab83a357/README.md)：追踪 agent 与机器人执行接口。
4. [博客索引](blogs/README.md)：阅读一手研究文章和项目方法说明；再结合 [X](x/README.md)、[Reddit](reddit/README.md) 和 [知乎](zhihu/README.md) 查看演示与讨论。

## 关键词导航

模型名称沿用来源中的写法。Astra、Opus、Fable 作为不同关键词保留，不根据简称推断未明确披露的型号或版本。

### Astra

- [Opus 5.5 与 Astra 用同一机械臂写字](x/x002.md) · x
- [Astra 与 Fable 的方块入碗评测](x/x003.md) · x
- [StationeryBench 双臂文具操作](x/x004.md) · x
- [Agent as Policy 实机操作发布](x/x005.md) · x
- [Phillip Isola 讨论 Robot Use Agents](x/x006.md) · x
- [Astra 用实体键盘学习打字](x/x008.md) · x
- [Astra 插入网线的人工介入记录](x/x009.md) · x
- [ENPIRE 机器人上下文学习演示](x/x010.md) · x
- [Vitrus OS 上适应新机器人](x/x011.md) · x
- [Astra 从视频迁移移动操作行为](x/x012.md) · x
- [Astra 机械臂绘制金门大桥](x/x013.md) · x
- [Wenli Xiao 的视频条件机器人模仿](x/x014.md) · x
- [RoboHarm 具身 agent 指令拒绝评测](x/x015.md) · x
- [Astra 与 Fable 5.1 工业机械臂工作站](reddit/reddit-002.md) · reddit
- [同一 SO-101 上比较 Fable 5.1 与 Astra 涂色](reddit/reddit-007.md) · reddit
- [Astra 规划绘画并编排整套机械臂工作室](reddit/reddit-011.md) · reddit
- [Astra 机械臂画金门桥的 Reddit 转发](reddit/reddit-015.md) · reddit
- [GPT-6 Astra开进机器人身体！清华联手无问芯穹等开源RPent](zhihu/zhihu_001.md) · zhihu
- [刚刚，机器人界王者归来！「神级硬件」带飞GPT-6，三大新品震撼掀桌](zhihu/zhihu_003.md) · zhihu
- [三榜第一，完胜GPT-6！中国物理RSI杀出黑马](zhihu/zhihu_004.md) · zhihu
- [清华具身模型登顶全球第一！突围GPT-6、英伟达，不靠外挂和额外数据](zhihu/zhihu_005.md) · zhihu
- [马斯克再暗示合并特斯拉和 SpaceX；传 iPhone 18 Pro 系列卖爆；大疆 Pocket 4P「珠光白」3799 开售｜极客早知道](zhihu/zhihu_007.md) · zhihu
- [中国物理AI大突破：PhysBrain 1.5登顶全球开源榜一，空间智能与GPT-6 Astra并驾齐驱](zhihu/zhihu_009.md) · zhihu
- [Robot-Use Agents](blogs/blog_001.md) · blogs
- [How Should We Use LLMs for Robot Control?](blogs/blog_002.md) · blogs
- [Are Astra, Fable 5.1 and Opus 5.5 ready for science lab tasks?](blogs/blog_003.md) · blogs
- [Claude Fable 5.2 and Mythos 5.2](blogs/blog_007.md) · blogs
- [GPT-6 Astra on robotic manipulation](blogs/blog_009.md) · blogs
- [PB27 — Paintings by coding agents](blogs/blog_018.md) · blogs

### Opus

- [Opus 5.5 与 Astra 用同一机械臂写字](x/x002.md) · x
- [Opus 5.5 通过工具调用控制 SO-101 对齐积木](reddit/reddit-001.md) · reddit
- [Are Astra, Fable 5.1 and Opus 5.5 ready for science lab tasks?](blogs/blog_003.md) · blogs
- [Claude plays robotics](blogs/blog_004.md) · blogs
- [Project Fetch: Phase two](blogs/blog_005.md) · blogs
- [Claude Fable 5.2 and Mythos 5.2](blogs/blog_007.md) · blogs
- [Claude as a Robot Teacher](blogs/blog_011.md) · blogs
- [PB27 — Paintings by coding agents](blogs/blog_018.md) · blogs

### Fable

- [Fable 5.2 官方实机机器人演示](x/x001.md) · x
- [Astra 与 Fable 的方块入碗评测](x/x003.md) · x
- [Phillip Isola 讨论 Robot Use Agents](x/x006.md) · x
- [RoboHarm 具身 agent 指令拒绝评测](x/x015.md) · x
- [Astra 与 Fable 5.1 工业机械臂工作站](reddit/reddit-002.md) · reddit
- [Fable 5.2 自行编写控制器并用机械臂画自画像](reddit/reddit-004.md) · reddit
- [Fable 5.2 自编程序完成工厂机械臂任务](reddit/reddit-005.md) · reddit
- [同一 SO-101 上比较 Fable 5.1 与 Astra 涂色](reddit/reddit-007.md) · reddit
- [Fable 5 通过 API 控制树莓派机器人身体](reddit/reddit-008.md) · reddit
- [Fable 5.2 机器人演示的社区技术质疑](reddit/reddit-010.md) · reddit
- [刚刚，机器人界王者归来！「神级硬件」带飞GPT-6，三大新品震撼掀桌](zhihu/zhihu_003.md) · zhihu
- [Robot-Use Agents](blogs/blog_001.md) · blogs
- [How Should We Use LLMs for Robot Control?](blogs/blog_002.md) · blogs
- [Are Astra, Fable 5.1 and Opus 5.5 ready for science lab tasks?](blogs/blog_003.md) · blogs
- [Claude Fable 5.2 and Mythos 5.2](blogs/blog_007.md) · blogs
- [GPT-6 Astra on robotic manipulation](blogs/blog_009.md) · blogs
- [Comparing Fable 5.1 to Fable 5 on robotic manipulation](blogs/blog_010.md) · blogs
- [PB27 — Paintings by coding agents](blogs/blog_018.md) · blogs

### Gemini

- [Gemini 3.0 通过逐步视觉观察完成清桌抓放](reddit/reddit-009.md) · reddit
- [ROS MCP Server 连接 Claude GPT Gemini 与实体机器人](reddit/reddit-013.md) · reddit
- [中国物理AI大突破：PhysBrain 1.5登顶全球开源榜一，空间智能与GPT-6 Astra并驾齐驱](zhihu/zhihu_009.md) · zhihu
- [宇树科技 8 月 10 日开启 IPO 申购；字节 ToB 变阵：飞书豆包火山组织调整；马斯克称人类 5-7 年登陆火星 | 极客早知道](zhihu/zhihu_010.md) · zhihu
- [Gemini Robotics 1.5 brings AI agents into the physical world](blogs/blog_014.md) · blogs
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](blogs/blog_015.md) · blogs
- [Gemini Robotics 2 brings whole body intelligence to robots](blogs/blog_016.md) · blogs

### 机器人接口与工具调用

- [Opus 5.5 通过工具调用控制 SO-101 对齐积木](reddit/reddit-001.md) · reddit
- [Claude Code 通过 MCP 控制 Franka Panda](reddit/reddit-006.md) · reddit
- [LLM 通过 MCP 和 ROS2 控制 Unitree Go2](reddit/reddit-012.md) · reddit
- [ROS MCP Server 连接 Claude GPT Gemini 与实体机器人](reddit/reddit-013.md) · reddit
- [OpenAI agent SDK 通过 ROS2 控制实体 CNC 绘图机](reddit/reddit-014.md) · reddit
- [Astra 机械臂画金门桥的 Reddit 转发](reddit/reddit-015.md) · reddit
- [AgenticROS 连接 Claude 与 RealSense 轮式机器人](reddit/reddit-016.md) · reddit
- [Previewing the Model Hardware Standard](blogs/blog_006.md) · blogs

## 如何理解资料

真机操作、仿真任务、高层规划、工具调用和学习到的 VLA 策略处于不同层次。某个模型能生成机械臂控制程序，并不表示它直接在电机伺服频率下输出控制信号；具体以每条记录的 control_layer 和 limitations 为准。

page_read 等状态表示读取到网页内容；project_crosschecked 或 mirror_post_read 表示使用项目页或公开镜像辅助核对；snippet_only 表示只获得搜索索引摘要。它们描述来源可见性，不代表独立验证作者的实验结论。不同目录的状态细分见各自 README。

搜索未找到或访问受限不等于相关工作不存在。未确认候选保留在各目录的 candidates.json，未计入主条目数；检索关键词与来源线索保留在 search_log.json。主记录按 URL 去重，同一项目在不同平台的帖子仍分别保存，数量不等于独立项目数量。

## 文件与后续整理

- 每类 records.json：完整结构化记录。
- catalog.json：跨平台链接目录，包含本地笔记路径、模型和标签。
- collection_stats.json：条目统计与检查结果。
- github/metadata/：每个仓库的 commit、remote、README SHA256 和许可证信息。
- scripts/index_github.py：重新检查已经下载的仓库并生成索引。
- scripts/build_catalog.py：重新生成总导航并检查记录及本地链接。

网页全文和媒体未批量转载，原始内容请通过每条笔记的来源链接访问。第三方仓库保留原许可证；上游未注明许可证的仓库已在元数据中注明。

## 下载全部资料

本项目使用 Git 子模块记录 11 个上游 awesome 仓库及其固定提交。完整下载命令：

```bash
git clone --recurse-submodules https://github.com/ShockCloud10/awesome-awesome-RUA.git
```

已经克隆主仓库时，在根目录执行 `git submodule update --init --recursive`。GitHub 下载 ZIP 不包含子模块内容；独立笔记、索引和 JSON 保存在主仓库。
