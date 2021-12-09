
import partitura
from music21.converter import parse
import numpy as np
import matplotlib.pyplot as plt
import time

def helper_func(func1, func2, file, reps):
    list1 = list()
    list2 = list()
    for i in range(reps):
        start = time.time()
        func1(file)
        end = time.time()
        list1.append(end - start)

        start = time.time()
        func2(file)
        end = time.time()
        list2.append(end - start)

    avtime1 = sum(list1) / len(list1)
    avtime2 = sum(list2) / len(list2)
    return avtime1, avtime2

# width of the bars
barWidth = 0.3
reps = 1000
xml_partitura, xml_music21 = helper_func(partitura.load_musicxml, parse, partitura.EXAMPLE_MUSICXML, reps)
mei_partitura, mei_music21 = helper_func(partitura.load_mei, parse, partitura.EXAMPLE_MEI, reps)
kern_partitura, kern_music21 = helper_func(partitura.load_kern, parse, partitura.EXAMPLE_KERN, reps)
# Choose the height of the blue bars
bars1 = list(map(lambda x : 1000*x, [xml_partitura, mei_partitura, kern_partitura]))

# Choose the height of the cyan bars
bars2 = list(map(lambda x : 1000*x, [xml_music21, mei_music21, kern_music21]))

# # Choose the height of the error bars (bars1)
# yer1 = [0.5, 0.4, 0.5]
#
# # Choose the height of the error bars (bars2)
# yer2 = [1, 0.7, 1]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

# Create blue bars
plt.bar(r1, bars1, width=barWidth, color='blue', edgecolor='black', capsize=7, label='partitura')

# Create cyan bars
plt.bar(r2, bars2, width=barWidth, color='cyan', edgecolor='black', capsize=7, label='music21')

# general layout
plt.title('{} Runs of Import'.format(reps))
plt.xticks([r + barWidth for r in range(len(bars1))], ['MusicXML', 'MEI', 'KERN'])
plt.ylabel('Runtime (ms)')
plt.legend()

# Show graphic
plt.show()