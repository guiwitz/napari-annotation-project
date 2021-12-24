import napari_annotation_project
import pytest

from pathlib import Path
import numpy as np
import skimage.io
import shutil

import napari_annotation_project.project as pr

demoimage = np.random.randint(0,255, (30,30), dtype=np.uint8)
demoimage2 = np.random.randint(0,255, (30,30), dtype=np.uint8)
image_annotation = np.random.randint(1,3, (30,30), dtype=np.uint8)
image_annotation2 = np.random.randint(1,3, (30,30), dtype=np.uint8)
data_path = Path('src/napari_annotation_project/_tests/test_data')
if not data_path.exists():
    data_path.mkdir()
skimage.io.imsave('src/napari_annotation_project/_tests/test_data/demo_data.tif', demoimage)
skimage.io.imsave('src/napari_annotation_project/_tests/test_data/demo_data2.tif', demoimage2)
proj_path = Path('src/napari_annotation_project/_tests/test_project')
if proj_path.exists():
    shutil.rmtree(proj_path)

'''def test_fake():
    assert True

def test_project_widget(make_napari_viewer, napari_plugin_manager):
    napari_plugin_manager.register(napari_annotation_project, name='napari-annotation-project')
    viewer = make_napari_viewer()
    num_dw = len(viewer.window._dock_widgets)
    viewer.window.add_plugin_dock_widget(
        plugin_name='napari-annotation-project', widget_name='Project manager'
    )
    
    assert len(viewer.window._dock_widgets) == num_dw + 1'''


@pytest.fixture
def project_widget(make_napari_viewer, napari_plugin_manager):
    napari_plugin_manager.register(napari_annotation_project, name='napari-annotation-project')
    viewer = make_napari_viewer()
    _, widget = viewer.window.add_plugin_dock_widget(
        plugin_name='napari-annotation-project', widget_name='Project manager'
    )
    return widget

def test_project_widget(project_widget):
    
    assert isinstance(project_widget, napari_annotation_project.ProjectWidget)

def test_project_widget_add_file(project_widget):
    
    proj_path = Path('src/napari_annotation_project/_tests/test_project')
    project_widget.params = pr.create_project(proj_path)
    assert proj_path.joinpath('Parameters.yml').is_file(), 'Parameters file not created'
    
    project_widget.file_list.addItem('src/napari_annotation_project/_tests/test_data/demo_data.tif')
    project_widget.file_list.setCurrentRow(0)
    assert project_widget.file_list.count() == 1, 'File not added'
    
    np.testing.assert_array_equal(project_widget.viewer.layers[0].data, demoimage, 'Image not added')
    assert project_widget.viewer.layers[1].name == 'annotations', 'Annotations layer not added'
    assert project_widget.viewer.layers[2].name == 'rois', 'Rois layer not added'
    
    project_widget.file_list.addItem('src/napari_annotation_project/_tests/test_data/demo_data2.tif')
    assert project_widget.file_list.count() == 2, 'Second file not added'

def test_project_add_roi(project_widget):
    
    project_widget._on_click_load_project(project_path='src/napari_annotation_project/_tests/test_project/')
    project_widget.file_list.setCurrentRow(0)
    project_widget.roi_size.setValue(10)
    project_widget._on_click_add_roi_fixed()
    
    assert len(project_widget.viewer.layers['rois'].data) == 1, 'Roi not added'

    project_widget.file_list.setCurrentRow(1)
    project_widget.roi_size.setValue(15)
    project_widget._on_click_add_roi_fixed()

    assert len(project_widget.viewer.layers['rois'].data) == 1, 'Second Roi not added'

def test_project_add_save_annotation(project_widget):
    
    project_path='src/napari_annotation_project/_tests/test_project/'
    project_widget._on_click_load_project(project_path=project_path)
    project_widget.file_list.setCurrentRow(0)
    project_widget.viewer.layers['annotations'].data = image_annotation
    project_widget.file_list.setCurrentRow(1)
    project_widget.viewer.layers['annotations'].data = image_annotation2
    project_widget.save_annotations()

    assert Path(project_path).joinpath('annotations','demo_data_annot.tif').is_file(), 'Annotation not saved'
    assert Path(project_path).joinpath('annotations','demo_data2_annot.tif').is_file(), 'Second annotation not saved'

def test_project_export(project_widget):
    
    project_path=Path('src/napari_annotation_project/_tests/test_project/')
    project_widget._on_click_load_project(project_path=project_path)
    project_widget.file_list.setCurrentRow(0)

    project_widget.export_folder = project_path.joinpath('export')
    if not project_widget.export_folder.exists():
        project_widget.export_folder.mkdir(exist_ok=False)

    project_widget._export_data()

    assert project_widget.export_folder.joinpath('source','img_0.tif').is_file(), 'Source image not exported'
    import_crop = skimage.io.imread(Path(project_widget.export_folder).joinpath('source','img_0.tif'))
    np.testing.assert_array_equal(import_crop, demoimage[0:10,0:10], 'Cropped image not correct')

    assert project_widget.export_folder.joinpath('source','img_1.tif').is_file(), 'Second source image not exported'
    import_crop = skimage.io.imread(Path(project_widget.export_folder).joinpath('source','img_1.tif'))
    np.testing.assert_array_equal(import_crop, demoimage2[0:15,0:15], 'Second cropped image not correct')

def test_project_load(project_widget):
        
    project_widget._on_click_load_project(project_path='src/napari_annotation_project/_tests/test_project/')
    assert project_widget.file_list.count() == 2, 'File not added'

    project_widget.file_list.setCurrentRow(1)
    assert len(project_widget.viewer.layers['rois'].data) == 1, 'Wrong number of rois'
    expected_roi = np.array([[0, 0], [0, 15], [15, 15], [15,0]])
    np.testing.assert_array_equal(project_widget.viewer.layers['rois'].data[0], expected_roi, 'Wrong roi')
    np.testing.assert_array_equal(project_widget.viewer.layers['annotations'].data, image_annotation2, 'Wrong annotation')

def test_project_remove_file(project_widget):
    
    project_path='src/napari_annotation_project/_tests/test_project/'
    project_widget._on_click_load_project(project_path=project_path)
    
    assert project_widget.file_list.count() == 2, 'Wrong number of files'
    
    project_widget.file_list.setCurrentRow(1)
    project_widget._on_remove_file()
    
    assert project_widget.file_list.count() == 1, 'Second image not removed correctly'