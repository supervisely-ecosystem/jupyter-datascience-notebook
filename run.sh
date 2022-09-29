set -o pipefail -e
cp /repo/demo.ipynb /sly-workdir/demo.ipynb
jupyter lab --ip=0.0.0.0 --port=8000 --allow-root --ServerApp.token='' --ServerApp.password='' --ServerApp.allow_origin=* --ServerApp.base_url=$BASE_URL --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=True --LabApp.default_url='/lab/tree/demo.ipynb'