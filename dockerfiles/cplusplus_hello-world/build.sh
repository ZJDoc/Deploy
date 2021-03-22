#!/bin/sh

set -eux

echo Building zjykzj/hello:build

docker build -t zjykzj/hello:build . -f Dockerfile.build

docker container create --name extract zjykzj/hello:build
docker container cp extract:/app/app ./app
docker container rm -f extract

echo Building zjykzj/hello:latest

docker build --no-cache -t zjykzj/hello:latest .
rm ./app