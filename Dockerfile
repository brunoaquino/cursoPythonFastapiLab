FROM python:3.11-alpine

WORKDIR /code
ADD . /code

RUN apk update && apk add postgresql-dev tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    apk add --no-cache \
    --virtual=.build-dependencies \
    gcc \
    g++ \
    musl-dev \
    git \
    python3-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev && \
    apk del --purge .build-dependencies && \
    pip install pipenv && \
    pipenv install --system --skip-lock && \
    adduser --disabled-password --shell /bin/sh teste && \
    chmod 755 entrypoint.sh && chown teste:teste entrypoint.sh

EXPOSE 8000
USER teste
ENTRYPOINT ["./entrypoint.sh"]