#!/bin/bash
# Ensure required environment variables are available for the containers when the 
source /var/lib/jenkins/.bashrc
# if stack does not exist then build otherwise update existing services
if [[ "$(docker stack services f1dat 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml f1dat
else
    docker service update --image markr1966/f1_service_2:latest f1dat_service_2
    docker service update --image markr1966/f1_service_3:latest f1dat_service_3
    docker service update --image markr1966/f1_service_4:latest f1dat_service_4
    docker service update --image markr1966/nginx:latest f1dat_nginx
    docker service update --image markr1966/f1_service_1:latest f1dat_service_1
fi
