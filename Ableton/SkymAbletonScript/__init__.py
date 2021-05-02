from __future__ import absolute_import, print_function, unicode_literals
from .skym import skym

def create_instance(c_instance):
    return skym(c_instance)
