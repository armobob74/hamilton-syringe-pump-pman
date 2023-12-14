# Installation Instructions
1. [Setup venv](#setup-venv)
2. [Setup Dependencies](#setup-dependencies)
3. [Run](#run)

## Setup Venv
Open a terminal and navigate to the directory where you've placed the `solvent_dispenser_ui` repository
Setup your python virtual environment, which will be used to install dependencies.

It's important that you do this from the `solvent_dispenser_ui` directory, otherwise `run.bat` will not work.
```bash
python -m venv venv
```
Then activate the virtual environment

Windows Powershell:
```PowerShell
.\venv\Scripts\activate.ps1
```
Linux/Mac:
```bash
source ./venv/bin/activate
```

Once venv is activated, install the dependencies that are in requirements.txt.

## Setup Dependencies

```bash
pip install -r  requirements.txt
```
## Run
Now you're ready to run the app! On windows, just double click on `run.bat`
For information on how to use the app, check out Instructions/readme.md
