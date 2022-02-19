#!/bin/bash

set -eux

BUILD_DIR=build/
if [[ ! -d "${BUILD_DIR}" ]]; then
  mkdir -p ${BUILD_DIR}
fi

cd ${BUILD_DIR}
cmake -DCON3=ON ../
make
./condition