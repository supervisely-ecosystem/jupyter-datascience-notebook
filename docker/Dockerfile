FROM jupyter/datascience-notebook

ENV NB_USER supervisely
ENV CHOWN_HOME yes
ENV CHOWN_EXTRA_OPTS -R

WORKDIR /sly-app-data
USER root

RUN pip install supervisely==6.63.0
