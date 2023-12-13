from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    Creates a list of products with length num_products.
    '''
    prod_list = []
    for x in range(num_products):
        rand_name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        rand_price = random.randint(5, 100)
        rand_w = random.randint(5, 100)
        rand_flam = round(random.uniform(0.0, 2.5), 1)
        prod_list.append(Product(rand_name, rand_price, rand_w, rand_flam))
    return prod_list


'''
def inventory_report(product_list):
    s = set(product_list)
    p = []
    w = []
    f = []
    leng = len(product_list)
    for i in range(len(product_list)):
        p.append(product_list[i].price)
        w.append(product_list[i].weight)
        f.append(product_list[i].flammability)
    return (len(s), sum(p) / leng, sum(w) / leng, sum(f) / leng)
'''

# if __name__ == "__main__":


def inventory_report(product_list):
    names_1 = set()
    total_price_1 = 0
    total_weight_1 = 0
    total_flammability_1 = 0.0
    for product in product_list:
        names_1.add(product.name)
        total_price_1 += product.price
        total_weight_1 += product.weight
        total_flammability_1 += product.flammability

        avg_price_1 = total_price_1 / len(product_list)
        avg_weight_1 = total_weight_1 / len(product_list)
        avg_flammability_1 = total_flammability_1 / len(product_list)
    return (len(names_1), avg_price_1, avg_weight_1, avg_flammability_1)
