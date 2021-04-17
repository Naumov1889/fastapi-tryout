Trying out fastapi. Setup with docker.

# Commands
## Deps
* ```./bin/update_deps.sh```

## Migrations
* ```docker-compose run --rm fastapi_tryout alembic -c db/migrations/alembic.ini revision -m "create_main_tables"```
* ```docker-compose run --rm fastapi_tryout alembic -c db/migrations/alembic.ini upgrade head```
* ```docker-compose exec fastapi_tryout_posgres psql -h fastapi_tryout_db_server_local -U fastapitryoutuserlocal --dbname=fastapitryoutdblocal```

## Testing
* ```docker-compose run --rm fastapi_tryout pytest -v```

# Secret
* ```openssl rand -hex 32```