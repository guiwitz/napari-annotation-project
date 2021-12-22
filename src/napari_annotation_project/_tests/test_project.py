import shutil
from pathlib import Path
import numpy as np
import skimage.io
from napari_annotation_project import project as pr


demoimage = np.random.randint(0,255, (30,30), dtype=np.uint8)
demoimage2 = np.random.randint(0,255, (30,30), dtype=np.uint8)
image_annotation = np.random.randint(1,3, (30,30), dtype=np.uint8)
image_annotation2 = np.random.randint(1,3, (30,30), dtype=np.uint8)
skimage.io.imsave('src/napari_annotation_project/_tests/test_data/demo_data.tif', demoimage)
skimage.io.imsave('src/napari_annotation_project/_tests/test_data/demo_data2.tif', demoimage2)

proj_path = Path('src/napari_annotation_project/_tests/test_project1')

def test_create_project():
    
    remove_test_folder()
    project = pr.create_project(project_path=proj_path)
    
    assert project.project_path.joinpath('Parameters.yml').is_file(), 'Parameters file not created'
    assert project.project_path.joinpath('annotations').is_dir(), 'annotations folder not created'

def test_create_complete_project():

    remove_test_folder()
    file_paths = ['src/napari_annotation_project/_tests/test_data/demo_data.tif',
                    'src/napari_annotation_project/_tests/test_data/demo_data2.tif']
    rois = {f: [] for f in file_paths}
    channels = {f: None for f in file_paths}
    project = pr.create_project(
        project_path=proj_path,
        file_paths=file_paths, rois=rois, channels=channels)
    
    assert project.project_path.joinpath('Parameters.yml').is_file(), 'Parameters file not created'


def test_load_project():
    
    project = pr.load_project(proj_path)
    
    assert project.file_paths == ['src/napari_annotation_project/_tests/test_data/demo_data.tif',
        'src/napari_annotation_project/_tests/test_data/demo_data2.tif']

    file_paths = ['src/napari_annotation_project/_tests/test_data/demo_data.tif',
                    'src/napari_annotation_project/_tests/test_data/demo_data2.tif']
    rois = {f: [] for f in file_paths}
    channels = {f: None for f in file_paths}

    assert project.rois == rois, 'rois not imported or saved correctly'
    assert project.channels == channels, 'channels not imported or saved correctly'

def remove_test_folder():

    proj_path = Path('src/napari_annotation_project/_tests/test_project')
    if proj_path.exists():
        shutil.rmtree(proj_path)