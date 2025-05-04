# bootcamp
# Web Server & Docker Setup on Azure VM

This project demonstrates the setup of a simple Linux server on an Azure VM, configured with a web server and Docker. It is part of a DevOps preparation bootcamp.

## 🌐 Web Server Setup

A minimal web server is hosted on an Azure Virtual Machine, displaying my name and photo to prove the server setup.

### 🔧 Steps to Set Up
1. Created a free Azure account using GitHub Student Pack.
2. Set up a virtual machine (VM) with Ubuntu 20.04 LTS.
3. Installed Apache web server.
4. Created an `index.html` page displaying my name and photo.

### ✅ Live Site

Visit the site here: **http://bootcamp-zone.strangled.net//ex-tools-1/**

## 🐳 Docker Setup

Docker was installed and tested on the same VM for future DevOps tasks.

### 📦 Docker Installation

1. Installed Docker:
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   sudo systemctl start docker
   sudo systemctl enable docker
   Verified Docker installation:

2. Verified Docker installation:
  ```bash
 docker --version

 
## 🐍 Python Docker Test
  1. Pulled a Python image:
      ```bash
      docker pull python
  
 2. Run a container and tested with Hello, World!:
    ```bash
     docker run python python -c "print('Hello, World!')"


 📹 Installation Video
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


