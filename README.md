# awesome-dsh-2026

面向国内开发者、按质量精选并持续维护的 DeepSeek Harness（DSH）2026 插件生态列表。<br>
A quality-focused, annually maintained collection of DeepSeek Harness (DSH) plugins for 2026, with Chinese-first descriptions.

> 📖 English: [README.en.md](README.en.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/Herdeny/awesome-dsh-plugins-2026?style=social)](https://github.com/Herdeny/awesome-dsh-plugins-2026)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Last updated: 2026-08](https://img.shields.io/badge/last--updated-2026--09--03-brightgreen.svg)
![Plugins: 55](https://img.shields.io/badge/plugins-215-orange.svg)
![Contributors](https://img.shields.io/github/contributors/Herdeny/awesome-dsh-plugins-2026.svg)

## 目录 / Contents

- [🔌 开发框架与工具](#development-tools)
- [🎨 设计与创意](#design-creative)
- [👁️ 视觉与多模态](#vision)
- [🖥️ Web UI 与界面](#web-ui)
- [🎨 主题与外观](#themes-appearance)
- [💰 模型与额度](#models-quota)
- [🧪 测试与质检](#testing-qa)
- [📦 示例与模板](#examples-templates)
- [💬 会话与消息](#sessions-messages)
- [🎮 趣味](#just-for-fun)
- [🧩 MCP 与集成](#mcp-integrations)
- [🧠 记忆与上下文](#memory-context)
- [🔒 安全与审计](#security-audit)
- [💻 桌面与客户端](#desktop-clients)
- [🌐 平台与渠道](#platforms-channels)
- [🌱 生态项目 / Ecosystem](#ecosystem)
- [官方资源 / Official resources](#official-resources)
- [贡献指南 / Contributing](#contributing)

## 质量评分分布（dsh-qc 检测） / Quality score distribution (dsh-qc)

评分来自 [dsh-qc](https://github.com/Herdeny/dsh-qc) 静态+动态质检，100 分制。🟢 良好 / 🟡 及格 / 🟠 一般 / 🔴 待改进。<br>
Scores from [dsh-qc](https://github.com/Herdeny/dsh-qc), 100-point static+dynamic QC.

- 🟢 70-100: 5
- 🟡 50-69: 37
- 🟠 30-49: 17
- 🔴 0-29: 23

<a id="development-tools"></a>

## 🔌 开发框架与工具

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) - DeepSeek Harness 官方主仓库，践行“一切皆插件”的扩展理念 (⭐201780)
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) - 两阶段 DSH 预设：先进行最小对齐引导，再完成标准化对齐 (⭐3550) 🛡️QC:31 🟠
- [edison7009/EchoBird](https://github.com/edison7009/EchoBird) - 一键安装 + 模型切换：覆盖 Claude Code、Codex、Grok、DSH、Kimi、Qwen、Aider 等 15+ 编程代理 (⭐3087) 🛡️QC:21 🔴
- [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) - 通用 Skill 路由器：自动路由本地 Skills，智能编排 Harness 工作流（含 DSH） (⭐2910) 🛡️QC:0 🔴
- [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) - 现代化可灵活嵌入的任务面板，支持 Codex、DeepSeek Harness (⭐2794)
- [tong-io/tongflow](https://github.com/tong-io/tongflow) - 多模态工作流工作室与引擎（画布 + Python 插件引擎），含 dsh-tongflow 工作室插件 (⭐1005) 🛡️QC:30 🟠
- [SheberDavid/v4-flash-godmode-opencode-go](https://github.com/SheberDavid/v4-flash-godmode-opencode-go) - DSH agent 预设：让 opencode-go 的 DeepSeek V4 Flash 从“鬼模式”切换到“神模式” (⭐499) 🛡️QC:25 🔴
- [RealSeaberry/AutoMCM-Pro](https://github.com/RealSeaberry/AutoMCM-Pro) - 全栈式自动数学建模竞赛 Skill：AI 自动驾驶、人类副驾，GitOps 流水线 + 强制代码自证，支持 Claude Code / Codex / opencode / DSH (⭐188)
- [dream-num/dsh-univer-office](https://github.com/dream-num/dsh-univer-office) - Univer 官方 Office 插件：表格、文档、幻灯片、画布与关系表合一运行时，支持多 Agent 协作与版本化变更 (⭐214)
- [liceses/dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset) - 一键安装「极简模式 (Git Bash)」agent preset：把 DSH 极简模式中的 bash 调用映射为 Git Bash 环境 (⭐135)
- [1692775560/dsh-Mimir-Academic-research](https://github.com/1692775560/dsh-Mimir-Academic-research) - Mimir 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表与 GPU 服务器 SSH 任务编排 (⭐132)
- [shengsheng90/DSH-taskboard](https://github.com/shengsheng90/DSH-taskboard) - 原生本地任务看板插件：SQLite 项目、Agent 认领/复核与原生 Web UI，无 iframe、无第二会话运行时 (⭐240)
- [christopherarter/superpowers-reasonix](https://github.com/christopherarter/superpowers-reasonix) - Superpowers 技能包移植到 Reasonix 编程 Harness（DeepSeek 原生终端代理，支持 DSH 生态） (⭐94)
- [LayneChai/superpowers-dsh](https://github.com/LayneChai/superpowers-dsh) - Superpowers 技能包移植到 DSH：TDD、调试、规划与协作技能 (⭐112)
- [skymecode/deepseek-harness-for-vscode](https://github.com/skymecode/deepseek-harness-for-vscode) - DSH 原生 VS Code 编码代理扩展：会话管理、流式 Markdown、斜杠命令与插件中心，零部署免 WebUI (⭐120)
- [omdsh-dev/dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) - 把 Claude Code 的 UltraCode 模式带给 DSH：一次性多 Agent 调度升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层 (⭐108)
- [dhicoc/dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) - 完整 reverse-skill（85 个 SKILL.md）DSH Cordis 插件：逆向工程、授权渗透测试与安全研究技能包 (⭐99)
- [sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills) - 88 个可安装开源 Agent Skills：研究、社交情报、营销与商业工作流，兼容 Codex / Claude Code / Cursor / Gemini CLI / DSH (⭐91)
- [MiaoQichuan/new-litigation-visualization](https://github.com/MiaoQichuan/new-litigation-visualization) - 给法律人的诉讼可视化工具集：把凌乱的诉讼图重画成能进材料的图，或直接读案件材料画准一张时间轴，Claude Skill / DSH 通用 (⭐49)
- [qkycir-123/dsh-run2skill](https://github.com/qkycir-123/dsh-run2skill) - 把成功的 DeepSeek Harness 会话自动沉淀为可复用、可审查的 Agent Skill (⭐44)
- [songyang0603/ds-spec-loop](https://github.com/songyang0603/ds-spec-loop) - 仓库原生 Spec 编程的可移植 Agent Skill，参考公开的 DeepSeek Harness 工程实践 (⭐38)
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - MattSkillsDeck：让 mattpocock/skills 在 DSH 里化作一块看得见、派得动的任务板 (⭐33)
- [linhut/gongwen-skill](https://github.com/linhut/gongwen-skill) - 中文公文全流程处理工具：GB/T 9704 格式检查与修复、内容优化、模板生成、Markdown 转公文、事实核验，原生支持 DSH 技能系统 (⭐30)
- [PerryLink/dsh-industry-research](https://github.com/PerryLink/dsh-industry-research) - 行业与公司研究领域包：方法论技能、产业链图谱、公开信源政策/新闻跟踪、公司研究卡片与可审计研究报告（仅研究，非投资建议） (⭐30)
- [HiWhaleW/dsh-toolbox](https://github.com/HiWhaleW/dsh-toolbox) - 本地优先 DSH 工具箱：产品研究、上下文切换、插件预检与兼容性监控，安全导向的可视化控制面板 (⭐29)
- [omdsh-dev/dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) - DSH 零依赖工具包合集：time/encoding/json/calculator/csv/regex/markdown/diff/stat/schema 十个确定性工具，统一入口一键安装 (⭐28)
- [MichengAI/dsh-skills-manager](https://github.com/MichengAI/dsh-skills-manager) - 在 DSH 中统一加载并安全管理本机 Agent Skills (⭐28)
- [a735624258/dsh-skill-picker](https://github.com/a735624258/dsh-skill-picker) - WorkBuddy 同款 Skill 选择器：在输入框挑选 skill，自动插入官方 /skill-name 手势随消息一起发送 (⭐26)

<a id="design-creative"></a>

## 🎨 设计与创意

- [zenstory-ai/oh-story-dsh](https://github.com/zenstory-ai/oh-story-dsh) - 小说创作与短剧生产插件：由 Oh Story 与 Drama Skills 驱动的写作工作流 (⭐229)
- [shanliuling/dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) - 在 DSH 对话中直接生成图片 (⭐288)
- [zseven-w/dsh-openpencil](https://github.com/zseven-w/dsh-openpencil) - OpenPencil 预览、检查与编辑插件 (⭐153) 🛡️QC:64 🟡
- [devin-axis/deepseek-design](https://github.com/devin-axis/deepseek-design) - 可编辑设计系统，支持 AI 生成、可视化编辑、模板市场与 PPT (⭐633) 🛡️QC:17 🔴
- [kwhi6693-web/photo-abstract-editorial](https://github.com/kwhi6693-web/photo-abstract-editorial) - 照片转杂志编辑风 Skill：场景感知布局、创意控制与严格保真合成，含 Codex 原版与 V3 自适应版 (⭐88)

<a id="vision"></a>

## 👁️ 视觉与多模态

- [liustack/modlens](https://github.com/liustack/modlens) - DSH 视觉桥接插件，为纯文本 Agent 提供视觉能力 (⭐3496) 🛡️QC:43 🟠
- [anionex/dsh-vision-toolkit](https://github.com/anionex/dsh-vision-toolkit) - 让纯文本模型完成意图图片问答、长截图 OCR 与 UI 还原 (⭐806) 🛡️QC:65 🟡
- [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) - 为纯文本 DSH Agent 提供内置免费视觉链路 (⭐998) 🛡️QC:52 🟡
- [xiincs/claude-code-vision-skill](https://github.com/xiincs/claude-code-vision-skill) - 接入豆包、通义千问与 GPT-4o，支持截图、UI 和图表分析 (⭐165) 🛡️QC:17 🔴
- [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) - 为 DeepSeek Harness 提供接近原生体验的图像理解能力 (⭐83) 🛡️QC:69 🟡
- [Yts1919/dsh-vision-complete](https://github.com/Yts1919/dsh-vision-complete) - 多模态「眼睛和耳朵」插件：看图/OCR/物体检测/视频理解/语音转写/截图直读 (⭐42) 🛡️QC:25 🔴
- [william-jin-cmu/dsh-vision](https://github.com/william-jin-cmu/dsh-vision) - view_image 工具桥接任意 OpenAI 兼容 VLM（默认智谱免费档，实测 4 厂商 10 模型） (⭐32) 🛡️QC:47 🟠
- [jing-hy/picturereader](https://github.com/jing-hy/picturereader) - 像素级图片读取插件：image_scan/image_ocr/image_sample 工具 + 图片阅读技能，纯文本模型也能读图，纯本地运行 (⭐34) 🛡️QC:44 🟠
- [tianmingwan/dsh-vision-any](https://github.com/tianmingwan/dsh-vision-any) - 让纯文本 DSH Agent 直接粘贴图片，支持任意 OpenAI 兼容 / Anthropic / Gemini 视觉 API (⭐22) 🛡️QC:61 🟡
- [hisence999/DSH-vision](https://github.com/hisence999/DSH-vision) - 纯文本模型直接发图：图片自动转文字描述回传，多模态模型原样放行，read_image 工具可用 (⭐34) 🛡️QC:38 🟠
- [HuanLinOTO/dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) - 向模型暴露 MinerU 文档解析工具：PDF/图片/DOCX/PPTX/XLSX 一键转为结构化 Markdown/JSON (⭐43)

<a id="web-ui"></a>

## 🖥️ Web UI 与界面

- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - 开放的侧边栏底座：支持三方扩展注册新侧边栏页面，内置文件渲染编辑/终端/Git/子代理页面 (⭐2978) 🛡️QC:51 🟡
- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) - 官方公众号收录的 Claude Code 风 TUI 补位插件：鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚，npm 一键安装 (⭐2604) 🛡️QC:33 🟠
- [ccch1mneyyy/working-activity](https://github.com/ccch1mneyyy/working-activity) - 为 pi CLI 与 DSH 打造的生动工作行（statusline）扩展 (⭐653) 🛡️QC:28 🔴
- [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) - 官方 DeepSeek Harness 交互式终端 UI 插件：自研 ANSI 极简渲染核心、流式 Markdown 与实时状态 (⭐251)
- [liangmianya/dsh-synapse](https://github.com/liangmianya/dsh-synapse) - 可视化的非线性对话工作区：基于画布的会话探索与分支工作区 (⭐280)
- [Aisland-SJL/dsh-worktable](https://github.com/Aisland-SJL/dsh-worktable) - Agent 项目工作台：侧边栏应用抽屉 + 可停靠分屏工作区 + 实时监控所有项目的控制室 (⭐411)
- [xuanyuanzhifeng/dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) - DSH Web UI 工作流标签页：按对话轮次展示模型请求、响应与工具调用的执行链路，含 Token 与缓存统计 (⭐133)
- [pengyue-polaron/deepseek-harness-genui](https://github.com/pengyue-polaron/deepseek-harness-genui) - 任务专属 React 应用生成插件：Agent 为当前任务创建聚焦界面，并把用户选择/输入的状态带入下一轮对话 (⭐106)
- [GraySilver/dsh-evolve-modes](https://github.com/GraySilver/dsh-evolve-modes) - 让 Agent 的工作方式可组合、可审查、可持续改进：可组合任务控制 + 隔离的人工审查自进化 (⭐189)
- [Fishquito7/dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) - DSH Web UI 插件：Web 界面的 Skill 与 MCP 管理工具 (⭐104)
- [sanqi-normal/dsh-webui-market-plugin](https://github.com/sanqi-normal/dsh-webui-market-plugin) - 面向 DSH Web UI 的插件市场入口 (⭐102) 🛡️QC:61 🟡
- [francis-xavier-code/dsh-balance-plugin](https://github.com/francis-xavier-code/dsh-balance-plugin) - 提供余额监控与用量统计能力 (⭐56) 🛡️QC:61 🟡
- [hsiangnianian/dsh-auto-continue](https://github.com/hsiangnianian/dsh-auto-continue) - 自动发送“继续”，恢复被中断的请求 (⭐53) 🛡️QC:72 🟢
- [william-jin-cmu/dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) - 支持双向发送与展示表情贴纸 (⭐23) 🛡️QC:66 🟡
- [buhuikongpan/dsh-pluginmanager](https://github.com/buhuikongpan/dsh-pluginmanager) - 面向 DSH 的分层插件管理器 (⭐9) 🛡️QC:61 🟡
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件，发送时复制进会话工作区 (⭐10) 🛡️QC:39 🟠
- [LX2000WASD/dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) - Web UI 一键插件管理：查看、实时启停、安装/卸载、更新检测与依赖/冲突/兼容性健康检查，bundle 与非 bundle 全覆盖 (⭐67)
- [Laplace-bit/dsh-smooth-stream](https://github.com/Laplace-bit/dsh-smooth-stream) - Web UI 流畅流式渲染与丝滑滚动插件 (⭐60)
- [Tasihi89/dsh-talk-map](https://github.com/Tasihi89/dsh-talk-map) - 可视化对话地图：会话以卡片呈现在白板上，拖拽排列、双击聊天、连线分叉注入上下文 (⭐69)
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - DSH Web 插件：把「Deep diving…」状态标签换成打字机动画彩虹短语轮播，附带实时状态 (⭐65)
- [rison114514/dsh-endfield-ui](https://github.com/rison114514/dsh-endfield-ui) - 终末地风格工业 UI 外壳（非官方粉丝主题）：dsh plugin --profile web add 一键安装 (⭐48)
- [MichengAI/dsh-codex-ui](https://github.com/MichengAI/dsh-codex-ui) - 为 DSH Web 提供 Codex 风格侧栏、工作区会话树、全局搜索与轮次导航 (⭐42)
- [plolpl789/dsh-raw-html](https://github.com/plolpl789/dsh-raw-html) - VCP 视觉联觉协议插件：在 DSH 中渲染 Agent 的 HTML 输出 (⭐44)
- [dsh-tui/dsh-tui](https://github.com/dsh-tui/dsh-tui) - 基于 pi-tui 构建的 Claude Code 风格 DSH 终端 UI，out-of-tree 插件包 (⭐31)
- [lehhair/dsh-diff-viewer](https://github.com/lehhair/dsh-diff-viewer) - DSH Web GUI PiUI 风格 diff 查看器：通过 ui-tool diff-card 链式槽位替换默认 DiffBlock（含 host 补丁） (⭐27)
- [magian1127/deepseek-harness-zh_pro](https://github.com/magian1127/deepseek-harness-zh_pro) - DSH 综合性中文增强插件：界面补全中文化、思考过程显示、会话归档/删除/多选管理、服务监控与模型请求中文化 (⭐26)
- [yyyyukari/dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) - Steam 创意工坊式 DSH Web UI 插件浏览器：零服务器、GitHub 驱动搜索、热度/飙升窗口、双语翻译与分级预检的一键安装/更新/卸载 (⭐25)

<a id="themes-appearance"></a>

## 🎨 主题与外观

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) - 适用于 DeepSeek Harness 的鲸鱼娘系列皮肤 (⭐1749) 🛡️QC:25 🔴
- [WYH66666666/DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - 高自由度玻璃质感主题：模糊度/磨砂度/背景自由调节，不改 DSH 源码 (⭐387) 🛡️QC:53 🟡
- [elysia395/dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine) - 把本机 Wallpaper Engine 壁纸变成 DSH 网页界面背景：Video 动态播放、Web 以 iframe 加载、Scene 壁纸静态帧 (⭐220)
- [d-dev0101/open-sea-skin](https://github.com/d-dev0101/open-sea-skin) - WebGPU 海洋皮肤：DSH 专属 Chrome/Edge 扩展、静态安装器与原生集成 (⭐193) 🛡️QC:58 🟡
- [ggbond2424648901/deep-whale-day-night-theme](https://github.com/ggbond2424648901/deep-whale-day-night-theme) - 完整 Deep Whale 昼夜主题 UI 包，含鲸鱼主视觉 (⭐107) 🛡️QC:66 🟡
- [RevolutionLA/dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) - 换肤/壁纸/主题包插件：8 套 Mirage 主题、每用户强调色、主题包导入导出与收藏 (⭐133) 🛡️QC:67 🟡
- [oil-oil/dsh-theme](https://github.com/oil-oil/dsh-theme) - 实时主题编辑器：精选调色板与字体排印控制 (⭐40) 🛡️QC:66 🟡
- [147228/dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) - 夕小瑶 × DSH Web 皮肤合集、安装器与社区创作工具链 (⭐24) 🛡️QC:33 🟠
- [kingao294/dsh-skin](https://github.com/kingao294/dsh-skin) - 皮肤切换器 + 自定义壁纸 (⭐19) 🛡️QC:64 🟡
- [nevertoday/dsh-theme-plugin](https://github.com/nevertoday/dsh-theme-plugin) - 中国传统色 DeepSeek Harness 主题包 (⭐21) 🛡️QC:72 🟢
- [LAN-TINA-WS/dsh-gui-customization](https://github.com/LAN-TINA-WS/dsh-gui-customization) - DSH 时装工坊：主题配色/自定义背景/视频背景/可调氛围灯，中英双语 (⭐17) 🛡️QC:33 🟠
- [suzike/freestyle-dsh-theme](https://github.com/suzike/freestyle-dsh-theme) - OKLCH 主题提案 + 主题设计器，跨重启持久化 (⭐12) 🛡️QC:59 🟡
- [Tommy00748/dsh-theme-cyberpunk2077](https://github.com/Tommy00748/dsh-theme-cyberpunk2077) - Cyberpunk 2077 / 夜之城主题：CRT 扫描线、Kiroshi 锁定、打字机特效 (⭐25) 🛡️QC:61 🟡
- [LaplaceYoung/dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) - QQ2006 怀旧皮肤：注册 qq2006 主题、镜像 body[data-ds-skin]、完整素材与全局皮肤表 (⭐27) 🛡️QC:67 🟡
- [yunxiiQwQ/dsh-maid-whale-webUI](https://github.com/yunxiiQwQ/dsh-maid-whale-webUI) - DSH Web UI 鲸鱼女仆主题 (⭐25) 🛡️QC:25 🔴
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - 终末地官网风格的 DSH Web 主题：奶油纸底、墨黑文字、信号黄强调、全直角工业编辑风 (⭐64)
- [HeiGeAi/deepseek-harness-skin](https://github.com/HeiGeAi/deepseek-harness-skin) - DSH 换肤系统：21 套内置皮肤 + 一张图生成整套配色的自定义皮肤，数据源驱动、保对比度推导、构建期校验可读性 (⭐51)
- [Ewnscat-ya/dsh-client-ui-skin-denia](https://github.com/Ewnscat-ya/dsh-client-ui-skin-denia) - 鸣潮·达妮娅 (Denia) DSH Web GUI 皮肤「虚无之泡」：双形态亮/暗、侧边立绘、玻璃卡片与浮动泡泡粒子 (⭐32)
- [niiang/dsh-kimino-theme](https://github.com/niiang/dsh-kimino-theme) - 《你的名字。》新海诚风格 DSH Web GUI 主题 (⭐28)
- [10086ggqq/dsh_theme_terraria](https://github.com/10086ggqq/dsh_theme_terraria) - 泰拉瑞亚像素世界主题：把 DSH 变成像素风控制台，向导陪你写代码，真实对话、工具审批、难度切换，单文件零依赖 (⭐27)
- [NoNameLeGo/dsh-catppuccin-theme](https://github.com/NoNameLeGo/dsh-catppuccin-theme) - DSH Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 一键切换，内置可开关的玻璃质感 (⭐26)
- [yoli-mi/dsh-client-ui-custom](https://github.com/yoli-mi/dsh-client-ui-custom) - 可配置 DSH Web 界面插件：壁纸与磨砂玻璃主题、强调色、自定义快捷键、应用使用面板与历史条，零侵入式修改 (⭐24)

<a id="models-quota"></a>

## 💰 模型与额度

- [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) - 注入器 + 路由标准套件：先装运行时注入器，再装任务感知的推理模式路由器预设（实测优先路由与相变证据） (⭐6785)
- [MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) - 住在 DSH 界面右下角的小鲸鱼娘余额监视器：拖拽吸附、数字滚动动画，随界面自动启用 (⭐1487)
- [V1ki/dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) - 把 ChatGPT (Codex)、Claude、Grok (X Premium) 订阅直接当作 DSH 的 LLM 提供商：Web UI 内 OAuth 登录，无需 API Key (⭐283)
- [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) - 会话成本计量插件：会话/每日花费、预算与历史记录 (⭐233)
- [Mars-Sea/dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider) - 非官方 Command Code LLM 提供商插件：实时模型目录、推理档位支持与 Models 页卡片，移植自 pi-commandcode-provider (⭐133)
- [feibi-mochi/deepseek-harness-wallet](https://github.com/feibi-mochi/deepseek-harness-wallet) - 余额监控、会话级花费与 Token 追踪 (⭐65) 🛡️QC:58 🟡
- [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) - ChatGPT OAuth 与 Codex 模型接入 (⭐69) 🛡️QC:68 🟡
- [LiangYin233/dsh-provider-model-configurator](https://github.com/LiangYin233/dsh-provider-model-configurator) - DSH 模型 Pro：一键应用 pi-ai 预设或任意提供商的模型上下文、输出上限、推理档位与兼容开关，集中管理模型条目 (⭐20) 🛡️QC:69 🟡
- [yxxbc/dsh-balance-plugin](https://github.com/yxxbc/dsh-balance-plugin) - DeepSeek 余额监控与用量统计（DSH Cordis 插件）：余额监控 · 官方充值入口 · 用量统计 · 三方插件管理 (⭐57)
- [BeforeWave/dsh-with-chatgpt](https://github.com/BeforeWave/dsh-with-chatgpt) - 把 ChatGPT 的推理能力带到本地代码库：直接工作，或把大型任务委派给 DSH (⭐38)
- [amlyczz/dsh-agy-link](https://github.com/amlyczz/dsh-agy-link) - Google Antigravity (agy CLI) 模型桥接插件：多账号智能池化、流式对话/思考/工具活动/用量，界面内 Google OAuth 登录 (⭐31)
- [WSL043/dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) - 把 ChatGPT / Codex 订阅直接接入 DSH：OAuth 登录、模型、搜索、额度与图片生成，无需 API Key 或 Codex CLI (⭐31)
- [Axiaohungry/dsh-llm-codebuddy](https://github.com/Axiaohungry/dsh-llm-codebuddy) - 在 DSH 中使用 WorkBuddy API 作为 LLM 提供商（当公司只提供 WorkBuddy 积分时的选择） (⭐28)
- [kenz1117/dsh-ui-usage-billing](https://github.com/kenz1117/dsh-ui-usage-billing) - DSH 用量计费仪表盘插件：侧边栏成本指标、从会话日志聚合真实用量、内置多提供商价目表 (⭐28)

<a id="testing-qa"></a>

## 🧪 测试与质检

- [herdeny/dsh-qc](https://github.com/herdeny/dsh-qc) - DSH 插件质量检测 CLI，支持静态分析与动态验证 (⭐2)
- [vostride/agent-qa](https://github.com/vostride/agent-qa) - 开源自进化 QA 代理：自然语言写测试，自动捕获 Web/移动端回归，支持 DSH (⭐952) 🛡️QC:16 🔴
- [omdsh-dev/dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) - 用于构建和测试 DSH 插件的 Agent Skills (⭐12) 🛡️QC:17 🔴
- [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) - 提供 `test_run` 能力的结构化测试运行器 (⭐2) 🛡️QC:53 🟡
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 支持实时刷新的 DSH 插件目录 (⭐49) 🛡️QC:23 🔴
- [zimodzh/dsh-plugin-dev-skills](https://github.com/zimodzh/dsh-plugin-dev-skills) - 开发 DSH 插件的 Agent Skill：覆盖插件/服务/事件/工具/LLM 适配器/打包安装标准，兼容 Claude Code、Codex、DSH 等 (⭐40)
- [oil-oil/build-deepseek-harness-plugin](https://github.com/oil-oil/build-deepseek-harness-plugin) - 面向已安装 DSH 插件的构建 Agent Skill：slots、Typert remotes 与凭据处理 (⭐39)
- [win4r/deepseek-harness-plugin-creator](https://github.com/win4r/deepseek-harness-plugin-creator) - 可复用的 Codex Skill：构建并校验 DeepSeek Harness 与 Cordis 插件 (⭐30)

<a id="examples-templates"></a>

## 📦 示例与模板

- [bugmaker2/dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) - DeepSeek Harness 插件开发模板 (⭐82) 🛡️QC:66 🟡
- [sunshine-lang/dsh-plugin-template](https://github.com/sunshine-lang/dsh-plugin-template) - 可直接发布的插件骨架，包含打包格式与工具注册示例 (⭐6) 🛡️QC:58 🟡
- [omdsh-dev/plugin-template](https://github.com/omdsh-dev/plugin-template) - 基于 Turtle UI 官方仓库构建的插件模板 (⭐12) 🛡️QC:64 🟡
- [onezero-y/dsh-plugin-kit](https://github.com/onezero-y/dsh-plugin-kit) - 集成 Agent Skills 与可运行模板的插件开发套件 (⭐3) 🛡️QC:25 🔴
- [adpanru/cordis-mini](https://github.com/adpanru/cordis-mini) - 约 600 行纯 Python 还原 Cordis/deepseek-harness 核心插件架构：插件系统、Context 服务注册、依赖拓扑、事件分发与 Waterfall 中间件（教学项目，内置 Fake LLM） (⭐30)

<a id="sessions-messages"></a>

## 💬 会话与消息

- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - 跨预设会话迁移插件：固定结构交接保留状态、源模型意图与未解决图像，迁移前可预览 (⭐163)
- [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) - 导入 14+ 外部 Agent 聊天记录（Claude Code、Codex、ChatGPT、Cursor、Gemini、DSH 等）为可续聊会话 (⭐126)
- [THEWOLFWALKER/dsh-notifier](https://github.com/THEWOLFWALKER/dsh-notifier) - 统一通知推送插件：一个 notify() API，8 个渠道适配器（Telegram/钉钉/飞书/微信推送/Bark/Webhook 等），自动与手动双触发 (⭐80)
- [anionex/dsh-turn-rewind](https://github.com/anionex/dsh-turn-rewind) - 对话与代码状态回退插件，可重放历史回合 (⭐102) 🛡️QC:74 🟢
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) - AI 回复自定义表情，支持 B 站、小红书、贴吧等多平台表情包 (⭐42) 🛡️QC:77 🟢
- [Chinesezjc/dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) - DSH 跨实例消息/事件交接插件：interconnect 服务与工具，打通多个 DSH 实例 (⭐35)
- [taxueseek/dsh-files](https://github.com/taxueseek/dsh-files) - 双面文件插件：会话隔离的文件上传（彩色 composer 卡片）+ read_document 工具（文本/PDF/DOCX/XLSX，内容嗅探与 LRU 缓存），原生图片直传视觉模型 (⭐29)
- [lsz-asd/dsh-plugin-session-delete](https://github.com/lsz-asd/dsh-plugin-session-delete) - 从 UI 删除 DSH 会话：头部危险按钮 + 侧栏会话菜单项，风险确认对话框、先停止运行中的 Agent、列表原地刷新 (⭐28)
- [Walvez/dsh-codex-sync](https://github.com/Walvez/dsh-codex-sync) - OpenAI Codex 与 DSH 的双向桥接：聊天双向同步、Skills 实时挂载与 MCP 自动镜像 (⭐25)

<a id="just-for-fun"></a>

## 🎮 趣味

- [Minglink/dsh-infinite-gen-3](https://github.com/Minglink/dsh-infinite-gen-3) - DeepSeek 专用「无限三代」破甲插件：稳定化破甲提示词 (⭐793)
- [Minglink/dsh-infinite-gen-2](https://github.com/Minglink/dsh-infinite-gen-2) - DeepSeek 专用「无限二代」插件：稳定化破甲提示词 (⭐660)
- [yejiming/MuseAI](https://github.com/yejiming/MuseAI) - 创建 AI 角色、进入故事世界：聊天、冒险、穿书，支持 DeepSeek Harness 插件 (⭐590) 🛡️QC:38 🟠
- [hewzhew/dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) - SillyTavern 迁移与新一代 DSH Agent 角色扮演插件 (⭐190)
- [cocofhu/anime-find](https://github.com/cocofhu/anime-find) - DSH 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力 (⭐155)
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - Web UI 右侧小游戏面板：18 款离线小游戏 (⭐27) 🛡️QC:63 🟡
- [dhicoc/dsh-chinese-traditional-wisdom-skill](https://github.com/dhicoc/dsh-chinese-traditional-wisdom-skill) - 「玄枢」中华传统智慧技能包：八字/紫微/六爻/梅花/奇门/风水等本地确定性引擎 + 可视化 Dashboard (⭐30)

<a id="mcp-integrations"></a>

## 🧩 MCP 与集成

- [agentrq/agentrq](https://github.com/agentrq/agentrq) - 人机协同的实时对话式任务管理器：自托管，移动/Web/桌面随时控制你的 Agent（ACP/MCP） (⭐1081) 🛡️QC:17 🔴
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) - AgentTeams 插件：为 DeepSeek Harness 组建与管理多 Agent 团队 (⭐1233) 🛡️QC:64 🟡
- [Lum1104/dsh-browser](https://github.com/Lum1104/dsh-browser) - Chrome 侧边栏扩展，让 DSH 无需视觉能力即可直接操控浏览器 (⭐539) 🛡️QC:28 🔴
- [liustack/modsearch](https://github.com/liustack/modsearch) - DSH 网页搜索插件：全模式通用的搜索桥接能力 (⭐328)
- [Utopia-V/mixagents](https://github.com/Utopia-V/mixagents) - Harness 原生 Agent 组件：为 Codex 与 Pi 提供 DeepSeek V4 Flash 子代理与 V4 Pro 的 DSH Minimal 模拟 (⭐177)
- [ZSeven-W/dsh-ios](https://github.com/ZSeven-W/dsh-ios) - 对话内接入实时 iOS 模拟器与 USB 连接的 iPhone：22 个 Agent 工具，可启动、构建、按无障碍标识驱动 UI 与 OCR 文本操作 (⭐257)
- [anysearch-team/anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) - AnySearch 网页搜索提供商与高级搜索工具，为 DSH 接入多源搜索 (⭐389)
- [mrpulor-gh/nuphus-mcp](https://github.com/mrpulor-gh/nuphus-mcp) - 桌面自动化 MCP 服务器：屏幕、窗口、键鼠与 Chrome 控制，任何 AI Agent 通用 (⭐281)
- [weijiafu14/pi2dsh](https://github.com/weijiafu14/pi2dsh) - 打通 Pi 与 DSH 生态：一套 Pi Host ABI 即可把 Pi 扩展原样跑成原生 DSH 插件 (⭐170)
- [toolclub/dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui) - 持久化多模型工作流团队：动态主导规划、有界 DAG、每 Agent 独立模型/工具，附 Run Center 与 Token 洞察 (⭐162)
- [ZSeven-W/dsh-android](https://github.com/ZSeven-W/dsh-android) - 对话内接入实时 Android 模拟器与 USB 设备：构建、运行并驱动设备 UI（与 dsh-ios 同系列） (⭐129)
- [omdsh-dev/dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) - 连接 DSH 与数据库，进行对话式数据分析并产出可执行的业务洞察 (⭐171)
- [Mr-potato-123/dsh-mcp](https://github.com/Mr-potato-123/dsh-mcp) - 把 dsh 变成 MCP 服务器：让 Claude Code / Codex 等更快、更强、更省钱 (⭐118)
- [Tabbit-Browser/dsh-tabbit](https://github.com/Tabbit-Browser/dsh-tabbit) - Tabbit 浏览器插件：让 DSH 通过 Tabbit 浏览器自动化操控网页 (⭐92)
- [ZSeven-W/dsh-crew](https://github.com/ZSeven-W/dsh-crew) - 从 Claude Code / Codex 向 DSH Agent 派发任务，原生子代理进度汇报 (⭐116) 🛡️QC:54 🟡
- [DDDMUC/dsh-free-search](https://github.com/DDDMUC/dsh-free-search) - 免费网页搜索提供商：DuckDuckGo 后端，无需 API Key (⭐96)
- [wxkingstar/SpecFusion](https://github.com/wxkingstar/SpecFusion) - 在 DSH / Claude Code / Cursor / Codex / Gemini CLI 里直接搜索 20 个中国开放平台 65,600+ 篇 API 文档，零配置 (⭐58)
- [PKUfudawei/dsh-capability-menu](https://github.com/PKUfudawei/dsh-capability-menu) - 统一能力菜单：按 Exposed / Progressive / Blocked 三档管理 MCP 工具与技能的能力暴露级别与执行模式 (⭐76)
- [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) - 官方 DSH MCP 客户端管理控制台：/mcp 命令带健康诊断与流水线试调用 (⭐50)
- [wp-a/nature-academic-search](https://github.com/wp-a/nature-academic-search) - 学术论文检索 Skill + MCP：面向中文科研用户，跨 CrossRef/PubMed/arXiv/OpenAlex/Europe PMC 检索去重，支持 MeSH、引用核验与引文图谱 (⭐153)
- [miniLV/Plexus](https://github.com/miniLV/Plexus) - 一键同步 MCP / Skills / Rules 到 Claude Code、Codex、DSH、Cursor、Gemini CLI、Qwen Code 等 Agent 工具的本地配置控制台 (⭐28)
- [limuyang2/agent-team](https://github.com/limuyang2/agent-team) - 在 DSH 内组建多 Agent 团队：每位成员独立模型/技能/MCP 工具/上下文 + 共享工作区，支持 Leader 指派与独立会话 (⭐27)
- [EdgeTypE/dsh-better-deepseek](https://github.com/EdgeTypE/dsh-better-deepseek) - Better DeepSeek Chrome 扩展的 DSH 桥接插件：经 webServer 提供 HTTP 握手端点与会话级 SSE 事件流 (⭐25)
- [A3Boy/dsh-web-tools](https://github.com/A3Boy/dsh-web-tools) - 多提供商 Web 搜索与抓取插件：8 个深度适配的提供商、SearchHints、弹性回退，原生支持 X / 小红书检索 (⭐24)

<a id="memory-context"></a>

## 🧠 记忆与上下文

- [zilliztech/memsearch](https://github.com/zilliztech/memsearch) - 面向所有 AI Agent（Claude Code / Codex / DSH 等）的持久统一记忆层，基于 Markdown 与 Milvus (⭐2503)
- [adoresever/graph-memory](https://github.com/adoresever/graph-memory) - 知识图谱记忆插件：从对话提取结构化三元组，压缩上下文 75%，跨会话复用经验 (⭐587) 🛡️QC:33 🟠
- [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) - 一站式上下文可视化与管理：Context 面板/浏览器/命令，透视上下文组成、演进、压缩与剪枝 (⭐1208) 🛡️QC:59 🟡
- [mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon) - LLM 监督的持久记忆：图召回 + 跨会话知识，单二进制，兼容 DSH 与任意 Agent 运行时 (⭐530) 🛡️QC:38 🟠
- [syncable-dev/memtrace-public](https://github.com/syncable-dev/memtrace-public) - 代码库结构化记忆：双时态知识图谱，MCP 原生、零 LLM 调用，毫秒级查询 (⭐454) 🛡️QC:25 🔴
- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) - 跨会话长期记忆 + 后台自我进化，五轨记忆 · git 分版本 (⭐251) 🛡️QC:31 🟠
- [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema) - Noema 长期记忆插件：持久、可检视的 Agent 记忆，带召回工具与设置页 (⭐126) 🛡️QC:64 🟡
- [seriousz158/dsh-memory](https://github.com/seriousz158/dsh-memory) - 本地 Git 长期记忆插件：记忆存于本地 Git 仓库，设置页双确认清除，含空闲会话同步器与路径安全防护 (⭐152)
- [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) - 跨 Agent、本地优先的持久记忆插件 (⭐303) 🛡️QC:59 🟡
- [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) - 有界、分层、审批门控、可审计的跨会话记忆 (⭐78) 🛡️QC:70 🟢
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) - 持久化、自动整合的记忆插件 (⭐68) 🛡️QC:17 🔴
- [aik358/dsh-auto-memory](https://github.com/aik358/dsh-auto-memory) - 三层自动记忆（用户级/项目笔记/每日日志）自动注入与检索 (⭐44) 🛡️QC:61 🟡
- [Phant0Meow/dsh-meow-memory](https://github.com/Phant0Meow/dsh-meow-memory) - 跨会话记忆插件：七层 SQLite 记忆库（灵魂/用户/项目/事实/课程/话题/规则）+ BM25 检索 (⭐64)
- [FuRongJun-1999/dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) - 白箱 AGI 架构探索：元认知、持续学习、世界模型、自我改进，零 LLM 白箱管线与可审计信任护栏 (⭐86)
- [Tyan66666/billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) - 模型驱动的上下文管理（Active Context Pruning / ACP）：由模型决定何时压缩什么，为 DSH 撑起超大上下文 (⭐62)
- [Qinling-Melon-Farmers/dsh-memoir](https://github.com/Qinling-Melon-Farmers/dsh-memoir) - DSH 本地优先跨会话项目记忆：零内置运行时依赖、有界 Hot Memory、BM25 召回/缓存、来源溯源与双语 Web GUI (⭐24)

<a id="security-audit"></a>

## 🔒 安全与审计

- [lire1131/dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint) - DSH 崩溃救援插件：撤销配置与插件代码改动、密钥安全快照、一键 SAFE MODE；DSH 无法启动时也有离线 CLI/GUI (⭐131)
- [micromilo/upstream-radar](https://github.com/micromilo/upstream-radar) - DSH 插件安全与依赖监控 (⭐9) 🛡️QC:41 🟠
- [jkrandom-sudo/dsh-plugin-audit](https://github.com/jkrandom-sudo/dsh-plugin-audit) - 插件静态权限审计 (⭐5) 🛡️QC:51 🟡
- [nanshan1995/dsh-plugin-market](https://github.com/nanshan1995/dsh-plugin-market) - 插件市场：安装前静态安全审计闸门 (⭐3) 🛡️QC:55 🟡
- [PerryLink/dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) - Claude Code 风格声明式权限规则：有序 allow/deny/ask + 工具/参数/路径匹配，会话日志审计与热重载 (⭐87)
- [xiajiajun516/dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) - DSH 备份与恢复插件：导出/导入/迁移/同步完整配置、插件、MCP 服务器、技能与工作区，一键迁移到新机器 (⭐58)
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - 企业级 FDE Harness 层：24 条 git-diff 审计规则、自动快照回滚、规则注入与自进化，以 9 个 DSH 插件 + MCP 服务器（79 工具）交付 (⭐41)
- [Zhenyu98/dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) - DSH 上下文注入审计插件：统计 AGENTS.md 指令链/技能目录/工具 schema 的 token 成本，检测重复与冲突；Web UI 圆环面板 + context_audit 工具 (⭐28)

<a id="desktop-clients"></a>

## 💻 桌面与客户端

- [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) - DSHDesktop：DeepSeek Harness 桌面版 (⭐3546)
- [zouyuxuan122/DSH-Desktop-EAC](https://github.com/zouyuxuan122/DSH-Desktop-EAC) - DSH Windows/Linux 桌面客户端：内置 Node.js + dsh CLI，一键启动，10 款内置 UI 皮肤 (⭐1445) 🛡️QC:0 🔴
- [dsh-tauri-desk/deepseek-harness-desktop](https://github.com/dsh-tauri-desk/deepseek-harness-desktop) - DeepSeek Harness Tauri 桌面版：仅 5MB 安装包、零环境配置、预置插件，支持 Windows/macOS/Linux (⭐1490) 🛡️QC:38 🟠
- [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) - 本地 AI 桌面工作空间：DSH 会话、项目、文件、联网研究、插件与 Office 文档 (⭐631) 🛡️QC:18 🔴
- [op7418/pilot-harness](https://github.com/op7418/pilot-harness) - CodePilot 风格桌面客户端与插件套件：为 DeepSeek Harness 打造，支持 macOS/Windows/Linux (⭐240)
- [lencx/Minke](https://github.com/lencx/Minke) - 🐳 DeepSeek Harness 桌面客户端 (⭐554) 🛡️QC:28 🔴
- [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) - GenUI：交互式 UI 组件渲染 (⭐384) 🛡️QC:52 🟡
- [QCYTSN/dsh-dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - 桌面原生大鱼（BigFish）陪伴应用：实时显示 Agent 状态，Windows 置顶常驻 (⭐262)
- [whitelonng/dshcode](https://github.com/whitelonng/dshcode) - 社区桌面伴侣：macOS/Windows 一键启动的 Electron 应用 (⭐603)
- [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) - DSH 桌面端：支持主题与背景图等多种个性化配置的 Electron 外壳 (⭐150)
- [bruc3van/dsh-desktop](https://github.com/bruc3van/dsh-desktop) - 主打安全、更尊重开发者的开源 DSH 桌面客户端：官方 Web UI、长任务常驻托盘、通知推送，内置安全市场 600+ 精选插件先审查再安装 (⭐76)
- [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop) - Windows 桌面客户端：零配置安装，内置 Codex/插件/技能/SSH 远程访问与 11 款皮肤 (⭐248) 🛡️QC:11 🔴
- [qiannianhuanxiang/DSHA](https://github.com/qiannianhuanxiang/DSHA) - 安卓启动器：内置 proot+Ubuntu，免 ROOT 免 Termux 一键运行 DeepSeek Harness (⭐349) 🛡️QC:25 🔴
- [WEP-56/DSH-Launcher](https://github.com/WEP-56/DSH-Launcher) - webui 内嵌式启动器：包管理/配置管理/插件管理，兼容所有 webui 强化插件 (⭐28) 🛡️QC:33 🟠
- [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) - 基于 DSH 插件机制的多端远程访问方案：桌面端与 Android 端安全连接并操作远程 Harness (⭐133)
- [Astro-Han/pawwork](https://github.com/Astro-Han/pawwork) - 免费开源桌面 AI Agent（macOS/Windows）：基于 DeepSeek Harness 构建，内置免费模型、免 API Key 免终端，支持 Office 文件、联网搜索与定时自动化 (⭐111)
- [FlashingChen/dsh-desktop-hub](https://github.com/FlashingChen/dsh-desktop-hub) - DSH Desktop Hub 桌面管理控制台（Electron + TypeScript）：多 Tab 管理 Harness / Plugin / MCP / Skills，双击即用 (⭐56)
- [Clarklevis1995/dsh-mobile](https://github.com/Clarklevis1995/dsh-mobile) - DeepSeek Harness 原生 iOS 客户端：通过 dsh-plugin-mobile-gateway 以 WebSocket 连接 Harness，把工作区、会话与 Agent 执行轨迹带到 iPhone (⭐83)
- [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) - DSH 远程工作助手：SSH（密钥或密码）连接远端工作区，rw_* 工具操作，SFTP 镜像到本地 DSH 工作区 (⭐48)
- [Nexus-Aethra/DSHBox](https://github.com/Nexus-Aethra/DSHBox) - 本地 DSH 容器化管理桌面：隔离运行多个 DSH 版本、内嵌 WebView、一键导入插件/技能，队列化安装带实时日志 (⭐30)
- [liguobao/dsh-desktop](https://github.com/liguobao/dsh-desktop) - 独立开源 DSH 桌面包装器：本地启动官方 Web UI，并以加固的 Electron 窗口加载，支持 Linux/macOS/Windows (⭐28)
- [See-Sol-Lab/DeepSeekGUI](https://github.com/See-Sol-Lab/DeepSeekGUI) - DeepSeek Harness Windows 桌面客户端：V1 封装官方 Web UI，V2 独立工作台开发中 (⭐27)

<a id="platforms-channels"></a>

## 🌐 平台与渠道

- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) - DSH 内置可视化插件市场：浏览、搜索、一键安装 (⭐2929) 🛡️QC:64 🟡
- [Nagi-ovo/dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) - 帮 DSH 搜索、安装并验证 GitHub 插件的 Skill (⭐160)
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 插件市场：在 Web GUI 中一键浏览、安装与更新 GitHub 插件 (⭐147)
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - 经过验证的 DeepSeek Harness 插件双语目录 (⭐17) 🛡️QC:25 🔴
- [AdamPlatin123/dsh-plugin-radar](https://github.com/AdamPlatin123/dsh-plugin-radar) - 开源 DSH 插件生态雷达：自动发现 15900+ 候选、k8s 运行级实测 10000+、15 分钟快照管线，插件目录为自动生成产物 (⭐1432)
- [runzhliu/deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) - 社区 Docker/Kubernetes 打包：加固镜像、Compose 栈、Helm Chart、Web UI 与 headless CLI 一键部署 (⭐54)
- [AwesomeHou/dsh-plugin-marketplace](https://github.com/AwesomeHou/dsh-plugin-marketplace) - DSH 插件市场：实时同步 GitHub dsh-plugin topic（1800+ 仓库）为可搜索、可翻页的设置页，一键安装并内置 market_search / market_install 工具 (⭐27)
- [techysy/deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) - DeepSeek Harness fnOS 应用：NAS 本地常驻服务，一键部署官方 Agent 浏览器 UI (⭐27)
- [PGZXB/dsh-feishu](https://github.com/PGZXB/dsh-feishu) - DeepSeek Harness 的飞书 UI：面板驱动控制台，斜杠命令变卡片按钮、卡内审批与提问、流式卡片，扫码一键配置 (⭐26)

<a id="ecosystem"></a>

## 🌱 生态项目 / Ecosystem

与 DSH 生态相关但不是标准插件（无 cordis 插件清单）的项目，QC 评分为 0 属正常。

- [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) - 为 DSH 插件生态打造的现代化桌面端解决方案 (⭐22068)
- [crafter-station/petdex](https://github.com/crafter-station/petdex) - Codex、Claude Code、DSH 等平台的动画宠物画廊 (⭐3842)
- [devin-axis/ipollowork](https://github.com/devin-axis/ipollowork) - 集成自进化 Agent 运行时的下一代 AI 工作空间 (⭐5285)
- [huangruiteng/loopx](https://github.com/huangruiteng/loopx) - Long-horizon Agent 控制平面：跨 Codex、Claude Code、dsh 等 Harness 提供持久状态、目标门控、治理与恢复，含 dsh goal-mode 适配器 (⭐5385)
- [haohao-end/openagent](https://github.com/haohao-end/openagent) - 融合 OpenAI Deep Research 与 Dify 的一体化平台 (⭐788)
- [nexu-io/open-design](https://github.com/nexu-io/open-design) - 开源 Claude Design 替代方案，提供 DSH 设计能力 (⭐87154)
- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) - 集成 MCP 工具的开源 CMA 兼容 Agent 运行时 (⭐596)
- [whiteguo233/openbiliclaw](https://github.com/whiteguo233/openbiliclaw) - 本地私有、自进化跨平台 AI 内容发现 Agent (⭐2932)
- [xiufengsun/tokentracker](https://github.com/xiufengsun/tokentracker) - 本地优先的 AI Token 用量与成本追踪器，支持 31 种编程工具 (⭐1476)
- [zhayujie/cowagent](https://github.com/zhayujie/cowagent) - 开源超级 AI 助手与 Agent Harness (⭐46523)
- [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) - DSH Web UI 的插件与皮肤合集 (⭐6660)
- [text2future/flowix](https://github.com/text2future/flowix) - 本地优先的 Markdown 笔记应用：笔记即 Agent 记忆，内置 DSH 插件 dsh-flowix-memory（MCP & CLI） (⭐374)
- [firstintent/ccteam](https://github.com/firstintent/ccteam) - 多 Agent 编排：把 Claude Code / Codex / Grok / Kimi / DeepSeek Harness 组成一个团队，任意会话派发与回收任务 (⭐347)
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - 自进化记忆操作系统：超持久记忆、混合检索、跨任务技能复用，实测节省 35.24% Token，支持 DeepSeek Harness（本地/云端插件） (⭐10763)
- [Nagi-ovo/voyager](https://github.com/Nagi-ovo/voyager) - Gemini / AI Studio / Claude / ChatGPT 增强套件 + 通用 Web UI 提示词管理器，DeepSeek Harness 同样适用 (⭐19647)
- [PM-Shawn/Abu-Cowork](https://github.com/PM-Shawn/Abu-Cowork) - 开源 Claude Cowork 替代：本地优先 AI Agent 桌面应用，多模型、自进化技能，集成 DeepSeek Harness (⭐334)
- [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) - 开源社区驱动的 Agent Harness，原生支持 DeepSeek Harness（DSH） (⭐40828)
- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) - DeepSeek 原生终端 AI 编程代理，围绕前缀缓存稳定性设计，支持 DSH (⭐34868)
- [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) - Harness Engineering 零基础教程：从 0 到 1 上手 (⭐14104)
- [paean-ai/deeptide](https://github.com/paean-ai/deeptide) - 为 DeepSeek 打造的 Swift 原生 macOS 编程代理，支持 DSH 插件 (⭐1085)
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) - DeepSeek Harness 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例（中英双语） (⭐692)
- [hikariming/dshfind](https://github.com/hikariming/dshfind) - DSH 原理学习、插件市场与最佳实践：由浅入深理解 Harness 与插件生态 (⭐228)
- [zhaoolee/notes](https://github.com/zhaoolee/notes) - 开源版锤子便签：复刻锤科美学，一键 Docker 私有化部署，支持 skill 调用与 dsh plugin (⭐148)
- [cocode-agency/cocode](https://github.com/cocode-agency/cocode) - 开箱即用的 DeepSeek Harness 发行版：DSH 桌面 GUI、终端 TUI 与 Harness 集成 (⭐152)
- [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) - HarnessRouter 社区版：自托管、Apache-2.0 的统一 Harness 接口，一套 API 跑 Codex / Claude Code / Hermes / PI / DSH，实现 Unified Harness Protocol (⭐650)
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo) - 原版 Agent meta-harness：多智能体 swarm 部署、自适应记忆与自学习、RAG 集成，原生支持 Claude Code / Codex / Hermes 等并集成 DSH 插件 (⭐69621)
- [sandbaseai/deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) - Agent 优先的 DeepSeek Harness 深度手册：运行时、插件、MCP、沙箱、评测与故障排查（多语言） (⭐103)
- [HenryZ838978/deepseek-harness](https://github.com/HenryZ838978/deepseek-harness) - 协议层验证 harness：Python witness stack 后验验证 + dsh doctor --node 探针，让协议保持诚实 (⭐47)
- [huiliyi37/oh-my-tianshu](https://github.com/huiliyi37/oh-my-tianshu) - 完全体开源 coding agent：DSH 友好 MIT fork，以插件组合带来视觉、跨会话记忆、验证门、Agent 路由与语义代码检索 (⭐38)

<a id="official-resources"></a>

## 官方资源 / Official resources

- [DeepSeek Harness 主仓库](https://github.com/deepseek-ai/deepseek-harness) - 源代码、发布记录与项目说明
- [DeepSeek Harness 官方文档](https://github.com/deepseek-ai/deepseek-harness/tree/master/docs) - 官方仓库中的开发与架构文档

<a id="contributing"></a>

## 贡献指南 / Contributing

欢迎通过 Pull Request 推荐新插件、更新星标数或修正失效链接。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并确认项目符合本列表的收录标准。

## 许可证 / License

本项目采用 [MIT License](LICENSE)。
