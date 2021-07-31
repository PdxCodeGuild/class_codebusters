# Async / Await

Async/await is just syntax sugar built on top of promises, so they can be written in a cleaner style, avoiding the need to explicitly configure promise chains.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
  </head>

  <body>
    <script>
      const posts = [
        { id: 1, title: "blog 1" },
        { id: 2, title: "blog 2" },
      ];

      function getPosts() {
        setTimeout(function () {
          console.log("adding post");
          let result = "";
          posts.forEach(function (blog) {
            result += `<li>${blog.title}</li>`;
          });
          document.body.innerHTML = result;
        }, 1000);
      }

      function addPost(post) {
        return new Promise(function (resolve, reject) {
          setTimeout(function () {
            console.log("pushing post");
            posts.push(post);
            const error = false;
            if (!error) {
              resolve();
            } else {
              reject("did not get data");
            }
          }, 2000);
        });
      }

      async function getAll() {
        try { //the try catch block is equivalent to the .catch and is specific to async/await syntax
          await addPost({ id: 3, title: "blog 3" });
          getPosts();
        } catch (error) {
          console.log(error);
        }
      }

      getAll();
    </script>
  </body>
</html>
```

Let's try this out with fetch:

```Javascript

async function getTodos(){
  const response = await fetch ("https://jsonplaceholder.typicode.com/todos/1")
  const data = await response.json()
  console.log(data)
}
 getTodos()

```

Much cleaner!
