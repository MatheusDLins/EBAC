$(document).ready(function(){
    $('header button').click(function(){
        alert("Expandir")
    })

    $('form').on('submit',function(e){
        e.preventDefault();
    })
})
