UPDATE mysql.user SET Password=PASSWORD('MyMySQLPass') WHERE User='root';
FLUSH PRIVILEGES;
