def is_number(x):
    return type(x) in (int, float, complex)

class C4(object):
    ''' Provides C like looping. (kinda)
    
    examples:
    C:
        for (i=0; i<10; i++) {}
    python with c4:
        for i in C4(0, lambda x:x<10, 1):

    C:
        for (i=10; i<10000; i = i*10) {}
    python with c4:
        for i in C4(10, lambda x:x<10000, lambda x:x*10):

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
