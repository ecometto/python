$(document).ready(function () {
    $('#myTable').DataTable();
    
    // desaparecer salido 
    saludo = document.querySelector('#welcome')
    setTimeout(() =>
        saludo.classList.toggle('hide')
        // saludo.style.display = 'none'
        , 2000
    )

    console.log("llega");



});
