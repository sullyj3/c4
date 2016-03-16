def is_number(x):
    return type(x) in (int, float, complex)

class C4(object):
    ''' Provides C like looping. (kinda)
    The general idea is that if you would write
        for (i=start; guard; inc) {}
    in c, you write
        for i in C4(start, guard, inc):

    start should be a number.
    guard should be a callable that takes a number and returns a bool.
    inc can be a number or a callable that takes a number and returns a number

    if inc is a number, on each iteration inc is added to the previous value.
    Alternatively, if inc is a callable, the next value will be inc(previous).

    examples:
    C:
        for (i=0; i<10; i++) {}
    python with c4:
        for i in C4(0, lambda x:x<10, 1):
    this one is uninteresting, because it can be done more easily with range(10). However it illustrates how c4 works

    C:
        for (i=10; i<10000; i = i*10) {}
    python with c4:
        for i in C4(10, lambda x:x<10000, lambda x:x*10):
    This one is a little cooler, since it can't be done using only range()

    '''
    def __init__(self, start, guard, inc):
        if not (callable(inc) or is_number(inc)):
            raise ValueError

        self.start = start
        self.guard = guard
        self.inc = inc

        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.guard(self.current):
            raise StopIteration

        current = self.current

        if callable(self.inc):
            self.current = self.inc(current)
        elif is_number(self.inc):
            self.current += self.inc

        return current
