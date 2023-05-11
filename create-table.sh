#!/bin/bash

mysql_host=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' once_mysql)

DB_USER="dev"
DB_PASS="Ag111^@ergnuio"
DB_NAME="prodMain"

docker exec -it once_mysql mysql -u $DB_USER -p$DB_PASS -h $mysql_host -D $DB_NAME -e "CREATE TABLE if not exists usersdata(id INT NOT NULL AUTO_INCREMENT,username VARCHAR(50) NOT NULL,password VARCHAR(50) NOT NULL,PRIMARY KEY (id));"
