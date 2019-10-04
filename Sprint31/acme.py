# Part 1: Acme

import random


class Product():
    """
    This Class represents products sold by the acme corp. It has parameters of:
    Name, No default
    Price, Default 10
    Weight, Default 20
    flammability, default .5
    identifier, Randomly generated ID number
    """

    def __init__(self, name, price=10, weight=20, flammability=.5,
                 identifier=random.randint(1000000, 9999999)):
        if type(name) != str:
            raise TypeError("name must be string")
        else:
            self.name = name
        if type(price) == int or type(price) == float:
            self.price = price
        else:
            raise TypeError("Price must be a number")
        if type(weight) == int or type(weight) == float:
            self.weight = weight
        else:
            raise TypeError("Weight must be a number")
        if type(flammability) == float:
            self.flammability = flammability
        elif type(flammability) == int:
            self.flammability = float(flammability)
        else:
            raise TypeError("flammability must be a float")
        if type(identifier) == int:
            self.identifier = identifier
        else:
            raise TypeError("Identifier must be an int")

    def stealability(self):
        """calulates the products stealability as a factor of its
        price and weight """
        stealrate = self.price/self.weight
        if stealrate < .5:
            message = 'Not so stealable...'
        elif stealrate < 1:
            message = 'Kinda stealable'
        else:
            message = 'Very stealable'
        return message

    def explode(self):
        """Potentially causes the product to explode depending on its weight
        and flammability"""
        explosionFactor = self.flammability*self.weight
        if explosionFactor < 10:
            message = '...fizzle'
        elif explosionFactor < 50:
            message = '...boom!'
        else:
            message = '...BABOOM!!'
        return message


class BoxingGlove(Product):
    """
    A special type of product that is specifically a boxing glove.
    Has same parameters as a product with only a default weight of 10
    """

    def __init__(self, name, weight=10):
        super().__init__(name, weight=weight)

    def explode(self):
        """Gloves don't explode"""
        return "... it's a glove."

    def punch(self):
        """returns the response of someone being punched by the glove depending
        on weight """
        if self.weight < 5:
            message = 'That tickles'
        elif self.weight < 15:
            message = 'Hey that hurt!'
        else:
            message = "OUCH!"
        return message
