inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].remove('dagger')
# del inventory['backpack'][1]
inventory['gold'] = [500, 50]
print(inventory)

