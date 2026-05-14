import * as vscode from 'vscode';
import * as cp from 'child_process';
import * as path from 'path';

let outputChannel: vscode.OutputChannel;

export function activate(context: vscode.ExtensionContext) {
    outputChannel = vscode.window.createOutputChannel('T&DS');
    context.subscriptions.push(outputChannel);

    let disposableTest = vscode.commands.registerCommand('tnds.runTest', async () => {
        const instanceUri = await vscode.window.showOpenDialog({
            canSelectFiles: true,
            canSelectFolders: false,
            canSelectMany: false,
            title: "Select source file (.cpp, .py)",
            filters: { 'Source files': ['cpp', 'c', 'py', 'cc', 'cxx'] }
        });

        if (!instanceUri || instanceUri.length === 0) return;

        const dataUri = await vscode.window.showOpenDialog({
            canSelectFiles: false,
            canSelectFolders: true,
            canSelectMany: false,
            title: "Select Data Directory containing .in and .out files"
        });

        if (!dataUri || dataUri.length === 0) return;

        runTndsCommand('-t', instanceUri[0].fsPath, dataUri[0].fsPath, context.extensionPath);
    });

    let disposableDebug = vscode.commands.registerCommand('tnds.runDebug', async () => {
        const instanceUri = await vscode.window.showOpenDialog({
            canSelectFiles: true,
            canSelectFolders: false,
            canSelectMany: false,
            title: "Select source file (.cpp, .py)",
            filters: { 'Source files': ['cpp', 'c', 'py', 'cc', 'cxx'] }
        });

        if (!instanceUri || instanceUri.length === 0) return;

        const dataUri = await vscode.window.showOpenDialog({
            canSelectFiles: true,
            canSelectFolders: false,
            canSelectMany: false,
            title: "Select Input File (.in)",
            filters: { 'Input files': ['in'] }
        });

        if (!dataUri || dataUri.length === 0) return;

        runTndsCommand('-d', instanceUri[0].fsPath, dataUri[0].fsPath, context.extensionPath);
    });

    context.subscriptions.push(disposableTest, disposableDebug);
}

function runTndsCommand(flag: string, instancePath: string, dataPath: string, extensionPath: string) {
    outputChannel.show(true);
    outputChannel.appendLine(`>>> Running T&DS ${flag === '-t' ? 'Test' : 'Debug'}...`);
    
    const mainScriptPath = path.join(extensionPath, 'OS', 'main.py');
    const command = `python "${mainScriptPath}" ${flag} "${instancePath}" -s "${dataPath}"`;

    outputChannel.appendLine(`Executing: ${command}\n`);

    cp.exec(command, { cwd: extensionPath }, (error, stdout, stderr) => {
        if (stdout) {
            outputChannel.append(stdout);
        }
        if (stderr) {
            outputChannel.append(stderr);
        }
        if (error) {
            outputChannel.appendLine(`\nProcess exited with error code: ${error.code}`);
        }
        outputChannel.appendLine(`\n>>> Done.`);
    });
}

export function deactivate() {}
