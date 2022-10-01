import os

# import subprocess
# import shlex
from dotenv import load_dotenv
import supervisely as sly

# for convenient debug, has no effect in production
if sly.is_development():
    load_dotenv("preprocessing/local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

input_file = os.environ.get("CONTEXT_SLYFILE")
team_id = int(os.environ["CONTEXT_TEAMID"])

default_nb = "demo.ipynb"
default_path = os.path.join(sly.app.get_synced_data_dir(), default_nb)


if input_file is None:
    sly.logger.info("App is started from ecosystem")
    sly.fs.copy_file(src=default_nb, dst=default_path)
else:
    sly.logger.info(f"App is started from context menu of file in TeamFiles: {input_file}")
    ext = sly.fs.get_file_ext(input_file)
    if ext != ".ipynb":
        sly.logger.warn(
            "JupyterLab Notebook can only be started from the context menu of '.ipynb' file or from Ecosystem. \n"
            + f"Default demo notebook will be started: {default_path}"
        )
        sly.fs.copy_file(src=default_nb, dst=default_path)
    else:
        default_nb = sly.fs.get_file_name_with_ext(input_file)
        default_path = os.path.join(sly.app.get_synced_data_dir(), default_nb)

        api = sly.Api()
        api.file.download(
            team_id,
            remote_path=input_file,
            local_save_path=os.path.join(sly.app.get_synced_data_dir(), default_nb),
        )

sly.logger.info(f"Default notebook: {default_path}")

# try:
#     process = subprocess.run(
#         shlex.split(
#             f'jupyter lab \
#                 --ip=0.0.0.0 \
#                 --port=8000 \
#                 --allow-root \
#                 --ServerApp.token="" \
#                 --ServerApp.password="" \
#                 --ServerApp.notebook_dir="{sly.app.get_data_dir()}" \
#                 --ServerApp.allow_origin=* \
#                 --ServerApp.base_url=$BASE_URL \
#                 --ServerApp.trust_xheaders=True \
#                 --ServerApp.disable_check_xsrf=True \
#                 --LabApp.default_url="/lab/tree/{default_nb}"'
#         ),
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         universal_newlines=True,
#     )
#     process.check_returncode()
#     sly.logger.info(f"jupyter lab have been successfully finished")
# except Exception as e:
#     print(repr(e))
#     raise e
