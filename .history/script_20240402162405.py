import json
from usuario import Usuario

usuarios = []

with open('usuarios.txt', 'r') as file:
    lineas = file.readlines()

with open('error.log', 'w') as log_file:
    for linea in lineas:
        try:
            datos = json.loads(linea)
            usuario = Usuario(datos['nombre'], datos['apellido'], datos['email'], datos['genero'])
            usuarios.append(usuario)
        except Exception as e:
            log_file.write(f"Error al procesar la línea: {linea}\n")
            log_file.write(str(e) + "\n")

print("Usuarios creados:")
for usuario in usuarios:
    print(f"Nombre: {usuario.nombre}, Apellido: {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")

# se adjunta archivo "COMENTARIOS.TXT" por el detalle
    # ademas arreglé los errores (excepciones" y corri de nuevo, por lo que el "ERROR.LOG" no tienen datos)
    # No asi el "ERROR-1.LOG" que es el primer resultado