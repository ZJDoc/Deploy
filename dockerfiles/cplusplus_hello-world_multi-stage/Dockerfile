FROM ubuntu:18.04
LABEL maintainer "zhujian <zjykzj@github.com>"

RUN set -eux && \
    apt-get update && apt-get install -f && apt-get install -y make cmake gcc g++
COPY CMakeLists.txt main.cpp test.cpp test.h /app/
WORKDIR /app
RUN cmake . && make

FROM alpine:latest
LABEL maintainer "zhujian <zjykzj@github.com>"

WORKDIR /root/
COPY --from=0 /app/app .
ENTRYPOINT ["./app"]