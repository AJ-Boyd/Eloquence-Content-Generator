//special form submssion code
document.addEventListener('DOMContentLoaded', function(){
    const form = document.getElementById('gen-form');
    const content_container = document.getElementById("content-container");
    const content = document.getElementById("content")

    form.addEventListener('submit', function(event){
        event.preventDefault(); 
        document.getElementById('loading-spinner').style.display = 'block'; //start loading animation
        content.innerHTML = ""; //clear content
        content_container.style.display = "none";

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
            content_container.style.display = "block";
            console.log(msg)
            typeWriter(0, msg)
        })
        .catch(error => {
            //if error
            document.getElementById('loading-spinner').style.display = 'none';
            content_container.style.display = "block";
            alert('An error occurred: ' + error.message); //display error message
            msg = "Error: " + error.message;
            typeWriter(0, msg);
        });
    });
});

const SPEED = 25;
//modified typewriter text effect via W3 schools
function typeWriter(i, text){
    if (i < text.length) {
      content.innerHTML += text.charAt(i);
      setTimeout(function(){
        typeWriter(++i, text) 
      }, SPEED);
    }
}

function copyContent(){
    copyBtn = document.getElementById("copyContent")
    const textToCopy = document.getElementById('content').textContent;
    navigator.clipboard.writeText(textToCopy).then(function() {
        copyBtn.innerHTML = "Copied!"
        icon = document.createElement("i");
        icon.classList = "fa-solid fa-copy";
        setTimeout(function(){
           changeElemText(copyBtn, 'Copy <i class="fa-solid fa-copy"></i>')
        }, 3000)
    }, function(err) {
        alert('Failed to copy text: ', err);
    });
}

function exportContent(){
    const exportText = document.getElementById('content').textContent;
    const blob = new Blob([exportText], { type: 'text/plain' });
    const anchor = document.createElement('a');
    anchor.href = URL.createObjectURL(blob);
    anchor.download = 'eloquentAI_generation.txt';
    anchor.click();
    URL.revokeObjectURL(anchor.href);
}

function changeElemText(elem, text){
    elem.innerHTML = text;
}