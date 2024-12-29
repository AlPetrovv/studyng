DC = docker compose
DC_FILE = docker-compose.yaml
ENV_FILE = ./envs/dc.env
EXEC = docker exec -it
POSTGRES_CONTAINER_NAME = django4course-postgres
POSTGRES_SERVICE = postgres

PHONY: run
run: stop
	${DC} -f ${DC_FILE} --env-file ${ENV_FILE} up --build -d

PHONY: stop
stop:
	${DC} -f ${DC_FILE} --env-file ${ENV_FILE} down

PHONY: run-db
run-db: stop-db
	${DC} -f ${DC_FILE} --env-file ${ENV_FILE} up ${POSTGRES_SERVICE} -d


PHONY: stop-db
stop-db:
	${DC} -f ${DC_FILE} --env-file ${ENV_FILE} down ${POSTGRES_SERVICE}
