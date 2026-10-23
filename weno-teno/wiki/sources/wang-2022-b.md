---
type: Source
title: "Wang & Don (2022) — Affine-invariant WENO weights and operator"
description: "Makes WENO-Z, WENO-D and WENO-JS weights invariant under affine maps of the data by scaling the regularization with the stencil's mean absolute deviation, proves the affine-invariance theorem, and shows intrinsic well-balancing for shallow water without weight linearization."
resource: "doi:10.1016/j.apnum.2022.07.007"
source_kind: paper
authors: [Wang B.-S., Don W.S.]
year: 2022
venue: "Appl. Numer. Math. 181:630-646"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Applied_Numerical_Mathematics_Wang_Affine-invariant_WENO_weights_and_operator.pdf"
tags: [weno-weights, scale-invariance, well-balanced, finite-difference, eno-property]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper asks what a nonlinear WENO reconstruction does to data that are an
affine image $\sigma f+\mu$ of a function $f$ (constants $\sigma\ne0$ and
$\mu$ over the global stencil). Such data occur physically: the momentum
flux is affine in $v^2$ when $\rho$ and $p$ are locally constant, and the
still-water shallow-water flux is affine in the bottom topography. Because the
regularization $\epsilon$ of the classical [WENO-Z weights](/methods/weno-z.md)
is absolute while the [smoothness indicators](/definitions/smoothness-indicator.md)
scale as $\sigma^2$, a small $\sigma$ with a non-zero $\mu$ lets $\epsilon$
swamp the $\beta_k$, the weights collapse to $d_k$, and the scheme oscillates:
the [ENO property](/definitions/eno-property.md) is lost.

The contribution is the [affine-invariant (Ai) weights](/methods/affine-invariant-weno.md):
$\epsilon$ is replaced by $\epsilon\mathsf m^2[f]$, where the *descaler* $\mathsf m[f]$ is
the mean absolute deviation of the stencil data from their mean. This
generalizes the scale-invariant (Si) weights of Don, Li, Wang & Wang (2022),
whose descaler is the mean absolute value and which remove only $\sigma$.
Theorem 1 proves the [affine-invariance property](/properties/scale-invariance.md)
$W[\sigma f+\mu]=\sigma W[f]+\mu$ for Z- and D-type weights, Theorem 2 for
[WENO-JS](/methods/weno-js-reconstruction.md) weights.

Numerics are fifth-order finite differences ($r=3$) with
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md),
[characteristic decomposition](/methods/characteristic-decomposition.md) and
[SSP RK3](/methods/ssp-runge-kutta.md). Quadruple-precision invariance tests
show only the Ai operators at roundoff; linear advection and a modified
[two-blast-wave problem](/benchmarks/woodward-colella-blast-wave.md) with a
background pressure oscillate with classical and Si weights but not with Ai
weights; the [Lax and 123 tubes](/benchmarks/sod-and-lax-shock-tubes.md), the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md) and a Mach 2000
[jet](/benchmarks/high-mach-astrophysical-jet.md) (with the
positivity-preserving flux limiter of Hu, Adams & Shu, a relative of the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)) are shown. For
shallow water the Ai operator is [well-balanced](/properties/well-balancing.md)
intrinsically, without the "WENO linearization technique" of common weights.
No convergence-order or critical-point test is presented.

# Version read

Version of record (Elsevier typeset, © 2022 IMACS), 17 PDF pages (journal
pp. 630–646), all read; equations and figures checked visually. Page 1
matches Crossref (title, authors, venue, DOI). Equation, theorem and figure
numbers cited here are those of this version.

# Key claims

Registry notation; the source's affine coefficients $(\lambda,c)$ are written
$(\sigma,\mu)$, its descaler $\mu[f]$ is written $\mathsf m[f]$, its exponents $(p,q)$
are written $(q,q_{\mathrm o})$, and its stencil mean $\bar\xi[f]$ is written $\langle f\rangle$
(see the notation map).

1. For the affine map $\mathcal A f=\sigma f+\mu$, $W[\mathcal Af,\epsilon]=\mathcal A W[f,\epsilon]$ if and only if the normalized weights are invariant, $\omega_k[\mathcal Af]=\omega_k[f]$, because the linear candidate interpolants commute with $\mathcal A$ and $\sum_k\omega_k=1$ (§2.3, Eqs. (15)–(16)). **Derived**
2. Theorem 1: the Ai-WENO operator with the Ai weights (9)–(14) satisfies the affine-invariance property for every $f$, $\epsilon$ and $\sigma\ne0$, under the floor $\mathsf m_0=0$ (§2.3, Thm. 1, Eqs. (17)–(18)). **Proved**
3. Scalings used in the proof: $\mathsf m[\mathcal Af]=\lvert\sigma\rvert\mathsf m[f]$, $\varphi[\mathcal Af]=\lvert\sigma\rvert\varphi[f]$, $\beta_k[\mathcal Af]=\sigma^2\beta_k[f]$, $\tau[\mathcal Af]=\sigma^2\tau[f]$, $\langle f\rangle[\mathcal Af]=\mathcal A\langle f\rangle[f]$ (Eqs. (17)–(18)). **Proved**
4. Theorem 2 (Appendix A): JS-type weights $\alpha_k=d_k/(\beta_k+\epsilon\mathsf m^2)^q$ with the affine-invariant descaler satisfy the property, since $\alpha_k[\mathcal Af]=\sigma^{-2q}\alpha_k[f]$ (Eqs. (32)–(33)). **Proved**
5. Hierarchy: Z-type weights are D-type weights with modifier $\Phi=1$; classical (Cl) WENO is Si-WENO with $\mathsf m=1$; Si-WENO is Ai-WENO with $\langle f\rangle=0$ (§2.4). **Stated** (by definition)
6. Remark 2: Ai-WENO equals subtracting the stencil mean $\langle f\rangle$, applying Si-WENO, and adding the mean back (§2.4). **Stated**
7. The extra cost of descaler and averager is a few cache-friendly flops, per the CPU timings of Don et al. 2022 [6] (Remark 3). **Stated** (cited)
8. The floating-point error of the reconstructed affine data is $\max\{\lVert\sigma f\rVert_\infty,\lvert\mu\rvert\}\cdot O(\epsilon_0)$, $\epsilon_0$ the machine epsilon (Eq. (19), §2.5). **Stated**
9. In quadruple precision, $N_x=160$, $\epsilon=10^{-12}$, the normalized Ai error of Ai-WENO-Z/D is $O(\epsilon_0)$ for sine, ReLU and Heaviside data and all tested $(\sigma,\mu)$, while Cl- and Si-WENO-Z/D errors lie far above roundoff (up to about $10^{-15}$ for the sine, $\sim10^0$ for ReLU and Heaviside) over a wide range of $\sigma$ with $\mu\ne0$ (§3.1, Figs. 1–3); the results "hold for $\varepsilon=10^{-40}$ generally", not shown. **Shown**
10. Si-WENO has zero Ai error for $\mu=0$ (scale invariance) but not for $\mu\ne0$; Cl-WENO fails even for $\mu=0$ when $\sigma$ is small (Figs. 1–3). **Shown**
11. Linear advection, $(\sigma,\mu)=(10^{-7},1)$, $\epsilon=10^{-12}$, $N_x=200$, $t=2$: Si-WENO-Z shows visible Gibbs oscillations, while for $\mu=0$ it is non-oscillatory (§3.2.1, Fig. 4). **Shown**
12. Mechanism: with $\sigma=10^{-7}$, $\mu=1$, the Si descaler gives $\mathsf m[\mathcal Af]\approx1$, so $\beta_k=O(10^{-14})$ is dominated by $\epsilon\mathsf m^2\approx10^{-12}$, the weights become independent of $k$ and the scheme reverts to the linear fifth-order scheme (§3.2.1, p. 638). **Derived**
13. Ai-WENO-Z on the same problem is non-oscillatory for both $\mu=0$ and $\mu=1$, with identical point-wise errors in the two cases (§3.2.1, Fig. 5). **Shown**
14. Modified two-blast-wave problem with $\sigma=10^{-7}$ and background pressure $p_\infty=\mu=1$: Cl-WENO-Z oscillates at strong and weak shocks, Si-WENO-Z reduces but does not remove the oscillations, Ai-WENO-Z is essentially non-oscillatory (§3.2.2, Fig. 6). **Shown**
15. The ENO property of a WENO scheme that is not affine-invariant can be violated when $\lvert\sigma\rvert\ll\lvert\mu\rvert$ (§3.2.2, p. 640). **Shown** (by the two examples)
16. On the 123, Lax, two-blast-wave and Shu–Osher problems with $(\sigma,\mu)=(10^{-7},0)$, $\epsilon=10^{-12}$, Ai-WENO-Z and Ai-WENO-D give essentially identical, non-oscillatory results (§3.2.3, Fig. 7). **Shown**
17. Ai-WENO schemes are not positivity-preserving in general; the Mach 2000 jet needs a positivity-preserving limiter [9,13], which activates only around the jet front and the two inlet corners at the final time (§3.2.4, Fig. 8). **Shown**
18. In the surface-level form of the shallow-water equations, the still-water flux component $\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b$ is affine in $b$ with coefficients $(-gH_{\mathrm s},\tfrac12gH_{\mathrm s}^2)$, so the Ai operator gives the well-balanced property intrinsically, also in characteristic variables because the projection is linear (§3.3, p. 643). **Derived**
19. Well-balanced WENO with classical weights needs the "WENO linearization technique" (common weights, Appendix B of Li, Caleffi & Qi 2015 [12]) (§3.3). **Stated** (cited)
20. Without linearization, $\epsilon=10^{-12}$, $t=50$, $N_x\le1000$, quadruple precision: Ai-WENO-Z/D keep $\lVert H_{\mathrm s}-10\rVert_\infty$ at $O(\epsilon_0)$ (about $10^{-33}$), whereas Cl/Si-WENO errors fall from about $10^{-11}$ to $10^{-23}$ with $N_x$ (smooth bottom $b_1$) and stay near $10^{-26}$ (discontinuous bottom $b_2$) (§3.3, Fig. 9). **Shown**
21. With $\epsilon=10^{-40}$, all operators are well-balanced except Cl- and Si-WENO-D on the smooth bottom $b_1$, explained by the modifier $\Phi=\min\{1,\varphi/\mathsf m\}$ not being affine-invariant when it equals $\varphi/\mathsf m$; for $b_2$, $\Phi=1$ and the D weights reduce to Z weights (§3.3, Fig. 10). **Shown**
22. Classical and scale-invariant WENO-D "do not generally satisfy the Ai-property and should only be used with care" for this class of problems (§3.3, p. 644). **Stated**
23. The Ai well-balanced scheme is well-balanced "for any sensitivity parameter" (§3.3 summary). **Shown** for $\epsilon\in\{10^{-12},10^{-40}\}$ only
24. For the Euler equations under gravity (zero translation constant), the characteristic-wise well-balanced Si/Ai-WENO scheme is well-balanced without linearization (abstract, Introduction, Conclusion; relies on [6]). **Stated** (no Euler-gravity test in the paper)
25. The Ai weights are "the new gold standard in designing an improved WENO operator" (Conclusion). **Stated**
26. Weight linearization is still needed when the WENO operator acts on a sum or product of two functions, e.g. for two-$\gamma$ multicomponent equilibrium [5] (Introduction, p. 632). **Stated**

# Printed slips

- §3.3, p. 643 gives the affine coefficients "$\Upsilon=(\lambda,c)=(-gH,\tfrac12gH^2)$", consistent with the flux $\tfrac12gH^2-gHb$ of (27); p. 644 then writes "a non-zero translation constant $c=-\tfrac12gH^2$". The sign of the second is wrong.
- p. 644: "For the smooth $b_1(x)$, $\Phi[f]=\varphi[f]/\mathsf m[f]=\varphi[f]$" — the last equality holds only for the classical descaler $\mathsf m=1$, not for Si-WENO-D, which the same bullet covers.
- Remark 4, Eq. (29): the momentum flux is printed "$(hu)^2+\tfrac12gh^2-\tfrac12gb^2$"; by (26) the first term is $(hu)^2/h$. The rest is consistent with (27), since $\tfrac12gh^2-\tfrac12gb^2=\tfrac12gH^2-gHb$ with $H=h+b$.
- Remark 2 (p. 635): "the affine-invariant property of the Si-WENO operator can be reformulated" — it is the Ai-WENO operator that is reformulated through Si-WENO; the remark writes $W[f^*,\epsilon]$ with $\epsilon$ instead of $\varepsilon$.
- Eq. (5) is called "the (linear) second-order polynomial interpolation"; the candidate polynomials are of second degree (third-order accurate).
- §3.2.1, p. 638: the collapsed weights make the scheme "the central upwind scheme"; what is meant is the linear fifth-order upwind-biased scheme ($\omega_k\to d_k$), not a central-upwind scheme.
- §1, p. 632: a dangling reference "… finite volume WENO methods. [21]." after the full stop.
- §3.3: "global Lax-Fredrichs flux splitting" (Friedrichs).
- §3.2.3 lists "the 123 problem, the two blast-waves interaction problem, and the shock-density interaction problem", while Fig. 7 also shows the Lax problem, which the Introduction cites as "shown in Section 3.2".
- p. 644: "The errors computed by the WENO schemes based on these two D-type weights fail (able) to achieve the WB-property for the smooth $b_1(x)$ (discontinuous $b_2(x)$)" — garbled sentence, consistent with Fig. 10.
- Eq. (16) is printed as an equivalence; only "$\Leftarrow$" follows from (15), since (15) vanishes for any weights when all candidate values coincide. Theorem 1 uses only "$\Leftarrow$". *(compiler check, not in the sources: (15) with $\hat f^{(0)}=\hat f^{(1)}=\hat f^{(2)}$ and $\sum_k\omega_k=1$ on both sides gives zero for arbitrary weights.)*

# Notation map

| Wang & Don (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$, $I_j$, $x_{j\pm1/2}$ | $i$, $I_i$, $x_{i\pm1/2}$ | cell index |
| $N$ | $N_x$ | number of cells; **$N$ is the DG degree in the registry** |
| $r$, $S_k$ ($k=0,1,2$), $S^5=S^{2r-1}$ | $r$, $S_k$ | $S_0$ the leftmost (most upwind for $W^-$); global stencil kept as $S^{2r-1}$ |
| $q^{(k)}_{j+1/2}[f]$, $b_{k,i}$ | $\hat f^{(k)}_{i+1/2}$ | candidate interface value; coefficients not printed |
| $f^\mp_{j+1/2}=W^\mp_{j+1/2}[f,\varepsilon]$ | $\hat f^{\mp}$-reconstruction; $W[f,\epsilon]$ kept as the operator name | left-/right-biased reconstruction of split fluxes |
| $d_k=(1/10,3/5,3/10)$ | $d_k$ | agrees |
| $\beta_k[f]$ | $\beta_k$ | Jiang–Shu form, agrees |
| $\tau[f]=\lvert\beta_0-\beta_2\rvert$ | $\tau_5$ | agrees |
| $\varepsilon$ | $\epsilon$ | regularization ("sensitivity parameter") |
| $p$ (inner exponent, $p=2$) | $q$ | **collision: the source's $q$ is a different exponent** |
| $q$ (outer exponent of $(1+\Gamma_k)^q$, $q=1$) | $q_{\mathrm o}$ (page-local) | **collision with registry $q$** |
| $\alpha^z_k$, $\alpha_k$, $\omega_k$ | $\alpha_k$, $\omega_k$ | agrees |
| $\Gamma_k=\Phi Z_k$, $Z_k=(\tau/(\beta_k+\varepsilon\mu^2))^p$ | $\Phi Z_k$, $Z_k=(\tau/(\beta_k+\epsilon\mathsf m^2))^q$ (page-local) | not in registry |
| $\Phi[f]$, $\phi[f]=\sqrt{\lvert\beta_0-2\beta_1+\beta_2\rvert}$ | $\Phi[f]$, $\varphi[f]$ (page-local) | D-type modifier of Wang, Wang & Don (2019) |
| $\mu[f]$, $\mu_0$ | $\mathsf m[f]$, $\mathsf m_0$ (page-local) | descaler and its floor; **$\mu$ is the translation constant here** |
| $\bar\xi[f]$ | $\langle f\rangle$ (page-local) | stencil mean ("averager"); **$\xi_j$ are DG nodes in the registry** |
| $\mathcal A$, $\Upsilon=(\lambda,c)$ | $\mathcal A$, $(\sigma,\mu)$ (page-local) | **$\lambda$ collides with eigenvalues $\lambda_l$, $c$ with the sound speed** |
| $\epsilon_0$ | $\epsilon_0$ | machine epsilon; distinct from $\epsilon$ |
| $Q$, $F(Q)$, $u$, $P$ | $u$, $f(u)$, $v$, $p$ | Euler variables |
| $h$, $u$, $b$, $H=h+b$, $g$ | $h$, $v$, $b$, $H_{\mathrm s}$, $g$ (page-local) | shallow water, as on the [well-balancing](/properties/well-balancing.md) page; **$H$ is the specific total enthalpy and $g(\omega)$ the mapping function in the registry** |
| $P_\infty$ | $p_\infty$ | background pressure |
| Cl/Si/Ai-WENO-Z/D | kept | classical / scale-invariant / affine-invariant descaler; Z or D modifier |

# Reference list

21 printed references in numbered style [1]–[21], all parsed. Only [15] is
incomplete (J. Comput. Phys. 2021 with a ResearchGate DOI and no volume,
pre-publication form, kept as its own entry). No printed duplicates. The list
is merged complete into the [bibliography](/bibliography.md) with `citedby`
`wang-2022-b`.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–9 (2026-10-22/23). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Affine-invariant WENO weights](/methods/affine-invariant-weno.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [ENO property](/definitions/eno-property.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Positivity-preserving flux limiter (Hu–Adams–Shu)](/methods/positivity-preserving-flux-limiter.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shallow-water equations](/definitions/shallow-water-equations.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Well-balancing](/properties/well-balancing.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
