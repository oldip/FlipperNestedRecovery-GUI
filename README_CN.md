# FlipperNestedRecovery GUI

[English Version](README.md) | [繁體中文](README_TW.md)

## 更新日志

### 2.0 版本
- **实时显示操作进度**：现在操作过程中可以实时显示进度，用户可以随时查看当前状态。
- **修复了一些已知问题**：包括在某些情况下调试模式下的非预期行为。

### 1.0 版本
- 初始发布版本，包含基本的 FlipperNestedRecovery 操作功能。

---

FlipperNestedRecovery GUI 是一个用于执行 FlipperNestedRecovery 工具的图形用户界面（GUI），简化了操作流程，使用户可以轻松地通过 GUI 运行 FlipperNestedRecovery。该软件适用于不熟悉 Python、不熟悉命令行操作或遇到安装问题的用户。

## 特性

- **运行 FlipperNestedRecovery**：通过图形界面操作 FlipperNestedRecovery 工具。
- **指定 UID 和端口**：用户可以通过界面输入目标卡片的 UID 和 Flipper 设备的通信端口。
- **实时显示操作进度**：现在可以实时显示操作的当前进度，让用户随时了解操作状态。
- **调试模式和保存 Nonces**：启用调试模式，并选择是否保存 Nonces 文件。
- **多语言支持**：支持简体中文、繁体中文和英文界面。

## 使用指南

### 1. 下载与安装

1. 下载最新版本的 FlipperNestedRecovery GUI 2.0。
2. 双击 `FlipperNestedRecovery GUI 2.0.exe` 运行程序。
3. 没啦，还想要多复杂？

### 2. 界面介绍

- **UID**: 请输入需要分析的卡片的唯一标识符，留空则分析所有卡片。
- **端口**: 指定 Flipper 设备的通信端口，留空则使用默认端口。
- **显示进度**: 在操作过程中实时显示进度。用户可以随时查看当前操作状态。
- **启用调试模式**: 勾选此选项以启用调试模式，显示更多调试信息。
- **保存 Nonces**: 勾选此选项以保存 Nonces 和密钥文件。
- **保留 Nonces**: 勾选此选项以在恢复密钥后保留 Flipper Zero 上的 Nonces。
- **Nonces 文件**: 选择一个 `.nonces` 文件来从中恢复密钥。
- **运行**: 点击此按钮开始执行 FlipperNestedRecovery 的操作。
- **停止**: 在操作过程中可以点击此按钮终止操作。
- **关于**: 查看关于本程序的信息。

### 3. 运行与终止

- **运行程序**: 输入必要的参数后，点击 `运行` 按钮，程序将开始执行 FlipperNestedRecovery 工具。由于当前的限制，操作进度无法实时显示，所有结果将在执行完成后显示。
- **终止操作**: 如果需要中止操作，点击 `停止` 按钮，程序将尝试终止所有相关进程。用户在任何时候都可以通过点击 `停止` 按钮来终止当前操作，程序会安全地关闭所有相关进程。

### 4. 注意事项

- **连接 Flipper Zero**: 请确保 Flipper Zero 通过 USB 线连接，并且没有被任何其他软件（例如 `./fbt log`、`qFlipper`、`lab.flipper.net`）占用。
- **检查 Flipper 设备**：使用前，请确保 Flipper Zero 已正确连接，且处于待机状态。

## 特别鸣谢

在此特别感谢以下个人和项目的支持与贡献：

- **宅人改造家**：感谢他提供nonces文件并协助测试，帮助我找出了软件中的一些bug。
- **AloneLiberty**：感谢他开发了原始的[FlipperNestedRecovery](https://github.com/AloneLiberty/FlipperNestedRecovery)工具，本项目基于其工作进行开发。

特别感谢所有在项目开发过程中提供反馈和建议的用户，你们的支持是我们持续改进的动力。

## 免责声明

本软件可能包含缺陷或错误，作者不对本软件的性能或效果作出任何明示或暗示的保证，包括但不限于适销性、特定用途适用性和非侵权性。无论是在合同诉讼、侵权诉讼或其他法律诉讼中，作者均不对因使用或无法使用本软件而导致的任何损害、损失或其他责任负责。