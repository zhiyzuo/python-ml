class EmptyError(Exception):
    msg = "Given input is empty!"
    def __str__(self):
        return EmptyError.msg
    def __repr__(self):
        return EmptyError.msg
