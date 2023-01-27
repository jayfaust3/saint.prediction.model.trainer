FROM python:3.10.5-slim-buster

EXPOSE 80

RUN apt-get update

# PYODBC DEPENDENCES
RUN apt-get install g++ -y \
    # Probably the below package is not necessary
    && apt-get install gcc -y \
    # Packages below are most likely necessary
    && apt-get install unixodbc -y \
    && apt-get install unixodbc-dev -y \
    && apt-get install unixodbc-bin -y \
    && apt-get install odbc-postgresql -y

RUN apt-get install libpq-dev

ADD odbcinst.ini /etc/odbcinst.ini
ADD odbc.ini /etc/odbc.ini

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