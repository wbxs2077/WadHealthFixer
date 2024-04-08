[中文](https://github.com/wbxs2077/WadHealthFixer/blob/main/README_CN.md) | [English](https://github.com/wbxs2077/WadHealthFixer/blob/main/README.md)
## Wad Health Fixer

Wad Health Fixer 是一个用于修复《英雄联盟》游戏中血条消失问题的工具，该问题通常由损坏的 wad.client 文件引起。该工具自动化修复这些文件的过程，以确保玩家能够顺畅地游戏。

### 依赖项

该项目依赖以下组件：

- [ritobin](https://github.com/moonshadow565/ritobin)：用于转换《英雄联盟》bin文件的工具。
- [cs-lol](https://github.com/LeagueToolkit/cslol-manager)：包含各种用于《英雄联盟》的工具，包括处理 wad.client 文件所需的必要资源。
- [CommunityDragon/Data](https://github.com/CommunityDragon/Data)：提供必要的数据文件，包括哈希值，用于工具的正常运行。

### 编译

该项目使用 Nuitka 进行编译和打包，生成可执行文件（exe），确保在 Windows 平台上轻松部署和使用。

### 使用方法

1. 克隆该存储库到本地计算机。
2. 安装所需的依赖项：ritobin 和 cs-lol。
3. 从 CommunityDragon/Data 下载必要的数据文件。
4. 运行脚本 `wad_health_fixer.py`。
5. 输入包含您要修复的 wad.client 文件的文件夹路径。
6. 按照屏幕上的提示完成修复过程。

### 许可证

该项目基于 [MIT 许可证](LICENSE)。

### 贡献

欢迎贡献！如果您遇到任何问题或有改进建议，请随时提出问题或提交拉取请求。

### 鸣谢

特别感谢 ritobin、cs-lol 和 CommunityDragon/Data 的开发人员，感谢他们为《英雄联盟》社区做出的宝贵贡献。
