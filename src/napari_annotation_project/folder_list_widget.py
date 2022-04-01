import shutil
import os
from pathlib import Path
from qtpy.QtWidgets import QListWidget
from qtpy.QtCore import Qt


class FolderList(QListWidget):
    # be able to pass the Napari viewer name (viewer)
    def __init__(self, viewer, parent=None, local_copy=False, local_folder=None):
        super().__init__(parent)

        self.viewer = viewer
        self.setAcceptDrops(True)
        self.setDragEnabled(True)

        self.local_copy = local_copy
        self.local_folder = local_folder

        #self.model().rowsInserted.connect(self.addFileEvent())

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):

        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            
            for url in event.mimeData().urls():
                file = str(url.toLocalFile())
                if Path(file).is_dir():
                    raise NotImplementedError("Folder drag and drop not implemented yet")
                else:
                    if self.local_copy:
                        copy_to = self.local_folder.joinpath(Path(file).name)
                        shutil.copy(Path(file), copy_to)
                        self.addItem(copy_to.as_posix())
                    else:
                        self.addItem(file)
    
    def addFileEvent(self):
        pass

    def select_first_file(self):
        
        self.setCurrentRow(0)