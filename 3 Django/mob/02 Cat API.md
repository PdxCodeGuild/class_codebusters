

# Cat API

[The Cat API](https://docs.thecatapi.com/) provides information about cats, including images and a lis of breeds. We can build an interface for users to browse this info.

## Version 1

Create a page with a "random cat" button that, when pressed, goes and gets a random cat image and displays it. Copy and paste the url below into your browser and look at the response. You can take the `url` and set it as the `src` attribute of an `img` to display it. [hint](https://docs.thecatapi.com/api-reference/images/images-search)

`https://api.thecatapi.com/v1/images/search`
(Hint: You may need to use the requests library)

## Version 2

There is another part of the cat api which will give a list of categories. Use the response from this api endpoint to build a dropdown list of categories. [hint](https://docs.thecatapi.com/api-reference/categories/categories-list)

`https://api.thecatapi.com/v1/categories`

Now when the user presses the button to get a random cat image, use the selected category to filter the results.

`https://api.thecatapi.com/v1/images/search?category_ids=1`


## Version 3

Now let's add a like feature. Create a model to keep track of all the liked cat images. Add a like button next to your images, that when pressed will save that image url to your database. Create a page for viewing all liked images.
