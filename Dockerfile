FROM dreamacro/clash

VOLUME /config

ENTRYPOINT ["/clash"]
CMD ["-d", "/config"]
