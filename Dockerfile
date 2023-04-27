FROM python:3.7
COPY . /app
EXPOSE 80

ENV FLASK_ENV="production"
ENV TZ=America/Sao_Paulo

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt