---
type: Method
title: "Discrete equations method (DEM)"
description: "The discrete equations method builds a multiphase Godunov scheme for the non-equilibrium Baer–Nunziato model from pairwise single- and two-phase Riemann problems in flow channels, with the non-conservative terms given by Lagrangian fluxes across contact waves; the page records the effective-cell-size time-step limit of its high-order extension and Paula et al.'s RDEMIC, which removes it."
status: established
aliases: [DEM, discrete-equations method, Abgrall–Saurel DEM, RDEMIC, robust DEM for interface capturing]
tags: [multiphase, finite-volume, riemann-solver, interface-capturing, reconstruction]
timestamp: 2026-10-23T23:00:00Z
---

# Discrete equations method (DEM)

The discrete equations method of Abgrall and Saurel, as recalled by
[Paula, Adami & Adams (2023)](/sources/paula-2023.md) §3.1, discretizes the
non-equilibrium multiphase model of Baer–Nunziato and Saurel–Abgrall
without discretizing its non-conservative terms directly. At every cell
face the phases are assumed to be stratified: each occupies a contiguous
sub-volume, and the face is divided into **flow channels**, single-phase
channels where the same phase lies on both sides and two-phase channels
where different phases meet. A single-phase Riemann problem is solved in
each single-phase channel and a two-phase one in each two-phase channel;
the non-conservative interface terms are the Lagrangian fluxes across the
contact wave of the two-phase problems, so no closure for the interface
pressure and velocity is needed. With piecewise-constant volume fractions
the method is very robust but diffuses interfaces strongly; Paula et al.
analyse why its high-order extension restricts the time step and propose
**RDEMIC** (robust DEM for interface capturing), which removes the
restriction.

## Model

For phase $k$, with volume fraction $\phi_k$, phase density $\rho_k$,
velocity $v_k$, pressure $p_k$ and total energy per unit volume
$E_k=\rho_ke_k+\tfrac12\rho_k\lvert v_k\rvert^2$, and with interface
pressure and velocity $p_{\mathrm I}$, $v_{\mathrm I}$ (page-local), the
model is (Paula et al. Eqs. 1–5)

$$\begin{aligned}
&\partial_t\phi_k+v_{\mathrm I}\cdot\nabla\phi_k=0,\qquad \partial_t(\phi_k\rho_k)+\nabla\cdot(\phi_k\rho_kv_k)=0,\\
&\partial_t(\phi_k\rho_kv_k)+\nabla\cdot(\phi_k\rho_kv_k\otimes v_k+\phi_kp_kI)=p_{\mathrm I}\nabla\phi_k,\\
&\partial_t(\phi_kE_k)+\nabla\cdot\big(\phi_k(E_k+p_k)v_k\big)=p_{\mathrm I}v_{\mathrm I}\cdot\nabla\phi_k,
\end{aligned}$$

with $\sum_k\phi_k=1$, $0\le\phi_k\le1$, and a
[stiffened-gas](/definitions/stiffened-gas-equation-of-state.md) law per
phase. The sum over the phases of the phase vectors $U_k$ (below) is conserved; of the phasic
quantities only the masses are. For two phases it is the seven-equation model; it reduces
to Euler for one phase. Relaxation terms, the authors note, are usually needed; Paula et al.
use none, because the two-phase Riemann problem enforces mechanical
equilibrium (§2.1, §7.4.1). The reduced Kapila, Allaire and six-equation
models of the [five-equation family](/definitions/five-equation-model.md)
are mentioned as alternatives (§1).

## The original method

Write $U_k=\phi_kV_k$, $V_k=(1,\rho_k,\rho_kv_k,E_k)$, and the phase flux
$\phi_kG_k$ (Eq. 11). With piecewise-constant volume fractions the face
$x_{i+1/2}$ carries the contact areas (Eqs. 12–13; page-local
$\delta_{kl}$, not the TENO flag $\delta_k$)

$$\delta_{kk}=\min(\phi^-_k,\phi^+_k),\qquad \delta_{kl}=\max(0,\phi^-_k-\phi^+_k),$$

with $\phi^\mp_k$ the left and right states, $\sum\delta=1$, and
$\delta_{kl}>0$ meaning phase $k$ on the left. Each two-phase channel
solves a Riemann problem with contact velocity and pressure $v^*_{kl}$,
$p^*_{kl}$, and its exchange term is the Lagrangian flux across the
contact,

$$b_{kl}=\big(-v^*_{kl},\,0,\,p^*_{kl},\,p^*_{kl}v^*_{kl}\big)\qquad(\text{Eq. 14}),$$

assigned upwind on the sign of $v^*_{kl}$, so it enters only the downwind
cell (Eqs. 15–18). Fluxes and exchange terms are scaled by the contact
areas and summed into the face flux and the cell's non-conservative term.

**High-order extension.** The original high-order DEM reconstructs the
volume fractions with a nonlinear scheme, adds an in-cell contact of
area $\max(0,\phi^+_{k,i-1/2}-\phi^-_{k,i+1/2})$ between the two face
values of cell $i$, and solves an additional in-cell two-phase Riemann
problem there (Eqs. 19–20).

**Its time-step limit** (Paula et al. §3.2). A nonlinear reconstruction
does not satisfy $\tfrac12(\phi^+_{k,i-1/2}+\phi^-_{k,i+1/2})=\bar\phi_{k,i}$,
so splitting the cell into two constant sub-volumes puts the in-cell
contact at

$$\tilde x_i=x_{i-1/2}+\frac{\bar\phi_{k,i}-\phi^-_{k,i+1/2}}{\phi^+_{k,i-1/2}-\phi^-_{k,i+1/2}}\,\Delta x\qquad(\text{Eq. 21}),$$

and the waves launched there reach a face or the contact after a fraction
of $\Delta x$. The CFL condition must then hold for the effective cell
size $\Delta\tilde x_i=\min(\tilde x_i-x_{i-1/2},\,x_{i+1/2}-\tilde x_i)$
(Eq. 22), which can be arbitrarily small. With piecewise-constant data
every wave runs within its phase sub-volume over the full $\Delta x$, so
the limit is that of single-phase flow (Fig. 3).

## RDEMIC

Paula et al. (§4.1) define the channels from the cell averages instead of
the face values,

$$\delta^C_{kk}=\min(\bar\phi_{k,i},\bar\phi_{k,i+1}),\qquad \delta^C_{kl}=\max(0,\bar\phi_{k,i}-\bar\phi_{k,i+1})\qquad(\text{Eqs. 23–24}),$$

and treat the reconstructed jumps inside the two-phase channel as
sub-volumes, $\delta^L_{kl}=\max(0,\bar\phi_{k,i}-\phi^-_{k,i+1/2})$ in the
upwind cell and $\delta^R_{kl}=\max(0,\bar\phi_{l,i+1}-\phi^+_{l,i+1/2})$
in the downwind cell (Eqs. 26–27). The whole two-phase channel evolves
with the single cell-face two-phase Riemann solution; no in-cell Riemann
problem is solved. For $v^*_{kl}>0$:

- the single-phase channel flux is $\delta^C_{kk}$ times the Riemann flux
  between the face states (Eq. 25);
- the sub-volume $\delta^L_{kl}$ receives the **pseudo-Riemann flux**
  $g^K_{kl,n}=v^*_{kl}V^K_n+b_{kl}$, $n\in\{k,l\}$, $K\in\{L,R\}$
  (Eq. 29): the cell-averaged state transported at the contact velocity,
  plus the Lagrangian flux;
- the matching exchange term and the pseudo-Riemann flux combine to
  $-\delta^L_{kl}v^*_{kl}V^L_l$ (Eq. 50), a uniform transfer of the
  upwind excess volume that launches no wave in the sub-volume, so the
  time-step limit of piecewise-constant DEM is kept (§4.3, Fig. 8);
- the downwind exchange term reduces to $(\delta^C_{kl}-\delta^L_{kl})b_{kl}$,
  independent of the downwind sub-volume (Eq. 31).

Reverse fluxes handle non-monotone reconstructions, where
$\delta^L_{kl}>\delta^C_{kl}$ or the in-cell gradient opposes the
cell-centre jump (Eqs. 32–34), and Eqs. (35)–(39) combine both flow
directions. The authors call the uniform transfer "the most essential
part of our method and … sufficient for most of the occurring interface
configurations" (§4.1).

**Arbitrary number of phases** (§4.2, Appendix A). With the jumps
$\Delta^K_k$ ($K=L,C,R$), their total $\Delta^K_{\mathrm{tot}}=\tfrac12\sum_k\lvert\Delta^K_k\rvert$
and the positive and negative parts $\delta^K_{k\bullet}$,
$\delta^K_{\bullet l}$, the pairwise contacts are products,
$\delta^K_{kl}=\delta^K_{k\bullet}\delta^K_{\bullet l}/\Delta^K_{\mathrm{tot}}$
(Eqs. 40–43; page-local). Phases other than the two of a channel are
**passive**: the pseudo-Riemann flux advects them without affecting the
Riemann solution (Eqs. 44–49). This general construction differs from the
physics-based prioritization of Chinnayya et al. (§4.2).

## Volume-fraction reconstruction and positivity

RDEMIC itself does not prevent a loss of positivity when the volume taken
from the upwind cell exceeds its content, and the CFL condition does not
control this (§4.3). Paula et al. reconstruct the volume fraction with a
genuinely multi-dimensional [THINC](/methods/thinc-reconstruction.md)
profile $u^{\mathrm T}$ of steepness $\beta_{\mathrm T}=3$ (linear surface
function, two-point Gauss quadrature, a Newton solve with the shift of
Kumar et al., normals from a THINC-inverted distance field; §5.1,
Appendices B and D), and **time-average** it over its translation by
$v_{\mathrm I}$ during each Runge–Kutta stage:

$$\tilde u^{\mathrm T}(x)=\frac1{\Delta t}\int_{t_a}^{t_b}u^{\mathrm T}(x-v_{\mathrm I}t)\,dt,\qquad [t_a,t_b]=[0,\Delta t],\ [-\Delta t,0],\ [-\tfrac12\Delta t,\tfrac12\Delta t]$$

for the three stages of [SSP-RK3](/methods/ssp-runge-kutta.md)
(Eqs. 56–58), the windows following from writing the second stage as a
prediction at $t^{n+1/2}$ (Eq. 57); $v_{\mathrm I}$ is the mass-weighted
mixture velocity (Eq. 59), and the time integral is a three-point
Gauss–Lobatto sum (Appendix C). This anticipates the advection of the
interface and prevents over-estimated volume fluxes. To the authors'
knowledge, time averaging of THINC had not been used with multi-stage
integration or for compressible flow (§5.2). The paper calls the result
"positivity-preserving"; no theorem is proved (see Qualifications).

The remaining variables are reconstructed by WENO3 on characteristic
projections of the primitive variables, with [HLLC](/methods/hll-riemann-solvers.md)
and Davis wave speeds in every channel, block-based multiresolution with
local time stepping in the ALPACA code
([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)), a
volume-fraction cut-off of $10^{-9}$, and CFL 0.5 (§6).

## Evidence

| Test (§7) | Result |
|---|---|
| [interface advection](/benchmarks/material-interface-advection.md), uniform $p$, $v$; 1D two phases, 2D two and five phases | maximum relative velocity and pressure errors $9.4\times10^{-15}$ / $4.7\times10^{-15}$ (1D), $1.1\times10^{-14}$ / $2.3\times10^{-15}$ (2D, two), $1.2\times10^{-14}$ / $8.4\times10^{-15}$ (2D, five); volume errors $5.4\times10^{-15}$, $1.1\times10^{-8}$, $3.3\times10^{-9}$ (Table 1) |
| five-phase advection | triple points with initial angle ratio 2:1:1 are distorted; the quadruple point with equal angles is not (Fig. 10c) |
| smooth profiles, 128–2048 cells | first-order scheme first order; "nominally third-order WENO3" second order; errors with and without a THINC interface about equal (Fig. 12) |
| weak water shock through a water–air interface, $\beta_{\mathrm T}\in\{0.325,1,3\}$ | interface and shock positions match theory without oscillations for every $\beta_{\mathrm T}$, "in contrast to" the cited reference; small deviations only at 0.325 (Figs. 13–14; [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)) |
| 1 TPa water–air shock tube | agrees with the reference and the exact solution at density ratio 100, also runs at 1000, CFL 0.4 (Fig. 15) |
| spherical [underwater explosion](/benchmarks/underwater-explosion.md) | minimum bubble radius about 0.422 m at about 0.196 s, converging from above like the sharp-interface reference (Fig. 16) |
| three-material [triple point](/benchmarks/triple-point-problem.md), $3584\times1536$ | agrees with Pan et al.; CFL lowered to 0.15 (Fig. 18) |
| [shock–bubble](/benchmarks/shock-bubble-interaction.md), He and R22, Mach 1.22, $8192\times1024$ | agrees with the experiment and numerical references; late downstream jet faster than the experiment, attributed to the missing viscosity (Fig. 22) |
| air bubble collapsing in water, Mach 1.715 | HLLC develops shock instabilities in the Mach > 2 gas inside the bubble; HLLC-LM in the air–air channels only removes them (Fig. 26; [carbuncle](/definitions/carbuncle-phenomenon.md)) |

The last test shows that DEM can use a different Riemann solver in each
kind of channel (§7.7).

## Qualifications

- "Positivity-preserving" is a design claim. THINC is symmetric only
  for two phases, so with more phases the face values are normalized to
  $\sum_k\phi_k=1$, which can defeat the time averaging; the triple-point
  run needed CFL 0.15 (§6, §7.5). Proved results are on the
  [bound-preservation](/properties/bound-preservation.md) page.
- Fluxes are computed dimension by dimension and not integrated over the
  faces, so the lateral order is two; "high-resolution" in the title
  does not mean high order (§6).
- The $10^{-9}$ volume-fraction cut-off, with rescaling of the remaining
  phases, introduces a conservation error that the authors call
  negligible and do not quantify (§6).
- The interface-position diagnostic of Eq. (66) omits the normal sign
  $n_i$ of the THINC profile, Eq. (51); with the interface at
  $x=x_i-d_i\Delta x/n_i$ it holds as printed only for $n_i=+1$
  *(compiler check, not in the sources)*.

# Citations

- [Paula, Adami & Adams (2023)](/sources/paula-2023.md) — §2.1–2.2, Eqs. (1)–(10); §3.1–3.2, Eqs. (11)–(22), Fig. 3; §4.1–4.3, Eqs. (23)–(50), Fig. 8; §5.1–5.2, Eqs. (51)–(59); §6; §7.1–7.7, Tables 1–4, Figs. 10–26; Appendices A–D.
