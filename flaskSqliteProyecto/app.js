
lista=[]

if ( ! localStorage.getItem("articulos") ){
    lista=[]
    console.log(lista);
} else{
    data = localStorage.getItem("articulos")
    lista=JSON.parse(data)
    console.log(lista);
}

const boton = document.querySelector("#boton")
boton.addEventListener('click', ()=> nuevo())

const btnReset= document.querySelector("#reset")
btnReset.addEventListener('click', ()=> reset())

function nuevo(){
    nombre=document.getElementById('nombre').value
    marca=document.getElementById('marca').value
    modelo=document.getElementById('modelo').value
    registro={'nombre': nombre,'marca': marca,'modelo': modelo}
    lista.push(registro)
    console.log(lista);
    
    data=JSON.stringify(lista)
    localStorage.setItem("articulos", data)
}

function reset(){
    console.log("borrando...")
    localStorage.clear();
}