#!/usr/bin/python3
""""This defines a locked class""""


class Lockclass:
    """
    prevents the user from dynamically creating new instance attributes, 
    except if the new instance attribute is called first_name.
    """

    __slots__["first_name"]
