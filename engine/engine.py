import os
import inspect
import importlib.util

from engine import executor


class Engine:
    """
    Main class of hypercoub
    :param module_path: path for relative find compilations models
    """

    def __init__(self, module_path):
        self._compilations_path = os.path.join(os.path.dirname(module_path), 'compilations')

    def enable_compilation(self, directory_name):
        """
        Method for enable certain compilation by name and run it in thread
        :param directory_name: name of directory,
         in compilation directory where place model
        """
        comp_path = os.path.join(self._compilations_path, directory_name)
        worker = executor.Worker(comp_path)
        worker.start()
