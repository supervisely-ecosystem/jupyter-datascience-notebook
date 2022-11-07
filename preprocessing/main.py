import os

# import subprocess
# import shlex
from dotenv import load_dotenv
import supervisely as sly

# for convenient debug, has no effect in production
if sly.is_development():
    load_dotenv("preprocessing/local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


input_folder = sly.env.folder(raise_not_found=False)
input_file = sly.env.file(raise_not_found=False)

# input_file = os.environ.get("CONTEXT_SLYFILE")
team_id = sly.env.team_id() 
#int(os.environ["CONTEXT_TEAMID"])

default_nb = "demo.ipynb"
default_path = os.path.join(sly.app.get_synced_data_dir(), default_nb)
default_url = f"/lab/tree/{default_nb}"

if input_file is None and input_folder is None:
    sly.logger.info("App is started from ecosystem")
    sly.fs.copy_file(src=default_nb, dst=default_path)
else:
    if input_file is not None:
        sly.logger.info(f"App is started from file context menu in TeamFiles: {input_file}")
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
    else:
        # input directory
        default_path = sly.app.get_synced_data_dir()
        api = sly.Api()
        api.file.download_directory(team_id, remote_path=input_folder, local_save_path=default_path)
        default_url = "/tree"

sly.logger.info(f"Default notebook: {default_path}")
with open("default_url.txt", "w") as text_file:
    text_file.write(default_url)

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
