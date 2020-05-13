"""
Metadata for HippiePlot.
"""

from pathlib import Path

# importlib.metadata is compat with Python 3.8 only
from importlib import metadata as __load

metadata = __load.metadata(Path(__file__).parent.name)
__status__ = "Development"
__copyright__ = "Copyright 2020"
__date__ = "2020-05-11"
__uri__ = metadata["home-page"]
__title__ = metadata["name"]
__summary__ = metadata["summary"]
__license__ = metadata["license"]
__version__ = metadata["version"]
__author__ = metadata["author"]
__maintainer__ = metadata["maintainer"]
__contact__ = metadata["maintainer"]


if __name__ == '__main__':
    print(__title__, __version__)
