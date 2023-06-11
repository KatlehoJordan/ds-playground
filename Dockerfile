FROM python:3.9.17-slim-bullseye

ENV \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_ROOT_USER_ACTION=ignore \
  PIP_DEFAULT_TIMEOUT=300

COPY python-requirements.txt python-requirements.txt

RUN \
  apt update && \
  apt install sudo && \
  sudo apt upgrade -y && \
  # Required for parallel processing in some ML libraries
  sudo apt install libgomp1 && \
  pip install -r python-requirements.txt --root-user-action=ignore

COPY . .

CMD ["python", "main.py"]
