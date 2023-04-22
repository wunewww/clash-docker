FROM alpine:3.17.3

COPY --from=build-clash /go/clash/bin/clash-linux-amd64 /usr/local/bin/clash
COPY ./src /src
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add python3 py3-pip py3-yaml py3-requests \
    && mkdir /configs

VOLUME /configs

CMD ["sh", "/src/start.sh"]
