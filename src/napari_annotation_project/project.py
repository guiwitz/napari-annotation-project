from pathlib import Path
from .parameters import Param
import yaml

def create_project(project_path, file_paths=None, channels=None, rois=None):
    """
    Create a project.

    Parameters
    ----------
    project_path : str
        path where the project is saved
    file_paths : list[str]
        list of paths of files belonging to the project
    channels : dict of str
        channel getting exported as source for each file
    rois : dict of arrays
        flat list of rois for each file

    Returns
    -------
    project : Project
        project object

    """

    project_path = Path(project_path)
    if not project_path.exists():
        project_path.mkdir()

    if rois is None:
        rois = {}
    if channels is None:
        channels = {}
    project = Param(
        project_path=project_path,
        file_paths=file_paths,
        channels=channels,
        rois=rois)

    if not project_path.joinpath('annotations').exists():
        project_path.joinpath('annotations').mkdir()
    project.save_parameters()

    return project

def load_project(project_path):
    """
    Load a project.

    Parameters
    ----------
    project_path : str
        path where the project is saved

    Returns
    -------
    project : Project
        project object

    """

    project = Param()
    project_path = Path(project_path)
    if not project_path.joinpath('Parameters.yml').exists():
        raise FileNotFoundError(f"Project {project_path} does not exist")

    with open(project_path.joinpath('Parameters.yml')) as file:
        documents = yaml.full_load(file)
    for k in documents.keys():
        setattr(project, k, documents[k])
    project.project_path = project_path

    return project