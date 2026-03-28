# Detect Python executable
$pythonCandidates = @(
    "python",
    "python3",
    (Get-Command python -ErrorAction SilentlyContinue)?.Source,
    (Get-Command python3 -ErrorAction SilentlyContinue)?.Source
) | Where-Object { $_ -ne $null -and $_ -ne "" } | Select-Object -Unique

$pythonExe = $null
foreach ($candidate in $pythonCandidates) {
    try {
        $ver = & $candidate --version 2>&1
        if ($ver -match "Python 3") { $pythonExe = $candidate; break }
    } catch {}
}

if (-not $pythonExe) {
    Write-Error "Python 3 not found. Please install Python 3 and ensure it is in your PATH."
    exit 1
}

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    & $pythonExe -m venv .venv
}

Write-Host "Installing requirements..."
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host "Setup complete."
