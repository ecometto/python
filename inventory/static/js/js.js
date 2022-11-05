
botonesArticulos = document.querySelectorAll("button")
botonesArticulos.forEach(element => {
    element.addEventListener('click', (e) => {
        window.location.href = "/" + (element.id)
    })

})


