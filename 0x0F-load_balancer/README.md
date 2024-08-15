
## Requirements

- Ubuntu 20.04 or later
- SSH access to the servers
- Basic knowledge of Bash, Nginx, and HAProxy
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0F-load_balancer`

## Tasks

### 0. Double the Number of Web Servers

This task involves configuring `web-02` to be identical to `web-01` and setting a custom Nginx header (`X-Served-By`) to indicate which server is responding.

#### Steps:
1. SSH into `web-01` and `web-02`.
2. Install and configure Nginx.
3. Add the custom header in the Nginx configuration.
4. Test the setup by using the `curl` command.

#### Example Commands:
```bash
curl -sI http://web-01_ip | grep X-Served-By
curl -sI http://web-02_ip | grep X-Served-By

