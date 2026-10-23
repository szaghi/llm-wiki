---
type: Source
title: "Grote et al. (2021) — Stabilized leapfrog based local time-stepping method for the wave equation"
description: "Leapfrog-based explicit local time stepping for the second-order wave equation, stabilized by damped Chebyshev polynomials: fully explicit, second order, energy conserving, with a CFL condition independent of the step ratio and optimal fully discrete convergence for mass-lumped conforming finite elements."
resource: "doi:10.1090/mcom/3650"
source_kind: paper
authors: [Grote M.J., Michel S., Sauter S.A.]
year: 2021
venue: "Math. Comp. 90:2603-2643"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Mathematics_of_Computation_Grote_Stabilized_leapfrog_based_local_time-stepping_method_for_the.pdf"
tags: [local-time-stepping, multirate, explicit, stability, wave-equation]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

Local mesh refinement forces the leapfrog method, like any standard explicit
scheme, to take a global step dictated by the smallest element. The
leapfrog-based [local time stepping](/methods/local-time-stepping.md) (LF-LTS)
of Diaz and Grote (2009) takes $m$ local leapfrog steps of size $H/m$ in the
refined region and one step $H$ elsewhere. It is explicit, second order and
energy conserving, but its earlier convergence proof needed a CFL condition
set by the smallest elements, and the method can become weakly unstable at
isolated step sizes, where eigenvalue curves of the LTS operator touch the
stability bounds.

The paper writes the inner loop with shifted Chebyshev polynomials and
replaces them by damped Chebyshev polynomials $P_{m,\varepsilon_{\mathrm d}}$
with $\delta=1+\varepsilon_{\mathrm d}/m^2$, the device of the Runge–Kutta–Chebyshev
methods ([stabilized explicit Runge–Kutta](/methods/stabilized-explicit-runge-kutta.md)),
here applied to the leapfrog stability interval $(0,4)$ rather than to a
parabolic real interval. The stabilized LF-LTS keeps a three-term recurrence,
is fully explicit and second order, and reduces to the original LF-LTS for
$\varepsilon_{\mathrm d}=0$ and to leapfrog for $m=1$. Carle and Hochbruck
developed the same algorithm independently.

For conforming, mass-lumped $H^1$ finite elements the paper proves symmetry,
continuity and coercivity of the stabilized bilinear form, bounds on its
extreme eigenvalues, exact conservation of a modified discrete energy,
stability, and an optimal error $O(\Delta x^{r+1}+H^2)$ with constants
independent of $m$ and growing only as $1+T$. All of it
holds under a CFL condition that involves only the coarse mesh size. In 1D
and on a 2D L-shaped domain with graded meshes, the experiments show $O(\Delta x_{\mathrm c}^2)$
convergence independent of $m$ up to $m=1000$, energy conservation to
machine precision, a maximal stable step 0.3 % below the optimal leapfrog
step for $\varepsilon_{\mathrm d}=0.01$, and the removal of the critical-step
instability of the unstabilized method.

# Version read

arXiv:2005.13350v4 [math.NA], 4 April 2022, the authors' amsart preprint, 40
pages, all read; pp. 9, 10 and 37 were checked visually. It is not the
version of record (Math. Comp. 90:2603–2643, 41 pages), and the DOI and
venue are not printed in the file. Title and authors match Crossref.
Section, equation and page numbers on this page are those of arXiv v4.

# Key claims

Notation (see the notation map): the semi-discrete problem is $y''+Ly=0$
with $L$ the operator of the mass-lumped bilinear form (the source's $A^S$);
$H$ is the global step, $m$ the coarse-to-fine step ratio and $H/m$ the
local step (the source's $\Delta t$, $p$, $\Delta\tau$); $\varepsilon_{\mathrm d}$
the damping parameter (the source's $\nu$); $\Delta x_{\mathrm c}$ the coarse mesh
size (the source's $h_c$); $\Pi_{\mathrm c}$, $\Pi_{\mathrm f}$ the coarse and fine degree-of-freedom
projections; $L_{m,\varepsilon_{\mathrm d}}$ the stabilized LTS operator (the
source's $A^{S,p,\nu}$); $r$ the finite-element degree (the source's $m$).

1. Local mesh refinement imposes on leapfrog, and on any standard explicit scheme, a global CFL step dictated by the smallest element, even when only a few elements are small (§1). **Stated**
2. The original LF-LTS of Diaz and Grote has optimal convergence for conforming finite elements (Grote, Mehlin and Sauter 2018) only under a CFL condition where $H$ depends on the smallest elements; this cannot be improved in general, because LF-LTS may become unstable at certain discrete values of $H$ (Abstract, §1). **Stated** (cited); instability **Shown** in §4.2.
3. Replacing the Chebyshev polynomials of the Chebyshev form of LF-LTS by damped Chebyshev polynomials, $0\le\varepsilon_{\mathrm d}\le1/2$, gives the stabilized LF-LTS (2.18)–(2.22): fully explicit, second order, a leapfrog-like three-term recurrence, and a conserved discrete energy (§2.4, §5). **Derived** / **Proved**
4. For $\varepsilon_{\mathrm d}=0$ the algorithm is the original LF-LTS ($\delta=1$, recurrence coefficients 1, $\omega_{m,0}=2m^2$ since $T_m'(1)=m^2$) (Remark 2.6). **Derived**
5. For $m=1$, the stabilized bilinear form equals the original one and the scheme is standard leapfrog (§2.4, after (2.22)). **Derived**
6. If $\Pi_{\mathrm f}$ is the identity (small step everywhere), the algorithm is the leapfrog–Chebyshev method of Gilbert and Joly for $\varepsilon_{\mathrm d}=0$ and the stabilized leapfrog–Chebyshev method of Carle, Hochbruck and Sturm for $\varepsilon_{\mathrm d}>0$ (Remark 2.7). **Stated** / **Derived**
7. In the coarse region away from the coarse/fine interface the algorithm is a standard leapfrog step of size $H$ for any $m$ and $\varepsilon_{\mathrm d}$ (§2.4). **Derived**
8. When the fine region is small, the cost of a global step is dominated by one application of $L\Pi_{\mathrm c}$; all further applications of $L\Pi_{\mathrm f}$ touch only unknowns of the fine region and its neighbouring coarse elements (§2.4). **Stated**
9. Although the original derivation splits $L=L\Pi_{\mathrm c}+L\Pi_{\mathrm f}$ into nonsymmetric singular terms, the leapfrog form (2.20)–(2.22) yields a symmetric bilinear form (Remark 2.7, Thm 3.5). **Proved**
10. Under CFL (3.9), the stabilized form is continuous, symmetric and coercive, with coercivity constant $\frac{c_{\mathrm{coer}}}{m^2}\frac{\varepsilon_{\mathrm d}}{(2+\varepsilon_{\mathrm d})^2}$ (Thm 3.5). **Proved**
11. The CFL conditions (3.8) and (3.9) are independent of $m$; (3.8) implies (3.10), $C_{\mathrm{cont}}C_{\mathrm{inv}}^2(H/\Delta x_{\mathrm c})^2\le4e^{-\varepsilon_{\mathrm d}}$, which implies (3.9) (Remark 3.4). **Proved**
12. The stability proof deteriorates as $\varepsilon_{\mathrm d}\to0$ (the right-hand side of (3.8) is $\varepsilon_{\mathrm d}/(\varepsilon_{\mathrm d}+1)$); the authors call that limit of no practical interest, since experiments are robust for small fixed $\varepsilon_{\mathrm d}>0$ (Remark 3.4). **Stated**
13. $(L_{m,\varepsilon_{\mathrm d}})^{-1}-L^{-1}$ vanishes outside the fine–fine block (the Schur complements coincide), and its bilinear form is bounded by $\frac{\varepsilon_{\mathrm d}+1}{2\varepsilon_{\mathrm d}}H^2$ in the mass-lumped norm ((3.20), Lemma 3.6). **Proved**
14. Under (3.8), the eigenvalues of the stabilized form satisfy $H^2\lambda_{\max}\le4-\frac{\varepsilon_{\mathrm d}}{\varepsilon_{\mathrm d}+1}$ and $\lambda_{\min}\ge\frac12\min\{c_{\mathrm{coer}}/C_{\mathrm{eq}}^2,\,2\varepsilon_{\mathrm d}/((\varepsilon_{\mathrm d}+1)H^2)\}$ (Thm 3.7). **Proved**
15. The discrete energy $E^{n+1/2}$ (3.28), built with the stabilized form, is non-negative and exactly conserved under (3.8) (Cor. 3.8). **Proved**; constant to machine precision over $T=100$ (more than 30,000 global steps, $\Delta x_{\mathrm c}=1/320$, $m=2$), Fig. 5. **Shown**
16. Stability: the mass-lumped norms of the staggered velocity and the solution are bounded by $C_0$ times their initial values, with $C_0$ independent of $n$, $H$, $\Delta x$ and $T$ (Thm 3.9, proof by reference to Grote, Mehlin and Sauter, Thm 15). **Proved**
17. Fully discrete time error: $\lVert e^{(n+1)}\rVert\le CH^2(1+T)\max_{2\le\ell\le5}\lVert\partial_t^\ell y\rVert_{L^\infty(L^2)}$, $C$ independent of $n$, $H$, $T$, $\Delta x$, $m$ (Thm 3.10). **Proved**
18. Total error: $\lVert y(t_{n+1})-y_{n+1}\rVert\le C(1+T)(\Delta x^{r+1}+H^2)Q(y)$ for $y\in W^{8,\infty}([0,T];H^{r+1})$, under the $m$-independent CFL (3.8) (Thm 3.11). **Proved**
19. 1D test, $m=1000$, $\Delta x_{\mathrm c}=0.01$, $H=e^{-\varepsilon_{\mathrm d}}\Delta x_{\mathrm c}$: stabilized ($\varepsilon_{\mathrm d}=0.01$) and unstabilized solutions coincide with the exact one at $t=2$ at plot scale (Fig. 3). **Shown**
20. The $L^2$ error at $t=2$ converges as $O(\Delta x_{\mathrm c}^2)$ independently of $m$ for $m=2,5,17,1000$ ($\varepsilon_{\mathrm d}=0.01$) (Fig. 4). **Shown**
21. The maximal stable step as a percentage of the optimal leapfrog step $2/\sqrt{\lambda_{\max}}$ is 99.9 % ($\varepsilon_{\mathrm d}=0.001$), 99.7 % ($0.01$), 98.4 % ($0.05$) and 87.6 % ($0.5$); the minimal distances $\min(1-H^2\lambda/4)$ are 0.0005, 0.0049, 0.0239, 0.1758 (Table 1). **Shown**; the authors conclude that the restrictive condition (3.8) "seems irrelevant in practice" (§4.1).
22. Without stabilization ($\varepsilon_{\mathrm d}=0$, $m=3$, $\Delta x_{\mathrm c}=1/40$), eigenvalue curves of $(H^2/4)L_{m,\varepsilon_{\mathrm d}}$ are tangent to 0 or 1 at isolated critical steps, the first at $0.5011$ times the optimal step; with $\varepsilon_{\mathrm d}=0.001$ all eigenvalues stay strictly inside $(0,1)$ (§4.2, Fig. 6). **Shown**
23. For $m=2$ the first critical step is $H=0.7104\,\Delta x_{\mathrm c}$; started from the critical eigenmode, the unstabilized method grows linearly in time up to $T=1000$ and faster afterwards ("probably due to round-off"), while $\varepsilon_{\mathrm d}=0.01$ stays bounded (§4.2, Fig. 7). **Shown**
24. Even at the critical step on each mesh, unstabilized LF-LTS ($m=2$) keeps optimal $O(\Delta x_{\mathrm c}^2)$ convergence on a finite interval ($t=2$); likewise for $\varepsilon_{\mathrm d}=0.01$ and $0.5$ (§4.2, Fig. 8). **Shown**
25. On a 2D L-shaped domain with graded meshes (grading exponent 1.6), stabilized LF-LTS ($\varepsilon_{\mathrm d}=0.01$, P1) converges as $O(\Delta x)$ in $H^1$ and $O(\Delta x^2)$ in $L^2$ at $t=0.3$, while standard leapfrog on uniform meshes does not reach optimal rates and is less accurate for each $\Delta x$ (§4.3, Fig. 10). **Shown**
26. The stabilized LF-LTS algorithm extends to general nonzero forcing (citing Grote, Michel and Sauter, in preparation) (§5). **Stated**
27. Replacing Chebyshev polynomials by damped ones is well known in the parabolic context (RKC) and was also used for leapfrog–Chebyshev methods and for a Lagrange-multiplier LTS approach (§1). **Stated**

*(Compiler caveats, not in the sources.)* "Energy conserving"
refers to the modified energy (3.28), built with the stabilized form, not
to the physical energy. The claim that (3.8) is irrelevant in practice rests
on 1D numerics. The unstabilized instability is a linear growth that matters
for long-time simulation (claims 23–24).

# Printed slips

1. §4.2, first sentence: "The LF-LTS method is stable for any particular $\Delta t$, as long as all the discrete eigenvalues of $(\Delta t^2/4)A^{S,p,\nu}$ strictly lie in $(0,4)$" — the scaling is inconsistent with §4.1 and Fig. 6: the interval is $(0,4)$ for $\Delta t^2A^{S,p,\nu}$, or $(0,1)$ for $(\Delta t^2/4)A^{S,p,\nu}$.
2. (3.8) is followed by "with $\delta_{p,\nu},\omega_{p,\nu}$ as in (2.18)", but neither symbol appears in (3.8); they appear in (3.9).
3. §4.2: "the LTS-LF method will indeed remain perfectly stable" — acronym inverted (LF-LTS elsewhere).
4. Critical steps in mixed units: "$\Delta t_{\rm crit}=0.5011\cdot\Delta t_{\rm opt}$" ($p=3$) but "$\Delta t_{\rm crit}=0.7104\cdot h_c$" ($p=2$).
5. Lemma B.1 states "$P_{p,\nu,k}(x)\in\mathbb P_k$" without the $\Delta t$ superscript of (B.1); $P^{\Delta t}_{p,\nu,k}$ has degree $k-1$, so the inclusion is true but loose.
6. Proof of Thm 3.7 (p. 19): "Since we can bound the last term in (3.24) as …" — the bounded term belongs to the display leading to (3.25), not to (3.24).
7. (A.13), p. 37: the subscript of $\omega$ in "$\nu/p^2\le x/\omega_{p,\nu}<2+\nu/p^2$" is garbled by an overlapping glyph (typesetting artifact, checked visually).
8. Thm 3.10 defines $M(u_S)$ with the $L^2(\Omega)$ norm, while $M_n(u_S)$ in its proof uses $\lVert\cdot\rVert_{\mathcal T}$; harmless through (2.12).
9. Typos: "accomodates" (p. 1), "definitions ans notations" (p. 7), "bilinearform" (p. 7), "postitive" (p. 14), "respresentation" (p. 18).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\ddot u+A^Su=0$, $u^{(n)}_S$ | $y''+Ly=0$, $y_n$ | second-order semi-discrete wave equation; $L$ the registry linear operator |
| $A^S$ | $L$ | operator of the bilinear form $a$ in the mass-lumped inner product |
| $A^{S,p,\nu}$, $a^{p,\nu}$ | $L_{m,\varepsilon_{\mathrm d}}$ (page-local), $a^{m,\varepsilon_{\mathrm d}}$ | stabilized LTS operator and form |
| $\Delta t$ | $H$ | global (coarse) step; multirate convention of the registry |
| $\Delta\tau=\Delta t/p$ | $h=H/m$ | local (fine) step |
| **$p$** | $m$ | step ratio; **collides** with the registry classical order |
| **$\nu$** | $\varepsilon_{\mathrm d}$ | damping parameter, as on the [stabilized explicit Runge–Kutta](/methods/stabilized-explicit-runge-kutta.md) page; **collides** with the registry Courant number |
| $\delta_{p,\nu}=1+\nu/p^2$ | $\delta=1+\varepsilon_{\mathrm d}/m^2$ | same form as the RKC shift $\omega_0=1+\varepsilon_{\mathrm d}/s^2$ |
| $\omega_{p,\nu}=2T_p'(\delta)/T_p(\delta)$ | $\omega_{m,\varepsilon_{\mathrm d}}$ | kept |
| $T_p$, $P_{p,\nu}$, $P^{\Delta t}_{p,\nu}$, $Q^{\Delta t}_{p,\nu}$ | $T_m$, $P_{m,\varepsilon_{\mathrm d}}$, kept | Chebyshev and damped Chebyshev polynomials; **$P_{p,\nu}$ is not** the registry stability polynomial $P(z)$ |
| **$\beta_k$, $\beta_{k+1/2}$** | kept (page-local) | recurrence coefficients; **collide** with the multistep $\beta_j$ and PID exponents |
| **$h$, $h_c$, $h_f$** | $\Delta x$, $\Delta x_{\mathrm c}$, $\Delta x_{\mathrm f}$ | mesh sizes; **$h$ collides** with the registry step |
| **$m$, $m'$** | $r$, $r'$ | finite-element degrees; **$m$ collides** with the multirate ratio |
| $\Pi^S_c$, $\Pi^S_f$ | $\Pi_{\mathrm c}$, $\Pi_{\mathrm f}$ | coarse/fine degree-of-freedom projections ($P$ and $I-P$ of Diaz–Grote) |
| $\lambda_{p,\nu}$, **$\eta_{p,\nu}$** | $\lambda$, kept | eigenpairs of the stabilized form; **$\eta$ collides** with the registry entropy |
| $E^{n+1/2}$ | kept | modified discrete energy (3.28) |
| $(\cdot,\cdot)_{\mathcal T}$, $\lVert\cdot\rVert_{\mathcal T}$ | $\langle\cdot,\cdot\rangle$, $\lVert\cdot\rVert$ with subscript $\mathcal T$ | mass-lumped inner product |
| $C_{\mathrm{cont}}$, $c_{\mathrm{coer}}$, $C_{\mathrm{eq}}$, $C_{\mathrm{inv}}$ | kept | continuity, coercivity, norm-equivalence, inverse-inequality constants |

# Reference list

44 printed references, numbered [1]–[44] in alphabetical AMS style, with
"———" dashes repeating the previous authors ([8], [13], [14], [17], [28],
[30], [44]). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` grote-2021. Ref. [5] is a
private communication of Carle and Hochbruck, undated, keyed with the citing
year and a note; [8] is a HAL preprint (hal-01894357v3, 2020); [18] is the
NIST DLMF web resource (Release 1.0.13, 2016), entered with its editors.
No DOIs or arXiv identifiers are printed. There are no printed duplicates
and no unparseable items.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Local time stepping](/methods/local-time-stepping.md)
* [Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping](/methods/stabilized-explicit-runge-kutta.md)
