#!/bin/bash

if [[ "$(docker stack services f1dat 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml f1dat
fi
docker service update --image markr1966/f1dat_service_1:latest --force f1dat_service_1
docker service update --image markr1966/f1dat_service_1:latest --force f1dat_service_2
docker service update --image markr1966/f1dat_service_1:latest --force f1dat_service_3
docker service update --image markr1966/f1dat_service_1:latest --force f1dat_service_4

docker system prune -f