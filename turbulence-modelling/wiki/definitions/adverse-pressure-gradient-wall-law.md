---
type: Definition
title: "Wall law in adverse pressure gradient"
description: "The inner-layer mean-velocity law of adverse-pressure-gradient turbulent boundary layers: a log law whose extent shrinks with the inner-scaled pressure-gradient parameter, a half-power law above it, the correlations calibrating both edges in Reynolds number and pressure gradient, and their use for RANS models and wall functions."
status: established
aliases: [APG wall law, log-law/half-power-law wall law, extended wall law, half-power law, pressure-gradient wall law]
tags: [boundary-layer, rans, wall-model, separated-flow]
timestamp: 2026-10-25T19:43:00Z
---

# Wall law in adverse pressure gradient

In a turbulent boundary layer under an adverse pressure gradient (APG) the
inner-layer mean velocity is no longer described by the
[law of the wall](/definitions/law-of-the-wall.md) alone. [Knopp (2022)](/sources/knopp-2022.md)
builds an empirical wall law for two-dimensional, incompressible, smooth-wall
APG boundary layers: a logarithmic layer, $u^+=\kappa^{-1}\ln y^++B$, between
$y^+_{\log,\min}$ and $y^+_{\log,\max}$; an intermediate region described by
neither law; and above it a "half-power" (extended) wall law that reaches the
outer edge of the inner layer (Eq. 12). The pressure gradient enters through
the inner-scaled parameter

$$\Delta p_s^+=\frac{\nu}{\rho u_\tau^3}\frac{dP}{ds}\qquad\text{(Eq. 2)},$$

with $P$ the mean pressure and $s$ the wall-tangential coordinate along the
mean velocity as $y\to0$ (page-local symbols $\Delta p_s^+$, $s$). The law is
aimed at RANS turbulence models and wall functions; the paper itself is an
analysis of experimental mean-velocity profiles at $Re_\theta>8000$ and
implements no model.

## Structure of the law

Knopp (2022, §2.3, Eqs. 12–14) fixes $\kappa=0.41$ in the log law and writes
the upper law as the extended wall law of Szablewski, Townsend and Afzal, as
the author recalls them, asymptotic to the log law for small and to a
square-root law for large pressure gradient:

$$u^+=\frac1K\left[2\left(\sqrt{1+\alpha^+y^+}-1\right)+\ln y^++2\ln\frac{2}{\sqrt{1+\alpha^+y^+}+1}\right]+B_o ,$$

with slope coefficient $K$, additive constant $B_o$ (value not printed) and
effective pressure gradient $\alpha^+=\lambda_M\Delta p_s^+$ (page-local
symbols $K$, $B_o$, $\alpha^+$, $\lambda_M$). The linear total-stress
approximation behind $\alpha^+$ is McDonald's, $\tau/\tau_w=1+\alpha^+y^+$
with $\lambda_M<1$ (Eq. 10); in all fits Knopp sets $\alpha^+=\Delta p_s^+$
(§6.4). Stratford's zero-skin-friction form
$\langle u\rangle=(2/K)\left(\rho^{-1}dP/ds\right)^{1/2}y^{1/2}+\text{const}$
(Eq. 15) is the separation limit. "Half-power law" is used loosely for the
extended law.

The local model behind it (§2.2, Eqs. 6–8): with the ansatz
$\langle u\rangle(s,y)=u_\tau(s)f(y^+)$ and the Reynolds-normal-stress term
neglected, the total shear stress is

$$\frac{\tau}{\tau_w}=1+\Delta p_s^+y^++\Delta u^+_{\tau,s}\int_0^{y^+}f^2\,d\tilde y^+,\qquad \Delta u^+_{\tau,s}=\frac{\nu}{u_\tau^2}\frac{du_\tau}{ds},$$

so $\Delta p_s^+$ is the leading-order parameter, the wall-shear-stress
gradient $\Delta u^+_{\tau,s}$ second order, and a parameter involving
$d^2P/ds^2$ of higher order (§7.1; page-local $\Delta u^+_{\tau,s}$).

## Calibrated correlations

The log law is robust in APG for every flow of the database, but it is
thinner than its zero-pressure-gradient counterpart at the same $Re_\tau$ and
does not reach $y=0.15\delta$; its extent relative to $\delta$ decreases as
$\Delta p_s^+$ grows (§5.1–5.2). Quantitatively $y_{\log,\max}/\delta<0.11$ for
$\Delta p_s^+>0.005$ and $\beta_{RC}>4.5$, and below 0.08 for $\Delta p_s^+>0.015$
and $\beta_{RC}>12$ ($\beta_{RC}$ the Rotta–Clauser parameter, below); it reaches
$0.15\delta$ only in the mild-APG equilibrium flows of Bradshaw and Clauser.

A similarity argument with the reduced Hartree parameter
$\Delta p_s^+Re_\tau^2$ and the $Re_\tau$ exponent that minimizes the spread
of the data ($y^+_{\log,\max}\sim Re_\tau^{1/2}$) gives an exponent $-1/4$ in
$\Delta p_s^+$; a scaling argument with Nickels' velocity scale gives $-1/6$
(Eqs. 27–34). The data fix (§6.2–6.4)

$$y^+_{\log,\max}=1.78\,Re_\tau^{1/2}(\Delta p_s^+)^{-1/5}\quad\text{(Eq. 35)},\qquad y^+_{\mathrm{sqrt},\min}=4.05\,Re_\tau^{1/2}(\Delta p_s^+)^{-0.13}\quad\text{(Eq. 36)},$$

and $K=0.45\pm0.15$, in agreement with the literature values Knopp recalls
(0.41–0.51 from Townsend, Perry and Szablewski; 0.447 and 0.57 from Kader &
Yaglom and Afzal for large pressure gradient), which depend on the form of the
law and the fit region (§6.4). Low-Reynolds
data (Nagano et al., $481\le Re_\tau\le639$; the DNS of Coleman et al.,
$Re_\tau$ up to 880) agree with the high-$Re$ correlation, and §7.3 suggests
lowering the constant of Eq. (35) from 1.78 to 1.68. The correlation changes
the author's own earlier one (Knopp 2016) after a revised analysis of the
database.

At $\Delta p_s^+=0.05$, Eq. (35) gives $y^+_{\log,\max}=3.24\,Re_\tau^{1/2}$:
the log law ends at $y^+=92$ for $Re_\tau=800$ and about 162 for
$Re_\tau=2500$; Knopp (§7.4) notes that this edge lies below "the widely
believed start of the log-law region in ZPG flows" (citing Marusic et al.)
and reads it as agreeing with the log-law breakdown at $\Delta p_s^+>0.05$ of
Alving & Fernholz, as recalled.

## Pressure-gradient parameters

Knopp (2022, §2.4–2.5) contrasts $\Delta p_s^+$ with the Rotta–Clauser parameter
$\beta_{RC}=(\delta^*/\tau_w)\,dP/ds$ and the Hartree parameter (page-local),
related by $\beta_H=-\Delta p_s^+Re_\tau^2(u_\tau/U_e)$ (Eq. 25). All
degenerate as $u_\tau\to0$; Nickels' modified velocity scale stays finite at
separation ($u_T\to Re_c^{1/3}u_p$, $Re_c=12$, $u_p=|\nu\rho^{-1}dP/ds|^{1/3}$,
Eqs. 17–20; page-local). Because Eq. (35) depends on $Re_\tau$ as well as on
the pressure gradient, inner-layer self-similarity cannot be expected at
equal $\beta_{RC}$ alone, in agreement with Bobke et al. and Vila et al. as
recalled (§8).

## Equilibrium and history

No systematic dependence of the edges or of $K$ on $\Delta u^+_{\tau,s}$ or
the second-order pressure parameter is found, and equilibrium and
streamwise-evolving flows cannot be told apart beyond slightly larger
$y^+_{\log,\max}/Re_\tau^{1/2}$ for mild equilibrium flows (§7.2). History
effects are visible: the DLR/UniBw flows, with upstream convex curvature and a
favourable-to-adverse gradient, give low $y^+_{\log,\max}/Re_\tau^{1/2}$ and $K$.
An eddy-turnover estimate (Eq. 37) gives relaxation distances of about
$\delta$ at $y/\delta=0.1$ and $2\delta$ at $0.2$ for
$\Delta p_s^+\gtrsim0.004$: the inner layer relaxes rapidly but not
instantaneously, so history matters more in the half-power region than in the
log region (§7.1). The author's conjecture is a local wall law governed at
leading order by $\Delta p_s^+$ and $Re_\tau$ (the moving equilibrium of Kader
& Yaglom, as recalled), perturbed by higher-order local and history effects.

## Use in models

Knopp (2022, §1) recalls a preliminary RANS modification (Knopp 2016): an
augmentation term in the $\omega$ equation of $k$-$\omega$-type models,
designed to reproduce the half-power solution and activated only in that
region by a blending function built from these correlations; no equations are
given in the source (see [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
for the baseline). The correlation is also offered as an initial guess of the
fit range for the Clauser-chart method (§8).

For wall-stress models, matching heights of order $0.1\delta$ are in use:
$0.1\delta_0$ ($\delta_0=4$ mm the reference boundary-layer thickness) in
[Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md), and $2\Delta y=0.1\delta$
on the $\Delta y=0.05\delta$ channel grids of [Bae & Koumoutsakos (2022)](/sources/bae-2022.md)
(their Table 1 gives $h^+_{\mathrm{wm}}=2Re_\tau\Delta y/\delta$ in every row)
*(compiler check, not in the sources)*. By Knopp's printed bound (§5.2) a
height of $0.1\delta$ lies above the log law for $\Delta p_s^+>0.015$ and
$\beta_{RC}>12$; by Eq. (35) it lies above $y_{\log,\max}$ when
$\Delta p_s^+>(17.8)^5Re_\tau^{-5/2}\approx1.79\times10^6\,Re_\tau^{-5/2}$, i.e.
about 0.057 at $Re_\tau=1000$, 0.0057 at 2500 and 0.0018 at 4000 (0.042,
0.0043 and 0.0013 with the constant 1.68) *(compiler check, not in the
sources)*. [Gillyns et al. (2022)](/sources/gillyns-2022.md)
(§1) state the related limit that their algebraic model is usable in APG only
while Coles' wake has not reached the top of the first element. See the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and the
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md) benchmark
page for the APG database.

## Qualifications

- The constant of Eq. (35) appears twice in the paper: 1.78 (Eq. 35, used in
  §7.4) and the suggested 1.68 (§7.3). With 1.68 the §7.4 values become
  about 87 and 153 *(compiler check, not in the sources)*.
- Knopp's Fig. 7 caption gives $\Delta p_s^+=7.17\times10^{-3}$ and
  $7.89\times10^{-3}$ for the Marusic & Perry and Perry profiles where §5.1
  gives $7.55\times10^{-3}$ and $7.85\times10^{-3}$; Eq. (9) writes subscript
  $x$ where the rest of the paper uses $s$.
- The variation of $\kappa$ and $B$ with pressure gradient is deliberately
  not studied: $\kappa=0.41$ is fixed, because inferred $\kappa$ is sensitive
  to the accuracy of $u_\tau$ (fitted $\kappa=0.312$–0.379 for the DLR/UniBw
  flow, App. B).
- The database is wind-tunnel mean-velocity profiles; few reach
  $\Delta p_s^+>0.02$ or $Re_\theta>30\,000$.

# Citations

- [Knopp (2022)](/sources/knopp-2022.md) — §1; §2.1–2.5, Eqs. (2)–(25); §5.1–5.2, Figs. 4–9; §6.1–6.5, Eqs. (27)–(36); §7.1–7.4, Eq. (37); §8; App. B.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §1.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Methods (training and testing).
