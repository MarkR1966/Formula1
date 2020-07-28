#!/bin/bash

if [[ "$(docker stack services f1dat 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml f1dat
else
    docker service update f1dat_service_1
    docker service update f1dat_service_2
    docker service update f1dat_service_3
    docker service update f1dat_service_4
fi