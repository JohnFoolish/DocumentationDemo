# -*- coding: utf-8 -*-
"""
This first one is a basic function that includes the code you would need to
add two numbers together!

Why is this function useful?
----------------------------
* It can replace the '+' key!
* It can cause you to bill more hours for less work since the import takes
  extra time to type!
* It can serve as a helpful demo.

Written by John Lewis Corker
"""

def basic_numpy(x, y):
    """A very basic addition numpy function.

    This function contains a basic numpy docstring that we should be able to
    look at and compare.

    Usage below:
        >>> basic(5, 8)
        >>> 13

    Parameters
    ----------
    x : int
        This is a basic variable that will be added to the y value.

    y : int
        This is a basic variable that will be added to the x value.

    Returns
    -------
    int
        The value of x and y added together

    """
    z = x + y
    return z

def basic_google(x, y):
    """A basic addition google function.

    This function contains a basic google docstring that we should be able to
    look at and compare.

    Usage below:
        >>> basic(5, 8)
        >>> 13

    Args:
        x (int): a basic variable that will be added to the y value

        y (int): a basic variable that will be added to the x value

    Returns:
        int: The value of x and y added together

    """
    z = x + y
    return z


if __name__ == '__main__':
    basic(5, 10)