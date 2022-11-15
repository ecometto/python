from werkzeug.security import generate_password_hash, check_password_hash

users = [
    {'id': '1', 'nombre': 'ecometto', 'pass': 'pbkdf2:sha256:260000$nb3FK6KtRjkIRC1h$831788796348ce414df57c1e1554083fe95474907914811de3cb0889a10e6d8d', 'mail': 'ecometto@ecometto.com.ar', 'type': 'admin'},
    {'id': '2', 'nombre': 'admin', 'pass': 'pbkdf2:sha256:260000$uveMY4yd3OXETf2a$47b4d7b9b6c13db814f9a3a25a1d242c1e310d14a03b89a1572f363d22819ed0', 'mail': 'admin@admin.com.ar', 'type': 'admin'},
    {'id': '3', 'nombre': 'user', 'pass': 'pbkdf2:sha256:260000$FxBPkF8K7gKcTd47$67d19ec852768276d19ddff20c7e8e34a8dd3a5d55ba70fa5e586a7b82bc34c6', 'mail': 'user@user.com.ar', 'type': 'user'},       
    {'id': '4', 'nombre': 'otro', 'pass': 'pbkdf2:sha256:260000$ZldqwEWm4EatANNy$ef1754bf87e2186257df6923834cd354e2e929b498eae31352c21b47d76d35aa', 'mail': 'otro@gmail.com', 'type': 'user'}
    ]


def validar(nombre, passw):
    for user in users:
        if nombre == user['nombre'] and check_password_hash(user['pass'], passw):
            return 1
    return 0

