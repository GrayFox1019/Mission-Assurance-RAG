$ErrorActionPreference = "Continue"
$raw = Join-Path $PSScriptRoot "..\data\raw"
New-Item -ItemType Directory -Force -Path $raw | Out-Null
$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
$files = [ordered]@{
  "dodd_3020.40.pdf"       = "https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodd/302040p.pdf"
  "dodi_8510.01.pdf"       = "https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/851001p.pdf"
  "nist_800-30r1.pdf"      = "https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf"
  "nist_800-37r2.pdf"      = "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf"
  "nist_800-53r5.pdf"      = "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf"
  "nist_800-82r3.pdf"      = "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf"
  "stpa_handbook.pdf"      = "https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf"
  "enterprise-attack.json" = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json"
}
foreach ($name in $files.Keys) {
  $dest = Join-Path $raw $name
  if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 100000)) { Write-Host "Have $name, skipping"; continue }
  Write-Host "Downloading $name ..."
  try {
    Invoke-WebRequest -Uri $files[$name] -OutFile $dest -UseBasicParsing -UserAgent $ua
  } catch {
    Write-Host "  FAILED: $name -> $($_.Exception.Message)" -ForegroundColor Red
  }
}
Get-ChildItem $raw | Select-Object Name, @{n="MB";e={[math]::Round($_.Length/1MB,1)}}
