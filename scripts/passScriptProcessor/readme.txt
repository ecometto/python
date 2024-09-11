

**** ATTENTION ****
in the current path, open a terminal and execute:

crea una carpeta para guardar los archivos separando por anio
>> mkdir 2024  

copia datos de origen
>> scp -r administrator@192.168.65.110:/kubernetes/products-manager/products-repo/PRODUCT/SB1/PassScript/2024/234/ ./2024

You should have the next directory tree:
--2024
------234
----------FileToProcess1.tar.gz
----------FileToProcess2.tar.gz
----------FileToProcess3.tar.gz
----------FileToProcess4.tar.gz
....................
----------FileToProcessN.tar.gz

corre el script que modifica el formato de fecha y evalua los tipos de pasadas y cantidad de TT
>> python passScriptProcesor.py 



//previous command:
>> scp -r administrator@192.168.65.110:/home/administrator/234/ ./2024