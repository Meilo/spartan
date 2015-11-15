$( ".add-produit" ).click(function() {
    alert( "Handler for .click() called." );
});

function allowDrop(ev) {
    ev.preventDefault();
    $("#"+ev.target.id).attr("style","background-color:#F60");
}

function LeaveCategory(ev) {
    ev.preventDefault();
    $("#"+ev.target.id).attr("style","background-color:none");
}

function drag(ev) {
    ev.dataTransfer.setData("text", $('#'+ev.target.id).text());
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    console.log(ev.target.id);
    console.log(data);
    console.log( $("#"+ev.target.id));
    $("#"+ev.target.id).prepend("<p>"+data+"<p>");
    $("#"+ev.target.id).attr("style","background-color:none");
}


///document.getElementById(data)