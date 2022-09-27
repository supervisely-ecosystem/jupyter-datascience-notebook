FROM jupyter/datascience-notebook

ENV CHOWN_EXTRA /sly-app-data
ENV CHOWN_HOME yes
ENV CHOWN_EXTRA_OPTS -R

WORKDIR /sly-app-data

RUN pip install supervisely==6.63.0
