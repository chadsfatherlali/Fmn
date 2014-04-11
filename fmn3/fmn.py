import sublime, sublime_plugin
import smtplib
import pprint
import os
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class FmnCommand(sublime_plugin.EventListener):
     settings = sublime.load_settings("fmn.sublime-settings")


     def on_post_save(self, view):
          file = view.file_name()

          if file in self.settings.get("ficheros") and self.settings.get("notificarenguardado"):
               print ("\n\n ==> SE LANZA EL EMAIL <==")

               msg = MIMEMultipart()
               msg["Subject"] = self.settings.get("sujeto")
               msg["From"] = self.settings.get("usuario")
               msg["To"] = ", ".join(self.settings.get("destinatarios"))
               msg.attach(MIMEText(self.settings.get("usuario") + ": " + self.settings.get("msg") + "\nFichero: " + file, "plain"))

               server = smtplib.SMTP("smtp.gmail.com:587")  
               server.ehlo()
               server.starttls()
               server.ehlo()
               server.login(self.settings.get("usuario"), self.settings.get("password"))
               text = msg.as_string()
               server.sendmail(self.settings.get("usuario"), self.settings.get("destinatarios"), text)
               server.quit()
           