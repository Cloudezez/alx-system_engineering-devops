MySQL Setup and Configuration
This repository contains scripts and instructions for setting up and configuring MySQL on two servers, setting up replication, and creating backups. Follow the steps below to complete the setup.

0. Install MySQL
Ensure MySQL 5.7.x is installed on both web-01 and web-02 servers. Verify installation with the following command:

bash
Copy code
mysql --version
Example output:

bash
Copy code
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
Repository:

GitHub Repository: alx-system_engineering-devops
Directory: 0x14-mysql
1. Let Us In!
Create a MySQL user holberton_user on both servers with the password projectcorrection280hbtn. Grant this user the permission to check replication status:

sql
Copy code
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
Verify user permissions:

bash
Copy code
mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Repository:

GitHub Repository: alx-system_engineering-devops
Directory: 0x14-mysql
2. If Only You Could See What I've Seen
On the primary server web-01, create a database tyrell_corp and a table nexus6 with at least one entry:

sql
Copy code
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
INSERT INTO nexus6 (name) VALUES ('Leon');
Ensure holberton_user has SELECT permissions on the table:

sql
Copy code
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
Repository:

GitHub Repository: alx-system_engineering-devops
Directory: 0x14-mysql
3. Quite an Experience to Live in Fear
Create a MySQL user replica_user for replication on web-01:

sql
Copy code
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
Verify the replica_user permissions:

bash
Copy code
mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
Repository:

GitHub Repository: alx-system_engineering-devops
Directory: 0x14-mysql
4. Setup a Primary-Replica Infrastructure
Set up replication with web-01 as the primary and web-02 as the replica. Ensure MySQL is configured correctly on both servers:

Primary Configuration: 4-mysql_configuration_primary
Replica Configuration: 4-mysql_configuration_replica
Verify replication:

bash
Copy code
mysql -uholberton_user -p -e "SHOW MASTER STATUS;"
On web-02:

bash
Copy code
mysql -uholberton_user -p -e "SHOW SLAVE STATUS\G"
Repository:

GitHub Repository: alx-system_engineering-devops
Directory: 0x14-mysql
Files: 4-mysql_configuration_primary, 4-mysql_configuration_replica
5. MySQL Backup
Create a Bash script 5-mysql_backup to dump all databases, compress them, and name the archive with the format day-month-year.tar.gz:

bash
Copy code
#!/bin/bash
DATE=$(date +%d-%m-%Y)
PASSWORD=$1
mysqldump -uroot -p${PASSWORD} --all-databases > backup.sql
tar -czvf ${DATE}.tar.gz backup.sql
Repository:

GitHub Repository: alx-system_engineering-devops
Directory: 0x14-mysql
File: 5-mysql_backup
Feel free to reach out if you have any questions or need further assistance!
