import tkinter as tk
import math

# Seaded
AKNA_LAIUS  = 520
AKNA_KORGUS = 620
KETTA_R     = 160          # ketta raadius
AUGU_R      = 18           # numbriaukude raadius
KESK_R      = 30           # keskaugu raadius
STOPPER_NURK = 290         # stopper asub 290° juures (päripäeva 0-st)

# Numbrid ketas (0 on viimane, nagu päris telefonil)
NUMBRID = ["1","2","3","4","5","6","7","8","9","0"]

# Iga numbri nurk kettal (kus augukese keskpunkt asub)
# Jaotame 10 auku vahemikus ~20° kuni ~270° (stopper on 290°)
def numbri_nurk(i):
    # Numbrid 1-0, alustame 20°-st, sammuga ~27°
    return 20 + i * 27

# Peaaken
aken = tk.Tk()
aken.title("Ketastelefon")
aken.resizable(False, False)
aken.configure(bg="#1a1a2e")

canvas = tk.Canvas(aken, width=AKNA_LAIUS, height=380,
                   bg="#1a1a2e", highlightthickness=0)
canvas.pack(pady=(20, 0))

# Numbrite kuvamine
info_raam = tk.Frame(aken, bg="#1a1a2e")
info_raam.pack(fill="x", padx=30)

number_muutuja = tk.StringVar(value="")
tk.Label(info_raam, text="Valitud number:", bg="#1a1a2e",
         fg="#aaaacc", font=("Courier", 11)).pack(side="left")
number_silt = tk.Label(info_raam, textvariable=number_muutuja,
                       bg="#1a1a2e", fg="#e0e0ff",
                       font=("Courier", 18, "bold"), width=12, anchor="w")
number_silt.pack(side="left", padx=8)

kustuta_nupp = tk.Button(info_raam, text="✕ Kustuta",
                          bg="#3a1a2e", fg="#ff6688",
                          font=("Courier", 10), relief="flat",
                          activebackground="#5a2a3e", activeforeground="#ff88aa",
                          command=lambda: number_muutuja.set(""))
kustuta_nupp.pack(side="right")

# Helista nupp
nupp_raam = tk.Frame(aken, bg="#1a1a2e")
nupp_raam.pack(pady=10)

olek_muutuja = tk.StringVar(value="")
olek_silt = tk.Label(aken, textvariable=olek_muutuja,
                     bg="#1a1a2e", fg="#66ffcc",
                     font=("Courier", 13, "bold"))
olek_silt.pack()

def helista():
    nr = number_muutuja.get()
    if nr:
        olek_muutuja.set(f"📞 Helistan ... {nr}")
    else:
        olek_muutuja.set("⚠  Vali kõigepealt number!")

helista_nupp = tk.Button(nupp_raam, text="📞  Helista",
                          bg="#16213e", fg="#66ffcc",
                          font=("Courier", 14, "bold"),
                          relief="flat", padx=20, pady=8,
                          activebackground="#0f3460", activeforeground="#aaffee",
                          command=helista)
helista_nupp.pack()

# ── Ketta olek
KESK_X = AKNA_LAIUS // 2
KESK_Y = 190

ketta_nurk   = 0.0    # praegune pöördenurk (kraadides)
lohistamine  = False
hiire_nurk_alg = 0.0  # hiire nurk lohistamise alguses
ketta_nurk_alg = 0.0  # ketta nurk lohistamise alguses
valitud_auk  = None   # millist auku tõmmatakse (-1 = ei ühtegi)
animatsioon_id = None

# ── Joonista ketas
def kraad_rad(k):
    return math.radians(k)

def joonista(nurk_offset=0.0):
    """Joonista kogu ketas antud pöördenurgaga."""
    canvas.delete("all")

    # Vari
    canvas.create_oval(KESK_X - KETTA_R + 6, KESK_Y - KETTA_R + 6,
                       KESK_X + KETTA_R + 6, KESK_Y + KETTA_R + 6,
                       fill="#0a0a18", outline="")

    # Ketta taust
    canvas.create_oval(KESK_X - KETTA_R, KESK_Y - KETTA_R,
                       KESK_X + KETTA_R, KESK_Y + KETTA_R,
                       fill="#16213e", outline="#3a3a6e", width=3)

    # Stopper joon
    sx = KESK_X + (KETTA_R - 10) * math.cos(kraad_rad(STOPPER_NURK))
    sy = KESK_Y + (KETTA_R - 10) * math.sin(kraad_rad(STOPPER_NURK))
    canvas.create_line(KESK_X + (KETTA_R - 35) * math.cos(kraad_rad(STOPPER_NURK)),
                       KESK_Y + (KETTA_R - 35) * math.sin(kraad_rad(STOPPER_NURK)),
                       sx, sy, fill="#ff6644", width=4, capstyle="round")
    canvas.create_oval(sx - 6, sy - 6, sx + 6, sy + 6, fill="#ff6644", outline="")

    # Numbriaugud
    for i, nr in enumerate(NUMBRID):
        alg_nurk = numbri_nurk(i)
        nurk = alg_nurk + nurk_offset
        rad  = kraad_rad(nurk)
        aug_x = KESK_X + (KETTA_R - 40) * math.cos(rad)
        aug_y = KESK_Y + (KETTA_R - 40) * math.sin(rad)

        # Augu taust
        canvas.create_oval(aug_x - AUGU_R, aug_y - AUGU_R,
                           aug_x + AUGU_R, aug_y + AUGU_R,
                           fill="#0a0a18", outline="#5a5a9e", width=2)
        # Number
        canvas.create_text(aug_x, aug_y, text=nr,
                           fill="#ccccff", font=("Courier", 12, "bold"))

    # Keskauk
    canvas.create_oval(KESK_X - KESK_R, KESK_Y - KESK_R,
                       KESK_X + KESK_R, KESK_Y + KESK_R,
                       fill="#0e1628", outline="#3a3a6e", width=2)

    # Ketta nimi
    canvas.create_text(KESK_X, KESK_Y - 70,
                       text="KETASTELEFON", fill="#444466",
                       font=("Courier", 9, "bold"))

joonista()

# ── Hiire loogika
def hiire_nurk(event):
    """Tagastab hiire nurga ketta keskpunkti suhtes (kraadides)."""
    dx = event.x - KESK_X
    dy = event.y - KESK_Y
    return math.degrees(math.atan2(dy, dx))

def mis_auk(nurk_offset):
    """Tagastab augu indeksi, mis on praegu stopper-joone juures, või None."""
    for i in range(len(NUMBRID)):
        aug_nurk = (numbri_nurk(i) + nurk_offset) % 360
        erinevus = abs(aug_nurk - STOPPER_NURK)
        if erinevus > 180:
            erinevus = 360 - erinevus
        if erinevus < 13:
            return i
    return None

def vajutus(event):
    global lohistamine, hiire_nurk_alg, ketta_nurk_alg, valitud_auk, animatsioon_id

    # Peata animatsioon
    if animatsioon_id:
        aken.after_cancel(animatsioon_id)
        animatsioon_id = None

    # Kas klikiti ketta peal?
    dx = event.x - KESK_X
    dy = event.y - KESK_Y
    kaugus = math.sqrt(dx**2 + dy**2)
    if kaugus < KESK_R + 5 or kaugus > KETTA_R:
        return

    # Kas klikiti augukese peal?
    valitud_auk = None
    for i in range(len(NUMBRID)):
        aug_nurk = (numbri_nurk(i) + ketta_nurk) % 360
        rad = kraad_rad(aug_nurk)
        aug_x = KESK_X + (KETTA_R - 40) * math.cos(rad)
        aug_y = KESK_Y + (KETTA_R - 40) * math.sin(rad)
        if math.sqrt((event.x - aug_x)**2 + (event.y - aug_y)**2) < AUGU_R + 5:
            valitud_auk = i
            break

    if valitud_auk is None:
        return  # klõpsati tühjale alale

    lohistamine    = True
    hiire_nurk_alg = hiire_nurk(event)
    ketta_nurk_alg = ketta_nurk

def liikumine(event):
    global ketta_nurk
    if not lohistamine:
        return

    praegune = hiire_nurk(event)
    delta = praegune - hiire_nurk_alg

    # Normaliseeri [-180, 180]
    while delta > 180:  delta -= 360
    while delta < -180: delta += 360

    uus_nurk = ketta_nurk_alg + delta

    # Lubame ainult päripäeva (positiivne delta) ja max stopperini
    aug_algnurk = numbri_nurk(valitud_auk)
    max_pooue = STOPPER_NURK - aug_algnurk  # kui palju tohib keerata

    if max_pooue < 0:
        max_pooue = 0

    uus_nurk = max(0.0, min(float(max_pooue), uus_nurk))
    ketta_nurk = uus_nurk
    joonista(ketta_nurk)



def vabastus(event):
    global lohistamine, valitud_auk
    if not lohistamine:
        return
    lohistamine = False

    # Kas auk jõudis stopperini? (lubame väikest viga)
    aug_algnurk = numbri_nurk(valitud_auk)
    max_pooue = STOPPER_NURK - aug_algnurk
    if ketta_nurk >= max_pooue - 10:
        # Lisa number
        nr = NUMBRID[valitud_auk]
        praegune = number_muutuja.get()
        number_muutuja.set(praegune + nr)
        olek_muutuja.set("")

    valitud_auk = None
    tagasi_animeeri()

def tagasi_animeeri():
    """Animeeri ketas tagasi 0-asendisse."""
    global ketta_nurk, animatsioon_id

    if ketta_nurk <= 0.5:
        ketta_nurk = 0.0
        joonista(0)
        animatsioon_id = None
        return

    ketta_nurk *= 0.82  # aeglustumine
    joonista(ketta_nurk)
    animatsioon_id = aken.after(16, tagasi_animeeri)  # ~60fps

canvas.bind("<ButtonPress-1>",   vajutus)
canvas.bind("<B1-Motion>",       liikumine)
canvas.bind("<ButtonRelease-1>", vabastus)

aken.mainloop()