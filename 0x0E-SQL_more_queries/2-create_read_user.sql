-- 2. Read user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost;
GRANT SELECT ON * . * TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
