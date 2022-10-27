
lista=[]

if ( ! localStorage.getItem("articulos") ){
    lista=[]
} else{
    data = localStorage.getItem("articulos")
    lista=JSON.parse(data)
}

const boton = document.querySelector("#boton")
boton.addEventListener('click', ()=> alert('FASDFADSFSADF'))


nombre=document.getElementById('nombre').value
marca=document.getElementById('marca').value
modelo=document.getElementById('modelo').value
registro={'nombre': nombre,'marca': marca,'modelo': modelo}
lista.push(registro)
console.log(lista);

data=JSON.stringify(lista)
localStorage.setItem("articulos", data)

function reset(){
localStorage.setItem("articulos", "")
}