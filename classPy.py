# October 05, 2019
class Kettle(object):
    power_source = "Electricity"

    def __init__(self, make, price):
        #super(, self).__init__()
        self.make = make
        self.price = price
        self.on = False
    def switch_on(self):
        self.on = True

kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price =12.75
print(kenwood.price)

hamilton = Kettle("hamilton", 18.00)
print(hamilton.make)
print(hamilton.price)
# The following  are Equal
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price},{1.make} = {1.price}".format(kenwood, hamilton))
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()
# The same
print("*" * 50)
print(50 * "*")
# Static field
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("Switch power source")
Kettle.power_source = "Atomic"
kenwood.power_source = "Gas"
print(Kettle.power_source)
print(kenwood.power_source)

print("*" * 50)
print(50 * "*")
# print(Kettle.__dict__)
# print(kenwood.__dict__)
# print(hamilton.__dict__)
