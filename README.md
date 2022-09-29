# jupyter-datascience-notebook
Ready-to-run Jupyter application with interactive computing tools. You can run JupyterLab server (app) from Supervisely on your computer with preinstalled Supervisely Agent

Files will be saved on the agent, or you can synchronize it with Git

# Requirements

docker version >= 20.10.18

# Debug

docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='my-app'"

docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='${BASE_URL}'"

# Acknowledgment

This app is based on the great work of `Jupyterlab` team ([github](https://github.com/jupyterlab/jupyterlab-git)). ![GitHub Org's stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-git?style=social)


[//]: # (TODO: )

[//]: # (disable jupyter token)

[//]: # (--NotebookApp.token='' --NotebookApp.password='')
