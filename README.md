# jupyter-datascience-notebook
Ready-to-run Jupyter application with interactive computing tools. You can run JupyterLab server (app) from Supervisely on your computer with preinstalled Supervisely Agent


# debug

docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='my-app'"

docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='${BASE_URL}'"

TODO: 
disable jupyter token
--NotebookApp.token='' --NotebookApp.password=''
