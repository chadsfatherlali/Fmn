Fmn
===

fmn => Sublime Text 2\n
fmn3 => Sublime Text 3

File mail notifier: Notificador por email para cuentas (@gmail) de cambios en archivos.

Configuración:
---------------

Preferences => Package Settings => File mailing notification => Settings default

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
