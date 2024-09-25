# FlipperNestedRecovery GUI

[English Version](README.md) | [简体中文](README_CN.md)

## 更新日誌

### 2.0 版本
- **實時顯示操作進度**：現在操作過程中可以實時顯示進度，用戶可以隨時查看當前狀態。
- **修復了一些已知問題**：包括在某些情況下調試模式下的非預期行為。

### 1.0 版本
- 初始發佈版本，包含基本的 FlipperNestedRecovery 操作功能。

---

FlipperNestedRecovery GUI 是一個用於執行 FlipperNestedRecovery 工具的圖形用戶界面（GUI），簡化了操作流程，使用戶可以輕鬆地通過 GUI 運行 FlipperNestedRecovery。該軟體適用於不熟悉 Python、不熟悉命令行操作或遇到安裝問題的用戶。

## 特性

- **運行 FlipperNestedRecovery**：通過圖形界面操作 FlipperNestedRecovery 工具。
- **指定 UID 和端口**：用戶可以通過界面輸入目標卡片的 UID 和 Flipper 設備的通信端口。
- **實時顯示操作進度**：現在可以實時顯示操作的當前進度，讓用戶隨時了解操作狀態。
- **調試模式和保存 Nonces**：啟用調試模式，並選擇是否保存 Nonces 文件。
- **多語言支持**：支持簡體中文、繁體中文和英文界面。

## 使用指南

### 1. 下載與安裝

1. 下載最新版本的 FlipperNestedRecovery GUI 2.0。
2. 雙擊 `FlipperNestedRecovery GUI 2.0.exe` 或者 `FlipperNestedRecovery GUI 2.0.app` 運行程序。
3. 沒啦，還想要多複雜？

### 2. 界面介紹

- **UID**: 請輸入需要分析的卡片的唯一標識符，留空則分析所有卡片。
- **端口**: 指定 Flipper 設備的通信端口，留空則使用默認端口。
- **顯示進度**: 在操作過程中實時顯示進度。用戶可以隨時查看當前操作狀態。
- **啟用調試模式**: 勾選此選項以啟用調試模式，顯示更多調試信息。
- **保存 Nonces**: 勾選此選項以保存 Nonces 和密鑰文件。
- **保留 Nonces**: 勾選此選項以在恢復密鑰後保留 Flipper Zero 上的 Nonces。
- **Nonces 文件**: 選擇一個 `.nonces` 文件來從中恢復密鑰。
- **運行**: 點擊此按鈕開始執行 FlipperNestedRecovery 的操作。
- **停止**: 在操作過程中可以點擊此按鈕終止操作。
- **關於**: 查看關於本程序的信息。

### 3. 運行與終止

- **運行程序**: 輸入必要的參數後，點擊 `運行` 按鈕，程序將開始執行 FlipperNestedRecovery 工具。操作過程中實時顯示進度，所有結果將在執行完成後顯示。
- **終止操作**: 如果需要中止操作，點擊 `停止` 按鈕，程序將嘗試終止所有相關進程。用戶在任何時候都可以通過點擊 `停止` 按鈕來終止當前操作，程序會安全地關閉所有相關進程。

### 4. 注意事項

- **連接 Flipper Zero**: 請確保 Flipper Zero 通過 USB 線連接，並且沒有被任何其他軟體（例如 `./fbt log`、`qFlipper`、`lab.flipper.net`）佔用。
- **檢查 Flipper 設備**：使用前，請確保 Flipper Zero 已正確連接，且處於待機狀態。

## 特別鳴謝

在此特別感謝以下個人和項目的支持與貢獻：

- **宅人改造家**：感謝他提供nonces文件並協助測試，幫助我找出了軟體中的一些bug。
- **AloneLiberty**：感謝他開發了原始的[FlipperNestedRecovery](https://github.com/AloneLiberty/FlipperNestedRecovery)工具，本項目基於其工作進行開發。

特別感謝所有在項目開發過程中提供反饋和建議的用戶，你們的支持是我們持續改進的動力。

## 免責聲明

本軟體可能包含缺陷或錯誤，作者不對本軟體的性能或效果作出任何明示或暗示的保證，包括但不限於適銷性、特定用途適用性和非侵權性。無論是在合同訴訟、侵權訴訟或其他法律訴訟中，作者均不對因使用或無法使用本軟體而導致的任何損害、損失或其他責任負責。