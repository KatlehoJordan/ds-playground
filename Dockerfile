FROM --platform=linux python:3.9

ENV \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_ROOT_USER_ACTION=ignore \
  PIP_DEFAULT_TIMEOUT=300

COPY requirements.txt requirements.txt

RUN \
  apt-get update && \
  apt-get install sudo && \
  pip install --upgrade pip==23.1.2 && \
  pip install -r requirements.txt --root-user-action=ignore

COPY . .

CMD ["python", "main.py"]
