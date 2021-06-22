

# Lab 4: Pokedex

Let's build a searchable pokedex! First we'll load the data from a `json` file into our own database. Then we'll list those pokemon in the page and add search and pagination.

## Part 1

Create an app `pokedex` and add two models to store our pokemon, `Pokemon` and `PokemonType`.

`PokemonType` should have the following fields:
- `name` (CharField)

`Pokemon` should have the following fields:
- `number` (IntegerField)
- `name` (CharField)
- `height` (FloatField)
- `weight` (FloatField)
- `image_front` (CharField)
- `image_back` (CharField)
- `types` (ManyToManyField with `PokemonType`)

## Part 2

Write a [custom management command](../docs/01%20-%20Django%20Overview.md#custom-management-commands) `load_pokemon.py` to load the data from [pokemon.json](./pokemon.json) into your database. You can do this by saving the file next to your `.py` file and using [opening the file](../../1%20Python/docs/../../1%20Python/docs/11%20-%20FileIO.md). To handle the types, check out [many to many fields](../docs/05%20-%20Models.md#many-to-many). In the first line of your management command, you may want to delete all the records in the table so each time you run it you start with a clean slate. To verify that the data was loaded, open your admin panel and check that the pokemon are there.

## Part 3

Write a `view`, `route` and `template` to show a list of pokemon on the front page. You can either show all the information as a table, or show only their name and icon and link to a detail page with all their information. Use `<img src="...">` to display their front and back image.


## Part 4 (optional)

Check out the [script](./pokedex.py) that creates the json file, you can use it to load even more pokemon into your database!

