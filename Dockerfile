# Base image
FROM python:3.8

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set workdir
WORKDIR /code

# Install dependencies
RUN apt-get install build-essential nano

RUN pip install pipenv && pipenv install --system