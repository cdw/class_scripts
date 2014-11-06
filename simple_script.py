#!/usr/bin/env python
# encoding: utf-8
"""
simple_script.py - generate some random data and then plot a histogram of it

Created by CDW on 2014.11.06
"""




import matplotlib.pyplot as plt
import numpy as np

print 'Hello there!' # Comma removal suggested by E_R
data = np.random.normal(1,1, 10)
plt.plot(data)
plt.show()