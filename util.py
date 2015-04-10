from collections import namedtuple

def create_named_tuple(*values):
     return namedtuple('NamedTuple', values)(*values)


