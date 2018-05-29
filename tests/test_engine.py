import os
import unittest

import engine


class EngineTestCase(unittest.TestCase):

    def test_enable_compilation(self):
        comp_path = os.path.join(os.path.dirname(__file__), 'misc/')
        test_engine = engine.Engine(comp_path)
        test_engine.enable_compilation('testcomp')
        self.assertIsNotNone(test_engine._compilations)
