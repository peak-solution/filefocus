# MCP Playground

Open this folder in VSCode to interact with *PeakTDM FileFocus* using Microsoft Copilot in combination with the ODSBox Python library, and the ODSBox Jaquel MCP Service - **ODSBox AIConnect**.

## Install Prerequisites

To use *ODSBox AIConnect* with Microsoft Visual Studio Code (VSCode) we recommend to have the following tools and applications installed:

* VSCode
* UV
* Python
* Git

The easiest way to get those installed is by using winget in CMD window (type `cmd` in windows command line) like shown below:

``` bash
winget install astral-sh.uv
winget install Python.Python.3.13
winget install Git.Git
winget install Microsoft.VisualStudioCode
```

Close the cmd window. Now `python`, `uvx`, `git`, `code` should be on path.
If it is not available Log out from Windows and Log in again.

## Using with VSCode Copilot Chat

You can now start working with *ODSBox AIConnect*. Open the Copilot Chat window in VSCode and start asking questions about your data stored in *PeakTDM FileFocus*. You can also ask for code snippets how to perform specific analysis operations on your data using the ODSBox Python library.

Connect to *PeakTDM FileFocus* using the following credentials:

```yaml
ods.serverUrl: "http://localhost:15003/api"
ods.username: "user"
ods.password: "welcome"
```

👉 See the example prompts below to retrieve some information from *PeakTDM FileFocus*:

![AI Connect Prompts](docs/images/ai_connect_prompts.png)
