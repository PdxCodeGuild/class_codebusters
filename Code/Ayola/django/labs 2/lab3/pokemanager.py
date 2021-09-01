import json, os
from . import models

models.Pokemon.objects.all().delete()
models.PokemonType.objects.all().delete()


path = os.path.dirname(__file__)
file = open(os.path.join(path,"pokemon.json"))
data = json.load(file)
data = data['pokemon']
i = 0
types = []
for each in data:
    type_list = each['types']
    for poke_type in type_list:
        if poke_type not in types:
            types.append(poke_type)
for each in types:
    instance = models.PokemonType.objects.create(name=each)
    instance.save()

for each in data:
    number = each['number']
    name = each['name']
    height = each['height']
    weight = each['weight']
    img_front = each['image_front']
    img_back = each['image_back']
    types_pok = each['types']
    pokemon  = models.Pokemon.objects.create(number=number,name=name,height=height,weight=weight,image_front=img_front,image_back=img_back)
    pokemon.save()
    for t in types_pok:
        single_type = models.PokemonType.objects.get(name=t)
        pokemon.types.add(single_type) 
print("Database Successfully populated")




