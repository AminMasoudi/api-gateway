FROM python:3.12-slim-bullseye

RUN apt-get update
RUN apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY requirements.txt .
RUN pip install --requirement requirements.txt

COPY . .

ENTRYPOINT [ "make" ]
CMD [ "deploy" ]


