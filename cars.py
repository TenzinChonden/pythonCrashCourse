cars = {}

def make_car(manufacturer, model, **kwargs):
    index = len(cars)
    cars[index] = {"Manufacturer" : manufacturer, 
                      "Model" : model, 
                       **kwargs,}

make_car("subaru", "outback", color="blue", tow_package=True)
make_car("honda", "crv", color="white", tow_package=False)
make_car("toyota", "rav4", color="black", tow_package=True, trim="sport")

print(cars)
