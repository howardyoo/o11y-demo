.DEFAULT_GOAL := help

help:
	@echo "*** docker ***"
	@echo "make up			docker compose up"
	@echo "*** curl ***"
	@echo "make fast		curl fast endpoint"
	@echo "make slow		curl slow endpoint"

up:
	@docker compose up --no-deps --build

fast:
	@curl localhost:8100/proxy/fast

slow:
	@curl localhost:8100/proxy/slow
