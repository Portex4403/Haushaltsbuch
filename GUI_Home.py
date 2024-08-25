import tkinter as tk
from tkinter import ttk
import json

def laden():
    try:
        with open('daten.json', 'r') as f:
            geladene_daten = json.load(f)
            aktuelles_geld.set(geladene_daten["aktuelles_geld"])
    except FileNotFoundError:
        print("Die Datei 'daten.json' wurde nicht gefunden.")

def Speichern():
    daten = {"aktuelles_geld": aktuelles_geld.get()}
    with open ('daten.json', 'w') as f:
        json.dump(daten, f)


def nur_zahlen(char):
    return char.isdigit() or char == ""

def geldhinzufügen():
    aktueller_wert = int(aktuelles_geld.get())
    hinzufügen_wert = int(eingabe1.get())
    aktueller_wert += hinzufügen_wert
    aktuelles_geld.set(str(aktueller_wert))
    eingabe1.delete(0, 'end')
    Speichern()

def geldabziehen():
    aktueller_wert = int(aktuelles_geld.get())
    hinzufügen_wert = int(eingabe1.get())
    aktueller_wert -= hinzufügen_wert
    aktuelles_geld.set(str(aktueller_wert))
    eingabe1.delete(0, 'end')
    Speichern()

root = tk.Tk()
root.geometry("400x400")


aktuelles_geld = tk.StringVar()
aktuelles_geld.set('0')

laden()

validierung = root.register(nur_zahlen)

Programm_name =ttk.Label(root, text= 'Haushaltsbuch', font=('arial',25))
Programm_name.pack()

void1 =ttk.Label(root)
void1.pack()

Geld_anzeigen =ttk.Label(root,textvariable = aktuelles_geld, font= ('arial',25))
Geld_anzeigen.pack()

eingabe1 =ttk.Entry(root, validate="key", validatecommand=(validierung, '%P'))
eingabe1.pack(fill='y')

rahmen1 = ttk.Frame(root)
rahmen1.pack()

rahmen2 =ttk.Frame(rahmen1)
rahmen2.pack(side='right')

rahmen3 =ttk.Frame(rahmen1)
rahmen3.pack(side='left')

button1 = ttk.Button(rahmen3,command= geldhinzufügen , text= '\n+\n')
button1.pack( side = 'left', fill='both')

button2 =ttk.Button(rahmen3,command=geldabziehen , text= '\n-\n')
button2.pack( side = 'right', fill= 'both')

sitenavigation = ttk.Frame(root)
sitenavigation.pack(side='bottom', fill='x')

sitenavigationbttn1 =tk.Button(sitenavigation, text='Verlauf', height= 5)
sitenavigationbttn1.pack(fill='both', expand=True, side= 'left')

sitenavigationbttn2 =tk.Button(sitenavigation, text='Home', height= 5)
sitenavigationbttn2.pack(fill='both', expand=True, side= 'left')

sitenavgitaionbttn3 =tk.Button(sitenavigation, text='Fix Kosten', height= 5)
sitenavgitaionbttn3.pack(fill='both', expand=True, side= 'left')

root.mainloop()