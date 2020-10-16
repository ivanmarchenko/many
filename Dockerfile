# FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/

# base image
FROM python:3.8-slim

# environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONDONTWRITEBYCODE 1

# work directory
WORKDIR /manypost

# install dependences
COPY Pipfile Pipfile.lock /manypost/
RUN pip install pipenv && pipenv install --system

# copy project from <root> to /copy/
COPY . /manypost/