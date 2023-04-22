# clash-docker

Running Clash for Docker with configuration tools.

## Quickstart

``` shell
docker build -t clash-build -f Dockerfile.build-clash
docker build -t docker-clash .
docker run -e SUB_URL=<your_sub_link> -p 7890:7890 -v <path_to_dir>:/configs docker-clash
```

This will build Clash locally (for AMD64), then run a Docker container.
The container will automatically fetch [Clash rules](https://github.com/Loyalsoldier/clash-rules),
adapt the rules for Clash (GPL version), and run Clash on port 7890.

After the config.yaml has been generated, you could add your rules to it.

## Issues

- [*] Rules are re-fetched every time the container starts
- [*] An external config solution should be added **(But it need to be easier.)**
- [] Currently only supports the url-test proxy group type
- [] A filter is needed as some subscription links are invalid
- [] Only supports Trojan links
- [*] The clashtools package cannot be installed for some reason (There is no need for doing this.)
- [] The code needs refactoring

## Author

Niu Zhaolong <wuniu@riseup.net>
