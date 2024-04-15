#!/usr/bin/python3

"""Defines a locked class."""


class LockedClass:
    """Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'."""

    # Use __slots__ to restrict attribute creation to 'first_name' only
    __slots__ = ["first_name"]
