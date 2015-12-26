# -*- coding: utf-8 -*-

class EmptyError(Exception):
    msg = "Given input is empty!"
    def __str__(self):
        return EmptyError.msg
    def __repr__(self):
        return EmptyError.msg


class DimensionError(Exception):
    msg = "Given input does not match the dimension!"
    def __str__(self):
        return DimensionError.msg
    def __repr__(self):
        return DimensionError.msg
