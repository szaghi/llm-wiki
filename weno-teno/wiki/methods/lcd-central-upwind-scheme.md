---
type: Method
title: "LCD central-upwind scheme"
description: "Chertock et al. replace the scalar diffusion coefficients of the central-upwind flux by field-wise ones built from the one-sided characteristic speeds, in a local characteristic decomposition; the scheme becomes exactly upwind for every linear system and resolves contacts and instabilities more sharply; Chu et al. (2025b) extend it to non-conservative balance laws through flux globalization."
status: established
aliases: [local characteristic decomposition based central-upwind scheme, New CU, LCD-based CU scheme]
tags: [central-scheme, characteristic, numerical-flux, finite-volume, low-dissipation]
timestamp: 2026-10-23T15:15:00Z
---

# LCD central-upwind scheme

The local-characteristic-decomposition (LCD) based central-upwind scheme of
[Chertock et al. (2023)](/sources/chertock-2023.md) keeps the
[central-upwind](/methods/central-upwind-scheme.md) structure — a central average of
cell-average fluxes plus a numerical diffusion built from one-sided speeds, no Riemann solver —
but gives each characteristic field its own diffusion. The base CU diffusion uses the same
scalar function of the extreme speeds $a^\pm_{i+1/2}$ for every field; the LCD version uses,
for field $l$, the one-sided speeds of that field.

## Definition

With $R=R_{i+1/2}$ and $L=R^{-1}$ the eigenvector matrices of $A$ at an averaged state
$\hat u_{i+1/2}$ (an arithmetic average of primitive variables for Euler, Apps. A–B), and
$\bar\zeta_k=L\,\bar u_k$, $\zeta^\pm_{i+1/2}=L\,u^\pm_{i+1/2}$ the local characteristic variables
(page-local symbols), the scheme is (§3, Eqs. (3.5)–(3.8), translated)

$$\frac{d}{dt}\bar u_i=-\frac{\hat f_{i+1/2}-\hat f_{i-1/2}}{\Delta x},\qquad \hat f_{i+1/2}=\tfrac12\big(f(\bar u_i)+f(\bar u_{i+1})\big)+\mathcal D^{\mathrm{LCD}}_{i+1/2},$$

$$\mathcal D^{\mathrm{LCD}}_{i+1/2}=R\mathcal P R^{-1}\Big[f(u^-_{i+1/2})-\bar f_{i+1/2}\Big]+R\mathcal M R^{-1}\Big[f(u^+_{i+1/2})-\bar f_{i+1/2}\Big]+R\mathcal Q\big(\zeta^+_{i+1/2}-\zeta^-_{i+1/2}\big),$$

$\bar f_{i+1/2}=\tfrac12\big(f(\bar u_i)+f(\bar u_{i+1})\big)$, with diagonal $\mathcal P,\mathcal M,\mathcal Q$
(page-local) whose $l$-th entries are

$$\big(\mathcal P_l,\mathcal M_l,\mathcal Q_l\big)=\begin{cases}\dfrac{\big(\lambda^+_l,\,-\lambda^-_l,\,\lambda^+_l\lambda^-_l\big)}{\lambda^+_l-\lambda^-_l}, & \lambda^+_l-\lambda^-_l>\epsilon_{\mathrm{CU}},\\ 0,&\text{otherwise},\end{cases}$$

$$\lambda^+_l=\max\big\{\lambda_l(A(u^-_{i+1/2})),\lambda_l(A(u^+_{i+1/2})),0\big\},\qquad \lambda^-_l=\min\big\{\lambda_l(A(u^-_{i+1/2})),\lambda_l(A(u^+_{i+1/2})),0\big\},$$

all at $x_{i+1/2}$ ($\lambda^\pm_l$ and $\epsilon_{\mathrm{CU}}=10^{-10}$ page-local). With
$\lambda^+_l=a^+$, $\lambda^-_l=a^-$ for all $l$ this is the original CU flux. The eigenvalues
are evaluated at the reconstructed states while $R$ diagonalizes $A(\hat u_{i+1/2})$, a
different state. The construction requires a diagonalizable Jacobian with real eigenvalues
(strict hyperbolicity is stated, §2.1).

The reconstruction is the second-order piecewise linear one with the generalized minmod
limiter applied to $\bar\zeta_{i-1},\dots,\bar\zeta_{i+2}$, all projected with the same
interface matrix (Eqs. (2.5)–(2.8)); see
[characteristic decomposition](/methods/characteristic-decomposition.md). In 2D the scheme is
applied dimension by dimension with the $y$-Jacobian's eigen-system at $x_{i,j+1/2}$ (§4).

## Lemma 3.1: exact upwinding for linear systems

For $f(u)=Au$ with $A$ constant, the scheme becomes the second-order semi-discrete upwind
scheme

$$\hat f_{i+1/2}=A^+u^-_{i+1/2}+A^-u^+_{i+1/2},\qquad A^\pm=R\,\mathrm{diag}\big(\max/\min\{\lambda_l,0\}\big)L,$$

*whatever* the signs of the eigenvalues (Lemma 3.1, Eqs. (3.9)–(3.12)). In the linear case
$\mathcal Q\equiv0$, since $\max\{\lambda_l,0\}\min\{\lambda_l,0\}=0$. The original CU scheme
reduces to upwind only when all eigenvalues share one sign (§1), which is the sense in which
the new scheme "has more built-in upwinding" (§3). A field with $\lambda_l=0$ gets zero
diffusion through the $\epsilon_{\mathrm{CU}}$ branch (*compiler check, not in the sources:*
$\lambda^+_l-\lambda^-_l=0$ then, and the upwind flux carries no contribution of that field,
consistent with Lemma 3.1).

## Numerical evidence

All tests: Euler, $\gamma=1.4$ (Examples 1–8) or $5/3$ (Example 9), CFL 0.4, SSP-RK3, New
CU versus the CU scheme of Kurganov–Noelle–Petrova in 1D and of Kurganov–Tadmor in 2D (§5).

- [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) (1D, $\Delta x=1/100$):
  sharper, less oscillatory; the old scheme oscillates at the contact (Ex. 1).
- [Shu–Osher](/benchmarks/shu-osher-problem.md) ($\Delta x=1/80$): "substantially more
  accurate" in the oscillatory region (Ex. 2).
- A stationary contact with travelling shock and rarefaction, $(\rho,v,p)=(1,-19.59745,1000)$
  / $(1,-19.59745,0.01)$: both non-oscillatory, the contact better resolved (Ex. 3; see
  [stationary contact preservation](/properties/stationary-contact-preservation.md)).
- [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
  ($\Delta x=1/400$): slightly higher second density spike (Ex. 4).
- [2D Riemann configuration 3](/benchmarks/two-dimensional-riemann-problems.md),
  explosion, implosion, [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md),
  [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) (Exs. 5–9): richer
  instabilities. In the implosion problem the new scheme on $1/2000$ beats the old one on
  $1/2500$, which costs the same CPU time, and matches the old one on $3/10000$; no timings or
  hardware are given (Ex. 7).

## The modified scheme of Chu, Herty and Kurganov

[Chu et al. (2025b)](/sources/chu-2025-b.md) (§2) restate a slightly modified second-order
LCD-CU scheme. They write the flux without the central average,

$$\hat f_{i+1/2}=R\mathcal PL\,f(u^-_{i+1/2})+R\mathcal ML\,f(u^+_{i+1/2})+R\mathcal QL\big(u^+_{i+1/2}-u^-_{i+1/2}\big)\qquad\text{(Eq. (2.2))},$$

which they state is identical to Chertock et al.'s flux after the simplification
$\mathcal P+\mathcal M=I$ (Remark 2.1, Eq. (2.9)). They change two ingredients:

- **Desingularization** (Eq. (2.8), $\varepsilon_0=10^{-18}$ page-local): field-wise coefficients
  $(\lambda^+_l,-\lambda^-_l,\lambda^+_l\lambda^-_l)/(\lambda^+_l-\lambda^-_l)$ if
  $\lambda^+_l-\lambda^-_l>\varepsilon_0$; otherwise the scalar central-upwind coefficients
  $(a^+,-a^-,a^+a^-)/(a^+-a^-)$ if $a^+-a^->\varepsilon_0$; otherwise $(\tfrac12,\tfrac12,0)$. They
  call it "more robust" than the earlier strategy in their experiments, without showing the
  comparison (Remark 2.3).
- **Reconstruction variables**: piecewise linear in conservative variables with the generalized
  minmod limiter, parameter $1.3$, instead of characteristic variables; it caused no substantial
  spurious oscillations in any of their examples and is cheaper (Remark 2.2; no timing given).

*(compiler check, not in the sources: with every branch of (2.8) $\mathcal P_l+\mathcal M_l=1$,
so Eq. (2.2) equals the central-average form above with $\bar f_{i+1/2}$ cancelled. In Chertock et
al.'s zero branch $\mathcal P_l=\mathcal M_l=0$ instead, so for a field with
$\lambda^+_l=\lambda^-_l$ the two schemes differ: Chertock et al. give that field the central
average of the cell-average fluxes, Chu et al. (2025b) the average of the reconstructed-state fluxes, or the
scalar CU coefficients when $a^+>a^-$.)*

Chu et al. (2025b) then extend the scheme to non-conservative balance laws by applying it to the
flux-globalized system $\partial_tu+\partial_xK=0$, with $R$ and the field speeds taken from
$A+\mathcal C$, the flux Jacobian plus the matrix of the non-conservative product in this bundle's
sign, and with modified states
$\check u^\pm$ in the diffusion term: the **LCD-PCCU** scheme (§3–§4), written out on
[path-conservative schemes](/methods/path-conservative-scheme.md) and
[flux globalization](/methods/flux-globalization.md), and proved well-balanced in 1D on
[well-balancing](/properties/well-balancing.md). Its closed-form eigenvector matrices for the
two-fluid and the thermal rotating shallow-water systems are in their Appendices A–B (see
[characteristic decomposition](/methods/characteristic-decomposition.md)).

## Qualifications

- "More upwinding" is proved only for constant-coefficient linear systems; no positivity,
  entropy or stability analysis is given for the nonlinear scheme.
- On the variables of the reconstruction the sources differ in experience, not in a claim about
  the same setting: Chertock et al. reconstruct in characteristic variables because minmod
  (the generalized minmod with factor 2) on conservative variables "typically leads to large oscillations" (§2.1);
  Chu et al. (2025b) see no substantial oscillations with conservative variables and the
  parameter $1.3$ instead of $2$.
- Printed slips of the arXiv v2 (none changes the result): in the proof of Lemma 3.1 the
  matrix $\mathcal M$ is printed with the sign opposite to its definition (3.8) and
  the printed identity between $\mathcal M$ times the eigenvalue matrix and the negative
  eigenvalue part is off by a sign, though the conclusion (3.12) is
  correct; the $y$-direction diffusion in §4 carries a minus sign in front of the
  $\mathcal M$ term, inconsistent with (3.7).
- The averaged state for $R$ is an arithmetic average of primitive variables, not a Roe
  average (Apps. A–B); most WENO and TENO papers of this bundle use Roe averages.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — §1, §2.1 (Eqs. (2.5)–(2.8)), §3 (Eqs. (3.5)–(3.12), Lemma 3.1), §4, §5 (Exs. 1–9), Apps. A–B (arXiv v2).
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — §2 (Eqs. (2.2)–(2.9), Remarks 2.1–2.3), §3–§4, Apps. A–B.
