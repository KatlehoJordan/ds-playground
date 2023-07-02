FROM python:3.9.17-slim-bullseye

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_ROOT_USER_ACTION=ignore \
    PIP_DEFAULT_TIMEOUT=300

COPY requirements.txt requirements.txt

RUN \
    apt update && \
    apt install sudo=1.9.5p2-3+deb11u1 && \
    sudo apt upgrade -y && \
    # Required for parallel processing in some ML libraries
    sudo apt install libgomp1=10.2.1-6 && \
    pip install -r requirements.txt --root-user-action=ignore

COPY . .

CMD [""]
