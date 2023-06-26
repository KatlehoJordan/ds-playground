FROM python:3.9.17-slim-bullseye

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_ROOT_USER_ACTION=ignore \
    PIP_DEFAULT_TIMEOUT=300 \
    R_VERSION=4.2.3

COPY python-requirements.txt python-requirements.txt
COPY r-requirements.r r-requirements.r

RUN \
    apt update && \
    apt install sudo=1.9.5p2-3+deb11u1 && \
    sudo apt upgrade -y && \
    # Required for parallel processing in some ML libraries
    sudo apt install libgomp1=10.2.1-6 && \
    pip install -r python-requirements.txt --root-user-action=ignore && \
    # Required for R installation
    sudo apt install gdebi-core=0.9.5.7+nmu5 -y && \
    sudo apt install curl=7.74.0-1.3+deb11u7 -y && \
    curl -O https://cdn.rstudio.com/r/debian-11/pkgs/r-${R_VERSION}_1_amd64.deb && \
    sudo gdebi r-${R_VERSION}_1_amd64.deb -n && \
    rm r-${R_VERSION}* && \
    sudo ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R && \
    sudo ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript && \
    # For radian
    pip install radian==0.6.6 && \
    echo "alias r='radian'" >> ~/.bashrc && \
    # For R language server package
    sudo apt install libxml2-dev=2.9.10+dfsg-6.7+deb11u4 && \
    # For httpgd
    sudo apt install libfontconfig1-dev=2.13.1-4.2 -y && \
    # For plotly
    sudo apt install libssl-dev=1.1.1n-0+deb11u5 && \
    #   # For knitting and rendering R Markdown
    #   sudo apt install pandoc=2.9.2.1-1+b1 -y && \
    # For devtools
    sudo apt install libharfbuzz-dev=2.7.4-1 -y && \
    sudo apt install libfribidi-dev=1.0.8-2+deb11u1 && \
    sudo apt install libtiff5-dev=4.2.0-1+deb11u4 -y && \
    #   # Install R packages
    Rscript r-requirements.r

COPY . .

CMD ["python", "main.py"]
