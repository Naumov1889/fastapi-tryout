FROM python:3.9

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./src /src

CMD uvicorn src.main:app --reload --port 8000 --host 0.0.0.0
