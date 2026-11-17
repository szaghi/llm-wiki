---
type: Source
title: "Pirozzoli (2010) — Generalized conservative approximations of split convective derivative operators"
description: "Shows that Feiereisen, Blaisdell and Kennedy–Gruber split convective derivatives discretized with explicit central differences of any order are locally conservative, with face fluxes that are double sums of products of two-point means and cheaper than direct split differencing; inviscid isotropic turbulence and a Mach 2 boundary-layer DNS favour the density-weighted (Kennedy–Gruber) split."
resource: "doi:10.1016/j.jcp.2010.06.006"
source_kind: paper
authors: [Pirozzoli S.]
year: 2010
venue: "J. Comput. Phys. 229:7180-7190"
local_file: "/home/stefano/papers/mosaic/weno-teno/2010_Crossref_Journal_of_Computational_Physics_Pirozzoli_Generalized_conservative_approximations_of_split_convective.pdf"
tags: [kinetic-energy-preserving, finite-difference, numerical-flux, low-dissipation, turbulence]
timestamp: 2026-11-17T08:43:20Z
---

# Summary

Split forms of the convective derivative $\partial_x(\rho v\phi)$ stabilize non-dissipative
central schemes, but discretized naively they are not differences of numerical fluxes, so
neither global conservation by telescoping nor the
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) is evident. Ducros et al. (2000, not
ingested) had found numerical fluxes for explicit central differences up to sixth order.
Pirozzoli (2010) shows that the Feiereisen and Blaisdell splits, discretized with an explicit
central derivative of any half-width, are exactly flux differences: one term of the central
sum is the difference of two pair products of arithmetic means, and adding the intermediate
pairs telescopes it. The face flux is a double sum of two-point products of means
([conservative split central derivative](/operators/conservative-split-derivative.md)). The
same holds for the Kennedy–Gruber split at its kinetic-energy-preserving weights, with a
triple product of means, called "density-weighted". Storing the means line by line makes the
conservative fluxes cheaper than differencing the split form directly up to high order.

The tests are shock-free: inviscid decaying isotropic turbulence on $32^3$ at initial
turbulent Mach numbers 0.07 and 0.3, orders 2 to 10, where the divergence form diverges, all
splits hold the kinetic energy at the low Mach number and only the Kennedy–Gruber split
survives at 0.3; and a Mach 2 spatially developing boundary-layer DNS with the sixth-order
Kennedy–Gruber flux on a stretched grid, plus under-resolved runs comparing splits and
orders and an effective-bandwidth cost estimate. The paper is the source of the
arbitrary-order flux that later bundle sources call "Pirozzoli's" form
([split convective forms](/methods/split-convective-forms.md),
[kinetic energy preservation](/properties/kinetic-energy-preservation.md),
[flux differencing](/methods/flux-differencing.md)).

# Version read

Version of record, J. Comput. Phys. 229 (2010) 7180–7190, 11 pages, all read. Received 27
January 2010, revised 21 April 2010, accepted 4 June 2010, available online 17 June 2010;
DOI printed on page 1. Single author, Università degli Studi di Roma "La Sapienza". The text
layer garbles every displayed equation; Eqs. (1)–(17) were read from page renders, Figs. 1, 3
and 10 from renders as well (Fig. 1 at 300 dpi to check the cost formulas). No identity
problem. Bundle label: Pirozzoli (2010).

# Key claims

Registry notation (see the Notation map): $x_i$, $\Delta x$, velocity $v$, transported scalar
$\phi$ (page-local), central derivative $\delta$ with weights $\mathsf a_\ell$ and half-width
$L_{\mathrm s}$, pair mean $\{\!\{a\}\!\}_{i,\ell}=\tfrac12(a_i+a_{i+\ell})$, Kennedy–Gruber
weights $\alpha_{\mathrm{KG}}$, $\beta_{\mathrm{KG}}$.

1. Local conservation guarantees global conservation of linear invariants by telescoping and makes the Lax–Wendroff theorem hold, "extremely useful" for a building block of hybrid shock-capturing schemes, in which "some artificial viscosity must be provided" to inhibit Gibbs oscillations and select the entropy solution (§1, citing Larsson et al. and Johnsen et al.). **Stated**
2. The split forms of $\partial_x(\rho v\phi)$, $\phi\in\{1,v_d,H\}$: Feiereisen (FE-SF) $\tfrac12\partial_x(\rho v\phi)+\tfrac12\phi\,\partial_x(\rho v)+\tfrac12\rho v\,\partial_x\phi$ and Blaisdell (BL-SF) $\tfrac12\partial_x(\rho v\phi)+\tfrac12v\,\partial_x(\rho\phi)+\tfrac12\rho\phi\,\partial_xv$ (§2, Eqs. (1)–(4)). **Stated**
3. Labelling these forms "skew-symmetric" "is not strictly correct", because the inner product of the operators with $\phi$ does not vanish under integration by parts and $\int\rho\phi^2$ is not preserved; semi-discrete energy consistency needs continuity and momentum both split as FE-SF (after Honein & Moin), while BL-SF stabilizes by reducing aliasing; strictly skew-symmetric forms are Morinishi's (§2, p. 7181). **Stated**
4. Discrete split derivative $\delta^{\mathrm{sp}}(ab)_i=\tfrac12\delta(ab)_i+\tfrac12a_i\delta b_i+\tfrac12b_i\delta a_i$, $(a,b)=(\rho v,\phi)$ for FE-SF and $(\rho\phi,v)$ for BL-SF, with $\delta a_i=\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell(a_{i+\ell}-a_{i-\ell})/\Delta x$ of maximum order $2L_{\mathrm s}$ or of DRP type (Eqs. (5)–(6)). **Stated** (definition)
5. For $L_{\mathrm s}=1$ the split flux is $\tfrac14(a_i+a_{i+1})(b_i+b_{i+1})$, against $\tfrac12(a_ib_i+a_{i+1}b_{i+1})$ for the divergence form (Eqs. (7)–(8)). **Derived**
6. One term of the central sum satisfies $\tfrac12\delta^{[\ell]}(ab)_i+\tfrac12a_i\delta^{[\ell]}b_i+\tfrac12b_i\delta^{[\ell]}a_i=\frac2{\Delta x}\big(\{\!\{a\}\!\}_{i,\ell}\{\!\{b\}\!\}_{i,\ell}-\{\!\{a\}\!\}_{i-\ell,\ell}\{\!\{b\}\!\}_{i-\ell,\ell}\big)$, and adding and subtracting $\sum_{m=1}^{\ell-1}$ of the intermediate pairs gives the flux difference with $\hat f^{[\ell]}_{i+1/2}=2\sum_{m=0}^{\ell-1}\{\!\{a\}\!\}_{i-m,\ell}\{\!\{b\}\!\}_{i-m,\ell}$ (§2, Eqs. (9)–(11)). **Derived** *(compiler check, not in the source: verified by expansion and numerically to round-off for $\ell\le4$.)*
7. The full flux is $\hat f_{i+1/2}=2\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell\sum_{m=0}^{\ell-1}\{\!\{a\}\!\}_{i-m,\ell}\{\!\{b\}\!\}_{i-m,\ell}$, Eq. (13) for FE-SF and Eq. (14) for BL-SF (Eq. (12)). Explicit fluxes therefore exist for arbitrary $L_{\mathrm s}$ and also for DRP weights (§2). **Derived**
8. Ducros et al. (2000)'s fluxes for $L_{\mathrm s}\le3$ are recovered from Eq. (14) with maximum-order weights ("It can be shown", §2, p. 7182). **Stated** (not shown)
9. Kennedy–Gruber split (KG-SF): $\alpha_{\mathrm{KG}}\partial_x(\rho v\phi)+\beta_{\mathrm{KG}}\big(v\,\partial_x(\rho\phi)+\rho\,\partial_x(v\phi)+\phi\,\partial_x(\rho v)\big)+(1-\alpha_{\mathrm{KG}}-2\beta_{\mathrm{KG}})\big(\rho v\,\partial_x\phi+\rho\phi\,\partial_xv+v\phi\,\partial_x\rho\big)$, which adds robustness for strong density variations after Kennedy & Gruber (Eq. (15)). **Stated**
10. Conservative approximations of KG-SF "can be recovered only under particular circumstances", namely $\alpha_{\mathrm{KG}}=\beta_{\mathrm{KG}}=\tfrac14$, with flux $2\sum_\ell\mathsf a_\ell\sum_m\{\!\{\rho\}\!\}_{i-m,\ell}\{\!\{v\}\!\}_{i-m,\ell}\{\!\{\phi\}\!\}_{i-m,\ell}$ (Eqs. (16)–(17)), called "density-weighted" because the density is averaged separately (pp. 7182–7183). **Derived** *(compiler check, not in the source: the flux difference reproduces the split derivative to round-off for $\ell\le4$; the whole line $\alpha_{\mathrm{KG}}+3\beta_{\mathrm{KG}}=1$ conserves mass and momentum with central differences, and $\tfrac14,\tfrac14$ is its only kinetic-energy-preserving member, so "only" understates the conservative family; see [split convective forms](/methods/split-convective-forms.md).)*
11. "One can easily prove" that KG-SF with $\alpha_{\mathrm{KG}}=\beta_{\mathrm{KG}}=\tfrac14$ preserves kinetic energy semi-discretely when applied to continuity and momentum (p. 7183). **Stated** (no proof printed)
12. Storing the means for all $i$ and $\ell\le L_{\mathrm s}$ before forming the combinations costs, per node and derivative, $2+2L_{\mathrm s}$ (D-CONV), $6+6L_{\mathrm s}$ (D-FE/BL-SF), $20+14L_{\mathrm s}$ (D-KG-SF), $2+\tfrac72L_{\mathrm s}+\tfrac12L_{\mathrm s}^2$ (C-FE/BL-SF) and, as printed, $1+\tfrac92L_{\mathrm s}+\tfrac12L_{\mathrm s}^2$ (C-KG-SF) operations; the conservative fluxes are cheaper for $L_{\mathrm s}\le6$ (two factors) and $L_{\mathrm s}\le18$ (three), "substantially more efficient" than Ducros et al.'s formulas, and C-KG-SF is "only marginally more expensive" than C-FE-SF (§2, p. 7183, Fig. 1, App. A). **Derived** (the C-KG-SF count is misprinted, see Printed slips)
13. Measured CPU times of the Euler-turbulence runs follow the estimated trend (App. A, Fig. 10: conservative schemes about 1.0 to 2.6–2.8 times second-order D-CONV for $L_{\mathrm s}=1$ to 5, D-FE/BL-SF 1.8 to 2.8, D-KG-SF 2.9 to 5.2, read from the plot). **Shown**
14. Inviscid decaying isotropic turbulence ($32^3$, $E(k)=A(k/k_0)^4\exp[-2(k/k_0)^2]$, $k_0=6$, zero initial temperature and density fluctuations, third-order TVD Runge–Kutta at CFL 1, after Honein & Moin): the divergence-form central schemes diverge in less than one eddy-turnover time at every order (not plotted) (§3.1, Eq. (18)). **Shown** (stated in the text)
15. At $M_{t,0}=0.07$ all split schemes keep the kinetic energy, C-FE-SF and C-KG-SF within 0.6 %, but the rms density drifts upward over long times, more at higher order; second order has the largest energy error and "an odd initial transient" (§3.1, Fig. 2). **Shown**
16. At $M_{t,0}=0.3$ "the standard split forms BL-SF and FE-SF lead to divergence", whereas the density-weighted form "seems to have a strong stabilizing effect", reaching $t/\tau=270$ at every order (read from Fig. 3c) with large density drift, its fourth-order version tending to a nearly statistically steady state (§3.1, Fig. 3). **Shown** (Fig. 3a shows the fourth-order C-BL-SF run reaching $t/\tau\approx245$; see Printed slips)
17. Better physics would need fully discrete energy preservation, the internal-energy or entropy equation, or suitable time integrators, which the paper does not pursue (§3.1). **Stated**
18. Mach 2 spatially developing boundary-layer DNS: recycling/rescaling inflow, $L_z=5\delta_0$, sixth-order C-KG-SF for convection, non-conservative sixth-order viscous terms, classical RK4; $\mathrm{Re}_\theta=1573$ and $\mathrm{Re}_\tau=356$ at $x/\delta_0=25$; grid $\Delta x^+=4.4$, $\Delta z^+=4.5$, $\Delta y^+_w=0.54$, $\Delta y^+=6.1$ at the edge; the D-CONV scheme diverges "in short time" even on this grid (§3.2, Table 1). **Shown**
19. "As pointed out by Ducros et al. [2000], a fully conservative finite-difference discretization using the split form of the convective derivatives is not possible on a mesh with variable spacing"; the paper applies the chain rule and the conservative discretization in computational space instead, "very effective in practice" (§3.2). **Stated** (see [local conservation and flux form](/results/local-conservation-flux-form.md), Contradictions)
20. Van Driest velocity collapses on Wu & Moin's incompressible DNS with a small logarithmic region; transverse rms fluctuations agree with DNS and Erm & Joubert's experiments, the streamwise one differs in the inner layer, attributed to compressibility ($M_t\lesssim0.24$) (§3.2, Eq. (19), Fig. 5). **Shown**
21. Under-resolved grids A–C ($L_{\mathrm s}=3$): non-monotone rms trend with resolution, similar results for the three splits, C-FE-SF "much less robust" and divergent on grid C, C-KG-SF "somewhat" more robust than C-BL-SF on still coarser grids (§3.2, Figs. 6–7). **Shown**
22. Order at grid A with C-BL-SF: second order overestimates the rms peak and the high-wavenumber energy; $L_{\mathrm s}\ge3$ gives adequate outer-layer fluctuations (§3.2, Fig. 8). **Shown**
23. With a spectral error $E_z/E^{\mathrm{DNS}}_z-1$ and an effective bandwidth $k_{\mathrm{eff}}$ at which it first exceeds 0.25, 0.5 or 1 (after Johnsen et al.), $k_{\mathrm{eff}}$ grows with order, and a cost $(2+\tfrac72L_{\mathrm s}+\tfrac12L_{\mathrm s}^2)/k_{\mathrm{eff}}^4$ gives an error-dependent optimal order, up to 10 for strict and down to 6 for rough tolerances (§3.2, Eq. (20), Fig. 9). **Shown** (cost model assumed)
24. Arbitrary-order explicit split schemes "can be properly recast in a locally conservative form" and "therefore yield automatic conservation of total mass, momentum, and energy"; "Apparently, a conservative formulation cannot be arrived at" with compact operators (§4). **Stated** (the compact remark unproved)
25. "Although local conservation cannot be proved on non-uniform grids, the algorithms work out very well in practice"; the experiments show a "significant advantage of the BL-SF and KG-SF (and especially of the latter)" in severely under-resolved, compressible calculations (§4). **Stated**

# Printed slips

- **C-KG-SF cost** (§2, p. 7183): the text prints $1+9/2L+L^2/2$ operations. Fig. 1 plots C-KG-SF at 7, 14, 22, 31, 41, 52 for $L=1,\dots,6$, which is $1+\tfrac{11}2L+\tfrac12L^2$ exactly (the printed formula gives 6, 12, 19, 27, 36, 46), while every other curve of Fig. 1 matches its printed formula. The text's threshold also needs $\tfrac{11}2$: cheaper than D-KG-SF for $L\le18$ ($L^2-17L-38<0$, i.e. $L<19$; with $\tfrac92$ the bound would be $L\le20$). "Only marginally more expensive" than C-FE-SF holds for both (excess $L-1$ with $\tfrac92$, $2L-1$ with $\tfrac{11}2$) and does not decide. *(Compiler check, not in the sources: three pair sums and two products per $\ell$, the $L(L+1)/2$ combinations and one difference give $1+\tfrac{11}2L+\tfrac12L^2$.)*
- **App. A summation** (p. 7189): "requires $\ell-1$ sums for each value of $\ell$, and $L$ multiplications, for a total of $\sum_{\ell=1}^L(1+\ell)=L(L+1)/2$". The printed sum equals $L(L+3)/2$; the stated count is $\sum_\ell\ell=L(L+1)/2$, the value used in $2+\tfrac72L+\tfrac12L^2$. The summand should read $\ell$.
- **"C-FE-BL scheme"** (§3.2, p. 7186) names no scheme; from context it is C-FE-SF.
- **"faster than KG-SF"** (§2, p. 7183): the non-conservative scheme is named D-KG-SF two sentences earlier.
- **Turbulent Mach number** (§3.1, p. 7183): "$M_t=u_{\mathrm{r.m.s.}}/\bar c$ (where the prime indicates the r.m.s. value ...)" — no prime appears, and whether $u_{\mathrm{r.m.s.}}$ is per component or of the magnitude is not said.
- **BL-SF at $M_{t,0}=0.3$**: the text says BL-SF and FE-SF "lead to divergence", but Fig. 3a shows the fourth-order C-BL-SF run reaching $t/\tau\approx245$ (the other orders stop between about 30 and 70). The conclusion's "significant advantage of the BL-SF and KG-SF ... when compressibility plays a significant role" is supported by Fig. 3 for KG-SF only; for BL-SF the support is the boundary-layer robustness.
- Minor: Eq. (10) carries the subscript $j,l$ for $j,\ell$; Table 1 gives $\Delta x^+=4.4$ for the DNS, the text "$\Delta x^+\approx\Delta z^+\approx4.5$"; the captions of Figs. 6–7 name the grids "a, b, c", Table 1 "A, B, C"; the Fig. 1 caption announces a dotted D-CONV line that is not visible in the plot.
- References: [4] (Lilly 1965) is printed in "J. Comput. Phys. 93 (1965) 11–26", a journal that did not exist in 1965 (the work is in Mon. Weather Rev. 93); [1] prints "structures meshes" for "structured meshes"; [13] "Sjgreen" for Sjögreen; [7] "Vasiliev"; [2] omits "for a compressible fluid" from the title.

# Notation map

| Pirozzoli (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x_j=j\,h$, $h$ | $x_i$, $\Delta x$ | $h$ collides with the two-point flux |
| $u$, $u_k$, $u_i$ | $v$, $v_d$ | velocity |
| $\varphi$ | $\phi$ (page-local) | transported scalar: 1, $v_d$, $H$ |
| $\rho$, $p$, $\gamma$, $H$ | $\rho$, $p$, $\gamma$, $H$ | agree |
| $f$, $g$, $h$ (generic factors) | $a$, $b$, $c$ (page-local) | registry $f$ is the flux; $a$ is not the wave speed |
| $D$, $D^\ell$ | $\delta$, $\delta^{[\ell]}$ (page-local) | explicit central derivative and its half-width-$\ell$ difference; not the SBP matrix $D$ |
| $D_S$, $D^\ell_S$ | $\delta^{\mathrm{sp}}$, $\delta^{\mathrm{sp}}_{[\ell]}$ | split central derivative ([operator page](/operators/conservative-split-derivative.md)) |
| $L$, $a_\ell$ | $L_{\mathrm s}$, $\mathsf a_\ell$ | half-width (order $2L_{\mathrm s}$) and weights, as on flux differencing; $L$ is the left-eigenvector matrix |
| $(\widetilde{f,g})_{j,\ell}$ | $\{\!\{a\}\!\}_{i,\ell}\{\!\{b\}\!\}_{i,\ell}$ | $\{\!\{a\}\!\}_{i,\ell}=\tfrac12(a_i+a_{i+\ell})$ |
| $(\widetilde{f,g,h})_{j,\ell}$ | $\{\!\{a\}\!\}_{i,\ell}\{\!\{b\}\!\}_{i,\ell}\{\!\{c\}\!\}_{i,\ell}$ | |
| $\hat f_{j+1/2}$, $\hat f^\ell_{j+1/2}$ | $\hat f_{i+1/2}$, $\hat f^{[\ell]}_{i+1/2}$ | brackets keep $\hat f^{(k)}$ for WENO candidates |
| $\alpha$, $\beta$ (Eq. (15)) | $\alpha_{\mathrm{KG}}$, $\beta_{\mathrm{KG}}$ (page-local) | keep $\alpha_k$, $\beta_k$ free |
| FE-SF, BL-SF, KG-SF; prefixes D-, C- | Feiereisen, Blaisdell, Kennedy–Gruber split; direct and conservative discretizations | KG-SF at $\tfrac14,\tfrac14$ is the KGP row of the split family |
| $N$ (nodes), $N_{op}$ | $N_x$, $N_{\mathrm{op}}$ (page-local) | |
| $M_t$, $M_{t0}$, $\bar c$ | $M_t$, $M_{t,0}$, $\bar c$ (page-local) | registry $M$ is the Mach number |
| $T=\int\rho u^2dV$ | $2\int\kappa\,dV$ | no ½ in the paper |
| $E(k)$, $k_0$, $A$, $\tau$ | page-local | $E$ is the registry's total energy |
| $M_\infty$, $\delta_{in}$, $\delta^+$, $Re_\theta$ | $M_\infty$, $\delta_0$, $\mathrm{Re}_\tau$, $\mathrm{Re}_\theta$ | |
| $\epsilon(k_z)$, $\bar\epsilon$, $k_{eff}$, $C$ | $\varepsilon_{\mathrm{sp}}(k_z)$, $\bar\varepsilon_{\mathrm{sp}}$, $k_{\mathrm{eff}}$, $N_{\mathrm{op}}/k_{\mathrm{eff}}^4$ (page-local) | keeps $\epsilon$ for WENO |
| $u_{vd}$ | $v_{\mathrm{vd}}$ | van Driest velocity |

# Reference list

The paper prints 25 references, numbered [1]–[25] in order of first citation, merged complete
into the [bibliography](/bibliography.md) with `citedby` including `pirozzoli-2010`. Nineteen
reuse existing keys; six are new (Larsson et al. 2007, Kraichnan 1955, Wu & Moin 2009, Erm &
Joubert 1991, Smits & Dussauge 2006, and the in-press form of [22]). [1] is Ducros et al.
(2000), not the ingested [Ducros et al. (1999)](/sources/ducros-1999.md). [22], printed
"J. Fluid Mech., in press", is kept as its own entry `pirozzoli-2010-c` per the bundle's
preprint rule; its published form is `pirozzoli-2010-b` (J. Fluid Mech. 657:361–393). [18] is
Shu & Osher (1989), part II, not the ingested [Shu & Osher (1988)](/sources/shu-1988.md). [4]
carries a wrong journal (see Printed slips); [5] prints the publisher Kluwer, Dordrecht; [12]
is a CTR Annual Research Briefs without pages; [14] prints the report number "TF 13". No DOIs
are printed in the list.

# Pages created or updated

Chunk 14 (2026-11-17). This source is cited on:

* [Compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Conservative split central derivative](/operators/conservative-split-derivative.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
* [URANOS](/software/uranos.md)
