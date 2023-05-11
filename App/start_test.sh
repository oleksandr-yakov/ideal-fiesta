#!/bin/bash

exists_all=$(docker ps -qf name=once* | wc -l)
needed_conteiner=$(docker ps -aqf name=app)

if [ ${exists_all} -eq 2  ]; then
	echo "all needs conteiner run and exeists"
	docker exec --tty=false -u0 ${needed_conteiner}  python3 testauto.py

else
	echo "whats going wrong"
	exit 1
fi










