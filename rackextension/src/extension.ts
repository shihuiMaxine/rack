// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as cp from "child_process";
import * as readline from 'readline';
// import * as readline from 'readline';
// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "rackextension" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('rackextension.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		const message='Hello World from rackextension!'
		vscode.window.showInformationMessage(message);
	});

	context.subscriptions.push(disposable);
	async function searchSnippets() {
		const selectedText = '';  // You would have some logic to get selected text, not provided here
	  
		const searchQuery = await vscode.window.showInputBox({
		  placeHolder: "Search query",
		  prompt: "Search my snippets on Codever",
		  value: selectedText
		});

		  if (searchQuery === '') {
			console.log(searchQuery);
			vscode.window.showErrorMessage('A search query is mandatory to execute this action');
		  } else if (searchQuery !== undefined) {
			console.log(searchQuery);
			console.log("working");
			// /Users/gaoshihui/shihui_rack_2023/rack/rackextension/src/rack1.py

			// // Replace with the actual path to "rack1.py"
			const filePath = "rack1.py";
			const pythonScriptPath = '/Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py';
			const inputArgument = searchQuery;
			console.log("python3 /Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py -q " + String(inputArgument));

			
			cp.exec("python3 /Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py -q " + String(inputArgument), (err, stdout, stderr) => {
				console.log('stdout: ' + stdout);
				console.log('stderr: ' + stderr);
				if (err) {
					console.log('error: ' + err);
				}			
			});
			
			
		  }
		}
	  
	  
	  // Call the function to initiate the search
	  searchSnippets();
	  context.subscriptions.push(disposable);

}


export function deactivate() {}
