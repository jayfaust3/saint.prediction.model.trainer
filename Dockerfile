FROM python:3.10.5-slim-buster

EXPOSE 80

RUN apt-get update

RUN apt-get update

RUN apt-get install libpq5 -y

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV DEBIAN_FRONTEND=noninteractive

# UPGRADE pip3
RUN pip3 install --upgrade pip

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./app /app

RUN useradd appuser && chown -R appuser /app
USER appuser

CMD ["python", "__main__.py"]
