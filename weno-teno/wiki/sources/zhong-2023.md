---
type: Source
title: "Zhong et al. (2023) — An improved fifth-order WENO scheme with symmetry-preserving smoothness indicators for hyperbolic conservation laws"
description: "Fifth-order finite-volume WENO (IMWENO-P) whose local smoothness indicators, built from the WENO-NS difference blocks with the parameter fixed to the cell width, satisfy a mirror-symmetry condition on their coefficients, paired with a squared fourth-difference global indicator and Z-type weights; tested on critical-point, Euler and instability problems."
resource: "doi:10.1016/j.jcp.2023.112350"
source_kind: paper
authors: [Zhong W., Wang S., Qiu J., Gao J.]
year: 2023
venue: "J. Comput. Phys. 491:112350"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Zhong_An_improved_fifth-order_WENO_scheme_with_symmetry-preserving.pdf"
tags: [weno, smoothness-indicator, weno-weights, critical-points, finite-volume]
timestamp: 2026-10-23T23:00:00Z
---

# Summary

Zhong, Wang, Qiu & Gao revise the fifth-order finite-volume WENO schemes that use the
$L^1$-type indicators of Ha et al. (WENO-NS), the re-weighted WENO-P of Kim et al. and the
MWENO-P of Rathan & Naga Raju. They criticize these schemes on two counts. First, their local
[smoothness indicators](/definitions/smoothness-indicator.md) depend on one or two tunable
parameters. Second, they violate a *symmetry-preserving property* that the indicators of
WENO-JS, [WENO-Z](/methods/weno-z.md), mapped WENO, WENO-ZS and WENO-η all have: the
coefficients inside the squared terms of $\beta_k$ and $\beta_{2-k}$ are mirror images about
the centre cell. This is a coefficient-level notion, distinct from the solution-level
[symmetry preservation](/properties/symmetry-preservation.md) of symmetric flows, which the
scheme still breaks in a Rayleigh–Taylor run.

The new scheme, IMWENO-P, builds symmetric indicators from the WENO-NS difference blocks with
the parameter fixed to the cell width $\Delta x$. It pairs them with a global indicator equal
to the squared five-point undivided fourth difference and Z-type weights with exponent $q=1$.
A Taylor analysis claims $\omega_k-d_k=O(\Delta x^3)$ away from critical points and at first-
and second-order critical points ([critical-point accuracy](/properties/critical-point-accuracy.md)).
At second-order critical points the printed chain supports only $O(\Delta x^2)$. Numerically,
IMWENO-P keeps fifth order on $\sin^3(\pi x)$, where WENO-JS, WENO-Z, WENO-NS and WENO-P drop
to about third order. It also gives the smallest error growth in long-time advection.

The 1D Euler tests are [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md), the
[Shu–Osher](/benchmarks/shu-osher-problem.md) and Titarev–Toro problems, and a low-density
[double rarefaction](/benchmarks/double-rarefaction-problem.md). The 2D tests are
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) instabilities,
[2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md), the
[forward-facing step](/benchmarks/forward-facing-step.md) and vortex pairing on a stretched
mesh. [Burgers](/benchmarks/burgers-equation-tests.md) tests are added. IMWENO-P resolves more
fine structure than the other schemes. On the double rarefaction, WENO-NS, WENO-P and MWENO-P
produce negative pressure and fail, while IMWENO-P and the symmetric-indicator schemes run;
the authors decline to link symmetry to positivity.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 491, 112350), 29 pages, DOI printed on
page 1; received 14 Dec 2022, online 17 Jul 2023. Title, authors and venue match Crossref; no
identity problem. Numbering is that of the version of record.

# Key claims

Registry notation: cell index $i$, cell averages $\bar u_i$, width $\Delta x$, stencils $S_k$
($S_0$ most upwind), linear weights $d_k=(0.1,0.6,0.3)$. Page-local: the WENO-NS difference
blocks $\mathsf L_{1,k}u=(1-k)\bar u_{i-2+k}+(2k-3)\bar u_{i-1+k}+(2-k)\bar u_{i+k}$ and
$\mathsf L_{2,k}u=\bar u_{i-2+k}-2\bar u_{i-1+k}+\bar u_{i+k}$; the IMWENO-P indicators
$\beta^{\mathrm{IMP}}_k$ and global indicator $\tau^{\mathrm{IMP}}$; derivatives $u^{(m)}$ at
$x_{i+1/2}$.

1. The indicators of WENO-JS, WENO-Z, mapped WENO, WENO-ZS and WENO-η satisfy the coefficient relations of Eq. (19), compactly $c(\beta_k,P_{k,m},\bar u_{i-n})=(-1)^{km}c(\beta_{2-k},P_{2-k,m},\bar u_{i+n})$ (Eq. (20)), where $c$ is the coefficient of $\bar u$ inside the $m$th squared term $P_{k,m}$; the authors name this the symmetry-preserving property (§3.1, Table 1, Fig. 1). **Stated** (Table 1)
2. The indicators of WENO-NS (Eq. (12)), WENO-P and MWENO-P (Eq. (15)) do not satisfy it (§3.2, abstract, §1). **Stated**. *(compiler check, not in the sources)*: $\mathsf L_{1,0}u=\bar u_{i-2}-3\bar u_{i-1}+2\bar u_i$ while $\mathsf L_{1,2}u=\bar u_{i+1}-\bar u_i$, so the WENO-NS $\beta_0$ and $\beta_2$ are not mirror images.
3. WENO-P and MWENO-P rely on two user-tunable parameters, WENO-NS on one (§1, abstract). **Stated**
4. The new indicators are $\beta^{\mathrm{IMP}}_k=\xi_{\mathrm{NS}}(2\mathsf L_{1,k}u-k\mathsf L_{2,k}u)^2+(\mathsf L_{2,k}u)^2$ with $\xi_{\mathrm{NS}}=\Delta x$ (Eq. (21)), explicitly $\beta^{\mathrm{IMP}}_0=4\Delta x(\bar u_{i-2}-3\bar u_{i-1}+2\bar u_i)^2+(\bar u_{i-2}-2\bar u_{i-1}+\bar u_i)^2$, $\beta^{\mathrm{IMP}}_1=\Delta x(\bar u_{i-1}-\bar u_{i+1})^2+(\bar u_{i-1}-2\bar u_i+\bar u_{i+1})^2$, $\beta^{\mathrm{IMP}}_2=4\Delta x(2\bar u_i-3\bar u_{i+1}+\bar u_{i+2})^2+(\bar u_i-2\bar u_{i+1}+\bar u_{i+2})^2$ (Eq. (22)). Definition (contribution)
5. Lemma 1: the coefficients of $\beta^{\mathrm{IMP}}_k$ satisfy Eq. (20); "the proof … is straightforward and therefore omitted" (§3.2). **Stated** (proof omitted)
6. The global indicator is $\tau^{\mathrm{IMP}}=(\mathsf L_{1,0}u-\mathsf L_{1,1}u-\mathsf L_{2,1}u+\mathsf L_{2,2}u)^2=(\bar u_{i-2}-4\bar u_{i-1}+6\bar u_i-4\bar u_{i+1}+\bar u_{i+2})^2$ (Eqs. (23)–(24)), itself symmetric (Eq. (25)). The weights are $\alpha_k=d_k\big(1+(\tau^{\mathrm{IMP}}/(\beta^{\mathrm{IMP}}_k+\epsilon))^q\big)$ with $q=1$ (Eq. (26)). Definition (contribution)
7. $\tau^{\mathrm{IMP}}=\big(\Delta x^4u^{(4)}+O(\Delta x^5)\big)^2=\Delta x^8(A+O(\Delta x))$ (Eq. (29)). **Derived**
8. Taylor expansions of $\mathsf L_{n,k}u$ (Eq. (27), from Theorem 3.2 of Ha et al.) and of $\beta^{\mathrm{IMP}}_k$ through $\Delta x^5$ (Eq. (28)). **Derived**
9. Away from critical points, $\beta^{\mathrm{IMP}}_k=4(u')^2\Delta x^3+O(\Delta x^4)$ (Eq. (30)) and $\omega_k=(d_k+O(\Delta x^6))/(1+O(\Delta x^6))$ (Eq. (31) ff.). **Derived**
10. At a first-order critical point ($u'=0$, $u''\ne0$), $\beta^{\mathrm{IMP}}_k=(u'')^2\Delta x^4+O(\Delta x^5)$ (Eq. (32)) and $\omega_k=(d_k+O(\Delta x^5))/(1+O(\Delta x^5))$ (Eq. (33) ff.). **Derived**
11. At a second-order critical point ($u'=u''=0$, $u'''\ne0$), $\beta^{\mathrm{IMP}}_0=\tfrac94(u''')^2\Delta x^6+O(\Delta x^7)$ and $\beta^{\mathrm{IMP}}_1=\beta^{\mathrm{IMP}}_2=\tfrac14(u''')^2\Delta x^6+O(\Delta x^7)$ (Eq. (34)). The paper concludes $\omega_k=d_k+O(\Delta x^3)$ for $k=0,1,2$ (Eqs. (40)–(41)), so the sufficient condition (11) holds. **Derived** as printed, but the printed chain gives only $O(\Delta x^2)$ (see Printed slips)
12. Larger $q$ brings the scheme closer to the linear-weight scheme in smooth regions. Smaller $q$ raises the relative weight of the discontinuous substencil and makes the scheme less dissipative; $q=1$ throughout (§3.2 after Eq. (26)). **Stated**
13. The technique is "limited only to the fifth-order case if no further modifications are done" (§3.2). **Stated**
14. Example 1 ($\sin(\pi x)$, $t=2$): all schemes reach fifth order. The IMWENO-P errors equal those of MWENO-P and WENO-Z to the printed digits ($L_1$ $5.39\times10^{-11}$ at $N=500$, order 4.90); WENO-JS has $3.05\times10^{-10}$ (Table 2). **Shown**
15. Example 2 ($\sin(\pi x-\sin(\pi x)/\pi)$): the WENO-JS order drops to about 4.19 ($L_1$) and 3.69 ($L_2$) at $N=500$; IMWENO-P reaches 5.00 and 5.00 with $L_1$ $5.13\times10^{-10}$ (Table 3). **Shown**
16. Example 3 ($\sin^3(\pi x)$, a second-order critical point at $x=0$): WENO-JS, WENO-Z, WENO-NS and WENO-P fall to $L_1$ orders of about 3.3–3.6 and $L_2$ orders of about 2.9–3.1. MWENO-P and IMWENO-P keep about 5 (IMWENO-P $L_1$ orders 4.94, 5.15, 5.11, 5.08; $L_1$ $8.17\times10^{-9}$ at $N=500$ against $8.10\times10^{-9}$ for MWENO-P) (Table 4). **Shown**
17. Example 4 ($\sin^9(\pi x)$, $\Delta x=1/100$, to $t=1000$): the error increase relative to the linear-weight scheme at $t=1000$ is, in $L_1$, 3647.36 % (WENO-JS), 1731.20 % (WENO-Z), 233.83 % (WENO-NS), 443.06 % (WENO-P), 9.28 % (MWENO-P) and −0.53 % (IMWENO-P). In $L_2$ it is 3538.77 %, 1967.84 %, 252.15 %, 536.40 %, 8.58 % and 1.87 % (Table 5, Eq. (42)). **Shown**
18. Example 5 (Burgers, $t=0.15$): IMWENO-P is about fifth order, $L_1$ $3.30\times10^{-9}$ at $N=320$ against $1.63\times10^{-8}$ for WENO-JS (Table 6). **Shown**
19. In CPU time against $L_2$ error (Examples 1–3), IMWENO-P has the "lowest and second lowest efficiency for Example 1 and Example 2 respectively". IMWENO-P and MWENO-P have "much higher efficiency" than WENO-JS, WENO-Z, WENO-NS and WENO-P on Example 3. No hardware or absolute times are printed (§4.2, Fig. 4). **Shown**
20. On the low-density, low-internal-energy Riemann problem ($N=300$, $t=0.15$), WENO-NS, WENO-P and MWENO-P "fail to finish the simulation". IMWENO-P, WENO-JS, WENO-Z, WENO-η and WENO-ZS succeed. At $N=30$, $t=0.0295$ the three failing schemes produce negative pressure (Ex. 10, Figs. 9–10). **Shown**
21. "The numerical phenomenon discussed above is not enough to link the symmetry-preserving property with the positivity-preserving property"; the symmetry-preserving schemes "are more stable numerically than other ones at least for the present test" (Ex. 10). **Stated** (hedged by the authors)
22. The symmetry error (Eqs. (45)–(46)) of IMWENO-P on Example 10 is the smallest of the schemes for about $0.041<t<0.093$. For $t>0.093$ it is at the level of WENO-JS, WENO-Z and WENO-η, and much smaller than WENO-ZS (Figs. 11–12). **Shown**
23. On the Shu–Osher (Ex. 8) and Titarev–Toro (Ex. 9) problems IMWENO-P has the highest resolution. On Titarev–Toro, WENO-P "falsely amplifies the smooth waves in front of and closely behind the main shock wave" (Figs. 7–8). **Shown**
24. In the Rayleigh–Taylor run (Ex. 11) IMWENO-P resolves finer structures than WENO-JS and WENO-Z, but its solution "still shows a symmetry-broken phenomenon"; the authors refer to Don et al. for remedies (Fig. 13). **Shown**
25. On 2D Riemann configuration 13 (Ex. 14) at $800\times800$, only IMWENO-P captures the slip-line instability. At $1200\times1200$ IMWENO-P and MWENO-P resolve it, WENO-JS, WENO-Z and WENO-P do not, and WENO-NS does so "very slightly" (Figs. 16–19). **Shown**
26. Weak solutions of the 2D Euler equations are not unique; the small-scale structures of such tests are set by scheme and mesh and "usually are non-physical", though widely used to compare dissipation (§4.4, Ex. 13). **Stated** (cited)
27. On non-uniform meshes the parameter becomes $\xi_{\mathrm{NS},x}=\min\{\Delta x_{i-2},\dots,\Delta x_{i+2}\}$, and likewise in $y$. On the stretched vortex-pairing mesh, IMWENO-P and MWENO-P give better temperature contours than WENO-JS, WENO-Z, WENO-NS and WENO-P (Ex. 17, Fig. 22). **Shown**

# Printed slips

- Eqs. (40)–(41), second-order critical point: the chain gives $\omega_0=d_0\tilde D^{k=0}_{\Delta x}(1+O(\Delta x^3))/\big[\tilde D^{k=0}_{\Delta x}(1+O(\Delta x^2))\big]$ and concludes "$=d_0+O(h^3)$"; the ratio is only $1+O(\Delta x^2)$. *(compiler check, not in the sources)*: expanding the cell averages of a smooth $u$ with $u'=u''=0$ at $x_{i+1/2}$ reproduces Eq. (34) and $\tau^{\mathrm{IMP}}=(u^{(4)})^2\Delta x^8+O(\Delta x^9)$. It then gives $\alpha_k=d_k(1+c_k\tilde D\Delta x^2+O(\Delta x^3))$, $c_0=\tfrac19$, $c_1=c_2=1$, $\tilde D=(2u^{(4)}/u''')^2$, hence $\omega_0-d_0=-\tfrac89d_0(1-d_0)\tilde D\Delta x^2+O(\Delta x^3)=-\tfrac{8}{25}\big(u^{(4)}/u'''\big)^2\Delta x^2+O(\Delta x^3)$, non-zero whenever $u^{(4)}\ne0$. The printed analysis does not establish the sufficient condition $O(\Delta x^3)$ at second-order critical points; the fifth order there rests on Table 4.
- §2.4, last sentence: WENO-P weights are said to be "in Eq. (14)"; Eq. (14) is WENO-NS, WENO-P is Eq. (16).
- Eqs. (35), (37), (39): the superscript is typeset "$s=1.2$" for "$s=1,2$".
- Example 2: "the solution satisfies $u'=0$ and $u'''\neq0$". *(compiler check, not in the sources)*: with $g(x)=\pi x-\sin(\pi x)/\pi$, $g'=\pi-\cos(\pi x)>0$, and where $u'=\cos(g)\,g'=0$ one has $u''=-\sin(g)\,g'^2\ne0$. The critical points are first order, as §4.2 itself says ("Example 1 and Example 2 … only have first-order critical points").
- Example 17: the domain is printed as $[0,30]\times[-50,50]$, while the mapping (52), $x=\frac{L_x}2\sinh(s_x\eta)/\sinh(s_x)$ with $\eta\in[-1,1]$, covers $[-15,15]$ in $x$ (a shift only, periodic direction).
- Ref. [35]: "NASA Technidal Memorandum".

# Notation map

| Zhong et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$ (cell index), $\bar u_j$ | $i$, $\bar u_i$ | finite volume; bars dropped inconsistently in Eq. (13) |
| $h$, $\Delta x$ | $\Delta x$ | both used for the cell width |
| $u^L_{j+1/2}$, $u^R_{j+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| $s$ (stencil index), $u^s_{j+1/2}$ | $k$, $u^{(k)}_{i+1/2}$ | $S_0$ leftmost, agrees |
| $d_s$ | $d_k$ | $(0.1,0.6,0.3)$ |
| $\beta_s$ (LSI), $\tilde\beta_s$ (WENO-P) | $\beta_k$, $\tilde\beta_k$ | |
| $\bar\beta_s$ | $\beta^{\mathrm{IMP}}_k$ (page-local) | **collision**: the bar is the registry's cell average |
| $P_{s,m}$, $c(\beta_s,P_{s,m},\bar u_k)$ | $P_{k,m}$, $c(\cdot)$ (page-local) | $m$th squared term and its coefficients; **collision** with the CWENO $P_k$ (§10) |
| $L_{n,s}u$ | $\mathsf L_{n,k}u$ (page-local) | **collision** with the left-eigenvector matrix $L$ and the operator $\mathcal L$ |
| $\xi$ | $\xi_{\mathrm{NS}}$ (page-local) | weight of the first-difference term; **collision** with the DG nodes $\xi_j$ |
| $\delta$ | $\delta$ (page-local) | WENO-P skew parameter; not the TENO flag $\delta_k$ |
| $\tau$ | $\tau_5$ | WENO-Z global indicator |
| $\zeta$, $\tilde\zeta$, $\eta$ | WENO-NS, WENO-P and MWENO-P global indicators (page-local) | **collisions**: $\zeta$ characteristic variables (§10), $\eta$ entropy |
| $\bar\zeta$ | $\tau^{\mathrm{IMP}}$ (page-local) | squared undivided fourth difference |
| $q$ | $q$ | weight exponent; agrees ($q=1$) |
| $\epsilon$ | $\epsilon$ | $10^{-40}$ in all tests |
| $\alpha$ (LF) | $a$ | global maximum wave speed |
| $u^{(k)}_{j+1/2}$ | $u^{(m)}$ at $x_{i+1/2}$ (page-local) | **collision**: registry $u^{(k)}$ is a stencil value |
| $D$, $\hat D$, $\tilde D$; $D_h$ | page-local constants; $D_{\Delta x}$ | |
| $L(u)$ | $\mathcal L$ | spatial operator |
| $\chi_1$, $\chi_2$ | error increase over the linear-weight scheme (page-local) | Eq. (42) |
| $E_x$, $E_s$ | symmetry errors (page-local) | Eqs. (45)–(46) |
| WENO5-ILW | linear-weight fifth-order scheme | the paper also calls it "the corresponding central-upwind scheme"; not a [central-upwind scheme](/methods/central-upwind-scheme.md) |

# Reference list

The paper prints 68 references, numbered [1]–[68]. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` including `zhong-2023`. Same-author same-year
works take suffixes in printed order: Harten 1987 [8]/[9], Fan 2014 [12]/[23], Hong 2020
[21]/[28], Li & Zhong 2022 [16]/[49] and 2023 [20]/[48]/[50]. Several Li & Zhong works and
Luo & Wu [42] share author–year keys with different Source pages and are re-keyed at the
merge. Printed items worth noting: [17] prints pages "3101–3211", [63] "SIAM J. Math. Anal.
24 (1998)", and [66] lists "P. Woodward, P. Colella" among its authors (the authors of [65]).
No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunk 7 (2026-10-23). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO-Z weights](/methods/weno-z.md)
