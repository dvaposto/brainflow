# import time
import numpy as np

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations


def main ():
    # demo for data windowing
    NO_WINDOW = 0
    HANNING = 1
    HAMMING = 2
    BLACKMAN_HARRIS = 3
    window_len = 20

    for window_function in range(4):

        if window_function == NO_WINDOW:
            print ('Window data for NO_WINDOW function:')
            window_data = DataFilter.get_window (NO_WINDOW, window_len)
        elif window_function == HANNING:
            print ('Window data for HANNING function:')
            window_data = DataFilter.get_window (HANNING, window_len)
        elif window_function == HAMMING:
            print ('Window data for HAMMING function:')
            window_data = DataFilter.get_window (HAMMING, window_len)
        else:
            print ('Window data for BLACKMAN_HARRIS function:')
            window_data = DataFilter.get_window (BLACKMAN_HARRIS, window_len)

        print (window_data)

if __name__ == "__main__":
    main ()