---
type: Source
title: "Allegrini & Vignal (2025) — Study of a New Low-Oscillating Second-Order All-Mach Number IMEX Finite Volume Scheme for the Full Euler Equations"
description: "Analyses IMEX flux splittings of the low-Mach-scaled full Euler equations for asymptotic stability, asymptotic consistency and contact preservation, and builds from the Toro–Vázquez-Cendón splitting a linear, decoupled all-Mach finite-volume scheme with implicit upwinding, a second-order ARS(2,2,2)–MUSCL version and a TVD blend."
resource: "doi:10.1137/23m1568703"
source_kind: paper
authors: [Allegrini P., Vignal M.H.]
year: 2025
venue: "SIAM J. Sci. Comput. 47:A268-A299"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_SIAM_Journal_on_Scientific_Computing_Allegrini_Study_of_a_New_Low-Oscillating_Second-Order_All-Mach_Number.pdf"
tags: [all-mach, asymptotic-preserving, imex, finite-volume, flux-splitting]
timestamp: 2026-10-23T20:29:00Z
---

# Summary

Allegrini & Vignal (2025) build an implicit–explicit finite-volume scheme for the full
Euler equations scaled so that the pressure gradient carries $1/\varepsilon$, with
$M^2=\varepsilon/\gamma$. The aim is [asymptotic preservation](/properties/asymptotic-preservation.md)
in the low-Mach limit: a time step independent of $\varepsilon$ and, as
$\varepsilon\to0$, a consistent discretization of the incompressible Euler system. The
authors ask three things of a [flux splitting](/methods/flux-vector-splitting.md)
$f=f_e+f_i$: real eigenvalues of both parts, those of the explicit part bounded in
$\varepsilon$; asymptotic consistency; and preservation of constant contact
discontinuities, a moving form of
[contact preservation](/properties/stationary-contact-preservation.md). The
Toro–Vázquez-Cendón splitting (explicit mass, convective momentum and kinetic-energy
fluxes; implicit $p/\varepsilon$ and enthalpy flux) has all three for non-well-prepared
data; the Cordier–Degond–Kumbaro, Dimarco–Loubère–Vignal and Lagrange-projection-type
splittings do not, and moving part of the enthalpy flux to the explicit side loses
consistency.

The new [semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)
linearizes the non-linear scheme of Boscheri et al.: the enthalpy and kinetic energy
of the elliptic pressure equation are evaluated on the explicitly convected state, so
density, pressure, momentum and energy follow in sequence from one linear elliptic
solve, without Picard iteration. It is asymptotically consistent for well-prepared
energy. A [Rusanov](/methods/lax-friedrichs-flux.md) flux on the explicit part with
centred implicit fluxes gives the "L2 AP" scheme; implicit upwinding scaled by the
implicit eigenvalue gives the "L∞ AP" scheme, which damps the density oscillations of
the former. A linearized Fourier analysis, finished numerically, gives the CFL
conditions. The second-order version uses [ARS(2,2,2)](/methods/imex-runge-kutta.md)
in time and minmod MUSCL in space; a convex blend with the first-order scheme gives a
[TVD](/definitions/total-variation-diminishing.md) but first-order "TVD AP" scheme.

Tests: [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md), a contact with a $10^5$
density ratio ([material-interface advection](/benchmarks/material-interface-advection.md)),
interacting Riemann problems at $\varepsilon=1$ to $10^{-2}$, a low-Mach shock tube,
the [isentropic vortex](/benchmarks/isentropic-vortex.md), the
[Gresho vortex](/benchmarks/gresho-vortex.md) at $M=10^{-1}$ to $10^{-3}$, a
[2D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) and a double
shear layer ([Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)) at
$\varepsilon$ down to $10^{-6}$.

# Version read

The archive file is the HAL deposit hal-04874138v1 (submitted 8 January 2025), the
authors' manuscript in article layout, not the SIAM typeset version of record: a HAL
cover page giving the journal citation and DOI, then 34 manuscript pages, all read
(pp. 13, 16 and 25 checked on the page images). Page numbers on this page are the
manuscript's. Title, authors and DOI match the Crossref record. Every claim, equation
and number on this page is that of the HAL version.

# Key claims

Registry notation: conserved state $u=(\rho,\rho v,E)$ (source $W=(\rho,\mathbf q,E)$),
velocity $v$ (source $\mathbf u$), cell index $i$ (source $j$), flux $f=f_e+f_i$
(source $F_e$, $F_i$). Page-local: $\varepsilon=\gamma M^2$ the scaling parameter (not
the weight regularization $\epsilon$, nor the reference Mach number $\varepsilon$ of the
[semi-implicit all-Mach page](/methods/semi-implicit-all-mach-scheme.md)),
$\kappa_\varepsilon=\varepsilon\rho\lvert v\rvert^2/2$ the scaled kinetic energy,
$h_{\mathrm v}=\gamma p/(\gamma-1)=\gamma(E-\kappa_\varepsilon)$ the enthalpy per unit
volume, $c^2=\gamma p/\rho$ (the physical sound speed being $c/\sqrt\varepsilon$),
$u^{n+1,\mathrm{ex}}$ the explicitly convected state, $\beta_h$ the explicit enthalpy
fraction, $\beta_{\mathrm{ARS}}=1-1/\sqrt2$, $\theta_{\mathrm{TVD}}$ the blending
weight, $M_\varepsilon=\sqrt\varepsilon\,\bar v/\bar c$.

1. In the scaled system $M^2=\varepsilon/\gamma$; explicit schemes need $\Delta t\le\Delta x/\max\lvert v\pm c/\sqrt\varepsilon\rvert=O(\sqrt\varepsilon)$ and are not asymptotically consistent without flux corrections (§1, p. 2). **Stated** (cited)
2. Formally, with impermeable boundaries, $p^{(0)}$ and $E^{(0)}=p^{(0)}/(\gamma-1)=\lvert\Omega\rvert^{-1}\int_\Omega E^{(0)}(x,0)\,dx$ are constant in space and $\nabla\cdot v^{(0)}=0$, for well-prepared or non-well-prepared data (§1, Eqs. (2)–(3)). **Derived**
3. Asymptotic stability needs the term $\frac{\gamma p}{\gamma-1}\nabla\cdot v$ of the internal-energy equation, i.e. the enthalpy flux, to be implicit; otherwise the pressure-wave operator $\varepsilon^{-1}\nabla\cdot(\rho^{-1}\nabla p)$ forces $\Delta t=O(\sqrt\varepsilon\,\Delta x)$ (§2.1, p. 5). **Derived**
4. Lemma 1: the splitting $f_e=(\rho v,\rho v\otimes v,\kappa_\varepsilon v)$, $f_i=(0,p\,\mathrm{Id}/\varepsilon,h_{\mathrm v}v)$ has (i) real eigenvalues in 1D, $0$ and $v$ (double) for $f_e$, $0$ and $v/2\pm\sqrt{v^2/4+c^2/\varepsilon}$ for $f_i$; (ii) asymptotic consistency for non-well-prepared data (proved in Boscheri et al.); (iii) preservation of constant contact discontinuities (§2.1, Eq. (8)). **Proved** ((ii) by citation)
5. With a fraction $\beta_h\in[0,1)$ of $h_{\mathrm v}v$ explicit, the limit gives $\nabla\cdot v^{n+1}=\frac{\beta_h}{\beta_h-1}\nabla\cdot v^n$, so $\beta_h=0$ is "the only choice which ensures the asymptotic consistency for non well-prepared initial data" (Remark 2.2, p. 7). **Derived**
6. Separate hyperbolicity of $f_e$ and $f_i$ "seems not necessary" in the Fourier analysis and the tests (Remark 2.1, p. 7). **Stated**
7. The Cordier–Degond–Kumbaro splitting is a multi-step method through $p^n$, so (i) is meaningless for it and (ii), (iii) hold only up to $O(\Delta t)$ (§2.2, p. 8). **Stated**
8. Lemma 2: the one-step variant of Dimarco–Loubère–Vignal has complex explicit eigenvalues for $\gamma<3$; their non-conservative splitting satisfies (i) but not (ii), $\nabla\cdot v^{n+1}=O(\Delta t)$ for $n\ge2$, nor (iii) (§2.2). **Proved**
9. Lemma 3: the Lagrange-projection-like splitting $f_e=(\rho v,\rho v\otimes v,Ev)$, $f_i=(0,p\,\mathrm{Id}/\varepsilon,pv)$ separates transport (explicit eigenvalue $v$, triple) from pressure waves (implicit $0$, $\pm\sqrt{(\gamma-1)c^2/(\gamma\varepsilon)}$); it satisfies (i) and (iii), and (ii) if and only if the initial velocity is well-prepared (§2.2). **Proved**
10. The new semi-discretization (13) evaluates $h_{\mathrm v}$ and $\kappa_\varepsilon$ on $u^{n+1,\mathrm{ex}}$; it is linear and decoupled, $\rho^{n+1}$, $p^{n+1}$, $(\rho v)^{n+1}$, $E^{n+1}$ in sequence; updating $E$ from the equation of state instead of the energy equation gives wrong intermediate states in Sod, as noticed for the scheme of Boscheri et al. (§3.1, pp. 10–11, Fig. 1). **Shown**
11. Lemma 4: (13) preserves constant contact discontinuities and is asymptotically consistent ($p^{n+1}=(\gamma-1)E^0$, $\nabla\cdot v^{n+1}=0$) for well-prepared energy $E(x,0)=E^0+\varepsilon\bar E(x)$ (pp. 11–12). **Proved**
12. Replacing $\gamma p^{n+1}/(\gamma-1)$ in the energy update by $h_{\mathrm v}^{n+1,\mathrm{ex}}$ restores consistency for non-well-prepared data but is rejected: it is less diffusive in the L2 version and "oscillations appear in some test-cases" (Remark 3.2, p. 12). **Stated**
13. The implicit upwinding of the L∞ AP scheme scales as $1/\sqrt\varepsilon$ and makes the consistency hold only up to $O(\Delta t)$: on a model viscous perturbation, $\nabla\cdot v_0^{n+1}=O(\Delta t)$ and $E_0^{n+1}=E^0+O(\Delta t)$ (Remark 5.2, p. 14). **Derived**
14. Lemma 5: the linearized L2 AP scheme is $L^2$ stable for $M_\varepsilon\in]0,25[$ and $\gamma\in[1,10]$ under $\gamma\lvert v\rvert\Delta t=\Delta x$; the explicit factor is stable under $\lvert v\rvert\Delta t/\Delta x\le1$, the quadratic factor of the total amplification is checked numerically, with maximum root modulus 1; for $\lvert v\rvert\Delta t/\Delta x>1/\gamma$ some $\gamma$ gives spectral radius above 1, so the condition "seems to be optimal" (pp. 16–17). **Derived** and **Shown** (numerically completed)
15. Lemma 6: the linearized L∞ AP scheme is $L^2$ stable for $M_\varepsilon\in]0,25[$, $\gamma\in[1,5]$ under $\lvert v\rvert\Delta t=\Delta x$, a CFL $\gamma$ times larger (pp. 17–18). **Derived** and **Shown**
16. Lemma 7: the linearized non-linear L2 AP scheme is $L^2$ stable for $M_\varepsilon\in]0,25]$ under $\lvert v\rvert\Delta t=\Delta x$, with the residual quadratic $P_2(\mu)$ printed and its root moduli plotted (pp. 18–19, Fig. 2). **Derived** and **Shown**
17. On Sod and Lax the linear L2 and L∞ AP schemes match the non-linear ones, more diffusive at the Lax contact, with differences vanishing from 200 to 500 cells; L2 AP overshoots slightly at the Sod contact (Figs. 3–6). **Shown**
18. Contact with density ratio $10^5$ and local Mach number between $2\cdot10^{-4}$ and $9\cdot10^{-2}$: velocity and pressure stay constant "up to an error of $10^{-5}$"; L∞ AP is more diffusive on density (Fig. 7). **Shown**
19. Interacting Riemann problems: every first-order AP scheme, the non-linear ones included, oscillates in density on coarse meshes unless the CFL is reduced, more as $\varepsilon$ decreases and more for the L2 versions; L∞ upwinding reduces the oscillations "significantly", and L∞ AP is kept as "Order 1 AP" (§3.4.2, Figs. 8–10). **Shown**
20. The CFL rules used are $\Delta t\le\nu\Delta x/\max_i\lvert v_i\rvert$ (L∞ AP and the non-linear schemes) and $\Delta t\le\nu\Delta x/(\gamma\max_i\lvert v_i\rvert)$ (L2 AP), $\nu\le1$ (§3.4.2). **Stated**
21. Implicit methods of order above one cannot be SSP, nor can IMEX ones; second-order IMEX in time with first-order space oscillates more as the Mach number decreases ($\varepsilon=10^{-2}$ to $10^{-4}$) (§4, §4.3, Fig. 11). **Stated** (cited) and **Shown**
22. The blend $u^{n+1}=(1-\theta_{\mathrm{TVD}})u^{n+1,O1}+\theta_{\mathrm{TVD}}u^{n+1,O2}$, $\theta_{\mathrm{TVD}}=\beta_{\mathrm{ARS}}/(1-\beta_{\mathrm{ARS}})$, "proved in [19] to be the largest possible value to ensure the TVD property in the case of an advection equation", is TVD, asymptotically consistent and first order with smaller errors than the first-order schemes (§4.3, Eq. (28), Fig. 12). **Stated** (cited) and **Shown**
23. Lemma 8: the ARS(2,2,2) semi-discretization (Eqs. (24)–(25)) is asymptotically consistent for well-prepared energy (p. 25). **Proved** (sketch)
24. Isentropic vortex to $t=1$: the expected orders for the first- and second-order L2 AP schemes (the latter without limiter) and the explicit schemes; TVD AP is first order with lower error (Fig. 12). **Shown**
25. Gresho vortex ($80^2$, one turn): the second-order L2 AP scheme keeps the local Mach distribution independent of $M\in\{10^{-1},10^{-2},10^{-3}\}$, without pressure oscillations at $M=10^{-3}$; the kinetic-energy loss is independent of $M$ and comes "mostly" from the limiter, kinetic-energy ratio 0.9825 unlimited against 0.92 with minmod on $40^2$ (§4.5, Figs. 13–14). **Shown**
26. 2D Riemann problem ($400^2$, $t=0.25$): both second-order schemes keep the contacts steady; L2 AP is much sharper but oscillates, and implicit upwinding reduces the oscillations (§4.6, Fig. 15). **Shown**
27. Double shear layer, second-order L2 AP on $128^2$ to $t=1.2$: the incompressible solution is matched at $\varepsilon=10^{-3}$ and $10^{-6}$ but not at large $\varepsilon$; the density $L^2$ error against $\rho=1$ at $\varepsilon=10^{-3}$ is $9.18\cdot10^{-3}$ ($128^2$) and $5.13\cdot10^{-3}$ ($256^2$), described as "of order ε" (§4.7, Fig. 16). **Shown**

The proofs of Lemmas 5–7 end on plotted root moduli and on the step "there exists at
least one norm matrix $\lVert\cdot\rVert$ … such that $\lVert B^{im}B^e\rVert\le r(B^{im}B^e)$",
followed by norm equivalence. *(Compiler check, not in the sources: the step does not
hold for every matrix. $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ has $r(B)=1$, but
$B^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$ is unbounded, so no induced norm gives
$\lVert B\rVert\le1$; a norm with $\lVert B\rVert\le r(B)$ exists when the eigenvalues
of modulus $r(B)$ are semisimple, which the paper does not check, and the plotted
maximum modulus is 1.)*

# Printed slips

- Eq. (15e), p. 13: the second flux term carries $\gamma\tilde p^{n+1}$ at $j-1$ where the first has $\gamma p^{n+1}$ at $j+1$; $\tilde p$ is defined only for the Dimarco–Loubère–Vignal splitting of §2.2. Eqs. (19d)–(19e), p. 16, likewise print $\tilde p^{n+1}_{j+1}$ next to $p^{n+1}_{j-1}$, although the text says the tildes are omitted.
- Eq. (26), p. 25: the centred part of the MUSCL flux is printed $\frac{F_e(W_{j+1,-})+F_e(W_{j,+})}{2\Delta x}$, where the first-order flux (15f) has the denominator 2.
- Remark 4, p. 13: the 2D explicit fluxes are printed $F^x_e=(u,\rho u^2,\rho uv,k_\varepsilon u)$ and $F^y_e=(v,\dots)$, with mass flux $u$ for $\rho u$; $W^{n+1,ex}_{j,l}=W^n_{i,l}-\dots$ mixes the indices $i$ and $j$; $(\mathcal D^y_e)^n_{j,l+\frac12,l}$ has an extra index.
- §4.3: "$W^{n+1,O1}$ is given by the 'L∞ AP' scheme (13)"; (13) is the semi-discretization, the L∞ AP scheme is (16).
- Remark 5.2: $p_0^{n+1}=E^0+O(\Delta t^2)$ lacks the factor $\gamma-1$ of Lemma 4's $p^{n+1}=(\gamma-1)E^0$.
- Lemma 8 proof, p. 25: "$\nabla p_0^{n+1}=(\gamma-1)E_0^{n+1}=0$" for $p_0^{n+1}=(\gamma-1)E_0^{n+1}$ and $\nabla p_0^{n+1}=0$; "$p_0^\star=\nabla p_1^\star=0$" for $\nabla p_0^\star=\nabla p_1^\star=0$; "$p_0^\star=(\gamma-1)\bar E_0=(\gamma-1)\bar E_0$" duplicates an equality.
- Lemmas 5–6 state $M_\varepsilon\in]0,25[$, the plots run over $]0,25]$.
- §3.4.1, p. 20: the left state of the Lax problem is printed with
  $u_L=1.698$; [Charles & Ray (2025)](/sources/charles-2025.md) and
  [Huang et al. (2025a)](/sources/huang-2025.md) print $0.698$ with the same
  $\rho_L=0.445$, $p_L=3.528$ ([Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).
  The paper does not show which value was run.
- Gresho data, third branch: a closing parenthesis is missing in "$(1,0,p_0-2+4\ln(2),$".
- References: [1] opens with the stray fragment "Commun. Comput Phys" before the author Alazard; [10] (Schulz-Rinne et al.) is out of alphabetical order; [45] (Vilar) prints "J. Comp. Phys., 245, 2019" with no clear volume and page.

# Notation map

| Allegrini & Vignal (HAL v1) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $W=(\rho,\mathbf q,E)$, $\mathbf q=\rho\mathbf u$ | $u=(\rho,\rho v,E)$ | **collision**: source $\mathbf q$ is momentum, registry $q$ the weight exponent |
| $\mathbf u$, $u$ (1D) | $v$ | **collision** of $u$ |
| $F=F_e+F_i$, $DF_e$, $DF_i$ | $f=f_e+f_i$, Jacobians | |
| $\varepsilon$ | $\varepsilon=\gamma M^2$ (local) | **collision** with the weight regularization $\epsilon$ and the reference Mach number $\varepsilon$ of other all-Mach pages |
| $k_\varepsilon$ | $\kappa_\varepsilon$ (local) | scaled $\kappa$ |
| $h=\gamma p/(\gamma-1)$ | $h_{\mathrm v}$ (local) | enthalpy per unit volume, not the specific $H$ nor the flux $h(u^-,u^+)$ |
| $c$ | $c$ | unscaled; physical speed $c/\sqrt\varepsilon$ |
| $j$, $j\pm1/2$, $(j,l)$ | $i$, $i\pm1/2$, $(i,j)$ | **index letters** |
| $(\mathcal F_e)_{j+1/2}$, $(\mathcal D_e)_{j+1/2}=\tfrac12\max\lvert u\rvert$ | Rusanov flux on $f_e$, coefficient $\tfrac12\max\lvert v\rvert$ | half of the registry's $a$ convention |
| $(\mathcal D_i)_{j+1/2}$, $\lvert\lambda_i\rvert$ | implicit viscosity, $\lvert v\rvert/2+\sqrt{v^2/4+c^2/\varepsilon}$ | |
| $W_{j,\pm}$, $\sigma_j$ | MUSCL states $u^\mp$ at the faces, minmod slope | **collision**: source $W_{j,+}$ is the registry $u^-_{i+1/2}$ |
| $\beta$ (three uses) | $\beta_h$, $\beta_{\mathrm{ARS}}$, amplification factor (local) | **collision** with $\beta_k$ |
| $\theta$ | $\theta_{\mathrm{TVD}}=\sqrt2-1$ (local) | **collision** with the Zhang–Shu $\theta$ |
| $\alpha$ | $\Delta t/\Delta x$ (§3.3); splitting parameter (§2.2) | **collision** with $\alpha_k$ |
| $M_\varepsilon$, $M_{loc}$, $M_p$ | local Mach numbers, $M$ | |
| $B^e$, $B^{im}$, $Q^{im}$, $P_2$, $\varphi$ | amplification matrices, residual polynomials, phase $\vartheta$ | |

# Reference list

The manuscript prints 46 references, numbered [1]–[46], roughly alphabetical ([10] out
of order), without DOIs. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `allegrini-2025`. Ref. [12]
(Chen, Li, Li, Yuan & Gao, anti-dissipation pressure correction, J. Comput. Phys. 456)
is a different work from the ingested `chen-2022` and takes a disambiguated key. Ref.
[1] is parsed without its stray journal fragment, kept in the entry's note; [8] prints
no article number, [15] the journal as "Comp. Phys.", [21] no volume, and [45] an
unclear volume. No item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunks 11–12 (2026-10-24/30). This source is cited on:

* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Flux vector splitting](/methods/flux-vector-splitting.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Stationary contact preservation](/properties/stationary-contact-preservation.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
