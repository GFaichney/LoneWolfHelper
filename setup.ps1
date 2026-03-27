$ErrorActionPreference = "Stop"

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    py -3 -m venv .venv
}

Write-Host "Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

Write-Host "Installing requirements..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host "Setup complete."
