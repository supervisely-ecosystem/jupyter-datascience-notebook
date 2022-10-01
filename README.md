<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48913536/193065037-3ad134cb-194f-4016-882e-326587ee096f.png"/>  

# Jupyter Datascience Notebook

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#Demo">Demo</a> •
  <a href="#Requirements">Requirements</a> •
  <a href="#Debug">Debug</a> •
  <a href="#Acknowledgment">Acknowledgment</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/jupyter-datascience-notebook)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/jupyter-datascience-notebook)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/jupyter-datascience-notebook.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/jupyter-datascience-notebook.png)](https://supervise.ly)

</div>

## Overview

The Jupyter Notebook is the original web application for creating and sharing computational documents.
It offers a simple, streamlined, document-centric experience.
You can run JupyterLab server (app) from Supervisely on your computer with preinstalled Supervisely Agent.
Files will be saved directly on the agent, or you can synchronize it with Git.

**⚠️App can be launched only on USER agents ⚠️**

## How to Run

**Step 1.** Run the app from Ecosystem

<img src="https://user-images.githubusercontent.com/48913536/193070478-50518ebd-d94b-404c-81f8-ded7267163d7.png" width="80%" style='padding-top: 10px'>  

**Step 2.** Wait for jupyter server to start, demo notebook will show up.

<img src="https://user-images.githubusercontent.com/48913536/193070501-8b53e9cd-6a37-41fb-8b5f-3d55d6c893dd.png" width="80%" style='padding-top: 10px'>

## Demo

Supervisely jupyter datascience notebook app comes with an example notebook explaining how to:

1) Create supervisely API object
2) Get user info
3) List all the user teams

<img src="https://user-images.githubusercontent.com/48913536/193070525-cc49875c-38d9-496d-ae3d-764805cbc444.png" width="80%" style='padding-top: 10px'>


## Requirements

```requirements.txt
Docker version >= 20.10.18
```

## Debug

```shell
docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='my-app'"
```

```shell
docker run --rm -it -p 8000:8000 jupyter/datascience-notebook /bin/bash -c "jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --NotebookApp.base_url='${BASE_URL}'"
```

## Acknowledgment

This app is based on the great work of `Jupyterlab` team ([github](https://github.com/jupyter/jupyter)). ![GitHub Org's stars](https://img.shields.io/github/stars/jupyter/jupyter?style=social)
