FROM python:3.10-alpine

ENV HOME /apt
WORKDIR $HOME

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYTHONPATH=$HOME

COPY poetry.lock pyproject.toml $HOME

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

COPY src $HOME/src