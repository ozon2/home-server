# Home Server

Docker compose services running behind Traefik.

## Services

### Media server

- [Jellyfin](https://github.com/jellyfin/jellyfin): media player
- [Sonarr](https://github.com/Sonarr/Sonarr): monitor and download TV shows
- [Radarr](https://github.com/Radarr/Radarr): download movies
- [Transmission OpenVPN](https://github.com/haugene/docker-transmission-openvpn): torrent client behind a VPN
- [Jackett](https://github.com/Jackett/Jackett): torrent indexer

### Monitoring

- [Uptime kuma](https://github.com/louislam/uptime-kuma): service monitoring
- [Node exporter](https://github.com/prometheus/node_exporter): server monitoring
- [Prometheus](https://github.com/prometheus/prometheus): time series database
- [Grafana](https://github.com/grafana/grafana): monitoring dashboard


### Other

- [Traefik](https://github.com/traefik/traefik): reverse proxy
- [Seafile](https://github.com/haiwen/seafile): file sync and share

## Installation

Edit .env with your config
```sh
cp .env.example .env
```

Run all services.
```sh
make
```
