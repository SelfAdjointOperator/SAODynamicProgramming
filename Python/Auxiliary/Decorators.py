def AllNonFalsyArgs(*handler_args):
    """Returns the tuple $handler_args if any of the decorated function's parameters are Falsy ie 0, [], False.
    Otherwise returns what the function normally does"""
    def helper(function):
        def inner(*args,**kwargs):
            if any(not arg for arg in args):
                return (*handler_args,)
            else:
                return function(*args,**kwargs)
        return inner
    return helper

if __name__ == "__main__":
    @AllNonFalsyArgs(777)
    def example(x,y):
        return "{} is good, also {}".format(x,y)
    print(example(4,7))
    print(example(True,8))
    print(example(1,False))
    print(example(0,False))
    print(example(0,8))
    print(example(1,9))
