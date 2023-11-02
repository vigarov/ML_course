# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    extended_polys = np.zeros((x.shape[0], degree + 1))
    for i, x_i in enumerate(x):
        extended_polys[i] = np.array([x_i ** j for j in range(0, degree + 1)])
    return extended_polys