FROM jupyter/datascience-notebook:r-4.2.2

COPY . .

RUN \
    Rscript dependencies.r && \
    echo "alias r=radian" >> /etc/bash.bashrc

CMD ["Rscript", "main.r"]
