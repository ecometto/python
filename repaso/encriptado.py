from werkzeug.security import generate_password_hash, check_password_hash

texto="user"

textoEncriptado=generate_password_hash(texto)
print(textoEncriptado)

# --------------------- 

checkeando=check_password_hash(textoEncriptado, texto)
print(checkeando)