def saludo():
    print("¡Hola! Bienvenido a mi programa de inicio de sesión.")

def login():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    # Aquí puedes agregar la lógica para verificar el nombre de usuario y la contraseña
    if username == "admin" and password == "1234":
        print("¡Inicio de sesión exitoso!")
    else:
        print("Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.")