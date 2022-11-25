# napari-annotation-project

[![License](https://img.shields.io/pypi/l/napari-annotation-project.svg?color=green)](https://github.com/guiwitz/napari-annotation-project/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-annotation-project.svg?color=green)](https://pypi.org/project/napari-annotation-project)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-annotation-project.svg?color=green)](https://python.org)
[![tests](https://github.com/guiwitz/napari-annotation-project/workflows/tests/badge.svg)](https://github.com/guiwitz/napari-annotation-project/actions)
[![codecov](https://codecov.io/gh/guiwitz/napari-annotation-project/branch/main/graph/badge.svg)](https://codecov.io/gh/guiwitz/napari-annotation-project)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-annotation-project)](https://napari-hub.org/plugins/napari-annotation-project)

This napari plugin allows to define projects consisting of multiple images that can be annotated with labels and rectangular regions of interest (rois). Those rois can then be exported as series of cropped images and labels, typically to train Machine Learning models. Projects can be easily reopened in order to browse through images and their annotations. This package is a meant to be a *light-weight plugin which does not introduce any specific dependencies* and that should be easily installable in any environment already containing napari and other plugins.

## Usage
To start a project, you can just drag and drop files in the file list area. This prompts for the selection of a project folder. After that, more files (also from different folders) can be dragged and dropped to be included in the project. Files can optionally be copied to the project folder but this option has to be set **before adding files**. When selecting a file in the list, it is opened (using the default image reader or a reader plugin if installed) and two layers, one for rois, and one for annotations are added.

https://user-images.githubusercontent.com/4622767/147265874-57dcd956-4d54-4c76-9129-c1fc2837e6a4.mp4

### Adding rois
After selecting the ```rois``` layer, you can add rectangular rois to the image. If you need square rois of a specific size (as often needed in DL training) you can select the ```Fixed roi size``` option and then use the ```Add roi``` button. **Note that currently only 2D rois are supported**. If you work with nD images, the roi is therefore added to the **current selected 2D plane**.

### Adding annotations
After selecting the ```annotations``` layer, you can add annotations to your image. There are no restrictions here and you can e.g. add as many labels as you need.

### Info storage
All relevant information on project location, project files and rois is stored in a yaml file ```Parameters.yml```. Annotations are stored as 2D tiff files in the ```annotations``` as files named after the original files. **Note that at the moment if multiple files have the same name, this will cause trouble**. This parameter file is used when re-loading an existing project.

https://user-images.githubusercontent.com/4622767/147265984-adb6ee1f-9319-45c9-a9a4-735ade2a3905.mp4

## Exporting rois
Once you are satisfied with your annotations and rois, you can use the rois to export only the corresponing cropped rois of both the image and annotation layers. For this you can head to the ```Export``` tab. Here you can set the location of the export folder, set the names of the folders that will contain cropped images and cropped annotations, and finally set the prefix names for these two types of files. Files are exported as tif files. 

https://user-images.githubusercontent.com/4622767/147266002-9c4485c9-5bcc-4c64-9c92-6c06775e2711.mp4

## Installation


You can install `napari-annotation-project` via [pip] (**note yet functional**):

    pip install napari-annotation-project

To install latest development version :

    pip install git+https://github.com/guiwitz/napari-annotation-project.git

## Contributing

Contributions are very welcome. Tests can be run with [tox].

## License

Distributed under the terms of the [BSD-3] license,
"napari-annotation-project" is free and open source software.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/guiwitz/napari-annotation-project/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
