import unittest
from src.utils import helper_func
import partitura
from music21.converter import parse
from src.test_runtime import MUSICXML_TESTFILES


class TestMusicxmlRuntime(unittest.TestCase):

    reps = 100

    def test_example(self):

        my_xml = partitura.EXAMPLE_MUSICXML
        time_partitura, time_music21 = helper_func(partitura.load_musicxml, parse, my_xml, self.reps)
        print(
            "AVERAGE TIME FOR {} REPETITIONS \n Partitura Parsing Time : {} \n Music21 Parsing time : {}".format(self.reps, time_partitura, time_music21)

        )
        self.assertTrue(time_partitura < time_music21, "Partitura is Slower")

    def test_all(self):
        for my_xml in MUSICXML_TESTFILES:
            time_partitura, time_music21 = helper_func(partitura.load_musicxml, parse, my_xml, self.reps)
            print(
                "AVERAGE TIME FOR {} REPETITIONS \n Partitura Parsing Time : {} \n Music21 Parsing time : {}".format(
                    self.reps, time_partitura, time_music21)
            )
            self.assertTrue(time_partitura < time_music21, "Partitura is Slower")

if __name__ == '__main__':
    unittest.main()
