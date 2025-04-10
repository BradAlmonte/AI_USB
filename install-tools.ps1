Write-Host "Installing Cybersecurity Tools..."
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
iex ((New-Object System.Net.WebClient).DownloadString("https://community.chocolatey.org/install.ps1"))
$env:Path += ";$env:ALLUSERSPROFILEchoco install nmap -y
choco install wireshark -y
choco install burpsuite -y
choco install john -y
choco install sqlmap -y
choco install aircrack-ng -y
choco install hashcat -y
choco install metasploit -y
choco install nikto -y
choco install curl -y
choco install wget -y
Write-Host "✅✅✅ All tools downloaded successfully! ✅✅✅"
