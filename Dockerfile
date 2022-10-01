FROM jupyter/datascience-notebook

USER root

RUN pip install supervisely==6.64.2

WORKDIR /sly-workdir

COPY /demo.ipynb /repo/demo.ipynb
COPY /run.sh /repo/run.sh
COPY /preprocessing /repo/preprocessing