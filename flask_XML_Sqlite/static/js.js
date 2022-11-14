$(document).ready(function () {
    $('#myTable').DataTable();

    // desaparecer saludo 
    saludo = document.querySelector('#welcome')
    setTimeout(() => {
        saludo.classList.toggle('hide')
        setTimeout(() => saludo.style.display = 'none', 200)
    }
        , 2000
    )


});
