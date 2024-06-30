var toggle = false;

function toggleOptions(){
    const options = document.getElementById("gen-options")

    toggle = toggle ? false : true 
    console.log("toggle:", toggle)
    if(toggle){
        options.style.display = "block";
    }else{
        options.styled.display = "none";
    }
}