#!/bin/bash
#cd ~/main_files/other/study/TgBot

#output=$( docker ps -af name=tgbot | grep tgbot 2> /dev/null )
exists=$(docker ps -qf name=tgbot | wc -l)

if [[ ${exists} -eq 1 ]];
then
  docker stop tgbot
  echo "Conteiner tgbot stoped "
else
  echo "Continue to CI"
fi





echo "FROM python" > Dockerfile
echo "WORKDIR /home/app/" >> Dockerfile
echo "COPY ./App/ ." >> Dockerfile
echo "RUN pip install --no-cache-dir -r requirements.txt " >> Dockerfile
echo 'CMD ["python3","/home/app/mainTgBot.py"]' >> Dockerfile


if [[ -f "./Dockerfile" ]]
then
    echo "Dockerfile created successfully."
    docker build -t tgbot_img:v1 .
else 
	echo "ERROR: Dockerfile not created"
	exit 1
fi



if [[ $(docker images | grep tgbot_img |wc -l) -eq 0  ]]
then
    echo "ERROR: image 'tgbot_img:v1' not created"
    exit 1
else 
	echo "OK LETS GO: Image 'tgbot_img:v1'Created $(docker images|grep tgbot_img | awk '{ print  $4, $5, $6 }')"

	docker run  -v /etc/timezone:/etc/timezone:ro -v /etc/localtime:/etc/localtime:ro --rm -t -d --name tgbot   tgbot_img:v1

fi




if [[ ${exists} -eq 1 ]]; then
  echo "A container with a name: tgbot exists and has status: $( echo ${output} | awk '{ print $7 }' )"
  docker top $(docker ps -aqf "name=tgbot")
else
  echo "Container with a name: tgbot does not exist"
  #exit 1
fi

#docker stats $(docker ps -aqf "name=tgbot")

