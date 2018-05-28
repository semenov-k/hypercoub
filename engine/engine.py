import os
import importlib.util


class Engine:
    """
    Main class of hypercoub
    :param module_path: path for relative find compilations models
    """

    def __init__(self, module_path):
        self._compilations_path = os.path.join(os.path.dirname(module_path), 'compilations')
        self._compilations = []

    def enable_compilation(self, directory_name):
        """
        Method for enable certain compilation by name
        :param directory_name: name of directory,
         in compilation directory where place model
        """
        compmap_spec = importlib.util.spec_from_file_location(
            'compmap',
            os.path.join(self._compilations_path, directory_name, 'compmap.py')
        )
        compmap = importlib.util.module_from_spec(compmap_spec)
        compmap_spec.loader.exec_module(compmap)

