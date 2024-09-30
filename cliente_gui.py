import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox


# Función para recibir mensajes del servidor
def recibir_mensajes():
    while True:
        try:
            # Recibir mensaje del servidor (hasta 1024 bytes)
            mensaje = cliente_socket.recv(1024).decode()

            if not mensaje:
                # Si no hay mensaje, el servidor cerró la conexión
                chat_box.config(state=tk.NORMAL)
                chat_box.insert(tk.END, "Conexión cerrada por el servidor.\n")
                chat_box.config(state=tk.DISABLED)
                cliente_socket.close()
                break

            # Mostrar el mensaje del servidor en la ventana
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, "Servidor: " + mensaje + '\n')
            chat_box.config(state=tk.DISABLED)
            chat_box.yview(tk.END)

        except ConnectionAbortedError:
            # Si la conexión se cierra, cerramos el socket y salimos del bucle
            print("Conexión cerrada.")
            cliente_socket.close()
            break
        except:
            print("Error al recibir mensajes.")
            cliente_socket.close()
            break


# Función para enviar mensajes al servidor
def enviar_mensaje():
    mensaje = mensaje_entry.get()
    if mensaje:  # Enviar solo si hay un mensaje
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Cliente: " + mensaje + '\n')
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)
        cliente_socket.sendall(mensaje.encode())  # Enviar mensaje al servidor
        mensaje_entry.delete(0, tk.END)

    if mensaje.lower() == "salir":
        cliente_socket.sendall(b'')  # Enviar un mensaje vacío para notificar al servidor
        cliente_socket.close()
        ventana.quit()


# Crear la ventana principal de la interfaz
ventana = tk.Tk()
ventana.title("Cliente de Chat")
ventana.geometry("400x400")

# Cuadro de texto para mostrar el chat
chat_box = scrolledtext.ScrolledText(ventana, state=tk.DISABLED, wrap=tk.WORD)
chat_box.pack(pady=10)

# Entrada para escribir mensajes
mensaje_entry = tk.Entry(ventana, width=50)
mensaje_entry.pack(pady=5)

# Botón para enviar mensajes
enviar_boton = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
enviar_boton.pack(pady=5)

# Crear el socket del cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(('localhost', 2004))  # Conectar al servidor

# Crear un hilo para recibir mensajes del servidor
recibir_hilo = threading.Thread(target=recibir_mensajes)
recibir_hilo.daemon = True  # Hilo en segundo plano
recibir_hilo.start()

# Ejecutar la interfaz gráfica
ventana.mainloop()
