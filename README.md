# FlipperNestedRecovery GUI

[繁體中文](README_TW.md) | [简体中文](README_CN.md)

## Changelog

### Version 2.0
- **Real-time Progress Display**: The progress of operations is now displayed in real-time, allowing users to monitor the current status.
- **Bug Fixes**: Addressed known issues, including unexpected behavior in debug mode under certain conditions.

### Version 1.0
- Initial release, including basic operations for FlipperNestedRecovery.

---

FlipperNestedRecovery GUI is a graphical user interface (GUI) for executing the FlipperNestedRecovery tool, simplifying the operation process so users can easily run FlipperNestedRecovery through the GUI. This software is designed for users who are not familiar with Python, command-line operations, or those who encounter installation issues.

## Features

- **Run FlipperNestedRecovery**: Operate the FlipperNestedRecovery tool through a graphical interface.
- **Specify UID and Port**: Users can input the target card's UID and the communication port of the Flipper device via the interface.
- **Real-time Progress Display**: The progress of operations can now be displayed in real-time, allowing users to monitor the current status.
- **Debug Mode and Save Nonces**: Enable debug mode and choose whether to save the Nonces file.
- **Multi-language Support**: Supports Simplified Chinese, Traditional Chinese, and English interfaces.

## User Guide

### 1. Download and Install

1. Download the latest version of FlipperNestedRecovery GUI 2.0.
2. Double-click `FlipperNestedRecovery GUI 2.0.exe` or `FlipperNestedRecovery GUI 2.0.app` to run the program.
3. That's it! No complex steps.

### 2. Interface Introduction

- **UID**: Enter the unique identifier of the card you want to analyze. Leave it blank to analyze all cards.
- **Port**: Specify the communication port of the Flipper device. Leave it blank to use the default port.
- **Show Progress**: Displays the progress of the operation in real-time, allowing you to see the current status.
- **Enable Debug Mode**: Check this option to enable debug mode, displaying more debugging information.
- **Save Nonces**: Check this option to save Nonces and key files.
- **Preserve Nonces**: Check this option to keep the Nonces on Flipper Zero after key recovery.
- **Nonces File**: Select a `.nonces` file to recover keys from.
- **Run**: Click this button to start executing the FlipperNestedRecovery operation.
- **Stop**: Click this button during the operation to terminate the process.
- **About**: View information about this program.

### 3. Run and Terminate

- **Run the Program**: After entering the necessary parameters, click the `Run` button. The program will start executing the FlipperNestedRecovery tool. The operation progress will be displayed in real-time, and all results will be shown upon completion.
- **Terminate Operation**: If you need to stop the operation, click the `Stop` button. The program will attempt to terminate all related processes. Users can click the `Stop` button at any time to terminate the current operation, and the program will safely close all related processes.

### 4. Notes

- **Connect Flipper Zero**: Ensure Flipper Zero is connected via USB and is not occupied by any other software (e.g., `./fbt log`, `qFlipper`, `lab.flipper.net`).
- **Check Flipper Device**: Before use, ensure that Flipper Zero is properly connected and in standby mode.

## Special Thanks

Special thanks to the following individuals and projects for their support and contributions:

- **ZhaiRenGaiZaoJia**: Thank you for providing the nonces file and assisting with testing, helping me identify some bugs in the software.
- **AloneLiberty**: Thank you for developing the original [FlipperNestedRecovery](https://github.com/AloneLiberty/FlipperNestedRecovery) tool, on which this project is based.

Special thanks to all users who provided feedback and suggestions during the development of the project. Your support is our motivation for continuous improvement.

## Disclaimer

This software may contain defects or errors, and the author makes no express or implied warranties regarding the performance or effects of this software, including but not limited to merchantability, fitness for a particular purpose, and non-infringement. The author shall not be liable for any damages, losses, or other liabilities arising from the use or inability to use this software, whether in contract, tort, or other legal actions.