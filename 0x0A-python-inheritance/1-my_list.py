#!/usr/bin/python3
"""Defines a class that inherited from a in-built Python list."""


class MyList(list):
    """inheritance implementation."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
