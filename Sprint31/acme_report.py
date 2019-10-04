from random import randint, sample, uniform
from acme import Product, BoxingGlove

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30, producttype=Product):
    """generates a list of generic products with names constructed from given
    lists. Generates number of products passed in, default 30
    """
    products = []
    for i in range(num_products):
        adj = sample(ADJECTIVES, 1)[0]
        noun = sample(NOUNS, 1)[0]
        name = adj+' '+noun
        prod = producttype(name)
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
    steal = sorted([i.stealability() for i in products])
    kinda = sum([1 if i == 'Kinda stealable' else 0 for i in steal])
    nots = sum([1 if i == 'Not so stealable...' else 0 for i in steal])
    very = sum([1 if i == 'Very stealable' else 0 for i in steal])
    print('Count of Not so stealable products: ', nots)
    print('Count of Kinda Stealable products: ', kinda)
    print('Count of Very stealable products: ', very)


if __name__ == '__main__':
    inventory_report(generate_products())
