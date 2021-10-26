import sys
import unittest
from unittest.suite import TestSuite

sys.path.append("../src")
loader = unittest.TestLoader()
testSuite = loader.discover("test")
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)