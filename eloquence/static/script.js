//special form submssion code
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('gen-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 
        document.querySelector('.loading-spinner').style.display = 'block'; //start loading animation

        // get form data
        const formData = new FormData(form);

        // make post request to generate route
        fetch('/generate', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            //get response
            document.getElementById('loading-spinner').style.display = 'none'; //finish loading animation
            console.log("STATUS:", data.status)
            
            //display generated content
            msg = data.content;
            content_box = document.getElementById("content");
            content_box.style.display = "block";
            typeWriter(0, msg)
        })
        .catch(error => {
            //if error
            document.getElementById('loading-spinner').style.display = 'none';
            alert('An error occurred: ' + error.message); //display error message
            msg = "Error: " + error.message;
            typeWriter(0, msg);
        });
    });
});

const SPEED = 25;
//modified typewriter text effect via W3 schools
function typeWriter(i, text) {
    if (i < text.length) {
      document.getElementById("content").innerHTML += text.charAt(i);
      setTimeout(function() {
        typeWriter(++i, text) 
      }, SPEED);
    }
  }