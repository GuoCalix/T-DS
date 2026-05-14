# T&DS (Test & Debug System)

[English](#english) | [中文](#中文)

---

## English

**T&DS** is a powerful yet lightweight VSCode extension designed to help you quickly test your programming assignments against test data and debug them seamlessly with AI assistance. It supports both **C++** and **Python**.

### Features

- **Batch Testing (`tnds.runTest`)**:
  - Automatically scan a data directory for `.in` and `.out` file pairs.
  - Compile your C++ source or run your Python source.
  - Automatically test all pairs and present a detailed breakdown of correct/incorrect answers, timeout errors, and compile/runtime errors.
  
- **Debug & AI Assist (`tnds.runDebug`)**:
  - Automatically generate `.vscode/launch.json` and `.vscode/tasks.json` tailored to your source code, enabling you to use VSCode's native `F5` debugging experience.
  - **OpenAI Integration**: If a test case fails, T&DS will automatically send the source code, the expected output, and your actual output to the OpenAI API (if configured). The AI will analyze the mismatch and provide concrete suggestions to fix your code!

### Installation

1. Go to the [Releases](https://github.com/GuoCalix/T-DS/releases) page of the GitHub repository.
2. Download the latest `tnds-x.x.x.vsix` file.
3. Open VSCode, go to the **Extensions** view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
4. Click on the `...` menu at the top right of the Extensions view.
5. Select **Install from VSIX...** and choose the downloaded file.

### Requirements

The extension bundles a Python backend to execute tests. You must have **Python 3** installed and available in your system `PATH` (executable as `python`).

For C++ testing, you must have `g++` installed and available in your system `PATH`.

### Setup & Configuration

Upon your first run, T&DS will automatically generate a `setting_DNTS.json` file in your workspace root. 

Open this file to configure your AI Debugger:
```json
{
    "default_language": "cpp",
    "openai_api_key": "YOUR_OPENAI_API_KEY",
    "openai_model": "gpt-4o",
    "ai_prompt": "You are an AI debugging assistant..."
}
```
*Tip: To use the AI debugging feature, you must provide a valid `openai_api_key`.*

### How to Use

1. Open your workspace containing your code and data.
2. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
3. Search for:
   - **`T&DS: Run Batch Test`**: You will be prompted to select your source file (`.cpp` or `.py`), and then the directory containing your `.in` and `.out` files.
   - **`T&DS: Debug & AI Assist`**: You will be prompted to select your source file, and then a specific `.in` file. The extension will test it, print AI debugging advice if it fails, and set up your `.vscode` debugger configuration.
4. Results are printed in real-time to the **T&DS** Output channel at the bottom of your VSCode editor.

### Project Structure (For Developers)
- `OS/main.py`: The CLI router and settings manager.
- `Test/`: General-purpose testing scripts.
- `Debug/`: VSCode configuration generator and OpenAI API client.
- `src/extension.ts`: The VSCode Extension TypeScript entry point.
- `example/`: Example faulty C++ script and test data.

---

## 中文

**T&DS** 是一款强大且轻量的 VSCode 插件，专为编程作业和轻量级项目设计。它可以帮你快速进行数据比对测试，并结合 AI 提供无缝的 Debug 体验。目前支持 **C++** 和 **Python**。

### 功能特性

- **批量测试 (`tnds.runTest`)**:
  - 自动扫描选中目录中的 `.in` 和 `.out` 文件对。
  - 自动编译你的 C++ 源码或运行你的 Python 源码。
  - 自动测试所有的测试点，并提供关于解答正确/错误、运行超时 (Timeout)、以及编译/运行错误的详细报告。
  
- **Debug 与 AI 辅助 (`tnds.runDebug`)**:
  - 根据你的源码自动生成 `.vscode/launch.json` 和 `.vscode/tasks.json`，让你能直接使用 VSCode 原生的 `F5` 体验进行断点调试。
  - **OpenAI 集成**: 如果某个测试点未能通过，T&DS 会自动将你的源码、期望输出、实际错误输出发送给 OpenAI API（需提前配置）。AI 会帮你分析错误原因，并直接给出修改代码的具体建议！

### 插件安装

1. 前往 GitHub 仓库的 [Releases](https://github.com/GuoCalix/T-DS/releases) 页面。
2. 下载最新的 `tnds-x.x.x.vsix` 插件包文件。
3. 打开 VSCode，进入 **扩展 (Extensions)** 视图 (`Ctrl+Shift+X` 或 `Cmd+Shift+X`)。
4. 点击视图右上角的 `...` 菜单图标。
5. 选择 **从 VSIX 安装... (Install from VSIX...)** 并选中你刚刚下载的文件。

### 环境要求

由于本插件内嵌了 Python 测试后端引擎，因此你必须在系统中安装 **Python 3**，并将其加入系统环境变量 `PATH` 中（保证能通过 `python` 命令直接调用）。

如果需要测试 C++ 代码，你还需要安装 `g++` 并将其加入系统环境变量 `PATH` 中。

### 配置与使用

在第一次运行插件时，T&DS 会在你的工作区根目录下自动生成一个 `setting_DNTS.json` 配置文件。

打开这个文件来配置你的 AI 调试助手：
```json
{
    "default_language": "cpp",
    "openai_api_key": "YOUR_OPENAI_API_KEY",
    "openai_model": "gpt-4o",
    "ai_prompt": "You are an AI debugging assistant..."
}
```
*提示: 想要体验完整的 AI 调试功能，请务必填入有效的 `openai_api_key`。*

### 如何开始测试

1. 在 VSCode 中打开包含代码和测试数据的工作区。
2. 打开命令面板 (`Ctrl+Shift+P` / `Cmd+Shift+P`)。
3. 搜索以下两个命令：
   - **`T&DS: Run Batch Test`**: 插件会弹窗让你选择你的源码文件（`.cpp` 或 `.py`），接着选择包含你 `.in` 和 `.out` 测试数据的目录，然后自动开始批量跑测。
   - **`T&DS: Debug & AI Assist`**: 插件会弹窗让你选择源码文件，以及某个特定的 `.in` 文件。插件会使用该数据进行测试，如果运行失败，会自动呼叫 AI 打印修改建议，并为你生成 `.vscode` 调试配置。
4. 所有的测试进度、结果、错误信息以及 AI 建议，都会实时打印在 VSCode 底部的 **T&DS 输出面板 (Output)** 中。

### 开发者项目结构
- `OS/main.py`: CLI 路由和配置管理器。
- `Test/`: 通用化测试执行引擎。
- `Debug/`: VSCode 调试配置文件生成器以及 OpenAI API 客户端。
- `src/extension.ts`: VSCode TypeScript 插件入口。
- `example/`: 包含错误 C++ 代码及测试数据的测试样例。