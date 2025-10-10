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

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](../../../../supervisely-ecosystem/jupyter-datascience-notebook)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/jupyter-datascience-notebook)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/jupyter-datascience-notebook.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/jupyter-datascience-notebook.png)](https://supervisely.com)

</div>

## Overview

The Jupyter Notebook is the original web application for creating and sharing computational documents.
It offers a simple, streamlined, document-centric experience.

You can run JupyterLab server (app) from Supervisely on your computer with preinstalled Supervisely Agent. It comes with default `demo.ipynb` notebook for quick tests.

**🌎 Note For Comunity Edition Users 🌎**

Community users can run this application only on their own agents. Just go to Cluster page and connect your computer to your Supervisely account ([how to video](https://youtu.be/aDqQiYycqyk)).

## Basic usage

### How to run

Run app from the `.ipynb` **file in Team Files** or from the **folder in Team files**. For quick start to try demo notebook you can run the app **from Ecosystem**. Wait for jupyter server to start, demo notebook will show up.

<img src="https://user-images.githubusercontent.com/12828725/193441522-fa6c062c-17b9-4419-838d-b032586a181a.gif">

### How to download from Jupyter

Right click on file -> select Download context menu.

<img src="https://user-images.githubusercontent.com/12828725/193441635-fa7b9672-b533-48f3-ae43-fae32834fb22.png">

### Upload custom notebook from your computer to Jupyter

Drag and drop file from your computer to the notebook.

<img src="https://user-images.githubusercontent.com/12828725/193441748-9e04b4f4-d69b-4662-8f80-27681fc22a39.gif">

### Shutdown application

Once your work with Jupyter is finished, you need to do the following steps:

1. ✅✅✅ Important ✅✅✅: Download files from Jupyter to you local computer before shutdown. By default all app files are stored on the computer where your Supervisely Agent is running. All details about how to store your notebooks in Supervisely, how to access them at any time in Team Files and how to find them on the your computer with Agent will be covered soon in [Advanced usage chapter](#Advanced-usage).

2. Shutdown app

<img src="https://user-images.githubusercontent.com/12828725/193442152-1a4912a4-8157-4f61-9c15-aa46c408a7a5.gif">

## Advanced usage

This section will explain, how to store your notebooks in Supervisely, how to find them on your computer, how to preview them in `Team Files`.

Every notebook in team files can be quickly previewed before run:

<img src="https://user-images.githubusercontent.com/12828725/193596703-d1ace1c2-e60d-48c6-a2a4-cf0899666079.gif">

You also can run Jupyter notebook from Team File (use existing notebook or upload from your computer using drag-and-drop):

<img src="https://user-images.githubusercontent.com/12828725/193598144-77796726-6f42-4520-b3b1-780b3deac611.gif">


By default all your notebooks are stored on the computer where agent is running. Also Supervisely allows to preview agent's files right in Team Files in web interface. You can open session info in get the paths where files are actually stored on your computer or get the link to Team Files to preview them in Supervisely:

<img src="https://user-images.githubusercontent.com/12828725/193599997-fb8061c8-0a1e-472a-886d-c00d665bb98f.gif">

## Demo

Supervisely jupyter datascience notebook app comes with an example notebook explaining how to:

1. Create supervisely API object
2. Get user info
3. List all the user teams

Learn more about Supervisely automation in [Supervisely Developer Portal](https://developer.supervisely.com/).

<img src="https://user-images.githubusercontent.com/12828725/193601181-76fbca3d-ced9-4cb4-9ae9-cee6ae576704.png">

## Acknowledgment

This app is based on the great work of `Jupyterlab` team ([github](https://github.com/jupyter/jupyter)). ![GitHub Org's stars](https://img.shields.io/github/stars/jupyter/jupyter?style=social)
