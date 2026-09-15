import tkinter as tk
from tkinter import ttk, messagebox

# --- Mapeamento de Cores da Tabela de Resistores ---
COLOR_MAP = {
    "preto": {"val": 0, "mult": 1, "hex": "#000000"},
    "marrom": {"val": 1, "mult": 10, "tol": 1.0, "hex": "#8B4513"},
    "vermelho": {"val": 2, "mult": 100, "tol": 2.0, "hex": "#FF0000"},
    "laranja": {"val": 3, "mult": 1000, "hex": "#FFA500"},
    "amarelo": {"val": 4, "mult": 10000, "hex": "#FFFF00"},
    "verde": {"val": 5, "mult": 100000, "tol": 0.5, "hex": "#008000"},
    "azul": {"val": 6, "mult": 1000000, "tol": 0.25, "hex": "#0000FF"},
    "violeta": {"val": 7, "mult": 10000000, "tol": 0.1, "hex": "#EE82EE"},
    "cinza": {"val": 8, "mult": 100000000, "tol": 0.05, "hex": "#808080"},
    "branco": {"val": 9, "mult": 1000000000, "hex": "#FFFFFF"},
    "dourado": {"mult": 0.1, "tol": 5.0, "hex": "#FFD700"},
    "prata": {"mult": 0.01, "tol": 10.0, "hex": "#C0C0C0"}
}

# --- Funções do Sistema ---

def format_resistance(value):
    """Formata a resistência com o prefixo correto (Ω, kΩ, MΩ)."""
    if value >= 1000000:
        return f"{value / 1000000:.2f} MΩ"
    elif value >= 1000:
        return f"{value / 1000:.2f} kΩ"
    else:
        return f"{value:.2f} Ω"

def draw_resistor(color1, color2, color_mult, color_tol):
    """Desenha a imagem estilizada do resistor dinamicamente no Canvas."""
    canvas.delete("all")
    width = canvas.winfo_width() or 400
    height = canvas.winfo_height() or 180

    # Linha/Fios do resistor
    canvas.create_line(20, height // 2, width - 20, height // 2, fill="#555555", width=4)
    
    # Corpo do resistor
    rx1, ry1 = 60, height // 2 - 30
    rx2, ry2 = width - 60, height // 2 + 30
    canvas.create_rectangle(rx1, ry1, rx2, ry2, fill="#F5E5C9", outline="#8B5A2B", width=2)

    # Coordenadas das faixas
    band_w = 12
    b1_x = rx1 + 30
    b2_x = rx1 + 80
    b3_x = rx1 + 130
    b4_x = rx2 - 40

    # Faixas
    canvas.create_rectangle(b1_x, ry1, b1_x + band_w, ry2, fill=COLOR_MAP[color1]["hex"], outline="")
    canvas.create_rectangle(b2_x, ry1, b2_x + band_w, ry2, fill=COLOR_MAP[color2]["hex"], outline="")
    canvas.create_rectangle(b3_x, ry1, b3_x + band_w, ry2, fill=COLOR_MAP[color_mult]["hex"], outline="")
    canvas.create_rectangle(b4_x, ry1, b4_x + band_w, ry2, fill=COLOR_MAP[color_tol]["hex"], outline="")

    # Rótulos abaixo do resistor
    canvas.create_text((rx1 + rx2) // 2, ry1 - 15, text="Resistor de 4 faixas", font=("Arial", 12, "bold"))
    labels = f"{color1.capitalize()}  {color2.capitalize()}  {color_mult.capitalize()}  {color_tol.capitalize()}"
    canvas.create_text((rx1 + rx2) // 2, ry2 + 18, text=labels, font=("Arial", 10))

def calculate_from_colors():
    """Calcula a resistência com base nas cores selecionadas[cite: 2]."""
    c1 = cb_band1.get()
    c2 = cb_band2.get()
    cm = cb_mult.get()
    ct = cb_tol.get()

    if not all([c1, c2, cm, ct]):
        messagebox.showwarning("Aviso", "Selecione todas as cores das faixas.")
        return

    val1 = COLOR_MAP[c1]["val"]
    val2 = COLOR_MAP[c2]["val"]
    mult = COLOR_MAP[cm]["mult"]
    tol = COLOR_MAP[ct].get("tol", 5.0)

    total_val = (val1 * 10 + val2) * mult
    formatted_val = format_resistance(total_val)
    
    lbl_result.config(text=f"Resistência: {formatted_val} ±{tol}%")
    draw_resistor(c1, c2, cm, ct)

def calculate_from_value():
    """Calcula as cores com base no valor numérico informado[cite: 2]."""
    val_str = entry_val.get().replace(",", ".")
    tol_color = cb_tol_val.get()

    try:
        val = float(val_str)
        if val <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor numérico válido para a resistência.")
        return

    # Normalizar valor para encontrar digitos e multiplicador
    mult = 1
    temp_val = val
    
    # Caso para multiplicadores menores que 1 (dourado/prata)
    if temp_val < 1:
        if temp_val >= 0.1:
            mult = 0.1
            mult_color = "dourado"
            sig_digits = round(temp_val / 0.1)
        else:
            mult = 0.01
            mult_color = "prata"
            sig_digits = round(temp_val / 0.01)
    else:
        while temp_val >= 100:
            temp_val /= 10
            mult *= 10
        sig_digits = int(round(temp_val))
        
        # Encontrar cor do multiplicador
        mult_color = next((k for k, v in COLOR_MAP.items() if v.get("mult") == mult), "preto")

    d1 = sig_digits // 10
    d2 = sig_digits % 10

    c1 = next((k for k, v in COLOR_MAP.items() if v.get("val") == d1), "marrom")
    c2 = next((k for k, v in COLOR_MAP.items() if v.get("val") == d2), "preto")

    lbl_result.config(text=f"Resistência: {format_resistance(val)} ±{COLOR_MAP[tol_color].get('tol')}%")
    draw_resistor(c1, c2, mult_color, tol_color)

def toggle_mode():
    """Alterna os controles visíveis conforme o modo escolhido[cite: 2]."""
    mode = mode_var.get()
    
    if mode == "colors":
        frame_val.grid_remove()
        frame_colors.grid(row=1, column=0, pady=10, sticky="ew")
        btn_calc.config(text="Calcular resistência", command=calculate_from_colors)
    else:
        frame_colors.grid_remove()
        frame_val.grid(row=1, column=0, pady=10, sticky="ew")
        btn_calc.config(text="Calcular cores", command=calculate_from_value)

# --- Interface Gráfica ---

root = tk.Tk()
root.title("Calculadora de Resistor")
root.geometry("450x520")
root.resizable(False, False)

# Estilos e Cabeçalho
lbl_title = tk.Label(root, text="Calculadora de Resistor", font=("Arial", 16, "bold"))
lbl_title.pack(pady=10)

# Modo de seleção
frame_mode = tk.LabelFrame(root, text="Como deseja informar o resistor?", font=("Arial", 10, "bold"))
frame_mode.pack(padx=15, fill="x")

mode_var = tk.StringVar(value="colors")
rb_colors = tk.Radiobutton(frame_mode, text="Cores do resistor", variable=mode_var, value="colors", command=toggle_mode)
rb_val = tk.Radiobutton(frame_mode, text="Valor da resistência", variable=mode_var, value="value", command=toggle_mode)
rb_colors.pack(side="right", padx=10, pady=5)
rb_val.pack(side="left", padx=10, pady=5)

# Container principal
container = tk.Frame(root)
container.pack(padx=15, fill="x")

# --- Painel Modo 1: Cores ---
frame_colors = tk.Frame(container)

digits_colors = ["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"]
mult_colors = digits_colors + ["dourado", "prata"]
tol_colors = ["marrom", "vermelho", "verde", "azul", "violeta", "cinza", "dourado", "prata"]

tk.Label(frame_colors, text="Banda 1:").grid(row=0, column=0)
cb_band1 = ttk.Combobox(frame_colors, values=digits_colors[1:], width=10, state="readonly")
cb_band1.grid(row=1, column=0, padx=2)
cb_band1.set("vermelho")

tk.Label(frame_colors, text="Banda 2:").grid(row=0, column=1)
cb_band2 = ttk.Combobox(frame_colors, values=digits_colors, width=10, state="readonly")
cb_band2.grid(row=1, column=1, padx=2)
cb_band2.set("vermelho")

tk.Label(frame_colors, text="Multiplicador:").grid(row=0, column=2)
cb_mult = ttk.Combobox(frame_colors, values=mult_colors, width=10, state="readonly")
cb_mult.grid(row=1, column=2, padx=2)
cb_mult.set("laranja")

tk.Label(frame_colors, text="Tolerância:").grid(row=0, column=3)
cb_tol = ttk.Combobox(frame_colors, values=tol_colors, width=10, state="readonly")
cb_tol.grid(row=1, column=3, padx=2)
cb_tol.set("violeta")

# --- Painel Modo 2: Valor ---
frame_val = tk.Frame(container)

tk.Label(frame_val, text="Valor da resistência (Ω):").grid(row=0, column=0, sticky="w")
entry_val = tk.Entry(frame_val, width=20)
entry_val.grid(row=1, column=0, padx=5, pady=5)

tk.Label(frame_val, text="Tolerância:").grid(row=0, column=1, sticky="w")
cb_tol_val = ttk.Combobox(frame_val, values=tol_colors, width=10, state="readonly")
cb_tol_val.grid(row=1, column=1, padx=5, pady=5)
cb_tol_val.set("dourado")

# Botão de Ação
btn_calc = tk.Button(root, text="Calcular resistência", bg="#1b8a71", fg="white", font=("Arial", 10, "bold"))
btn_calc.pack(pady=10)

# Resultado e Desenho Grafico
lbl_result = tk.Label(root, text="", font=("Arial", 11, "bold"))
lbl_result.pack(pady=5)

canvas = tk.Canvas(root, width=400, height=160, bg="white", relief="sunken", bd=1)
canvas.pack(padx=15, pady=5)

# Inicialização da tela
toggle_mode()

root.mainloop()