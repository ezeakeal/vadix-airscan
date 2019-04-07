FROM ubuntu:18.04

MAINTAINER Daniel Vagg "https://github.com/ezeakeal/vadix-airscan"

RUN apt-get update \
 && apt-get install -y \
    git zlib1g-dev openjdk-8-jdk-headless autoconf curl libtool \
    libpq-dev libssl-dev ccache unzip zip python3 \
    python3-virtualenv python3-pip pkg-config cmake libffi-dev \
 && pip3 install cython buildozer \
 && echo "python3 -m virtualenv" > /usr/bin/virtualenv \
 && chmod +x /usr/bin/virtualenv

RUN mkdir -p /buildozer/ \
 && cd /buildozer/ \
 && echo "print('success')" > main.py \
 && yes | buildozer init . \
 && sed -i 's/warn_on_root.*/warn_on_root = 0/' buildozer.spec \
 && sed -i 's/log_level.*/log_level = 2/' buildozer.spec \
 && yes | buildozer android debug

VOLUME /buildozer/
VOLUME /p4a/
volume /opt/

WORKDIR /buildozer/

CMD buildozer android debug