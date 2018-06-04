"""Do a minimal test of all the modules that aren't otherwise tested."""

from test import test_support
import sys
import unittest


class TestUntestedModules(unittest.TestCase):
    def test_at_least_import_untested_modules(self):
        with test_support.check_warnings(quiet=True):

            if sys.platform.startswith('win'):
                pass

            if sys.platform.startswith('win'):
                pass

            try:
                import tty     # not available on Windows
            except ImportError:
                if test_support.verbose:
                    print "skipping tty"

            # Can't test the "user" module -- if the user has a ~/.pythonrc.py, it
            # can screw up all sorts of things (esp. if it prints!).
            #import user


def test_main():
    test_support.run_unittest(TestUntestedModules)

if __name__ == "__main__":
    test_main()
