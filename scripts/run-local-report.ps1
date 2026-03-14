param(
    [string]$Player1Cmd = "",
    [string]$Player1Name = "",
    [string]$Player2Cmd = "",
    [string]$Player2Name = "",
    [string]$Seed = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Ensure-JavaOnPath {
    $javaCmd = Get-Command java -ErrorAction SilentlyContinue
    if ($javaCmd) {
        return
    }

    $jdkDir = Get-ChildItem 'C:\Program Files\Eclipse Adoptium' -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -like 'jdk-17*' } |
        Sort-Object Name -Descending |
        Select-Object -First 1

    if (-not $jdkDir) {
        throw 'Java 17 introuvable. Installez Temurin 17 puis relancez.'
    }

    $env:JAVA_HOME = $jdkDir.FullName
    $env:PATH = "$($jdkDir.FullName)\bin;$env:PATH"
}

function Ensure-MavenCmd {
    $mvnCmd = Get-Command mvn -ErrorAction SilentlyContinue
    if ($mvnCmd) {
        return $mvnCmd.Source
    }

    $toolsDir = Join-Path $PSScriptRoot '..\.tools'
    if (-not (Test-Path $toolsDir)) {
        New-Item -ItemType Directory -Path $toolsDir | Out-Null
    }

    $existing = Get-ChildItem $toolsDir -Directory -Filter 'apache-maven-*' -ErrorAction SilentlyContinue |
        Where-Object { Test-Path (Join-Path $_.FullName 'bin\mvn.cmd') } |
        Sort-Object Name -Descending |
        Select-Object -First 1

    if (-not $existing) {
        Get-ChildItem $toolsDir -Directory -Filter 'apache-maven-*' -ErrorAction SilentlyContinue |
            Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

        $version = '3.9.9'
        $zipName = "apache-maven-$version-bin.zip"
        $zipPath = Join-Path $toolsDir $zipName
        $url = "https://archive.apache.org/dist/maven/maven-3/$version/binaries/$zipName"

        Invoke-WebRequest -Uri $url -OutFile $zipPath
        Expand-Archive -Path $zipPath -DestinationPath $toolsDir -Force
        Remove-Item $zipPath -Force

        $existing = Get-ChildItem $toolsDir -Directory -Filter 'apache-maven-*' |
            Where-Object { Test-Path (Join-Path $_.FullName 'bin\mvn.cmd') } |
            Sort-Object Name -Descending |
            Select-Object -First 1
    }

    if (-not $existing) {
        throw 'Maven n a pas pu etre telecharge automatiquement (bin\mvn.cmd introuvable).'
    }

    return (Join-Path $existing.FullName 'bin\mvn.cmd')
}

Ensure-JavaOnPath
$mvn = Ensure-MavenCmd

if ($Player1Cmd) {
    $env:CG_PLAYER1_CMD = $Player1Cmd
}
if ($Player1Name) {
    $env:CG_PLAYER1_NAME = $Player1Name
}
if ($Player2Cmd) {
    $env:CG_PLAYER2_CMD = $Player2Cmd
}
if ($Player2Name) {
    $env:CG_PLAYER2_NAME = $Player2Name
}
if ($Seed) {
    $env:CG_SEED = $Seed
}

Push-Location "${PSScriptRoot}\..\external\WinterChallenge2026-Exotec"
try {
    $mvnArgs = @(
        '-q'
        'test-compile'
        'exec:java'
        '-Dexec.classpathScope=test'
        '-Dexec.mainClass=LocalReportMain'
    )
    & $mvn @mvnArgs
}
finally {
    Pop-Location
}
