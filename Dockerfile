FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/


RUN python3 -m venv myenv
RUN source /app/myenv/bin/activate
RUN pip install -r requirements.txt

COPY . /app/

