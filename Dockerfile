FROM python:3.9.17-slim-bullseye

RUN \
  pip install --upgrade pip==23.1.2


# ENV PYTHONUNBUFFERED=1
# ENV PIP_ROOT_USER_ACTION=ignore

# COPY pyproject.toml pyproject.toml
# COPY poetry.lock poetry.lock

# RUN \
# apt update && \
# apt install sudo && \
# sudo apt upgrade -y && \
# sudo apt install git -y && \
# pip install --upgrade pip==23.1.2 && \
#     pip install poetry==1.4.2 ipython==8.13.2 --root-user-action=ignore && \
#     poetry config virtualenvs.create false && \
#     poetry install --no-interaction --no-ansi

# COPY . .

# CMD ["python", "main.py"]
