from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """generates a list of generic products with names constructed from given
    lists. Generates number of products passed in, default 30
    """
    products = []
    for i in range(num_products):
        adj = sample(ADJECTIVES, 1)[0]
        noun = sample(NOUNS, 1)[0]
        name = adj+' '+noun
        prod = Product(name)
        prod.weight = randint(5, 100)
        prod.price = randint(5, 100)
        prod.flammability = uniform(0, 2.5)
        products.append(prod)
    return products


def inventory_report(products):
    """Prints out sumarry statistics of the current inventory passed in"""

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    unique = set([i.name for i in products])
    print('Unique Product names: ', len(unique))
    meanPrice = (sum([i.price for i in products])/len(products))
    print(f'Average Price: ${meanPrice: .2f}')
    meanWeight = (sum([i.weight for i in products])/len(products))
    print(f'Average weight: {meanWeight}')
    meanFlammability = (sum([i.flammability for i in products])/len(products))
    print(f'Average flammability: {meanFlammability}')


if __name__ == '__main__':
    inventory_report(generate_products())
