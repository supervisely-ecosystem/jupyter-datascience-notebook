FROM jupyter/datascience-notebook

USER root

RUN pip install supervisely==6.64.0

WORKDIR /sly-workdir

COPY /demo.ipymb /repo/demo.ipynb
COPY /run.sh /repo/run.sh
