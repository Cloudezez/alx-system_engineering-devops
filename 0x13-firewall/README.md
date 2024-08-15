# Firewall Configuration Project

This project involves configuring a firewall using `ufw` (Uncomplicated Firewall) on an Ubuntu server. The goal is to secure the server by blocking unnecessary incoming traffic and setting up port forwarding rules.

## Project Tasks

### Task 0: Block All Incoming Traffic Except Specific Ports

**Objective:**
- Install the `ufw` firewall and configure it to block all incoming traffic, except for the following TCP ports:
  - **Port 22:** SSH
  - **Port 443:** HTTPS SSL
  - **Port 80:** HTTP

**Commands Used:**
```bash
# Install ufw if not already installed
sudo apt-get update
sudo apt-get install ufw

# Allow specific ports
sudo ufw allow 22/tcp  # Allow SSH
sudo ufw allow 80/tcp  # Allow HTTP
sudo ufw allow 443/tcp # Allow HTTPS

# Enable ufw
sudo ufw enable

# Check ufw status
sudo ufw status

