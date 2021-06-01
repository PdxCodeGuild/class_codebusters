# Lab 1: Bio

Write up a short bio webpage for someone or something. It can be about a celebrity, a fictionary character, a place, a species, etc. Check out the [examples](https://github.com/PdxCodeGuild/class_bumble_bee/tree/main/2%20HTML%20%2B%20CSS/labs/images)

## Part 1

- A written introduction
  - Use a header element (`h1`, `h2`, `h3`... etc) to introduce your topic.
  - Use a paragraph element `p` for the body of your introduction
- A link to a Wikipedia article
  - Use an anchor element `a`. Don't forget the `href` attribute.
- A picture of them
  - Use an image element `img`.
  - Image elements need a `src` attribute for the images source.
  - You may also use `height` and `width` attributes to set the size.
  - Don't forget the `alt` attribute! We need to stay accessible.
- A list of places where they've lived
  - Dealer's choice, you could use an unordered list `ul` or an ordered list `ol`. Don't forget about those list items `li`.
- A quote from them
  - This would be a great time to use either a quote `q` element or a blockquote `blockquote` element.

## Part 2 - Adding CSS

At this point you could either write your styles within a `style` element, or link to an external css file.

Style tag:

```html
<style>
  body {
    background-color: gray;
  }
</style>
```

External style sheet:

```html
<link rel="stylesheet" href="./style.css" />
```

- Center the entire content of the body
- Modify the padding and margins on your paragraphs to look better.
  - Here are docs on [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) and [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)
- Use a custom font. [google fonts](https://fonts.google.com/) is a great place to find fonts.
- Add a background image
  - Take a look at the [background-image](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image) property.

## Part 3

- Pick a color scheme and modify the background, body text, and link text color.
  - I personally like to use [coolors.co](https://coolors.co/8895b3-8e94f2-9fa0ff-bbadff-dab6fc) when trying to come up with a color scheme.
- Change the typeface of the quote.
- Add a rounded border to the picture.
  - Take a look at the [border-radius](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius) property
- Change the bullet points on the list of places.
  - Take a look at the [list-style-type](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type) property.
