Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$python = Join-Path $PSScriptRoot '..\.venv\Scripts\python.exe'
if (-not (Test-Path $python)) {
	$python = 'python'
}

& $python .\scripts\build_single_file.py
