FROM jupyter/datascience-notebook

USER root

RUN pip install supervisely==6.64.4

WORKDIR /sly-app-data

COPY /demo.ipynb /repo/demo.ipynb
COPY /run.sh /repo/run.sh
COPY /preprocessing /repo/preprocessing