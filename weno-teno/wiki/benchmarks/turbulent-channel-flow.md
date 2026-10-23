---
type: Benchmark
title: "Turbulent channel flow"
description: "Pressure-driven compressible flow between two isothermal no-slip walls in a periodic 2πh×2h×πh box, run as DNS, wall-resolved LES and wall-modeled LES from friction Reynolds number 180 to 20000 and bulk Mach 0.1 and 1.5, and judged against incompressible and compressible DNS profiles and friction laws."
status: established
aliases: [plane channel flow, turbulent plane channel, compressible channel flow, channel between immersed blocks]
tags: [benchmark, turbulence, gpu, immersed-boundary]
timestamp: 2026-10-22T19:46:00Z
---

# Turbulent channel flow

The turbulent channel is the flow between two parallel walls a distance
$2h$ apart, periodic in the streamwise ($x$) and spanwise ($z$)
directions and driven by a body force that keeps the mass flow rate
constant. Its statistics are one-dimensional (functions of the wall
distance only), it has a large DNS literature, and it isolates the near-wall
cycle that a scheme or wall model must sustain. The sources use it to
validate a compressible finite-difference solver in DNS, wall-resolved
LES (WRLES) and wall-modeled LES (WMLES), and to validate a wall model
coupled with an [immersed boundary method](/methods/immersed-boundary-method.md).
The case is defined by the friction Reynolds number
$\mathrm{Re}_\tau=u_\tau h/\nu_w$, the bulk Reynolds number
$\mathrm{Re}_b=2\rho_bu_bh/\mu_w$ and the bulk Mach number
$M_b=u_b/c_w$ ($u_\tau$ the friction velocity, $u_b$, $\rho_b$ the bulk
velocity and density, $c_w$, $\mu_w$, $\nu_w$ the wall sound speed and
viscosities; page-local).

## Data

| | [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) §5.1, Table 1 | [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) §4.1, Table 1 |
|---|---|---|
| box | $2\pi h\times2h\times\pi h$ | $2\pi h\times2.6h\times\pi h$, of which two immersed blocks of $0.3h$, fluid height $2h$ |
| walls | isothermal no-slip | isothermal no-slip immersed-boundary walls with the wall model |
| wall-normal grid | error-function stretching (DNS, WRLES), uniform (WMLES) | uniform |
| forcing | constant mass flow | $f_i=(0,f,0,0,fv_1)$ for constant mass flow |
| initial data | not printed | Henningson–Kim vortex pair on a Poiseuille profile |
| convective scheme | the code's sixth-order energy-preserving central scheme | pure sixth-order energy-preserving central scheme |

**Cases of De Vanna et al. (2023b).** TC01: DNS, $\mathrm{Re}_\tau=180$,
$\mathrm{Re}_b=5632$, $M_b=0.1$, $192\times128\times192$,
$\Delta x^+=5.9$, $\Delta y^+=0.7$–$3.8$, $\Delta z^+=2.9$, run on CPU
and GPU. TC02: DNS, $\mathrm{Re}_\tau=215$, $\mathrm{Re}_b=6008$,
$M_b=1.5$, $256\times128\times128$. TC03: WRLES, $\mathrm{Re}_\tau=590$,
$\mathrm{Re}_b=22242$, $96^3$, with the MXTS, Sigma and WALE subgrid
models. TC04: WMLES with WALE, $\mathrm{Re}_\tau=5200$,
$\mathrm{Re}_b=253374$, $160\times128\times80$,
$\Delta x^+=\Delta z^+=204$, $\Delta y^+=41$.

**Cases of De Vanna et al. (2023c).** Nine WMLES cases tch1–tch9 at
$M_b=0.1$ with nominal $\mathrm{Re}_\tau$ 590, 1000, 2000, 5200 (twice),
10000 (twice) and 20000 (twice), on grids from $48\times78\times24$ to
$224\times312\times112$; the repeated cases marked (a) reuse the
$120\times104\times60$ grid of the $\mathrm{Re}_\tau=2000$ case. Inner-scaled
spacings run from $77.2\times7.6\times77.2$ to $1047.2\times250.0\times1047.2$.

## Runs and findings

**Code validation (De Vanna et al. 2023b).** TC01 agrees with the
incompressible DNS of Bernardini et al., with computed
$\mathrm{Re}_\tau=179$ (0.6 % error), and the CPU and GPU runs agree
"down to machine precision". TC02 ($\mathrm{Re}_\tau=218$ computed)
agrees with the compressible DNS of Modesti & Pirozzoli in velocity,
Reynolds stresses and temperature. In TC03 the computed
$\mathrm{Re}_\tau$ is 588 (MXTS) and 586 (Sigma, WALE) against the
nominal 590, compared with Vreman & Kuerten. TC04 agrees with the
DNS far from the wall (Figs. 4–7). See
[URANOS](/software/uranos.md) and [wall-modeled LES](/methods/wall-modeled-les.md).

**Wall model with immersed walls (De Vanna et al. 2023c).** The computed
$\mathrm{Re}_\tau$ of the nine cases (596 to 19580) fit
$\mathrm{Re}_\tau=0.084\,\mathrm{Re}_b^{0.89}$, against $0.079\,\mathrm{Re}_b^{0.89}$
for a fit of DNS data and $0.09\,\mathrm{Re}_b^{0.88}$ from Pope (Table 2,
Fig. 5). Mean velocity and turbulent kinetic energy agree with DNS apart
from the log-layer mismatch the authors call typical of WMLES; above
$\mathrm{Re}_\tau=2000$ the coarse (a)-grid runs reproduce the finer ones.
The $\mathrm{Re}_\tau=20000$ case, beyond available DNS, is compared
with Reichardt's law only (§4.1, Fig. 6).

**Pipe variant.** De Vanna et al. (2023c) also run a pipe of radius $R$
carved out of an immersed square block ($2.4R\times2.4R\times2\pi R$,
$M_b=0.1$, $\mathrm{Re}_\tau$ 500–6000): the friction factor lies on the
DNS data and the Prandtl law except a slight overestimate at the lowest
Reynolds number, and the velocity fluctuations are systematically
underestimated (§4.2, Figs. 9–10).

## Qualifications

- Both sources compare profiles with DNS in figures only, without
  printed error norms; the quantitative measures are the computed
  $\mathrm{Re}_\tau$ and the friction-law fit.
- The inner-scaled wall-normal spacings of De Vanna et al. (2023c) follow
  an undocumented convention: for tch2–tch9 the printed $\Delta y^+$ is
  exactly half of $2.6\,\mathrm{Re}_{\tau,0}/N_y$, and for tch1 it is
  neither the full nor the half spacing (7.6 against 19.7 and 9.8)
  *(compiler check, not in the sources)*.
- De Vanna et al. (2023b) cite Moser et al. for the $\mathrm{Re}_\tau=5200$
  reference in the Fig. 7 caption and Lee & Moser in the text.

# Citations

- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §5.1, Table 1, Figs. 4–7.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §4.1–4.2, Tables 1–3, Figs. 3–10.
