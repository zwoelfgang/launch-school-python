pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet'
}

print(pets.get('Dog'))
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))
