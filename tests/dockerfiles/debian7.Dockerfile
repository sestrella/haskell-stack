FROM debian:7

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y python-minimal && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["tail", "-f", "/dev/null"]
