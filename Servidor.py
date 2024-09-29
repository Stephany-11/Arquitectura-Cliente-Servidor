import socket

# Crear el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind(('localhost', 2004))  # localhost en minúscula
mi_socket.listen(5)

print("Servidor escuchando en puerto 2004...")

while True:
    # Aceptar la conexión entrante
    conexion, addr = mi_socket.accept()
    print(f"¡Nueva conexión establecida con: {addr}")

    while True:
        # Recibir mensaje del cliente
        mensaje = conexion.recv(1024)
        if not mensaje:  # Si no hay mensaje, el cliente ha cerrado la conexión
            print("Conexión cerrada por el cliente.")
            conexion.close()  # Cerrar la conexión con el cliente
            break

        # Imprimir el mensaje del cliente
        print("Cliente: " + mensaje.decode())

        # Obtener la respuesta del servidor
        respuesta = input("Servidor: ")
        conexion.sendall(respuesta.encode())  # Enviar la respuesta al cliente

    # Opción para cerrar el servidor
    cerrar_servidor = input("¿Quieres cerrar el servidor? (si/no): ")
    if cerrar_servidor.lower() == 'si':
        mi_socket.close()
        print("Servidor cerrado.")
        break
