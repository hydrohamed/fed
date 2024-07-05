# Dockerfile
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin

# Set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /usr/src/app/

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "fed.wsgi:application"]
