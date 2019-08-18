# code: utf-8

'''
Gather util function regarding list operations
'''

import numpy as np


def nanify_list(input_list):
    '''
    Replace every 9999 value from the list with a np.nan
    :param input_list: list to process
    :type input_list: python list object
    '''
    return [np.nan if x == 9999 else x for x in input_list]
