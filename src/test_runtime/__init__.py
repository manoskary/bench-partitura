"""
This module contains tests.
"""

import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(BASE_PATH, "data_samples")
MUSICXML_PATH = os.path.join(DATA_PATH, "musicxml")
MEI_PATH = os.path.join(DATA_PATH, "mei")
KERN_PATH = os.path.join(DATA_PATH, "kern")


MUSICXML_TESTFILES = [
    os.path.join(MUSICXML_PATH, fn)
    for fn in ["K570-2.musicxml", "k080-01.musicxml", "Bruckner_7_Adagio.musicxml"]
]

MEI_TESTFILES = [
    os.path.join(MEI_PATH, fn)
    for fn in ["Bach_Hilf_Herr_Jesu.mei"] # put files here
]

KERN_TESTFILES = [
    os.path.join(KERN_PATH, fn)
    for fn in ["bach_chorale.krn"] # put files here
]