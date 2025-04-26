docker run --name my-postgres --env POSTGRES_PASSWORD=postgres --volume postgres-volume:/var/lib/postgresql/data --publish 5432:5432 --detach postgres
