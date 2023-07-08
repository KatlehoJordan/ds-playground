FROM r-base:4.2.3

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_ROOT_USER_ACTION=ignore \
    PIP_DEFAULT_TIMEOUT=300

COPY requirements.r requirements.r

RUN \
    apt update && \
    apt install sudo && \
    sudo apt upgrade -y && \
    sudo apt install python3-pip -y && \
    pip install radian --break-system-packages && \
    echo "alias r='radian'" >> ~/.bashrc && \
    # For R language server package
    sudo apt install libxml2-dev -y && \
    # For httpgd
    sudo apt install libfontconfig1-dev -y && \
    # For plotly
    sudo apt install libssl-dev && \
    # For jupyter
    pip install jupyter_client --break-system-packages && \
    # Install R packages
    Rscript requirements.r

CMD ["r"]
