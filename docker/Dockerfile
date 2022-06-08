FROM python:3.7.12-alpine

ENV PYTHONUNBUFFERED 1

ARG APP=/app

RUN apk add --no-cache --virtual .build-deps build-base \
    linux-headers postgresql-dev
RUN apk add --no-cache libffi-dev jpeg-dev zlib-dev \
    zeromq-dev \
    openssl-dev \
    postgresql-client \
    postgresql-libs

# Define: the main dir where my application will live
WORKDIR ${APP}

# Copy the code into the image
COPY . ${APP}

# Install libraries or packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Django stuff
RUN python manage.py collectstatic --noinput

RUN apk --purge del .build-deps

# 
ENTRYPOINT [ "/app/docker/docker-entrypoint.sh" ]

CMD ["runserver"]
