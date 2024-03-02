# bierce = {
#     'day': 'A period of twenty-four hours, mostly misspent',
#     'positive': "Mistaken at the top of one's voice",
#     'misfortune': 'The kind of fortune that never misses'
#     }
# print(bierce.values())

# acme_custome = dict(first='Wile', niddle='E', last="Coyote")
# print(acme_custome.keys())

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

other = {'Mark': 'Groucho', 'Howard': 'Moe'}
pythons.update(other)
print(pythons)

# del pythons['Mark']
# del pythons['Howard']
pythons.pop('Howard')
print(pythons)

# print(pythons)
#
# pythons['Gilliam'] = 'Terry'
# print(f'Новый список группы: {pythons}')
#
# print('Groucho' in pythons)
#
# print(pythons.values())
# print(pythons.items())