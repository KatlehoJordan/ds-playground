FROM python:3.9.17-slim-bullseye

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_ROOT_USER_ACTION=ignore \
    PIP_DEFAULT_TIMEOUT=300

COPY pyproject.toml pyproject.toml

RUN \
    apt update && \
    apt install sudo && \
    sudo apt upgrade -y && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --without ml --without dev

CMD ["ipython"]
