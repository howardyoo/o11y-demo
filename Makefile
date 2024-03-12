.DEFAULT_GOAL := help

help:
	@echo "*** docker ***"
	@echo "make up			docker compose up"
	@echo "*** curl ***"
	@echo "make fast		curl fast endpoint"
	@echo "make slow		curl slow endpoint"
	@echo "make many		many curls via fast endpoint"

up:
	@docker compose up --no-deps --build

fast:
	@curl localhost:8100/proxy/fast

slow:
	@curl localhost:8100/proxy/slow

many:
	@while true; do curl -m 5 -q localhost:8100/proxy/random &> /dev/null; done
