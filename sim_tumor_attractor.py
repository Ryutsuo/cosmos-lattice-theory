"""
Simulacion: restauracion del atractor phi=0.762 en tumor GBM
100 celulas sanas (phi=0.762) introducidas en 900 celulas GBM (phi=0.211)
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)

N_cells   = 1000
N_healthy = 100
N_steps   = 500
dt        = 0.01
V_healthy = -70.0
V_GBM     = -15.0
V_threshold = 70.0

def phi(V):
    return np.tanh(abs(V) / V_threshold)

def step_cells(V, gamma=0.5, noise=0.3):
    V_mean = np.mean(V)
    dV = -gamma * (V - V_mean) + np.random.normal(0, noise, len(V))
    return V + dt * dV

# Inicializar: 900 GBM + 100 sanas
V_pop = np.concatenate([
    np.random.normal(V_GBM,     2.0, N_cells - N_healthy),
    np.random.normal(V_healthy, 2.0, N_healthy)
])

print("="*60)
print("  SIMULACION: Restauracion Atractor en GBM")
print("="*60)
print(f"  Celulas GBM      : {N_cells - N_healthy}  phi={phi(V_GBM):.4f}")
print(f"  Celulas sanas    : {N_healthy}   phi={phi(V_healthy):.4f}")
print(f"  Atractor objetivo: phi=0.7616")

phi_history = []
V_history   = []

for step in range(N_steps):
    phi_history.append(np.mean([phi(v) for v in V_pop]))
    V_history.append(np.mean(V_pop))
    V_pop = step_cells(V_pop)
    # Anclar celulas sanas al atractor
    V_pop[N_cells-N_healthy:] = np.clip(
        V_pop[N_cells-N_healthy:], -80, -60)

phi_ini   = phi_history[0]
phi_final = phi_history[-1]
V_final   = V_history[-1]
restaurado = phi_final > 0.65

print(f"\n  phi inicial : {phi_ini:.4f}")
print(f"  phi final   : {phi_final:.4f}")
print(f"  V_m final   : {V_final:.2f} mV")
print(f"  Mejora      : +{(phi_final-phi_ini)*100:.1f}%")
print(f"  Resultado   : {'ATRACTOR RESTAURADO' if restaurado else 'PARCIALMENTE RESTAURADO'}")

# Visualizacion
fig, axes = plt.subplots(1, 3, figsize=(18, 6), facecolor='black')
fig.suptitle(
    f'Restauracion Atractor phi=0.762 en GBM\n'
    f'100 celulas sanas en 900 GBM  |  phi: {phi_ini:.3f} → {phi_final:.3f}',
    color='white', fontsize=11, fontweight='bold'
)

def dark(ax, title):
    ax.set_facecolor('#050510')
    ax.set_title(title, color='white', fontsize=9)
    ax.tick_params(colors='white', labelsize=7)
    for sp in ax.spines.values(): sp.set_edgecolor('#333')

ax1 = axes[0]
dark(ax1, 'Evolucion phi — Restauracion')
ax1.plot(phi_history, color='yellow', lw=1.5)
ax1.axhline(0.7616, color='lime',   lw=0.8, ls='--', label='Atractor sano')
ax1.axhline(phi_ini, color='red',   lw=0.5, ls=':', label='GBM inicial')
ax1.set_xlabel('Pasos', color='white', fontsize=8)
ax1.set_ylabel('phi medio', color='white', fontsize=8)
ax1.legend(fontsize=6, facecolor='#111', labelcolor='white')
color_txt = 'lime' if restaurado else 'orange'
ax1.text(0.4, 0.15, f'phi final: {phi_final:.4f}\n{"RESTAURADO" if restaurado else "PARCIAL"}',
         transform=ax1.transAxes, color=color_txt, fontsize=10, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='#001100', alpha=0.9))

ax2 = axes[1]
dark(ax2, 'Distribucion V_m final')
ax2.hist(V_pop[:N_cells-N_healthy], bins=40, color='red',
         alpha=0.6, label='GBM', density=True)
ax2.hist(V_pop[N_cells-N_healthy:], bins=20, color='lime',
         alpha=0.7, label='Sanas', density=True)
ax2.axvline(V_healthy, color='lime', lw=1.0, ls='--', label='-70mV atractor')
ax2.set_xlabel('V_m (mV)', color='white', fontsize=8)
ax2.legend(fontsize=6, facecolor='#111', labelcolor='white')

ax3 = axes[2]
dark(ax3, 'Trayectoria en espacio de fase')
sc = ax3.scatter(V_history, phi_history,
                 c=range(len(V_history)), cmap='plasma', s=2, alpha=0.7)
ax3.scatter([V_history[0]],  [phi_history[0]],  color='red',  s=150, zorder=5, label='Inicio')
ax3.scatter([V_history[-1]], [phi_history[-1]], color='lime', s=150, zorder=5, label='Final')
ax3.axhline(0.7616, color='lime', lw=0.7, ls='--')
ax3.set_xlabel('V_m medio (mV)', color='white', fontsize=8)
ax3.set_ylabel('phi medio', color='white', fontsize=8)
ax3.legend(fontsize=6, facecolor='#111', labelcolor='white')

plt.tight_layout()
out = r'c:\Users\kiros\Desktop\simulacion-cosmos\tumor_attractor_output.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='black')
print(f"\n  Imagen guardada: {out}")
