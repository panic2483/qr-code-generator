import qrcode
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys

quit_variable = False 

# Funktionen
def quit():
    global quit_variable 
    quit_variable = True
    root.destroy()
    sys.exit()

def check_input(event = None): #event = None -> Ohne Fehler wegen .bind() in der for schleife, so klappt (hab nich ganz gecheckt)
    if link_input.get().strip() and speicherpfad_input.get().strip() and name_input.get().strip(): #.strip() bereinigt Leerzeichen, sonst auch ein Leertasten Input != leer, wenn überall was eingegeben -> Download Button freischalten
        download_button["state"] = tk.NORMAL
    else:
        download_button["state"] = tk.DISABLED

def save_qr_code(): #Erstellt + Speichert den QR-Code
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    qr.add_data(link_input.get())
    qr.make()
    qr_code_image = qr.make_image(fill_color = "black", back_color = "white")
    speicherordner = os.path.join(speicherpfad_input.get(), name_input.get() + ".png")
    qr_code_image.save(speicherordner)

#While Schleife = True, damit Programm durchgehend läuft, bis geschlossen wird
while True:

    root = tk.Tk() # Window erstellen
    root.title("QR-Code Generator")
    root.geometry("600x600")

    style = ttk.Style(root) # Style Theme
    style.theme_use("alt")

    image = Image.open(r"C:\Users\Patrick\Pictures\Screenshot 2025-05-21 181015.png") # QR-Code Foto (auf der Startseite)
    photo = ImageTk.PhotoImage(image)

    label1 = ttk.Label(root, text = "QR-Code Generator", font=("Arial", 20, "bold"), background="white", anchor="center") #"Überschrift"
    label1.pack(fill="x")
    label2 = ttk.Label(root, image=photo,background="white", anchor="center", padding=5) #QR-Code Image
    label2.pack(fill="x")
    label3 = ttk.Label(root, text="Link:", background="white", anchor="center", font=("Arial", 16), padding=10) #Schrift "Link:"
    label3.pack(fill="x")

    link_input = ttk.Entry(root, justify="center", font="Arial", foreground="blue", background="white", width=40) #Eingabefeld für Link
    link_input.pack(fill="x")

    label4= ttk.Label(root, text="Speicherpfad:", background="white", anchor="center", font=("Arial", 16), padding = 10) #Schrift "Speicherpfad:"
    label4.pack(fill="x")

    speicherpfad_input = ttk.Entry(root, justify="center", font="Arial", background="white", width=40) #Eingabefeld Speicherpfad
    speicherpfad_input.pack(fill="x")

    label5 = ttk.Label(root, text="Dateiname:", background="white", anchor="center", font=("Arial", 16), padding = 10) #Schrift "Dateiname:"
    label5.pack(fill="x")

    name_input = ttk.Entry(root, justify="center", font="Arial", background="white", width=40) #Eingabe für Datei-Name
    name_input.pack(fill="x")

    download_button = ttk.Button(root, state=tk.DISABLED, text="Download QR-Code", command=save_qr_code) #Download Button
    download_button.pack()
    quit_button = ttk.Button(root, text = "Programm beenden.", command= quit) #Quit Button
    quit_button.pack(side="bottom")

    root.protocol("WM_DELETE_WINDOW", quit) # Schließt das Programm auch richtig, wenn man das Fenster über Schließen, oben rechts in der Ecke schließt -> vorher While schleife wurde weiterhin ausgeführt, deshalb direkt neu gestartet

    for widget in [link_input, name_input, speicherpfad_input]: # führt die check_input Funktion immer aus, wenn in einem der drei Eingabe Felder eine Taste gedrückt wird
        widget.bind("<KeyRelease>", check_input)

    if  quit_variable == True:
        break
    
    root.mainloop()