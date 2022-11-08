
msgDiv=document.querySelector('.MSG')
close=document.getElementById('close')
close.addEventListener('mouseover', ()=> msgDiv.style.cursor='pointer')
close.addEventListener('click', ()=> msgDiv.style.display='none')