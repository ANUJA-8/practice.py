#need to understand concept for this method and use it in real life example
'''Create class Counter:
count
method increment()
Create class CounterManager:
static method that resets count to 0'''
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


class CounterManager:

    @staticmethod
    def reset(counter_obj: Counter):
        counter_obj.count = 0
        print("Counter reset to:", counter_obj.count)


# Test
c = Counter()
c.increment()
c.increment()
print("Before reset:", c.count)

CounterManager.reset(c)
c.increment()
print("After reset and increment:", c.count)

c.increment()
c.increment()
c.increment()
print("After 3 increments:", c.count)
CounterManager.reset(c)
print("After second reset:", c.count)