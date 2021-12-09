# Bench Partitura Runtimes

This is a repository to check partitura package runtime vs music21.

We test Runtime of :
- Internal functions such as notearray and pianoroll computation
- Multiformat Parsing such as MEI, MUSICXML and KERN.
- Package Importing

In the future we plan a testing within the package itself by implementing a parallel processing option and benchmarking it.

## Requirements

- matplotlib
- music21
- partitura latest version or develop branch

With pip :
```shell
pip install -r requirements.txt
```

## How to use.

You can run the bench functions to output plots or run the Unitests to check if partitura is faster in your system.

**Example :**
```shell
cd src
python ./test_runtime/bench_xml_runtime.py
```