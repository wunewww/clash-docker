FROM alpine:3.17.3

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add python3 py3-yaml py3-requests

COPY --from=build-clash /go/clash/bin/clash-linux-amd64 /usr/local/bin/clash

VOLUME /config

CMD ["head", "/dev/zero"]
#ENTRYPOINT ["clash"]
#CMD ["-d", "/config"]
