import math


def add_pizza(pizzas):
    """Gather user input and add pizza to list"""
    print 'Enter a pizza'
    dm = input('Diameter (inches): ')
    price = input('Price: $')
    notes = raw_input('Notes (brand, toppings, etc.): ')
    pizzas.append(Pizza(dm, price, notes))

def print_results(pizzas):
    """Sort pizzas by price/sq. in. and output in a fancy table."""
    pizzas.sort(key=lambda pizza: pizza.price_per_sq_inch())  #Sort pizza by
    #price per square inch.
    print ''
    print 'Pizzas, sorted by value from best to worst'
    print ''
    print 'Price  | Diameter | $/sq. in. | Notes'
    print '========================================='
    for pizza in pizzas:
        pizza.print_row()

class Pizza(object):
    def __init__(self, dm, price, notes):
        """Create a yummy pizza"""
        self.dm = dm
        self.price = price
        self.notes = notes

    def price_per_sq_inch(self):
        """Calculate price per square inch"""
        area = (self.dm / 2) ** 2 * math.pi
        return round(self.price / area, 4)

    def print_row(self):
        """Print pizza as a row in the table"""
        print ('${0:5g} | {1:8g} | ${2:8g} | '+self.notes).format(
                self.price,
                self.dm,
                self.price_per_sq_inch(),
                )



if __name__=='__main__':
    pizzas = []

    print 'Pizzeria'
    print '=========='
    print 'Find the best pizza for the best price by comparing price / sq. inch.'

    add_pizza(pizzas)

    while True:
        print ''
        print ''
        print 'What would you like to do?'
        print 'a = add a pizza'
        print 'p = print results'
        print 'q = quit'
        choice = raw_input('Choice: ')
        if choice=='q':
            break
        elif choice=='a':
            add_pizza(pizzas)
        elif choice=='p':
            print_results(pizzas)

