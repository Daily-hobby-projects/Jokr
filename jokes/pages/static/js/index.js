const joke_form = document.querySelector('form');
const API_URL = '/api/'

joke_form.addEventListener('submit', (event) => {

    let joke = new FormData(joke_form);

    let jokeObj = {
        name: joke.get('name'),
        content: joke.get('content')
    }

    fetch(API_URL, {
        method: 'POST',
        body: JSON.stringify(jokeObj),
        headers: {
            'content-type': 'application/json'
        }
    }
    ).then((response)=>{response.json()})
     .then((response)=>{console.log(response)})

    joke_form.reset();
    event.preventDefault();
})