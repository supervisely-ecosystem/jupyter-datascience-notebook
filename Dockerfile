FROM jupyter/datascience-notebook

USER root

RUN pip install supervisely==6.64.0

WORKDIR /sly-workdir

COPY /demo.ipynb /repo/demo.ipynb
COPY /run.sh /repo/run.sh
