"""agent-markitdown"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("agent-markitdown")
except PackageNotFoundError:  # running from an uninstalled source tree
    __version__ = "0.0.0+unknown"
