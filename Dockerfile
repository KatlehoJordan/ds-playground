FROM jupyter/datascience-notebook:r-4.2.2

COPY . .

# RUN \
#     pip install -U radian \
#     Rscript dependencies.r
