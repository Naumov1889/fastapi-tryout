# get base image
FROM python:3.9

# prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevent python from buffering stdout and stderr
ENV PYTHONBUFFERED 1

# copy requirements.txt
COPY ./requirements.txt /requirements.txt
# install requirements.txt
RUN pip install -r /requirements.txt

COPY ./src /src

WORKDIR /src/backend

CMD uvicorn api.server:app --reload --host ${FASTAPI_HOST} --port ${FASTAPI_PORT}
