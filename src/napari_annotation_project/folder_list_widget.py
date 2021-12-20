from pathlib import Path
from qtpy.QtWidgets import QListWidget
from qtpy.QtCore import Qt


class FolderList(QListWidget):
    # be able to pass the Napari viewer name (viewer)
    def __init__(self, viewer, parent=None):
        super().__init__(parent)

        self.viewer = viewer
        self.setAcceptDrops(True)
        self.setDragEnabled(True)

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
                    self.addItem(file)

    def select_first_file(self):
        
        self.setCurrentRow(0)