# AI_USB

Welcome to the AI_USB repository! This repo contains essential cybersecurity tools and libraries, making it easy to set up your environment with minimal effort.

---

## Before You Pull the Repo

Follow these setup steps based on your operating system to ensure everything works smoothly.

---

## For All Operating Systems

1. **Ensure you have Git installed**  
   You need Git to pull the repository.  
   Install Git: [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## For Windows Users

1. **Set PowerShell Execution Policy**  
   PowerShell may block scripts by default. To allow them:

   - Open **PowerShell as Administrator**
   - Run:

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Chocolatey
The script uses Chocolatey to install tools. If it's not installed, the script will automatically install it.

## For macOS/Linux Users
The script uses Homebrew to install tools. If not installed, it will auto-install it.

Steps to Get Started
Clone the Repository

bash
git pull https://github.com/BradAlmonte/AI_USB.git main
Run the Installation Script

###On macOS/Linux:

bash
./update_and_install.sh
On Windows:

 powershell

.\update_and_install.ps1
The scripts will handle everything — no further input needed!

What’s Included
- nmap

- Wireshark

- Burp Suite

- John the Ripper

- SQLmap

- Aircrack-ng

- Hashcat

- Metasploit

- Nikto

- curl

- wget

### Troubleshooting
macOS/Linux:
If installation fails, check Homebrew:
bash - brew doctor

Windows:
Make sure you're running PowerShell as Administrator.
Check Chocolatey:
powershell - choco -v

### License
This project is licensed under the MIT License – see the LICENSE file for details.

### Key Elements Included:
1. **Clear instructions for prerequisites (Git, PowerShell execution policy, Homebrew/Chocolatey)**.
2. **Steps to pull and run the repository**.
3. **A section on what's included and the tools that will be installed**.
4. **Troubleshooting tips**.
5. **System requirements**.
6. **Credits for external tools used**.
7. **Contributing guidelines**.
8. **License section** (optional, but if you have a license for the project, this is good to include).
