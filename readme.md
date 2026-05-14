# T&DS (Test & Debug System)

**T&DS** is a powerful yet lightweight VSCode extension designed to help you quickly test your programming assignments against test data and debug them seamlessly with AI assistance. It supports both **C++** and **Python**.

## Features

- **Batch Testing (`tnds.runTest`)**:
  - Automatically scan a data directory for `.in` and `.out` file pairs.
  - Compile your C++ source or run your Python source.
  - Automatically test all pairs and present a detailed breakdown of correct/incorrect answers, timeout errors, and compile/runtime errors.
  
- **Debug & AI Assist (`tnds.runDebug`)**:
  - Automatically generate `.vscode/launch.json` and `.vscode/tasks.json` tailored to your source code, enabling you to use VSCode's native `F5` debugging experience.
  - **OpenAI Integration**: If a test case fails, T&DS will automatically send the source code, the expected output, and your actual output to the OpenAI API (if configured). The AI will analyze the mismatch and provide concrete suggestions to fix your code!

## Installation

1. Go to the [Releases](https://github.com/GuoCalix/T-DS/releases) page of the GitHub repository.
2. Download the latest `tnds-x.x.x.vsix` file.
3. Open VSCode, go to the **Extensions** view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
4. Click on the `...` menu at the top right of the Extensions view.
5. Select **Install from VSIX...** and choose the downloaded file.

## Requirements

The extension bundles a Python backend to execute tests. You must have **Python 3** installed and available in your system `PATH` (executable as `python`).

For C++ testing, you must have `g++` installed and available in your system `PATH`.

## Setup & Configuration

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

## How to Use

1. Open your workspace containing your code and data.
2. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
3. Search for:
   - **`T&DS: Run Batch Test`**: You will be prompted to select your source file (`.cpp` or `.py`), and then the directory containing your `.in` and `.out` files.
   - **`T&DS: Debug & AI Assist`**: You will be prompted to select your source file, and then a specific `.in` file. The extension will test it, print AI debugging advice if it fails, and set up your `.vscode` debugger configuration.
4. Results are printed in real-time to the **T&DS** Output channel at the bottom of your VSCode editor.

## Project Structure (For Developers)
- `OS/main.py`: The CLI router and settings manager.
- `Test/`: General-purpose testing scripts.
- `Debug/`: VSCode configuration generator and OpenAI API client.
- `src/extension.ts`: The VSCode Extension TypeScript entry point.
- `example/`: Example faulty C++ script and test data.