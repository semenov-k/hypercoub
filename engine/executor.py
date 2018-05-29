import os
import threading
import importlib.util

from engine import map
from engine import builder


class Worker(threading.Thread):
    """
    Compilation thread executor
    """

    def __init__(self, compmap_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._compmap_path = compmap_path

    def run(self):
        """
        - Prepare compilation map
        - Fill map with local compmap.py
        - Run builder with map
        """
        compmap_spec = importlib.util.spec_from_file_location(
            'compmap',
            os.path.join(self._compmap_path, 'compmap.py')
        )
        compmap = importlib.util.module_from_spec(compmap_spec)

        compilation_map = map.CompilationMap(
            os.path.join(self._compmap_path, 'assets')
        )
        thread_local = threading.local()
        thread_local.cm = compilation_map

        compmap_spec.loader.exec_module(compmap)

        builder.Builder(compilation_map)
