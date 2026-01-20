import tkinter as tk
from tkinter import messagebox
import random
FRASES = [
    "Un chocolate 🍫","Un abrazo 🤗","Un deseo cumplido ✨",
    "Un momento feliz 😊","Un regalo sorpresa 🎁",
    "Magia navideña ⭐","Hoy todo saldrá bien 💫"
]

COLORES_LUCES = ["red","gold","lime","cyan","magenta","orange","pink","blue","purple","white"]
ADORNOS = ["⭐","❄️","🎀","🔔","🎁","🎄","🧸","🍭","🕯️","🌟"]

class CalendarioNavideno:
    def __init__(self, master):
        self.master = master
        self.master.title("🎄 Calendario de Adviento 🎄")
        self.master.configure(bg="#081b2f")

        self.w, self.h = 900, 650
        self.canvas = tk.Canvas(
            master, width=self.w, height=self.h,
            bg="#081b2f", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        # ===== TÍTULO CON LUCES =====
        self.titulo = self.canvas.create_text(
            self.w//2, 45,
            text="🎄 Calendario de Adviento 🎄",
            font=("Arial", 28, "bold"),
            fill="gold"
        )

        self.crear_esquinas()
        self.crear_dibujos_extra()

        self.copos = self.crear_nieve()
        self.estrellas = self.crear_estrellas()

        self.marco = tk.Frame(self.canvas, bg="#145a32", padx=14, pady=14)
        self.canvas.create_window(self.w//2, self.h//2 + 30, window=self.marco)

        self.botones = {}
        self.crear_calendario()

        self.animar()
        self.animar_titulo()

    # -------- TÍTULO ANIMADO --------
    def animar_titulo(self):
        self.canvas.itemconfig(
            self.titulo,
            fill=random.choice(COLORES_LUCES)
        )
        self.master.after(250, self.animar_titulo)

    # -------- ESQUINAS --------
    def crear_esquinas(self):
        esquinas = [(40,40),(self.w-40,40),(40,self.h-40),(self.w-40,self.h-40)]
        for x,y in esquinas:
            self.canvas.create_text(
                x, y,
                text=random.choice(ADORNOS),
                font=("Arial",30),
                fill=random.choice(COLORES_LUCES)
            )

    # -------- DIBUJOS EXTRA --------
    def crear_dibujos_extra(self):
        for _ in range(120):
            x = random.randint(0,self.w)
            y = random.randint(80,self.h)
            self.canvas.create_text(
                x, y,
                text=random.choice(ADORNOS),
                font=("Arial", random.randint(10,20)),
                fill=random.choice(COLORES_LUCES)
            )

    # -------- CALENDARIO --------
    def crear_calendario(self):
        dia = 1
        for i in range(5):
            for j in range(5):
                boton = tk.Button(
                    self.marco,
                    text=f"🎁\n{dia}",
                    width=7,
                    height=3,
                    font=("Arial",10,"bold"),
                    bg=random.choice(COLORES_LUCES),
                    fg="white",
                    bd=3,
                    command=lambda d=dia: self.abrir_dia(d)
                )
                boton.grid(row=i,column=j,padx=4,pady=4)
                self.botones[dia] = boton
                dia += 1

    # -------- ABRIR DÍA --------
    def abrir_dia(self, dia):
        if dia == 24 or dia == 25:
            mensaje = "🎄✨ FELIZ NAVIDAD ✨🎄"
        else:
            mensaje = random.choice(FRASES)

        messagebox.showinfo(f"Día {dia}", mensaje)

        self.botones[dia].config(
            text="✔",
            state="disabled",
            bg="#7f8c8d"
        )

    # -------- NIEVE --------
    def crear_nieve(self):
        copos=[]
        for _ in range(200):
            x=random.randint(0,self.w)
            y=random.randint(0,self.h)
            r=random.randint(1,3)
            copo=self.canvas.create_oval(
                x,y,x+r,y+r,
                fill="white", outline=""
            )
            copos.append((copo,random.uniform(1,3)))
        return copos

    # -------- ESTRELLAS --------
    def crear_estrellas(self):
        estrellas=[]
        for _ in range(60):
            x=random.randint(0,self.w)
            y=random.randint(80,self.h)
            estrella=self.canvas.create_text(
                x,y,
                text="⭐",
                font=("Arial",random.randint(8,16)),
                fill=random.choice(COLORES_LUCES)
            )
            estrellas.append(estrella)
        return estrellas

    # -------- ANIMACIÓN GENERAL --------
    def animar(self):
        for copo,vel in self.copos:
            self.canvas.move(copo,0,vel)
            if self.canvas.coords(copo)[1] > self.h:
                x=random.randint(0,self.w)
                self.canvas.coords(copo,x,0,x+2,2)

        for estrella in self.estrellas:
            self.canvas.itemconfig(
                estrella,
                fill=random.choice(COLORES_LUCES)
            )

        for boton in self.botones.values():
            if boton["state"] != "disabled":
                boton.config(bg=random.choice(COLORES_LUCES))

        self.master.after(120, self.animar)

# -------- EJECUCIÓN --------
if __name__=="__main__":
    root=tk.Tk()
    app=CalendarioNavideno(root)
    root.mainloop()
