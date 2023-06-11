FROM python:3.9.17-slim-bullseye

COPY python-requirements.txt python-requirements.txt

RUN \
  apt update && \
  apt install sudo && \
  sudo apt upgrade -y && \
  # Required for parallel processing in some ML libraries
  sudo apt install libgomp1 && \
  pip install -r python-requirements.txt --root-user-action=ignore
# --upgrade pip==23.1.2


# ENV PYTHONUNBUFFERED=1
# ENV PIP_ROOT_USER_ACTION=ignore

# COPY pyproject.toml pyproject.toml
# COPY poetry.lock poetry.lock

# RUN \
#     poetry config virtualenvs.create false && \
#     poetry install --no-interaction --no-ansi

# COPY . .

# CMD ["python", "main.py"]
