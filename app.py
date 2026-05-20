import os
import time
import random
import threading
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

# Ocultar prompt de pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

class RegaloNutriaHamster:
    def __init__(self, root):
        self.root = root
        self.root.title("Archivo de Memoria: Nutria y Hamster")
        self.root.geometry("850x950")
        self.root.configure(bg="#0c0f12")
        self.root.resizable(False, False)

        self.archivo_musica = "cancion.mp3"
        self.archivo_imagen = "tulipan.png"

        pygame.mixer.init()
        self.particulas = []
        self.simbolos = ['❄', '♥', '✨', '💖', '🌹', '💞', '✧']
        
        self.canvas = tk.Canvas(self.root, bg="#0c0f12", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.construir_interfaz()
        self.animar_fondo()

    def construir_interfaz(self):
        # Campos de validación inicial
        self.lbl_titulo = tk.Label(self.root, text="SISTEMA DE SEGURIDAD NUTRIA", font=("Consolas", 14, "bold"), fg="#17b890", bg="#0c0f12")
        self.lbl_titulo.pack(pady=20)

        self.lbl_fecha = tk.Label(self.root, text="FECHA QUE INICIÓ TODO (DD/MM/AAAA):", font=("Consolas", 10), fg="#ffffff", bg="#0c0f12")
        self.lbl_fecha.pack()
        self.entry_fecha = tk.Entry(self.root, font=("Consolas", 12))
        self.entry_fecha.pack(pady=5)

        self.lbl_apodo = tk.Label(self.root, text="DIME MI APODO RECIENTE (CHELSITO O CHEFSITO):", font=("Consolas", 10), fg="#ffffff", bg="#0c0f12")
        self.lbl_apodo.pack(pady=(10, 0))
        self.entry_apodo = tk.Entry(self.root, font=("Consolas", 12))
        self.entry_apodo.pack(pady=5)

        self.btn_validar = tk.Button(self.root, text="DESBLOQUEAR", command=self.validar_acceso, bg="#ff4d6d", fg="white", font=("Consolas", 10, "bold"))
        self.btn_validar.pack(pady=20)

        self.txt_carta = tk.Text(self.root, font=("Segoe UI Emoji", 11, "bold"), fg="#ffffff", bg="#0c0f12", bd=0, width=85, height=18, wrap="word", state="disabled")
        self.txt_carta.pack_forget() # Oculto hasta desbloquear

    def validar_acceso(self):
        fecha = self.entry_fecha.get()
        apodo = self.entry_apodo.get().upper()
        
        if fecha == "27/04/2019" and (apodo == "CHELSITO" or apodo == "CHEFSITO"):
            # Ocultar campos de validación
            self.lbl_titulo.pack_forget()
            self.lbl_fecha.pack_forget()
            self.entry_fecha.pack_forget()
            self.lbl_apodo.pack_forget()
            self.entry_apodo.pack_forget()
            self.btn_validar.pack_forget()
            
            # Mostrar interfaz real
            self.txt_carta.pack(pady=5)
            self.txt_carta.config(state="normal")
            
            self.btn_inicio = tk.Button(self.root, text=" [ PULSE PARA INICIAR ] ", font=("Consolas", 11, "bold"), 
                                        fg="#0c0f12", bg="#ff4d6d", bd=0, padx=20, pady=8, cursor="hand2", 
                                        command=self.comenzar_experiencia)
            self.btn_inicio.pack(pady=5)
            self.lbl_frase = tk.Label(self.root, text="", font=("Segoe UI Emoji", 11, "bold"), fg="#17b890", bg="#0c0f12")
            self.lbl_frase.pack(pady=5)
            self.lbl_foto = tk.Label(self.root, bg="#0c0f12")
            self.lbl_foto.pack(pady=5)
        else:
            messagebox.showerror("Error", "Datos incorrectos. Intenta de nuevo.")

    # ... (El resto de tus métodos: animar_fondo, comenzar_experiencia y efecto_maquina siguen igual)
    
    def animar_fondo(self):
        if len(self.particulas) < 80:
            x = random.randint(10, 840)
            char = random.choice(self.simbolos)
            id_p = self.canvas.create_text(x, 0, text=char, font=("Segoe UI Emoji", 15), fill=random.choice(["#ff4d6d", "#ffffff", "#ade8f4"]))
            self.particulas.append({'id': id_p, 'x': x, 'y': 0, 'vel': random.uniform(2, 4)})
        for p in self.particulas[:]:
            p['y'] += p['vel']
            self.canvas.coords(p['id'], p['x'], p['y'])
            if p['y'] > 950:
                self.canvas.delete(p['id'])
                self.particulas.remove(p)
        self.root.after(40, self.animar_fondo)

    def comenzar_experiencia(self):
        self.btn_inicio.config(state="disabled", text="🎵 REPRODUCIENDO...")
        try:
            pygame.mixer.music.load(self.archivo_musica)
            pygame.mixer.music.play(-1)
        except: pass
        threading.Thread(target=self.efecto_maquina, daemon=True).start()

    def efecto_maquina(self):
        # (Tu bloque de 'parrafos' igual que siempre)
        parrafos = ["Siete años de enamorados 💞... (etc, pega aquí el resto de tu carta)", ...] 
        self.txt_carta.config(state="normal")
        for p in parrafos:
            for char in p:
                self.txt_carta.insert(tk.END, char)
                self.txt_carta.see(tk.END)
                time.sleep(0.09)
            time.sleep(2.0)
        self.txt_carta.config(state="disabled")
        self.lbl_frase.config(text="👉 Y PARA FINALIZAR UN OBSEQUIO...")
        try:
            img = Image.open(self.archivo_imagen).resize((340, 380), Image.Resampling.LANCZOS)
            self.tk_img = ImageTk.PhotoImage(img)
            self.lbl_foto.config(image=self.tk_img)
        except: pass

if __name__ == "__main__":
    root = tk.Tk()
    app = RegaloNutriaHamster(root)
    root.mainloop()
