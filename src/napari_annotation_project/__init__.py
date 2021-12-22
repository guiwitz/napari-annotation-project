
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"


from .project_widget import napari_experimental_provide_dock_widget
from .project_widget import ProjectWidget