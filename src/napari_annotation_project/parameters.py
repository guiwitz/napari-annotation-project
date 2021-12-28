from __future__ import annotations
from dataclasses import dataclass, field
import dataclasses
from pathlib import Path
import yaml

@dataclass
class Param:
    """
    Class for keeping track of processing parameters.
    
    Paramters
    ---------
    project_path: str
        path where the project is saved
    file_paths: list[str]
        list of paths of files belonging to the project
    channels: dict of str
        channel getting exported as source for each file
    rois: dict of arrays
        flat list of rois for each file
    local_project: bool
        if True, images are saved in local folder
    
    """
    project_path: str = None
    file_paths: list[str] = None
    channels: dict = field(default_factory=dict)
    rois: dict = field(default_factory=dict)
    local_project: bool = False

    def save_parameters(self, alternate_path=None):
        """Save parameters as yml file.

        Parameters
        ----------
        alternate_path : str or Path, optional
            place where to save the parameters file.
        """

        if alternate_path is not None:
            save_path = Path(alternate_path).joinpath("Parameters.yml")
        else:
            save_path = Path(self.project_path).joinpath("Parameters.yml")
    
        with open(save_path, "w") as file:
            dict_to_save = dataclasses.asdict(self)
            if dict_to_save['project_path'] is not None:
                if not isinstance(dict_to_save['project_path'], str):
                    dict_to_save['project_path'] = dict_to_save['project_path'].as_posix()
            if dict_to_save['file_paths'] is not None:
                if not isinstance(dict_to_save['file_paths'][0], str):
                    dict_to_save['file_paths'] = [x.as_posix() for x in dict_to_save['file_paths']]
            yaml.dump(dict_to_save, file)
