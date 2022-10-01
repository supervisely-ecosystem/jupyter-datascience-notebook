import os
from dotenv import load_dotenv
import supervisely as sly

# for convenient debug, has no effect in production
load_dotenv("preprocessing/local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

input_file = os.environ.get("context.slyFile")
if input_file is None:
    sly.logger.info("App is started from ecosystem")
    exit(0)

sly.logger.info(f"App is started from context menu of file in TeamFiles: {input_file}")
ext = sly.fs.get_file_ext(input_file)
if ext != ".ipynb":
    raise ValueError(
        "JupyterLab Notebook can only be started from the context menu of '.ipynb' file or from Ecosystem"
    )
