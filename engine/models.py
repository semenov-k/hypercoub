import abc


class AbstractMedia(abc.ABC):
    """
    Abstract media class
    """

    def get_assets_path(self):
        """
        Getting path relative assets folder
        :rtype: str
        """
        pass


class LocalMedia(AbstractMedia):
    """
    Local media file
    :param assets_relative_path: path to media file,
    relative to assets folder of compilation
    """

    def __init__(self, assets_relative_path):
        self._


class Compilation:
    """
    Compilation model class
    """

    def __init__(self):
        self._items = []

    def append_media(self, media):
        """
        Append media descriptor for compilation
        :param media: media descriptor
        """
        self._items.append(media)