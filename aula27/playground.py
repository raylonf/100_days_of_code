def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(7 ,5, 6, 67,52, 120,2, 10,0))

class car():

    def __init__(self, **kw):
        self.model = kw.get('model')
        self.make = kw.get('make')
        self.color = kw.get('color')


my_car = car(make='Nissan', model='Gtr')
print(my_car.model)
print(my_car.color)