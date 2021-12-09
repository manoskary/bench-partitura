import unittest
import time
from utils import helper_func
import partitura
from music21.converter import parse
from test_runtime import MEI_TESTFILES


class TestMeiRuntime(unittest.TestCase):

    reps = 100

    def test_example(self):

        fn = partitura.EXAMPLE_MEI
        time_partitura, time_music21 = helper_func(partitura.load_mei, parse, fn, self.reps)
        print(
            "AVERAGE TIME FOR {} REPETITIONS \n Partitura Parsing Time : {} \n Music21 Parsing time : {}".format(self.reps, time_partitura, time_music21)

        )
        self.assertTrue(time_partitura < time_music21, "Partitura is Slower")

    def test_all(self):
        for fn in MEI_TESTFILES:
            time_partitura, time_music21 = helper_func(partitura.load_mei, parse, fn, self.reps)
            print(
                "AVERAGE TIME FOR {} REPETITIONS \n Partitura Parsing Time : {} \n Music21 Parsing time : {}".format(
                    self.reps, time_partitura, time_music21)
            )
            self.assertTrue(time_partitura < time_music21, "Partitura is Slower")

if __name__ == '__main__':
    unittest.main()
