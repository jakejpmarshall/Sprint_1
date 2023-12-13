from acme import Product
from acme import BoxingGlove
import acme_report
import random

hi = Product("hi")
bg = BoxingGlove('yeet')


def test_product_id_int():
    '''Test both Product and BoxingGlove identifier method deault type.'''
    assert type(hi.identifier) is int
    assert type(bg.identifier) is int


def test_prod_name():
    '''Test both Product and BoxingGlove name method default values.'''
    assert hi.name == "hi"
    assert bg.name == "yeet"


def test_init_price():
    '''Test both Product and BoxingGlove price method default values.'''
    assert hi.price == 10
    assert bg.price == 10


def test_init_weight():
    '''Test both Product and BoxingGlove weight method default values.'''
    assert hi.weight == 20
    assert bg.weight == 10


def test_init_flam():
    '''
    Test both Product and BoxingGlove flammability method returns a float.
    Test default
    '''
    assert type(hi.flammability) is float
    assert hi.flammability == 0.5
    assert type(bg.flammability) is float
    assert bg.flammability == 0.5


def test_steal_type():
    '''Test both Product and BoxingGlove staelability method returns string.'''
    assert type(hi.stealability()) is str
    assert type(bg.stealability()) is str


def test_splode_type():
    '''Test both Product and BoxingGlove explode method returns string.'''
    assert type(hi.explode()) is str
    assert type(bg.explode()) is str


def test_bg_splode():
    '''Tests BoxingGlove explode method overrides Product.explode.'''
    assert bg.explode() == "...it's a glove."


def test_bg_punch_type():
    '''Test BoxingGlove punch method returns a string.'''
    assert type(bg.punch()) is str


def test_prod_list():
    '''
    Tests acme_report.generate_report function retuns a list.
    By default the list should be 30 items long.
    '''
    assert type(acme_report.generate_products()) is list
    assert len(acme_report.generate_products()) == 30


def test_report_tuple():
    '''Tests that the acme_report.inventory_report function returns a tuple.'''
    one = acme_report.generate_products(1)
    assert type(acme_report.inventory_report(one)) is tuple


def test_generate_products_product_names():
    """
    Testing Part 4 - Class Report: The generate_products function
    generates valid product names

    Test Cases:
    generate_products()
    """
    products = acme_report.generate_products()
    for product in products:
        adjective, noun = product.name.split()
        assert adjective in acme_report.ADJECTIVES, '''first word in product
        name not in ADJECTIVES list'''


def test_generate_products_product_names_noun():
    products = acme_report.generate_products()
    for product in products:
        adjective, noun = product.name.split()
        assert noun in acme_report.NOUNS


def test_inventory_report(capfd):
    """
    Testing Part 4 - Class Report: The instantiation of the Product
    class has the correct constructor (__init__)

    Test Cases:
    generate_products()
    generate_products(randint(30, 100))
    """
    # testing generate_products(randint(30, 100))
    names_1 = set()
    total_price_1 = 0
    total_weight_1 = 0
    total_flammability_1 = 0.0
    test_int = random.randint(30, 100)
    print(test_int)
    test_products_1 = acme_report.generate_products(test_int)
    for product in test_products_1:
        names_1.add(product.name)
        total_price_1 += product.price
        total_weight_1 += product.weight
        total_flammability_1 += product.flammability

        report = acme_report.inventory_report(test_products_1)

    assert len(names_1) == report[0]
