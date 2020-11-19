# FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/

# base image slim
# FROM python:3.8-slim
# for selenium
FROM python:3.8


# environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

# work directory
WORKDIR /manypost

# install dependences
COPY Pipfile Pipfile.lock /manypost/
RUN pip install pipenv && pipenv install --system

# copy project from <root> to /copy/
COPY . /manypost/


# FOR CHROME WEBDRIVER 
# install wget with -y 
RUN apt -y update
RUN apt install -y wget

# adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# updating apt to see and install Google Chrome
RUN apt -y update

# install Google Chrome
RUN apt install -y google-chrome-stable

# download latest Chrome Webdriver 
# blocked for CRIMEA
# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN wget -O /tmp/chromedriver.zip http://manypost.ru/files/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99
