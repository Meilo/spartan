$( ".add-produit" ).click(function() {
    alert( "Handler for .click() called." );
});

function allowDrop(ev) {
    ev.preventDefault();
    $("#"+ev.target.id).attr("style","background-color:#F60;height:35px; width:100%;");
    $("#"+ev.target.id+"testSpan").attr("style","display:visible; width:100%;text-align:center;padding:6%;");

}

function LeaveCategory(ev) {
    ev.preventDefault();
    $("#"+ev.target.id).attr("style","background-color:none;height:35px; width:100%;");
}

function drag(ev) {
    console.log($('#'+ev.target.id).children().text());
    ev.dataTransfer.setData("text", $('#'+ev.target.id).children().text());
    $( ".DropZoneHide" ).addClass( "DropZone" );
    $( ".DropZoneHide" ).removeClass( "DropZoneHide")
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    console.log("#"+ev.target.id+"Drop");
    $("#"+ev.target.id+"Drop").prepend("<div class=\"produit\"><p>"+data+"<p></div>");
    $( ".DropZone" ).addClass( "DropZoneHide" );
    $( ".DropZone" ).removeClass( "DropZone")
}


///document.getElementById(data)