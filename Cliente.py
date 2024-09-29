import socket

# Crear el socket del cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor en 'localhost' y puerto 2004
cliente_socket.connect(('localhost', 2004))
print("Conectado al servidor.")

while True:
    # Enviar mensaje al servidor
    mensaje = input("Cliente: ")
    
    if mensaje.lower() == "salir":  # Si el cliente escribe "salir", cerrar la conexión
        cliente_socket.sendall(b'')  # Enviar un mensaje vacío para notificar al servidor
        print("Cerrando conexión...")
        break

    # Enviar mensaje al servidor
    cliente_socket.sendall(mensaje.encode())

    # Recibir respuesta del servidor
    respuesta = cliente_socket.recv(1024)
    if not respuesta:  # Si no hay respuesta, el servidor ha cerrado la conexión
        print("Conexión cerrada por el servidor.")
        break
    print("Servidor: " + respuesta.decode())

# Cerrar la conexión con el servidor
cliente_socket.close()
print("Conexión cerrada.")
