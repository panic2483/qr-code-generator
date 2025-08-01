import qrcode # QR-Code libary (download mit "pip install qrcode pillow" im terminal)
import os
import tkinter as tk

while True: #Führt das Programm solange aus, bis es Verlassen wird
    website_link = str(input("Link: ")) #Benutzer kann Link selber eingeben, wird in einer Variable gespeichert
    datei_name = str(input("Name der PNG-Datei: ")) # Speichert den gewünschten Dateinamen in einer Variable

    speicherordner = input("In welchen Ordner soll der QR-Code gespeichert werden? Gib bitte den Speicherpfad ohne Anführungszeichen an: ") # Ordner, in der der QR-Code gespeichert werden soll
    if not os.path.isdir(speicherordner): # Checkt ob der eingegebene Ordner auch existiert
        print("Der angegebene Ordner existiert nicht. Programm beendet.")
        exit()

    speicherpfad = os.path.join(speicherordner, datei_name + ".png") # Erstellt den neuen Sepciherpfad, zusammengesetzt aus: speicherordner, dateiname und der Endung .png

# Speichert den QR-Code, der erstellt werden soll in einer Variable
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5) # version: Größe des Codes (1-40), box_size = Pixel-Größe der einzelnen "Boxen", border = Größe des Randes
    qr.add_data(website_link) # Verbindet Link mit QR-Code
    qr.make() # Erstellt den QR-Code
    qr_code_image = qr.make_image(fill_color = "black", back_color = "white") # fill_color = Farbe der "Boxen" back_color = Hintergrundfarbe

# Lässt das Programm nicht abstürzen bei einem Fehler, beim speichern
    try:
        qr_code_image.save(speicherpfad) # Speichert den QR-Code, mit eingegebenen Namen als PNG-Datei
        print(f"QR-Code erfolgreich im Pfad {speicherpfad} gespeichert!")

    except Exception as e: #Speichert den aufgetretenen Fehler in der Variable e und kann ihn nun ausgeben, ohne dass das Programm abstürzt
        print("Fehler beim Speichern: ", e)

# Funktion zum Wiederholen oder Verlassen des Programms
    wiederholen = input("Möchtest du einen weiteren QR-Code erstellen? (Ja/Nein): ")
    if wiederholen != "Ja":
        print("Programm beendet.")
        break