import unittest
import partitura
import time
from music21.converter import parse

class ExportNotearrays(unittest.TestCase):
    def test_notearray_compute(self):
        xml = partitura.EXAMPLE_MUSICXML
        pfile = partitura.load_musicxml(xml)
        mfile = parse(xml)

        start = time.time()
        partitura.utils.ensure_notearray(pfile)
        end = time.time()
        ptime = end - start

        start = time.time()
        mfile.recurse().notes
        end = time.time()
        mtime = end - start
        self.assertTrue(ptime < mtime, "Music21 is faster than partitura.")

if __name__ == '__main__':
    unittest.main()
