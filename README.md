# Arquitectura-Cliente-Servidor
este un modelo de arquitectura en sistemas de red que divide las tareas o cargas de trabajo entre dos entidades principales:

* **`Cliente:`** Es la parte que realiza solicitudes de servicios o recursos.
* **`Servidor:`** Es la parte que procesa esas solicitudes y proporciona los recursos o servicios solicitados.
### Objetivos
* **`Distribución de tareas:`** Separar las responsabilidades entre los clientes (el que solicitan) y el servidor (el que responde).
* **`Escalabilidad:`** Facilitar la escalabilidad del sistema, ya que se pueden añadir más clientes sin necesidad de modificar el servidor.
* **`Eficiencia en el uso de recursos:`** Optimizar el uso de recursos, ya que los servidores pueden estar diseñados para manejar grandes volúmenes de solicitudes.


### Guia para usar el codigo
1. En primer lugar se debe asegutar de tener el paquete de python.3 y socket instalado ya que este codigo fue desarrollado mediante estas herramientas.
2. Crea 2 documentos uno para el servidor y otro para el cliente, copiando el respectivo codigo proporcionado es tes repositorio.
 
    ```bash
    Servidor.py
     ```
     ```bash
     Cliente.py
      ```
3. Se debe guardar el codigo para su ejecucion, verificando la integridad del codigo.
   
   ### Pasos para ejecutar el codigo
   1. una vez que tengamos los dos codigo listo para ejecutar debemor ir primero al archivo del servidor y dejecutarlo, ya que el servidor debe estar en linea para         poder recibir la solicitud
   2. Se debe ejecutar el codigo del cliente donde se debera escribir lo siguite para activar la conexion
      
    ```bash
    Python cliente.py
     ```
     automaticamente se genera un mesaje donde se garantiza que la conexion con el servidor fue exitosamente establecida.
   3. una vez que este la conexion se podra generar la conversacion entre *cliente-servidor*
