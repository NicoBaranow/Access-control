# Safety Stock access control

Safety Stock access control es un control de acceso asociado a [Safety stock web app](https://github.com/NicoBaranow/SafetyStockWebApp) para aumentar la seguridad de depósitos y facilitar el acceso.

## Agregar nuevos usuarios
Para agregar nuevos usuarios, primero conectar el ESP32 a la PC y abrirlo con cualquier IDE. Una vez hecho esto, escanear la tarjeta a agregar. Esto mostrará en el monitor serial su UID. Una vez tengamos ese UID, debemos copiarlo, presionar CTRL+C en el monitor serial para detener la ejecución del programa y pegar el UID en el array de **Profesores** de la linea 21 del archivo boot.py, seguido de una "," en caso de tener otro seguido a este. Debería quedar de la siguiente manera: **profesores = ["4:4e:23:82:86:62:80","51:75:24:d9", "b6:71:61:5e"]**

## Correr el programa
Para correr el programa nuevamente, alcanza con presionar **F5**.   
En caso de detectarse algún error en la lectura, el programa se reiniciará automaticamente.  
En caso de perder el suministro eléctrico, el programa comenzará a correr automaticamente cuando este se restablezca.
