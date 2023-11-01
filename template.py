
import os
from pathlib import Path

project = "DimondPricePrediction"

list_of_files = [
"github/workflow/.gitkeep",
f"src/{project}/__init__.py",
f"src/{project}/components/__init__.py",
f"src/{project}/components/data_ingestion.py",
f"src/{project}/components/data_transformation.py",
f"src/{project}/components/model_trainer.py",
f"src/{project}/pipelines/__init__.py",
f"src/{project}/pipelines/training_pipeline.py",
f"src/{project}/pipelines/prediction_pipeline.py",
f"src/{project}/logger.py",
f"src/{project}/exception.py",
f"src/{project}/utils/__init__.py",
"notebooks/research.ipynb",
"notebooks/data/.gitkeep",
"requirements.txt",
"setup.py",
"init_setup.sh"
]

for file_path in list_of_files:
    file_path=Path(file_path)
    directory, file = os.path.split(file_path)
  
    if directory != "":
        os.makedirs(directory,exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0) :
        with open(file_path, "w") as f:
            pass
