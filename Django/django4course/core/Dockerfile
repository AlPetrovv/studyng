# FROM - base image
FROM python:3.11.9

# ENV - environment varialbles in container
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# RUN - run a command
RUN useradd -m app

RUN apt upgrade -y && apt update -y &&  \
    apt install -y python3-dev gcc musl-dev gdal-bin libgdal-dev gettext

# Working directory
WORKDIR home/app

# ADD - copy file (not folder) from pc to container
ADD pyproject.toml .

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

RUN mkdir -p /home/app/files \
    /home/app/files/logs/app \
    /home/app/files/media  \
    /home/app/files/static \
    /home/app/files/static_source \
    /home/app/files/locale

# COPY - copy folder from pc to container
COPY core .

RUN chown -R app:app /home/app/

# USER - change user to app
USER app



