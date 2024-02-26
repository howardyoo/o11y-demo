FROM python:3.11.7-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY app.py .

CMD python3 /app/app.py
