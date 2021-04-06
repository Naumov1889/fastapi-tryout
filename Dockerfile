FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps g++ gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client\
  # lxml (zeep)
  && apk add libxslt-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./src /src

CMD uvicorn src.main:app --reload --port 8000 --host 0.0.0.0
