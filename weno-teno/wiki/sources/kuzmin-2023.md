---
type: Source
title: "Kuzmin & Vedral (2023) — Dissipation-based WENO stabilization of high-order finite element methods for scalar conservation laws"
description: "Continuous-Galerkin finite elements stabilized by a cellwise blend of high-order projection stabilization and low-order artificial viscosity, with the blending factor computed from the deviation of the solution from a Hermite WENO reconstruction that never overwrites it, plus an O(h^{N+1/2}) consistency analysis."
resource: "doi:10.1016/j.jcp.2023.112153"
source_kind: paper
authors: [Kuzmin D., Vedral J.]
year: 2023
venue: "J. Comput. Phys. 487:112153"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Kuzmin_Dissipation-based_WENO_stabilization_of_high-order_finite_el.pdf"
tags: [weno, limiting]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper proposes
[dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md) for
high-order continuous Galerkin (CG) finite elements solving scalar conservation laws. It also
offers the method as an alternative to WENO limiters in
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) schemes.

RKDG schemes overwrite the solution in troubled cells with a WENO reconstruction. CG-WENO never
modifies the solution. It computes a [Hermite WENO](/methods/hermite-weno.md) reconstruction
$u_h^{e,*}$ only to measure how far the finite-element polynomial $u_h^e$ deviates from it. The
deviation sets a cellwise blending factor $\varsigma_e\in[0,1]$. This factor acts as a
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) of smoothness type: it is
measured in a scaled Sobolev seminorm that generalizes the Jiang–Shu
[smoothness indicator](/definitions/smoothness-indicator.md).

$\varsigma_e$ blends two stabilizations:

- an accuracy-preserving symmetric projection stabilization;
- a low-order isotropic [artificial viscosity](/methods/artificial-viscosity.md)
  $\mu_e=a_eh_e/(2N)$.

The result is a high-order multidimensional finite-element analogue of the Jameson–Schmidt–Turkel
scheme. The Hermite candidates come from von Neumann neighbours and are combined with
[Jiang–Shu-type nonlinear weights](/methods/weno-js-reconstruction.md).

The analysis treats the steady advection–reaction problem with the Strang-lemma tools of algebraic
flux correction. In the worst case the consistency error is $O(h^{1/2})$; for smooth solutions it
is $O(h^{N+1/2})$. An a priori estimate follows under an assumed Lipschitz condition, and the method
reproduces polynomials of degree $\le N$ exactly.

The tests use MFEM with $\mathbb Q^N$ elements, $N=1,\dots,4$. The method attains $L^1$ order about
$N+1$ on smooth advection and on Burgers before the shock. It captures discontinuities with almost
no overshoot, and it handles solid-body rotation. On the [KPP rotating wave](/benchmarks/kpp-rotating-wave.md)
it reproduces the entropy spiral where plain CG and high-order-only stabilization fail, which ties
the method to [entropy stability](/properties/entropy-stability.md). The authors point to
[convex limiting](/methods/convex-limiting.md) and algebraic flux correction as the way to add
strict bounds on top.

# Version read

The file is arXiv:2212.14224v1 [math.NA] of 29 Dec 2022, with the footer "Submitted to J. Comput.
Phys. special issue in honor of Prof. Roland Glowinski, January 2, 2023". It is not the version of
record. It has 28 pages, all read; the formulas on pp. 5–8, 11–12 and 18–20 were checked visually.
Page 1 matches the published title and authors, so there is no identity issue. All numbers cited
here are the preprint's.

# Key claims

1. Unstabilized CG for linear advection on general meshes converges only as
   $\|u-u_h\|_{L^2}=O(h^N)$; a properly stabilized CG method reaches $O(h^{N+1/2})$. (§2) **Stated**
2. The low-order artificial diffusion (4), with $\mu_e=a_eh_e/(2N)$, introduces an $O(h^{1/2})$
   consistency error. (§3, §6) **Derived**
3. VMS stabilization (5) with $\|g_h-\nabla u_h\|_{L^2}=O(h^N)$ has consistency error
   $O(h^{N+1/2})$. (§3, §6) **Derived**
4. Lohmann et al.: in 1D, VMS stabilization (5) with the consistent-mass $L^2$ projection $g_h$ of
   $\nabla u_h$ is equivalent to a consistent SUPG method. (§3) **Stated**
5. The nonsymmetric VMS form (5) "may produce entropy". The symmetric form (7) is coercive,
   $s^{e,H}_h(v_h,v_h)\ge0$, and therefore "truly dissipative". (§3) **Stated**
6. The blended operator (8) reduces to the low-order operator (4) for $\varsigma_e=0$, and to the
   high-order operator (7) for $\varsigma_e=1$ with the scaling $\omega_{\mathrm H}=1$. (§3) **Derived**
7. On order barriers for bound preservation:
   - schemes of order above 2 cannot in general be locally bound preserving;
   - global bounds impose no order barrier (Zhang–Shu);
   - local discrete maximum principles impose a second-order barrier.

   (§1, §3) **Stated**
8. CG-WENO does not overwrite $u_h^e$ with $u_h^{e,*}$; the reconstruction only feeds $\varsigma_e$.
   The semi-discrete scheme therefore keeps the structure of a CG method, while overwriting DG
   approaches "have more in common with finite volume methods". (Remark 2) **Stated**
9. The seminorm (10) involves only derivatives, so the cell-average correction in (11) does not
   affect $\varsigma_e$ and is unnecessary in practice. (Remark 3) **Derived**
10. A smaller linear weight $d_0$ on the central (identity) candidate makes shock detection more
    reliable and the nonlinear stabilization stronger. (§5; KPP with $d_k=0.2$) **Stated / Shown**
11. For fixed $u_h$, $s_h(u_h;\cdot,\cdot)$ is a symmetric positive semidefinite bilinear form and
    satisfies a Cauchy–Schwarz inequality (15). (§6) **Derived**
12. Strang-type bound (16):
    $\|u-u_h\|_h\le\|u-I_hu\|_a+\sup_{w_h}a(u-I_hu,w_h)/\|w_h\|_h+\sqrt{s_h(u_h;I_hu,I_hu)}$. The
    first two terms are $O(h^N)$. (§6, after Lohmann) **Derived**
13. In the worst case $\sqrt{s_h(u_h;I_hu,I_hu)}=O(h^{1/2})$. If the high-order part dominates a
    posteriori, it is $O(h^{N+1/2})$. (§6) **Derived**
14. Polynomial reproduction: if $u_h$ is a polynomial of degree $\le N$ on the union of the
    stencils, then $\|u_h^e-u_h^{e,*}\|_e=0$ and $\varsigma_e=1$ for any nonlinear weights. Polynomial
    exact solutions are therefore reproduced exactly. (Remark 6) **Proved**
15. Main estimate (17): for $u\in C^{N+1}(\bar\Omega)$ and $\mathsf q=2$,
    $\sqrt{s_h(I_hu;I_hu,I_hu)}=O(h^{N+1/2})$. A Taylor-basis expansion gives
    $\|v_h^e-v_h^{e,*}\|_e^2=O(h^{2N+2})$, and the low-order part is $O(h^{2N+1})$. (§6,
    eqs. (17)–(18)) **Derived** (a "preliminary" formal analysis)
16. Under the assumed Lipschitz condition
    $|s_h(u_h;v_h,v_h)-s_h(v_h;v_h,v_h)|\le s_h(u_h;v_h-u_h,v_h-u_h)$ for $v_h=I_hu$, the a priori
    bound
    $\|u-u_h\|_a\le\|u-I_hu\|_a+\sup(\cdot)+\sqrt{s_h(I_hu;I_hu,I_hu)}$
    follows. (§6) **Derived** (conditional on an unverified assumption)
17. The $O(h^{N+1/2})$ estimate is "optimal for general meshes". On uniform meshes with smooth
    solutions the observed rate is $N+1$. (Abstract, §7) **Stated / Shown**
18. Smooth 1D advection of $\cos(2\pi(x-0.5))$ to $t=1$ with $\mathsf q=3$: CG, VMS and WENO all give
    $L^1$ order about $N+1$ for $N=1,\dots,4$. The finest-grid WENO errors are:

    | $N$ | $N_h$ | error | order |
    |---|---|---|---|
    | 1 | 1024 | 2.06e-6 | 2.01 |
    | 2 | 1024 | 7.90e-9 | 3.00 |
    | 3 | 1536 | 4.05e-11 | 3.97 |
    | 4 | 512 | 4.30e-11 | 5.08 |

    The pre-asymptotic WENO orders are irregular, for example 3.77 for $N=1$ and 6.01 for $N=4$.
    (Table 1) **Shown**
19. Advection of a mixed discontinuous and smooth profile, $N_h=200$. The solution ranges are:

    | stabilization | $N=1$ | $N=2$ | $N=4$ |
    |---|---|---|---|
    | WENO | $[-0.0066,1.0066]$ | $[-0.0013,1.0013]$ | $[0.0000,0.9999]$ |
    | CG | $[-0.2210,1.1725]$ | $[-0.2704,1.3186]$ | $[-0.3303,1.2257]$ |
    | HO | $[-0.0564,1.0564]$ | $[-0.0821,1.0821]$ | $[-0.1557,1.1560]$ |

    LO is nonoscillatory but smeared (maximum about 0.8424–0.8428). (Table 2, Fig. 1) **Shown**
20. Burgers with $u_0=\sin(2\pi x)$ to $t=0.1$, before the shock time $t_c=1/(2\pi)$: WENO attains
    the optimal orders. Plain CG attains $N+1$ for odd $N$ but drops to $N$ for even $N$:
    - $N=2$: CG 2.01, WENO 3.00;
    - $N=4$: CG 4.04, WENO 5.10.

    (Table 3) **Shown**
21. Burgers to $t=1$, after the shock, $N_h=200$:
    - high-order dissipation alone is unsuitable for shock capturing and oscillates;
    - LO is nonoscillatory, and less diffusive than in linear advection;
    - WENO is sharper still;
    - LO and WENO change little with $N$ at fixed $N_h$.

    (Fig. 2) **Shown**
22. Solid-body rotation, $N_h=129^2$, $t=1$:
    - CG oscillates globally;
    - HO overshoots strongly at the slotted cylinder;
    - LO is very diffusive;
    - WENO is superior for all $N$.

    For $N=1$, the errors $E_1$ are 3.70e-2 (CG), 1.47e-2 (HO), 1.10e-1 (LO) and 2.68e-2 (WENO, with
    $u_h\in[-0.001,0.993]$). For $N=4$, WENO gives $E_1=2.76\mathrm{e}{-2}$ with
    $u_h\in[0.000,0.998]$. HO has the smallest $E_1$ despite its overshoots. (Figs. 3–5) **Shown**
23. KPP, $N_h=129^2$, $t=1$:
    - lumped-mass CG oscillates and produces an entropy-violating shock;
    - HO reduces the oscillations but does not cure the lack of entropy stability;
    - LO and WENO are nonoscillatory and reproduce the spiral entropy solution.

    The WENO ranges are $[0.785,10.990]$ ($N=1$), $[0.785,10.983]$ ($N=2$) and $[0.778,10.980]$
    ($N=4$). The small undershoot for $N=4$ is attributed to the cell-based indicator on a coarse
    mesh. (Figs. 6–8, §7.4) **Shown** (that it disappears under refinement is **Stated**)
24. If needed, algebraic flux correction can strictly enforce global bounds and entropy inequalities
    on top of CG-WENO, which was designed as a baseline for accuracy-preserving flux limiting.
    (§7.4) **Stated**
25. The hybrid has the structure of a nonlinear artificial-diffusion method. It is therefore "easier
    to analyze than DG-WENO schemes in which partial derivatives of approximate solutions are
    manipulated directly". (§8) **Stated**

# Printed slips

- **§6, definition of $s_h(u_h;v_h,w_h)$.** The low-order part is printed with
  $\int_{K_e}\nabla w_h\cdot\nabla u_h\,dx$. For the form to be bilinear in $(v_h,w_h)$, as the next
  sentence asserts, the factor must be $\nabla v_h$.
- **§6, p. 12, low-order estimate.** It is printed with integrand $|v_h|^2$ and norm
  $\|v_h^e\|^2_{L^2(\Omega)}$. The integrand should be $|\nabla v_h|^2$, with a gradient norm on
  $K_e$.
- **§6, p. 12.** The left side is printed as $D^kv^e_{h,l}-D^kv^e_{h,0}$, while the right side sums
  over $l$. It should be $D^kv_h^{e,*}-D^kv^e_{h,0}$.
- **§6, p. 11.** The triangle-inequality term $\|\pi_h(\nabla u-I_h\nabla u)\|$ should read
  $\pi_h(\nabla u-\nabla I_hu)$.
- **Eq. (8).** Stray comma after the first integral.
- **Remark 2.** "a GG method" should be "a CG method".
- **§5.** The nonlinear reconstruction is printed $\tilde u_h^{e,*}$ here and $u_h^{e,*}$
  elsewhere.
- **§7.** "$g_h=\pi_e\nabla u_h$": $\pi_e$ denotes the cell average in §5, and (8) uses $\pi_h$.
- **§7.3.** "the linear advection equation (22)": (22) is Burgers; (24) is meant.
- **Table 2 caption.** It says "$p\in\{1,2,3,4\}$", but only $p=1,2,4$ are tabulated.
- **Fig. 4(d) caption.** WENO $E_1=2.67\mathrm{e}{-01}$ for $p=2$, against 2.68e-02 ($p=1$) and
  2.76e-02 ($p=4$) and the visually comparable plot; this is almost certainly 2.67e-02.
- **§7.1–7.2.** The text says "HO and WENO stabilization" achieve optimal orders, but Tables 1 and 3
  tabulate CG, VMS and WENO. The VMS column uses (5), while §3 says the experiments use (7).

# Notation map

| Kuzmin & Vedral | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$ | $N$ | polynomial degree; elements $\mathbb Q^N$, order $N+1$ |
| $u_h$, $u_h^e=u_h\vert_{K_e}$ | $u_h$, $u_h\vert_K$ | continuous FE solution; $K_e$ is cell $e$ |
| $f(x,u)$ | $f$ | flux, may depend on $x$ |
| $\lambda_e$ | $a_e$ | local maximum wave speed |
| $\nu_e=\lambda_eh_e/(2p)$ | $\mu_e=a_eh_e/(2N)$ | artificial viscosity; **collision** with the CFL number $\nu$ |
| $\gamma_e$ | $\varsigma_e$ | blending factor, 1 = smooth (HO), 0 = troubled (LO); **collision** with $\gamma$ and $\gamma_k$ |
| $\omega\in[0,1]$ | $\omega_{\mathrm H}$ (local) | scaling of the HO dissipation, not a WENO weight |
| $\tilde\omega_l^e$ | $d_k$ | linear weights |
| $\omega_l^e$, $\tilde w_l^e$ | $\omega_k$, $\alpha_k$ | nonlinear and unnormalized weights |
| $\beta_l^e=\Vert u^e_{h,l}\Vert_e^q$ | $\beta_k$ | smoothness indicator in integral seminorm form |
| $q$ (exponent of $\gamma_e$ and $\beta_l^e$) | $\mathsf q$ (page-local) | **collision** with the weight exponent $q$ |
| $r=2$ | $q=2$ | exponent of the nonlinear weights |
| $\epsilon=10^{-6}$ | $\epsilon$ | |
| $u^e_{h,l}$, $S^e_l$, $m_e$ | candidate on $S_k$, $S_k$ | Hermite candidates from neighbour cells; $l=0$ is the FE polynomial |
| $\pi_ev$ | $\bar v$ on $K_e$ | cell average |
| $\pi_h$ | — | $L^2$ projection of gradients |
| $\Vert\cdot\Vert_e$ | — | scaled Sobolev seminorm (10) over derivative orders $1..N$ |
| $N_h$ | — | number of degrees of freedom |
| $E_1$ | — | $L^1$ error |

# Reference list

The paper prints 54 references in numbered style [1]–[54], ordered alphabetically by first author.
The list is merged complete into the [bibliography](/bibliography.md) with `citedby` set to
`kuzmin-2023`. Notes on individual items:

- [28], the Kuzmin–Hajduk book printed as "to appear" in 2023, would collide with this source's own
  key and is keyed `kuzmin-2023-b`;
- [39] is an undated web site;
- [20] is lecture notes, [22] an AIAA paper, [40] a conference paper, and [27] and [44] book
  chapters;
- three pairs share an author and year and take suffixes in printed order: `barrenechea-2017`/`-b`,
  `kuzmin-2020`/`-b` and `zhang-2010`/`-b`.

All items parse.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–4 (2026-10-22/23). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Convex limiting and invariant-domain-preserving schemes](/methods/convex-limiting.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Dissipation-based WENO stabilization of continuous finite elements](/methods/weno-stabilized-continuous-galerkin.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Hermite WENO](/methods/hermite-weno.md)
* [KPP rotating wave](/benchmarks/kpp-rotating-wave.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Solid-body rotation](/benchmarks/solid-body-rotation.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
