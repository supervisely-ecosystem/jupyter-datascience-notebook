printenv && \
python ./preprocessing/main.py  && \
jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --ServerApp.token='' --ServerApp.password='' --ServerApp.notebook_dir='/sly-app-data' --ServerApp.allow_origin=* --ServerApp.base_url=$BASE_URL --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=True 
#--LabApp.default_url='/lab/tree/demo.ipynb'