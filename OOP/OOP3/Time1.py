class Time:
    """
    Represents the time of day.
    
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        pass

    def __str__(self):
        """return a Time object in a human-readable format
        
        text representation of this object
        """
        pass

    def __add__(self, other):
        pass

    def print_time(self):
        pass

    def time_to_int(self):
        """Computes the number of seconds since midnight.
        """
        pass

    def is_after(self, other):
        pass

    def increment(self, seconds):
        pass


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
 
def main():
    start = Time(9, 45, 00)# create and initialize the Time object
    start.print_time()

    end = start.increment(1337)
    # end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()