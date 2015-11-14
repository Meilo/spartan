$( ".add-produit" ).click(function() {
    alert( "Handler for .click() called." );
});

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    //ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    console.log(ev.dataTransfer);
    ev.target.appendChild(document.getElementById(data));
}