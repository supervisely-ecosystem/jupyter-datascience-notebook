# jupyter-datascience-notebook
Ready-to-run Jupyter application with interactive computing tools. You can run JupyterLab server (app) from Supervisely on your computer with preinstalled Supervisely Agent

Files will be saved on the agent, or you can synchronize it with Git

# requirements

docker version >= 20.10.18

# debug

docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='my-app'"

docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='${BASE_URL}'"

[//]: # (TODO: )

[//]: # (disable jupyter token)

[//]: # (--NotebookApp.token='' --NotebookApp.password='')
