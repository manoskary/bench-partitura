import unittest
import time

class ImportTime(unittest.TestCase):
    def test_import(self):
        start = time.time()
        import partitura
        end = time.time()
        ptime = end - start

        start = time.time()
        import music21
        end = time.time()
        mtime = end - start
        self.assertTrue(ptime < mtime, "Music21 is faster than partitura.")

if __name__ == '__main__':
    unittest.main()
