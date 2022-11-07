// console.log('llegando');

saludo=document.querySelector('.welcome')
boton = document.getElementById('boton')
function desaparecer(){
    setTimeout(()=>
    saludo.style.display='none'
    , 2000
    )
}

// desaparecer()

boton.addEventListener('click', ()=>
    saludo.classList.toggle('hide')
)
