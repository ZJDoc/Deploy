#!/bin/sh

set -eux

docker run -it --rm -e LOCAL_USER_ID=`id -u ${USER}` -v ${HOME}/storage:/home/user/storage gosu_test bash