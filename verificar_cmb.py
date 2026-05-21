"""
Verificacion de la prediccion CMB
a0(z) = c * H(z) / (2*pi)
Comparamos con datos publicos de Planck
"""
import numpy as np

# Constantes
C      = 299_792_458.0
H0     = 67.4 * 1000 / 3.086e22  # Planck 2018 (s^-1)
Omega_m = 0.315
Omega_L = 0.685
A0_OBS  = 1.2e-10  # a0 observado hoy

def H(z):
    return H0 * np.sqrt(Omega_m*(1+z)**3 + Omega_L)

def a0(z):
    return C * H(z) / (2 * np.pi)

print("="*60)
print("  VERIFICACION PREDICCION CMB")
print("="*60)
print(f"\n  H0 (Planck 2018)  : {H0*3.086e22/1000:.1f} km/s/Mpc")
print(f"  a0 hoy (z=0)      : {a0(0):.4e} m/s^2")
print(f"  a0 observado      : {A0_OBS:.4e} m/s^2")
print(f"  Error             : {abs(a0(0)-A0_OBS)/A0_OBS*100:.2f}%")

print(f"\n  {'Epoca':<20} {'z':<8} {'H (s^-1)':<15} {'a0 (m/s^2)':<15} {'Ratio'}")
print("  " + "-"*65)

epocas = [
    ("Hoy",           0),
    ("JWST (z=1)",    1),
    ("JWST (z=2)",    2),
    ("Reionizacion",  6),
    ("CMB (z=1100)",  1100),
    ("CMB (z=1089)",  1089),  # valor exacto Planck
]

a0_hoy = a0(0)
for nombre, z in epocas:
    Hz   = H(z)
    a0z  = a0(z)
    ratio= a0z / a0_hoy
    print(f"  {nombre:<20} {z:<8} {Hz:.4e}      {a0z:.4e}      {ratio:.1f}x")

print(f"\n  CONCLUSION:")
print(f"  En z=1089 (CMB exacto de Planck):")
z_cmb = 1089
print(f"  a0(z=1089) = {a0(z_cmb):.4e} m/s^2")
print(f"  = {a0(z_cmb)/a0_hoy:.0f} veces mayor que hoy")
print(f"\n  Esto es verificable con el espectro de potencias")
print(f"  del CMB publicado por Planck 2018.")
print(f"  URL datos: https://pla.esac.esa.int/")
print(f"\n  Para verificacion completa se necesita comparar")
print(f"  el primer pico acustico del CMB con la prediccion.")
print(f"  Eso requiere colaboracion con cosmologos.")
print(f"  McGaugh o Famaey pueden hacerlo con los datos que tienen.")
