# clash-docker

Running Clash for Docker with configuration tools. Convert [Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules) to clash (GPL version) conpatible.

The configuration script is seriously primitive for now. For my usage habits, this could only accepts trojan links from subscription.
It will set all the proxies in to a single proxy group with method `url-test`. The config.yaml shall be reconfigured
if needed.

## Quickstart

A continer can be run directly from the image on docker hub.

``` shell
docker run -e SUB_URL=<your_sub_link> -p 7890:7890 -v <path_to_dir>:/configs wuniu/clash-docker
```

Replace `<your_sub_link` with your subscription link (which returns aset of **base64-encoded**
**Trojan** links). It is also recommended to set `-v <path_to_dir>:/configs and replace `<path_to_dir>` 
with a local path to store the generated clash config to enable to change the clash config manually later.

Container will fetch rules from @Loyalsoldier/clash-rules and adds the converted rules to config.yaml conbined with the subscripted trojan links and some pre-defined settings.Container won't fetch the rules once the config.yaml have been generated.

Also, the project can be built locally hereafter.

``` shell
docker build -t clash-build -f Dockerfile.build-clash
docker build -t clash-docker .
docker run -e SUB_URL=<your_sub_link> -p 7890:7890 -v <path_to_dir>:/configs clash-docker
```

This will build Clash locally (for AMD64), then run a Docker container.
The container will automatically fetch [Clash rules](https://github.com/Loyalsoldier/clash-rules),
adapt the rules for Clash (GPL version), and run Clash on port 7890.

After the config.yaml has been generated, you could add your rules to it.

## Issues

- [x] Rules are re-fetched every time the container starts
- [x] An external config solution should be added **(But it need to be easier.)**
- [ ] Currently only supports the url-test proxy group type
- [ ] A filter is needed as some subscription links are invalid
- [ ] Only supports Trojan links
- [x] The clashtools package cannot be installed for some reason (There is no need for doing this.)
- [ ] The code needs refactoring

## Author

Niu Zhaolong <wuniu@riseup.net>
