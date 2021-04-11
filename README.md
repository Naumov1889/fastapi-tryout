Trying out fastapi. Setup with docker.

# Deps
* ```docker build - < Dockerfile_pip_tools -t pip_tools_image```
* ```docker run --rm -it -v $(pwd):/app pip_tools_image pip-compile --output-file requirements.txt requirements.in```
* ```docker image rm pip_tools_image```

# Migrations
* ```docker-compose run --rm fastapi_tryout alembic -c db/migrations/alembic.ini revision -m "first_migration"```
* ```docker-compose run --rm fastapi_tryout alembic -c db/migrations/alembic.ini upgrade head```
* ```docker-compose exec fastapi_tryout_posgres psql -h fastapi_tryout_db_server_local -U fastapitryoutuserlocal --dbname=fastapitryoutdblocal```
