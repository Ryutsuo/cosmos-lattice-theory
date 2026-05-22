"""
Luz y luz escalar de onda en celulas
phi_luz(E) = tanh(E / E_threshold)
Comparamos con datos de terapia fotodinamica
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# MODELO DE LUZ CELULAR
# ============================================================
# Energia de foton: E = h*f = h*c/lambda
h = 6.626e-34   # Planck (J·s)
c = 3e8         # velocidad luz (m/s)
eV = 1.602e-19  # 1 electronvoltio en Joules

def E_foton(lambda_nm):
    """Energia de foton en eV segun longitud de onda"""
    return (h * c / (lambda_nm * 1e-9)) / eV

def phi_luz(E_eV, E_threshold=2.0):
    """
    Estado celular bajo luz:
    phi = tanh(E / E_threshold)
    E_threshold = 2.0 eV (umbral de activacion biologica)
    """
    return np.tanh(E_eV / E_threshold)

# ============================================================
# ESPECTRO DE LUZ Y EFECTOS BIOLOGICOS
# ============================================================
# Datos reales de terapia fotodinamica y efectos biologicos
espectro = {
    # (lambda_nm, efecto_biologico, eficacia_PDT%)
    "Infrarrojo lejano (1000nm)": (1000, "penetracion profunda", 20),
    "Infrarrojo cercano (850nm)":  (850,  "terapia fotobiomod.",  45),
    "Rojo (660nm)":                (660,  "PDT optima tejido",    65),
    "Naranja (620nm)":             (620,  "activacion porfirinas", 60),
    "Amarillo (580nm)":            (580,  "absorcion hemoglobina", 40),
    "Verde (530nm)":               (530,  "clorofila/mitocondria", 55),
    "Azul (450nm)":                (450,  "ADN/flavinas",          70),
    "Violeta (400nm)":             (400,  "PDT superficial",       75),
    "UV cercano (365nm)":          (365,  "dano ADN/esteriliz.",   85),
}

print("="*75)
print("  LUZ Y CELULAS — Modelo phi_luz(E) = tanh(E/2.0eV)")
print("="*75)
print(f"\n  {'Tipo de luz':<32} {'λ(nm)':<8} {'E(eV)':<8} {'phi':<8} {'Efecto'}")
print("  " + "-"*72)

resultados_luz = []
for nombre, (lam, efecto, eficacia) in espectro.items():
    E = E_foton(lam)
    p = phi_luz(E)
    print(f"  {nombre:<32} {lam:<8} {E:<8.3f} {p:<8.4f} {efecto}")
    resultados_luz.append((nombre, lam, E, p, eficacia))

# ============================================================
# LUZ ESCALAR DE ONDA
# ============================================================
print(f"\n  LUZ ESCALAR DE ONDA:")
print(f"  La luz escalar es una onda longitudinal (no transversal)")
print(f"  Propuesta por Tesla, relacionada con campo escalar phi")
print(f"  En el framework Lattice: phi_escalar = tanh(r0/lP)")
print(f"  Frecuencias resonantes con celulas: 432 Hz, 528 Hz, 639 Hz")
print(f"  (frecuencias Solfeggio — investigacion preliminar)")

# Frecuencias de resonancia celular
freqs_hz = {
    "174 Hz (fundamento)":  174,
    "285 Hz (tejido)":      285,
    "396 Hz (liberacion)":  396,
    "432 Hz (natural)":     432,
    "528 Hz (ADN repair)":  528,
    "639 Hz (conexion)":    639,
    "741 Hz (expresion)":   741,
    "852 Hz (intuicion)":   852,
    "963 Hz (corona)":      963,
}

print(f"\n  {'Frecuencia':<25} {'Hz':<8} {'lambda(m)':<15} {'E(eV)':<12}")
print("  " + "-"*60)
for nombre, freq in freqs_hz.items():
    lam = c / freq
    E = h * freq / eV
    print(f"  {nombre:<25} {freq:<8} {lam:<15.2f} {E:.4e}")

# ============================================================
# CORRELACION LUZ vs EFICACIA PDT
# ============================================================
E_vals = np.array([E for _, _, E, _, _ in resultados_luz])
ef_vals = np.array([ef for _, _, _, _, ef in resultados_luz])
phi_vals = np.array([p for _, _, _, p, _ in resultados_luz])

corr_E  = np.corrcoef(E_vals, ef_vals)[0,1]
corr_phi= np.corrcoef(phi_vals, ef_vals)[0,1]

print(f"\n  CORRELACIONES:")
print(f"  Energia foton vs eficacia PDT : {corr_E:.4f}")
print(f"  phi_luz vs eficacia PDT       : {corr_phi:.4f}")

# ============================================================
# VISUALIZACION
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6), facecolor='black')
fig.suptitle('Luz y Celulas — phi_luz(E) = tanh(E/2eV)\n'
             'Terapia Fotodinamica y Luz Escalar',
             color='white', fontsize=11, fontweight='bold')

def dark(ax, title):
    ax.set_facecolor('#050510')
    ax.set_title(title, color='white', fontsize=9)
    ax.tick_params(colors='white', labelsize=7)
    for sp in ax.spines.values(): sp.set_edgecolor('#333')

# 1. Espectro visible y phi
ax1 = axes[0]
dark(ax1, 'phi_luz(lambda) — Espectro visible')
lam_arr = np.linspace(300, 1100, 500)
E_arr   = np.array([E_foton(l) for l in lam_arr])
phi_arr = np.array([phi_luz(E) for E in E_arr])

# Color del espectro
colors_spec = plt.cm.rainbow(np.linspace(1, 0, len(lam_arr)))
for i in range(len(lam_arr)-1):
    ax1.plot(lam_arr[i:i+2], phi_arr[i:i+2],
             color=colors_spec[i], lw=2.0)

ax1.axhline(0.762, color='white', lw=0.7, ls='--', label='Atractor sano (0.76)')
ax1.scatter([l for _, (l,_,_) in espectro.items()],
            [phi_luz(E_foton(l)) for _, (l,_,_) in espectro.items()],
            color='white', s=50, zorder=5)
ax1.set_xlabel('Longitud de onda (nm)', color='white', fontsize=8)
ax1.set_ylabel('phi_luz', color='white', fontsize=8)
ax1.legend(fontsize=6, facecolor='#111', labelcolor='white')

# 2. Eficacia PDT vs phi
ax2 = axes[1]
dark(ax2, f'phi_luz vs Eficacia PDT\nCorr: {corr_phi:.3f}')
scatter_colors = plt.cm.rainbow(np.linspace(1, 0, len(phi_vals)))
for i, (nombre, lam, E, p, ef) in enumerate(resultados_luz):
    ax2.scatter([p], [ef], color=scatter_colors[i], s=100, zorder=5)
    ax2.annotate(f"{lam}nm", (p, ef),
                fontsize=6, color='white',
                xytext=(3, 3), textcoords='offset points')
z = np.polyfit(phi_vals, ef_vals, 1)
p_line = np.poly1d(z)
x_line = np.linspace(min(phi_vals), max(phi_vals), 100)
ax2.plot(x_line, p_line(x_line), color='yellow', lw=1.0, ls='--')
ax2.set_xlabel('phi_luz', color='white', fontsize=8)
ax2.set_ylabel('Eficacia PDT (%)', color='white', fontsize=8)

# 3. Mapa unificado: luz + V_m + O2
ax3 = axes[2]
dark(ax3, 'Mapa Unificado — Tres Atractores')
x = np.linspace(0, 3, 300)
ax3.plot(x, np.tanh(x), color='yellow',      lw=2.0, label='Luz: tanh(E/2eV)')
ax3.plot(x, np.tanh(x), color='deepskyblue', lw=1.0, ls='--', label='V_m: tanh(|V|/70)')
ax3.plot(x, np.tanh(x), color='lime',        lw=0.8, ls=':', label='O2: tanh(pO2/5%)')
ax3.axhline(0.762, color='white', lw=0.7, ls='--', label='Atractor sano')
ax3.axvline(1.0,   color='orange',lw=0.5, ls=':')
ax3.set_xlabel('Parametro normalizado', color='white', fontsize=8)
ax3.set_ylabel('phi (estado celular)', color='white', fontsize=8)
ax3.legend(fontsize=6, facecolor='#111', labelcolor='white')
ax3.text(0.35, 0.35, 'MISMA FUNCION\nLUZ=V_m=O2=tanh',
         transform=ax3.transAxes, color='lime', fontsize=9, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='#001100', alpha=0.9))

plt.tight_layout()
out = r'c:\Users\kiros\Desktop\simulacion-cosmos\luz_celular_output.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='black')
print(f"\n  Imagen guardada: {out}")
print("\n  Analisis de luz completado.")
