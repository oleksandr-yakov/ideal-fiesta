#!/bin/bash

spinner=( Ooooo oOooo ooOoo oooOo ooooO oooOo ooOoo oOooo);
 

count(){
  spin &
  pid=$!

  sleep 0.2
  echo " -> Starting collapse the TgBot project"
  docker stop $(docker ps -aqf name=tgbot) > /dev/null && echo " -> Conteiner 'tgbot' deleted" && sleep 0.2
  docker rmi -f  tgbot_img:v1 > /dev/null && echo " -> Image 'tgbot_img:v1' deleted" && sleep 0.2
  #rm -f ~/main_files/other/study/TgBot/Dockerfile > /dev/null && echo " -> Dockerfile deleted" && sleep 0.2

  echo " -> Finished collapse the TgBot project" 
  kill $pid  
}
 
spin(){
  while [ 1 ]
  do 
    for i in ${spinner[@]}; 
    do 
      echo -ne "\r$i ";
      sleep 0.2;
    done;
  done
}
 
count
