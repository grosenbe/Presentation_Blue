#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 30, 5
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 25, facecolor='b', alpha=0.75, edgecolor='black')
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])

plt.xlabel('Frame Delay $\delta$ [ms]')
plt.ylabel('# of Frames')
plt.title('Histogram of Frame Rendering Delays')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
