import os
import threading


class CompilationMap:
    """
    Model of compilation
    :param assets_path: path to local assets folder
    """

    def __init__(self, assets_path):
        self._assets_path = assets_path
        self._coub_media = {}
        self._local_media = []
        self._index = 0

    def append_local_media(self, assets_filename):
        """
        Ordered append media to compilation from local file
        :param assets_filename: filename into local assets folder
        """
        self._local_media.append({
            'media': os.path.join(self._assets_path, assets_filename),
            'index': self._index
        })
        self._index += 1

    def append_coub_media(self, category):
        """
        Ordered append media to compilation from coub.com
        :param category: category of media from coub.com
        :type category: CoubCategories.*
        """
        if not self._coub_media.get(category):
            self._coub_media[category] = []
        self._coub_media[category].append(self._index)
        self._index += 1


# Local compilation map
local = threading.local()
compilation_map = local.cm
