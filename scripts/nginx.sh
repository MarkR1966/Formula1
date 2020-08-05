#!/bin/bash

docker build --no-cache -t markr1966/nginx ./NGINX
docker push markr1966/nginx:latest