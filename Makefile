COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

run: run-monitoring run-seafile run-torrent run-traefik run-uptime-kuma run-dashboard

run-%:
	@echo "$(COLOUR_GREEN)Running $*$(COLOUR_END)"
	cp .env $*
	cd $* && docker-compose up -d

update:
	docker run -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --run-once
