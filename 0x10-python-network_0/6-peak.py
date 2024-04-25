#!/usr/bin/python3
"""Defines a function to find a peak in an unsorted list of integers."""


def find_peak(int_list):
    """Finds a peak in the given list of integers."""

    if not int_list:
        return None

    low = 0
    high = len(int_list) - 1

    while low < high:
        mid = (low + high) // 2

        if int_list[mid] < int_list[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return int_list[low]
