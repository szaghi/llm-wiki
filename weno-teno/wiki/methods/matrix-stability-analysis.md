---
type: Method
title: "Matrix stability analysis of shock-capturing schemes"
description: "Matrix stability analysis linearizes a semi-discrete shock-capturing scheme about a steady shocked state, assembles the stability matrix of the perturbations and declares the scheme stable when no eigenvalue has positive real part; the page gives the first-order and fifth-order WENO versions, their validation, and the saw-tooth analysis used beside it."
status: established
aliases: [matrix stability method, Dumbser–Moschetta–Gressier analysis, linear stability analysis of shock instability, shock-instability eigenvalue analysis, saw-tooth perturbation analysis]
tags: [riemann-solver, finite-volume, weno, numerical-flux, carbuncle, stability-analysis]
timestamp: 2026-10-23T20:39:00Z
---

# Matrix stability analysis of shock-capturing schemes

**Matrix stability analysis** tests whether a shock-capturing scheme amplifies small
perturbations of a steady discrete shock, the mechanism behind the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md). The semi-discrete finite-volume
scheme on a uniform Cartesian grid is linearized about a steady mean state $\bar u_{i,j}$,
$u_{i,j}=\bar u_{i,j}+\delta u_{i,j}$; collecting all perturbations in one vector
$\delta\mathbf U$ gives the linear time-invariant system

$$\frac{d}{dt}\delta\mathbf U=\mathbf S\,\delta\mathbf U,\qquad \delta\mathbf U(t)=e^{\mathbf St}\delta\mathbf U(0),$$

and the scheme is called stable iff $\max\mathrm{Re}\,\lambda(\mathbf S)\le0$ (page-local
$\mathbf S$, the stability matrix; [Ren et al. (2025)](/sources/ren-2025.md), §3.1, Eqs. (29)–(31);
[Hu et al. (2022)](/sources/hu-2022.md), §3.2, Eqs. (3.13)–(3.16)). Both sources take the method
from Dumbser, Moschetta and Gressier, as they recall it. Because the system is semi-discrete,
the verdict does not depend on the CFL number: Hu et al. call the instability of HLLEM found
this way "unconditional" (§3.2).

## First-order version

With first-order fluxes the interface states are the cell values,
$u^-_{i+1/2,j}=u_{i,j}$ and $u^+_{i+1/2,j}=u_{i+1,j}$, so linearizing each two-point flux
$h(u^-,u^+)$ gives

$$\delta\hat f_{i+1/2,j}=\frac{\partial h}{\partial u^-}\,\delta u_{i,j}+\frac{\partial h}{\partial u^+}\,\delta u_{i+1,j},$$

the Jacobians evaluated at the mean states, and the perturbation of cell $(i,j)$ couples to its
four neighbours, a five-point stencil (Ren et al., §2, Eqs. (19)–(23); the face lengths over the
cell area enter as weights). Ren et al. stress that this form assumes first-order interface
states and so holds only for first-order schemes (§3.1).

**Setup of Hu et al. (2022)** (§3.2). An isolated steady shock at Mach 8 on $[0,1]^2$,
$30\times30$ cells, between columns 15 and 16, upstream and downstream states from the
[Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md) conditions, with random relative
noise $10^{-8}$ for the time-marching check. HLLE has no eigenvalue with positive real part and
damps the noise; HLLEM has such eigenvalues and does not (Figs. 3.1–3.2); their shock-stable
RHLLEM gives $\max\mathrm{Re}\,\lambda(\mathbf S)=-0.6963$ (Fig. 4.2;
[HLL-family solvers](/methods/hll-riemann-solvers.md)).

## Fifth-order WENO version

[Ren et al. (2025)](/sources/ren-2025.md) (§3.1, Eqs. (24)–(28)) extend the analysis to
fifth-order finite-volume [WENO-Z](/methods/weno-z.md). The key assumption is that the
perturbations do not change the nonlinear weights: with the weights frozen at their mean-state
values, collected per conserved variable in diagonal matrices
$\boldsymbol\omega_k=\mathrm{diag}(\omega_{k,\rho},\omega_{k,\rho v_1},\omega_{k,\rho v_2},\omega_{k,E})$
(page-local) for the candidate stencils $S_0$ (most upwind), $S_1$, $S_2$, the reconstructed
left state is a fixed linear combination,

$$\delta u^-_{i+1/2}=\tfrac13\boldsymbol\omega_0\,\delta u_{i-2}-\tfrac16\big(7\boldsymbol\omega_0+\boldsymbol\omega_1\big)\delta u_{i-1}+\tfrac16\big(11\boldsymbol\omega_0+5\boldsymbol\omega_1+2\boldsymbol\omega_2\big)\delta u_i+\tfrac16\big(2\boldsymbol\omega_1+5\boldsymbol\omega_2\big)\delta u_{i+1}-\tfrac16\boldsymbol\omega_2\,\delta u_{i+2},$$

and its mirror image over $i-1,\dots,i+3$ for $\delta u^+_{i+1/2}$ (Eq. (24); $j$ suppressed).
*(compiler check, not in the sources: the coefficients are those of the three third-order
candidate values of WENO5 summed with the weights.)* The linearized flux at $x_{i+1/2}$ then
depends on the six cells $i-2,\dots,i+3$ (Eqs. (25)–(26)), and the perturbation of cell $(i,j)$
couples to 13 cells, a cross of half-width 3, with mid-point integration of the face flux, and
to 45 cells with two Gauss points per face, where the transverse reconstruction of the Gauss-point
values inside each cell enters as well and the face weight is halved (§3.4, App. C,
Eqs. (C.7)–(C.13)). The same model is written for primitive variables, premultiplied by the
inverse of $\partial u/\partial(\rho,v,p)$ (App. A), and for characteristic variables $Lu$ with
the left-eigenvector matrix of the face (App. B;
[characteristic decomposition](/methods/characteristic-decomposition.md)).

**Smoothing the flux.** The Jacobians must exist at the mean state. Ren et al. smooth the absolute
eigenvalues of the Roe-averaged system, $\lvert\lambda\rvert\to(\lambda^2+\delta_0^2)/(2\delta_0)$ for
$\lvert\lambda\rvert<\delta_0=10^{-4}$, after Shen, Yan and Yuan (Eqs. (32)–(33)), and state that the
Roe flux is differentiable when the shock does not sit exactly between two cells (§3.3).

**Mean flow.** A 1D steady solution with one intermediate state on the Hugoniot curve,
projected to 2D and perturbed by $10^{-7}$; its position $\varepsilon_{\mathrm s}\in[0,1]$
(page-local, as on the carbuncle page) moves the intermediate state from upstream to downstream
([steady shock problems](/benchmarks/steady-shock-problems.md)). When the 1D computation is itself
unstable, Roe and HLLC use Xie et al.'s mass-flux consistency fix across the shock, and HLL and
van Leer, whose shocks have more than one interior point, the 1D solution of the second-order
scheme (§3.2, Eq. (37)).

**Validation** (§3.3). The time-marching diagnostic is $\lVert v_2\rVert_\infty(t)$, which vanishes
on the mean flow; after an initial transient it grows as $e^{\lambda_{\mathrm{num}}t}$ (page-local
$\lambda_{\mathrm{num}}$) before the nonlinear stage (Eq. (38); third-order TVD Runge–Kutta, CFL 0.1).
On the $11\times11$, Mach-20, fifth-order Roe case at $\varepsilon_{\mathrm s}=0$ the measured
$\lambda_{\mathrm{num}}=2.17904$ against the predicted 2.65580 without smoothing (error 21.88%) and
2.19187 with it (0.59%) (Table 1). Over $\varepsilon_{\mathrm s}\in\{0,0.1,\dots,0.9,0.99\}$ prediction
and measurement agree in the stable and unstable ranges (Fig. 6; agreement for other solvers is
stated, not shown). Mid-point and two-point Gauss integration give identical verdicts for Roe
(stable only at $\varepsilon_{\mathrm s}=0.8,0.9$) and HLL (only at $0.6,0.7$) (Table 2, Fig. 8), which
the authors use to justify the cheaper 13-cell model, the Gauss-point reconstruction meeting the
same discontinuous stencils (§3.4, §4.1.3).

## Diagnostic devices

- **Directional hybrids.** Hu et al. combine HLLEM on the streamwise faces with HLLE, or HLLE
  plus only the entropy-wave or only the shear-wave anti-diffusion, on the transverse ones, and
  find that both anti-diffusion terms must be controlled (Figs. 3.3–3.4). Ren et al.'s hybrid-1
  (fifth-order Roe on transverse faces, first-order van Leer on normal faces) and hybrid-2 (the
  reverse) are both unstable, so at fifth order the normal faces need dissipation too (Eq. (40),
  Figs. 24–26, §4.2).
- **Freezing the reconstruction locally.** Replacing the WENO weights by the ENO choice of the
  smoothest quadratic on the faces near the shock keeps $\max\mathrm{Re}\,\lambda>0$, a constant
  reconstruction there makes it negative (Ren et al., Figs. 21–22).
- **Eigenvectors.** The most unstable mode ($\lambda=0.67356$, real; Roe, Mach 20,
  $\varepsilon_{\mathrm s}=0.1$) has a saw-tooth distribution at the intermediate cell (Fig. 27),
  which the time history confirms as the origin of the perturbation (§4.3).
- **Design check.** Ren et al. verify their MR-WENO-SD with the HLLC/HLL hybrid flux by the same
  analysis: all eigenvalues on a $50\times25$ normal shock have negative real part (§5.2.2,
  Fig. 35; [multi-resolution WENO](/methods/multi-resolution-weno.md)).

The findings themselves (which solvers fail at which order, and why) are on the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md) page.

## The saw-tooth perturbation analysis beside it

Hu et al. (§3.1, Eqs. (3.1)–(3.12)) use a second, local tool after Quirk, extended to perturb both
directions: a **uniform** mean state $(\rho_0,v_{1,0},0,p_0)$ with sound speed $c_0$ (page-local)
carries a perturbation alternating in sign from cell to cell, and one forward-Euler step of the
first-order scheme gives an amplification matrix for $(\delta\rho,\delta v_1,\delta v_2,\delta p)$.
For a supersonic mean flow its eigenvalues are $1-2\sigma_xv_{1,0}$ (twice) and
$1-2\sigma_x(v_{1,0}\pm c_0)$, $\sigma_x=\Delta t/\Delta x$, stable for $\sigma_x<1/(v_{1,0}+c_0)$ (Eqs.
(3.3)–(3.4)); transverse perturbations under HLLEM keep amplification factor 1 for density and
shear velocity at every time step (Eq. (3.12)). The two analyses differ in mean state (uniform
against shocked), perturbation (saw-tooth against random) and locality, and Hu et al. require a
shock-stable scheme to pass both (§3.3); the saw-tooth analysis is also fully discrete, the
matrix analysis semi-discrete.

## Related spectra of semi-discrete operators

The same eigenvalue criterion decides the linear stability of a semi-discrete method on smooth
data. [Barsukow et al. (2026)](/sources/barsukow-2026.md) (§4.1–4.2, Eqs. (37)–(42); arXiv v2)
compute the spectrum of their arbitrary-order 2D [Active Flux](/methods/active-flux.md)
operator for linear advection on periodic grids of up to $10\times10$ cells, taking
$\mathrm{Re}\,\lambda\le0$ as necessary and as sufficient when the eigenvalues on the imaginary
axis are semisimple; Gauss–Legendre edge points pass for orders 3–7, uniform and
Gauss–Lobatto ones fail for orders 4–7 (at order 3 the single edge point is the midpoint for
all three), and the
diagonalization then gives the maximal SSP-RK3 time steps
([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## Qualifications

- **Frozen weights.** Ren et al.'s fifth-order model is that of a fixed linear combination of
  candidate stencils; the dependence of the WENO weights on the perturbation is not linearized
  (§3.1).
- **Mid-point rule.** The analysed scheme uses mid-point face integration, which the authors,
  citing Zhang, Zhang and Shu, call second-order accurate for nonlinear smooth problems; the
  transfer of the verdicts to the Gauss-point scheme rests on the agreement of Table 2 on one
  problem.
- **Variables.** Ren et al. present the reconstruction and the analysis in conservative variables
  (§2.2, §3.1) but state in §4.4 that §§4.1–4.3 reconstruct primitive variables; which form the
  main results use is not settled by the text.
- **Necessary, not sufficient.** *(compiler check, not in the sources: if $\mathbf S$ has a
  defective eigenvalue on the imaginary axis, $e^{\mathbf St}$ grows polynomially although
  $\max\mathrm{Re}\,\lambda(\mathbf S)\le0$; the criterion as stated by Ren et al. and Hu et al. is
  therefore sufficient for boundedness only with the semisimplicity condition that Barsukow et
  al. state for their spectra.)*
- Ren et al.'s Eq. (27) and its appendix analogues drop the $\delta$ on the outermost terms, and
  App. C mixes indices ($j+3$ against $j+2$ in Eqs. (C.11)–(C.12)); the structure stated above
  follows Eqs. (24)–(26).

# Citations

- [Ren et al. (2025)](/sources/ren-2025.md) — §2 (Eqs. (19)–(23)), §3.1–3.4 (Eqs. (24)–(38), Tables 1–2, Figs. 6, 8), §4.1.3, §4.2 (Eq. (40)), §4.3–4.4, §5.2.2, Apps. A–C.
- [Hu et al. (2022)](/sources/hu-2022.md) — §3.1 (Eqs. (3.1)–(3.12)), §3.2 (Eqs. (3.13)–(3.16), Figs. 3.1–3.4), §3.3, Fig. 4.2.
- [Barsukow et al. (2026)](/sources/barsukow-2026.md) — §4.1–4.2 (Eqs. (37)–(42)) (arXiv v2).
