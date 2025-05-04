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

Visit the site here: **[http://bootcamp-zone.strangled.net//ex-tools-1/]**

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

1. Pulled a Python image:
   ```bash
   docker pull python

2. Ran a container and tested with Hello, World!:
   ```bash
   docker run python python -c 'print("Hello, World!")'

## 📹 Installation Video

Docker installation and Python test steps are documented in this video:
👉 [https://drive.google.com/file/d/1Wyfo_Y5U4a_WAvu1c-RnlL5G3mbQG7AM/view?usp=sharing] 

## 🖥️ Client Setup Notes

WSL and Ubuntu were successfully installed on a Windows machine to provide a Linux-like development environment. This setup allows for native command-line tools and better compatibility with Docker and other DevOps tools.
Using WSL2 with Ubuntu ensures smooth development and closely mirrors a real server environment.


## 📌 Summary

This project sets up a foundational DevOps server with:
A hosted website proving server access.
Docker installed and tested.
A ready environment for deploying services in containers.

