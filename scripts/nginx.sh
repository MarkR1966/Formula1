#!/bin/bash
# Build image for nginx with my tag and push to DockerHub
docker build --no-cache -t markr1966/nginx ./NGINX
docker push markr1966/nginx:latest
