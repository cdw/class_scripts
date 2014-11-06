#!/usr/bin/env python
# encoding: utf-8
"""
simple_script.py - generate some random data and then plot a histogram of it

Created by CDW on 2014.11.06
"""

import matplotlib.pyplot as plt
import numpy as np

## Globals
DIST_CENTER = 0
DIST_SKEW = 1


## Support functions
def show_bryant(data_length=500000, bins=100):
    """Create some data with the gumbel distribution, then plot it as a histogram
    Takes:
        data_length: how many points to generate (500000)
        bins: how many bins to sort the data into for the histogram (100)
    Gives:
        None
    """
    data = np.random.gumbel(DIST_CENTER,DIST_SKEW,data_length)
    plt.hist(data, bins)
    plt.show()

## Boilerplate
def main():
    show_bryant(10000, 50)


if __name__ == '__main__':
	main()
