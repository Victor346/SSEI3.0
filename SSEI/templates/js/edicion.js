function editToggle(){
    let elements = document.getElementsByClassName('editInfo');
    for (let i = 0; i < elements.length; i++){
        if(elements[i].style.display === "none"){
            elements[i].style.display = "block";
        } else {
            elements[i].style.display = "none";
        }
    }
}
