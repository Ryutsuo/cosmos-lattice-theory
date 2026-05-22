"""
FUTURO DEL UNIVERSO — Lattice Vacuum Theory
a0(z) = c * H(z) / (2*pi)
Mapeamos desde el Big Bang hasta el fin del universo
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

C       = 299_792_458.0
H0      = 67.4 * 1000 / 3.086e22
Omega_m = 0.315
Omega_L = 0.685
Omega_r = 9.4e-5  # radiacion

def H(z):
    """H(z) para pasado (z>0) y futuro (z<0 equivale a a>1)"""
    a = 1 / (1 + z)
    # H^2 = H0^2 * (Omega_r/a^4 + Omega_m/a^3 + Omega_L)
    return H0 * np.sqrt(Omega_r/a**4 + Omega_m/a**3 + Omega_L)

def a0(z):
    return C * H(z) / (2 * np.pi)

# Tiempo cosmico aproximado (Gyr)
def tiempo_Gyr(z):
    """Edad del universo en Gyr para redshift z"""
    # Integracion numerica simple
    if z >= 1000:
        return 0.0
    z_arr = np.linspace(z, 1000, 10000)
    integrand = 1.0 / ((1+z_arr) * H(z_arr))
    return np.trapz(integrand, z_arr) / (3.156e7 * 1e9)  # en Gyr

print("="*65)
print("  FUTURO DEL UNIVERSO — Lattice Vacuum Theory")
print("="*65)

# Tabla completa: pasado + presente + futuro
epocas = [
    ("Big Bang",          1e6,   "pasado"),
    ("CMB",               1089,  "pasado"),
    ("Reionizacion",      6,     "pasado"),
    ("Primeras galaxias", 3,     "pasado"),
    ("Via Lactea forma",  2,     "pasado"),
    ("HOY",               0,     "presente"),
    ("Futuro cercano",    -0.3,  "futuro"),   # a=1.43, ~5 Gyr
    ("Futuro medio",      -0.6,  "futuro"),   # a=2.5,  ~20 Gyr
    ("Futuro lejano",     -0.8,  "futuro"),   # a=5,    ~50 Gyr
    ("Era oscura",        -0.95, "futuro"),   # a=20,   ~200 Gyr
]

print(f"\n  {'Epoca':<22} {'z':<8} {'H (s^-1)':<15} {'a0 (m/s^2)':<15} {'Ratio'}")
print("  " + "-"*70)

a0_hoy = a0(0)
for nombre, z, era in epocas:
    Hz  = H(z)
    a0z = a0(z)
    ratio = a0z / a0_hoy
    marca = "◄ HOY" if era == "presente" else ("▶ FUTURO" if era == "futuro" else "")
    print(f"  {nombre:<22} {z:<8.2f} {Hz:.4e}      {a0z:.4e}      {ratio:.3f}x  {marca}")

# Limite futuro
H_inf = H0 * np.sqrt(Omega_L)
a0_inf = C * H_inf / (2 * np.pi)
print(f"\n  {'Limite futuro (inf)':<22} {'inf':<8} {H_inf:.4e}      {a0_inf:.4e}      {a0_inf/a0_hoy:.3f}x")

print(f"\n  CONCLUSION:")
print(f"  En el futuro lejano H -> H_inf = {H_inf:.4e} s^-1")
print(f"  a0 converge a {a0_inf:.4e} m/s^2")
print(f"  = {a0_inf/a0_hoy:.3f} veces el valor actual")
print(f"  El universo no colapsa. Se estabiliza.")
print(f"  La gravedad efectiva MOND disminuye pero nunca llega a 0.")
print(f"  Consistente con r0 > 0 siempre.")

# ============================================================
# VISUALIZACION
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7), facecolor='black')
fig.suptitle('FUTURO DEL UNIVERSO — Lattice Vacuum Theory\na₀(z) = cH(z)/(2π)',
             color='white', fontsize=12, fontweight='bold')

# Rango: desde Big Bang hasta futuro lejano
# Usamos factor de escala a = 1/(1+z)
a_arr = np.logspace(-4, 1.5, 1000)  # a desde 0.0001 hasta ~30
z_arr = 1/a_arr - 1

H_arr  = np.array([H(z) for z in z_arr])
a0_arr = np.array([a0(z) for z in z_arr])

# Panel 1: a0 vs factor de escala
ax1 = axes[0]
ax1.set_facecolor('#050510')
ax1.loglog(a_arr, a0_arr, color='yellow', lw=2.0)
ax1.axvline(1.0, color='lime',  lw=1.0, ls='--', label='HOY (a=1)')
ax1.axhline(a0_inf, color='red', lw=0.8, ls=':', label=f'Limite futuro')
ax1.axhline(a0_hoy, color='cyan', lw=0.8, ls=':', label=f'a0 hoy')
# Marcar epocas
ax1.axvline(1/1090, color='magenta', lw=0.5, ls=':', alpha=0.7)
ax1.text(1/1090, a0_arr.max()*0.3, 'CMB', color='magenta', fontsize=7, rotation=90)
ax1.axvline(1/7, color='orange', lw=0.5, ls=':', alpha=0.7)
ax1.text(1/7, a0_arr.max()*0.3, 'z=6', color='orange', fontsize=7, rotation=90)
ax1.set_xlabel('Factor de escala a = 1/(1+z)', color='white', fontsize=9)
ax1.set_ylabel('a₀ (m/s²)', color='white', fontsize=9)
ax1.set_title('a₀(a) — Pasado y Futuro', color='white', fontsize=10)
ax1.tick_params(colors='white')
ax1.legend(fontsize=7, facecolor='#111', labelcolor='white')
for sp in ax1.spines.values(): sp.set_edgecolor('#333')

# Panel 2: H(z) vs factor de escala
ax2 = axes[1]
ax2.set_facecolor('#050510')
ax2.loglog(a_arr, H_arr * 3.086e22/1000, color='#00FF88', lw=2.0)
ax2.axvline(1.0, color='lime', lw=1.0, ls='--', label='HOY')
ax2.axhline(H_inf*3.086e22/1000, color='red', lw=0.8, ls=':', label='H limite')
ax2.set_xlabel('Factor de escala a', color='white', fontsize=9)
ax2.set_ylabel('H (km/s/Mpc)', color='white', fontsize=9)
ax2.set_title('H(a) — Expansion del Universo', color='white', fontsize=10)
ax2.tick_params(colors='white')
ax2.legend(fontsize=7, facecolor='#111', labelcolor='white')
for sp in ax2.spines.values(): sp.set_edgecolor('#333')

plt.tight_layout()
out = r'c:\Users\kiros\Desktop\simulacion-cosmos\futuro_universo.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='black')
print(f"\n  Imagen guardada: {out}")
print("\n  Mapa completo del universo completado.")
