FROM jupyter/datascience-notebook

ENV CHOWN_EXTRA /sly-app-data
ENV CHOWN_HOME yes
ENV CHOWN_EXTRA_OPTS -R

RUN mkdir /sly-app-data

WORKDIR /sly-app-data
USER root

RUN pip install supervisely==6.63.0
