"use strict"


let formData = {
    flavor : $("#flavor").val(),
    size : $("#size").val(),
    rating : $("#rating").val(),
    image : $("#image").val()
};

console.log(formData);


function handleForm(evt){

    console.log("are we even getting here");

    evt.preventDefault();    

    let formData = {
        flavor : $("#flavor").val(),
        size : $("#size").val(),
        rating : $("#rating").val(),
        image : $("#image").val()
    };

    console.log("THis is our form data: ",formData);

    axios.post("/api/cupcakes", formData);
}



$("#addButton").on("click", handleForm);