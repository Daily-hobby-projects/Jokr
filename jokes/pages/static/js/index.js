const joke_form = document.querySelector('form');

const joke_container=document.querySelector('.posts');
const loading_spinner=document.querySelector('.loading');
const API_URL = '/api/'

joke_form.addEventListener('submit', (event) => {

    joke_form.style.display="none";
    loading_spinner.style.display="block"


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
    ).then((response)=>{return response.json()})
     .then((data)=>{
         console.log(data.joke)
         joke_form.style.display=""
            loading_spinner.style.display="none"

            
            let joke=`
                <div class="joke">
                    <h3>${data.joke.name}</h3>
                    <p>${data.joke.content}</p>
                    <a href="/delete/${data.joke.content}">Remove</a>
                </div>
            `;

            joke_container.innerHTML+=joke;


            let del_buttons=document.querySelectorAll('.del-btn');
    
            for (let i of del_buttons){
                i.addEventListener('click',()=>{
                    console.log("Hello");

                    console.log(i);
                })
            }
        })
    
    
    joke_form.reset();

   
    event.preventDefault();
})