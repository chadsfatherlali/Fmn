Fmn
===

File mail notifier: Notificador por email para cuentas (@gmail) de cambios en archivos.

Configuración:
---------------

"notificarenguardado" => (bool) => desactiva o activa el envío del correo.

```html
{
  "notificarenguardado": true,
  "usuario": "email@gmail.com",
  "password": "password",
  "destinatarios": [
    "usuario1@mail.com",
    "usuario2@email.com",
    "usuario3@correo.com"
  ],
  "msg": "ha modificado 'commons.js' UPDATE !!!!",
  "sujeto": "Cambio en el common.js",
  "ficheros": [
    "/camino/al/fichero/common.js"
  ]
}
```
