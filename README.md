# bootcamp
# Web Server & Docker Setup on Azure VM

This project demonstrates the setup of a simple Linux server on an Azure VM, configured with a web server and Docker. It is part of a DevOps preparation bootcamp.

## 🌐 Web Server Setup

A minimal web server is hosted on an Azure Virtual Machine, displaying my name and photo to prove the server setup.

### 🔧 Steps to Set Up

1. **Azure VM Creation**
   - Registered for the [GitHub Student Developer Pack](https://education.github.com/pack).
   - Used the pack to create a **free Azure account** (no credit card required).
   - Launched a **Linux VM (Ubuntu 20.04 LTS)** on Azure.

2. **DNS Setup (Optional)**
   - A free DNS can be obtained from [afraid.org](https://freedns.afraid.org/), but it’s optional.

3. **Web Server Configuration**
   - SSH’d into the VM using the public IP.
   - Installed Apache:
     ```bash
     sudo apt update
     sudo apt install apache2
     ```
   - Replaced the default web page with a custom `index.html`:
     ```bash
     sudo nano /var/www/html/index.html
     ```
   - The page includes my **name** and **photo**.

4. **Firewall Configuration**
   - Ensured port 80 (HTTP) is open in both Azure portal and the VM:
     ```bash
     sudo ufw allow 'Apache Full'
     ```

### ✅ Live Site

Visit the site here: **[http://<Your-Public-IP>](http://<Your-Public-IP>)**

## 🐳 Docker Setup

Docker was installed and tested on the same VM for future DevOps tasks.

### 📦 Docker Installation

1. Installed Docker:
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   sudo systemctl start docker
   sudo systemctl enable docker

2. Verified Docker installation:
   ```bash
   docker --version

## 🐍 Python Docker Test

