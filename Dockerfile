# Base image
FROM python:3.8

LABEL author ="ANDY"
LABEL description="Sample Singer-tap"

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set workdir
WORKDIR /code

# Install dependencies
RUN apt-get update
RUN apt-get install build-essential nano

RUN pip install pipenv && pipenv install --system

RUN pip install singer-python && pip install singer-tools

# importing source files
COPY * /code/

CMD python -m main.py | singer-check-tap
