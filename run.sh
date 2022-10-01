python ./preprocessing/main.py && \
DEFAULT_URL=`cat default_url.txt` && \
echo "Default notebook url: " $DEFAULT_URL && \
jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --ServerApp.token='' --ServerApp.password='' --ServerApp.notebook_dir='/sly-app-data' --ServerApp.allow_origin=* --ServerApp.base_url=$BASE_URL --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=True --LabApp.default_url=$DEFAULT_URL