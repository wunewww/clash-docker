FROM alpine:3.17.3

COPY --from=build-clash /go/clash/bin/clash-linux-amd64 /usr/local/bin/clash
COPY ./clashtools /clashtools
COPY ./start.sh /start.sh
COPY ./requirements.txt /requirements.txt
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add python3 py3-pip \
    && python3 -m pip install -r requirements.txt \
    && mkdir /configs

VOLUME /configs

CMD ["sh", "/start.sh"]
