
DROP DATABASE IF EXISTS ehdtd ;
CREATE DATABASE ehdtd ;

GRANT ALL PRIVILEGES ON ehdtd.* TO 'ehdtd' IDENTIFIED BY 'ehdtd_9898';
GRANT ALL PRIVILEGES ON ehdtd.* TO 'ehdtd'@'localhost' IDENTIFIED BY 'ehdtd_9898';
GRANT ALL PRIVILEGES ON ehdtd.* TO 'ehdtd'@'127.0.0.1' IDENTIFIED BY 'ehdtd_9898';