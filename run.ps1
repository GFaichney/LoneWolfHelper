$ErrorActionPreference = "Stop"

if (-not (Test-Path ".venv")) {
    Write-Error "Virtual environment not found. Run .\setup.ps1 first."
    exit 1
}

. .\.venv\Scripts\Activate.ps1
python app.py
