#!/bin/bash
source /var/lib/jenkins/.bas
if [[ "$(docker stack services f1dat 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml f1dat
fi
docker service update --image markr1966/f1_service_1:latest f1dat_service_1
docker service update --image markr1966/f1_service_2:latest f1dat_service_2
docker service update --image markr1966/f1_service_3:latest f1dat_service_3
docker service update --image markr1966/f1_service_4:latest f1dat_service_4

docker system prune -f