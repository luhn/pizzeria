import math
import pickle
import os.path


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

def save_data(pizzas):
    """Pickles the pizzas list, and stores it in file"""
    fn = raw_input('Enter filename: ')
    with open(fn, 'w') as f:
        pickle.dump(pizzas, f)
        print 'Data saved to '+fn

def read_data(pizzas):
    """Reads in pickled data """
    fn = raw_input('Enter filename: ')
    if not os.path.exists(fn):
        print 'Error: No such file.'
        return
    cuke = []
    with open(fn, 'r') as f:
        cuke = pickle.load(f)
        print 'Pizzas loaded.'
    pizzas.extend(cuke)

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


def main():
    pizzas = []

    print 'Pizzeria'
    print '=========='
    print 'Find the best pizza for the best price by comparing price / sq. '+\
            'inch.'

    while True:
        print ''
        print ''
        print 'What would you like to do?'
        print 'a = add a pizza'
        print 'p = print results'
        print 's = save data'
        print 'r = read data'
        print 'q = quit'
        choice = raw_input('Choice: ')
        if choice=='q':
            break
        elif choice=='a':
            add_pizza(pizzas)
        elif choice=='p':
            print_results(pizzas)
        elif choice=='s':
            save_data(pizzas)
        elif choice=='r':
            read_data(pizzas)
            print_results(pizzas)

if __name__=='__main__':
    main()
