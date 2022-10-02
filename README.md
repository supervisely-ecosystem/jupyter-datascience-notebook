<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48913536/193065037-3ad134cb-194f-4016-882e-326587ee096f.png"/>

# Jupyter Datascience Notebook

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Basic-usage">Basic usage</a> •
  <a href="#Advanced-usage">Advanced usage</a> •
  <a href="#Demo">Demo</a> •
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

You can run JupyterLab server (app) from Supervisely on your computer with preinstalled Supervisely Agent. It comes with default `demo.ipynb` notebook for quick tests.

**🌎 Note For Comunity Edition Users 🌎**

Community users can run this application only on their own agents. Just go to Cluster page and connect your computer to your Supervisely account ([how to video](https://youtu.be/aDqQiYycqyk)).

## Basic usage

### How to run

Run the app from Ecosystem. Wait for jupyter server to start, demo notebook will show up.

<img src="https://user-images.githubusercontent.com/12828725/193441522-fa6c062c-17b9-4419-838d-b032586a181a.gif">

### How to download from Jupyter

Right click on file -> select Download context menu.

<img src="https://user-images.githubusercontent.com/12828725/193441635-fa7b9672-b533-48f3-ae43-fae32834fb22.png">

### Upload custom notebook from your computer to Jupyter

Drag and drop file from your computer to the notebook.

<img src="https://user-images.githubusercontent.com/12828725/193441748-9e04b4f4-d69b-4662-8f80-27681fc22a39.gif">

### Shutdown application

Once your work with Jupyter is finished, you need to do the following steps:

1. ✅✅✅ Important ✅✅✅: Download files from Jupyter to you local computer. By default all app files are stored on the computer where your Supervisely Agent is running. All details about how to store your notebooks in Supervisely, how to access them at any time in Team Files and how to find them on the your computer with Agent will be covered soon in [Advanced usage chapter](#Advanced-usage).

2. Shutdown app

## Advanced usage

Will be ready soon. This section will explain, how to store your notebooks in Supervisely, how to find them on your computer, how to preview them in `Team Files`.

## Demo

Supervisely jupyter datascience notebook app comes with an example notebook explaining how to:

1. Create supervisely API object
2. Get user info
3. List all the user teams

Learn more about Supervisely automation in [Supervisely Developer Portal](https://developer.supervise.ly/).

<img src="https://user-images.githubusercontent.com/48913536/193070525-cc49875c-38d9-496d-ae3d-764805cbc444.png" width="80%" style='padding-top: 10px'>

## Acknowledgment

This app is based on the great work of `Jupyterlab` team ([github](https://github.com/jupyter/jupyter)). ![GitHub Org's stars](https://img.shields.io/github/stars/jupyter/jupyter?style=social)
