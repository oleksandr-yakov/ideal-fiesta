#!/bin/bash

mysql_host=$(sudo docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' once_mysql)

DB_USER="dev"
DB_PASS="Ag111^@ergnuio"


DB_NAME="prodMain"

sudo docker exec --tty=false once_mysql mysql -u $DB_USER -p$DB_PASS -h $mysql_host -D $DB_NAME -e "CREATE TABLE if not exists usersdata(id INT NOT NULL AUTO_INCREMENT,username VARCHAR(50) NOT NULL,password VARCHAR(50) NOT NULL,PRIMARY KEY (id));"
echo "finish"
