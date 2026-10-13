---
type: Source
title: "Jiang & Shu (1996) — Efficient Implementation of Weighted ENO Schemes"
description: "The WENO-JS paper: point-value finite-difference WENO with a new smoothness indicator that gives fifth order from three-point stencils, characteristic-wise systems, a convergence proof for smooth solutions and scalar and Euler tests; no MHD and no divergence content."
resource: "doi:10.1006/jcph.1996.0130"
source_kind: paper
authors: [Jiang G.-S., Shu C.-W.]
year: 1996
venue: "J. Comput. Phys. 126:202-228"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1996-JCP-Jiang-101006jcph19960130.pdf"
tags: [weno, finite-difference, high-order, reconstruction, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper recasts the WENO schemes of Liu, Osher & Chan in the
point-value, flux-difference (Shu–Osher) finite-difference framework and
analyzes their accuracy. The Liu–Osher–Chan smoothness measure gives only
order $r+1$ (fourth order for $r = 3$) in smooth regions and third order
at critical points. Its apparent super-convergence comes from large
coarse-grid errors (§2).

The main contribution is a **new smoothness indicator**: a sum of scaled
$L^2$ norms of all derivatives of each candidate interpolant over the cell
(eq. 3.1). With it the $r = 3$ scheme is fifth order in smooth regions,
and the paper claims it is fifth order at critical points too (§3,
eqs. 3.8–3.9). This is the scheme the literature calls WENO-JS (WENO5);
it is compiled in [WENO reconstruction](/methods/weno.md). The paper also
gives:
* cheaper weights for the Euler equations, computed from pressure and
  entropy (§4);
* Yang's artificial compression at contacts (§5);
* a convergence proof for smooth solutions via Strang's theorem (§6);
* an efficiency comparison on a CRAY C-90 and workstations (§7);
* 1D and 2D scalar and Euler tests (§8).

**The paper contains no MHD.** It has no magnetic field, no MHD
eigensystem, no $\nabla\cdot\mathbf B$ and no MHD test. The equations are
scalar conservation laws and the Euler equations (3D for timings only).
It enters this bundle as the base scheme of its finite-difference MHD
sources, chiefly the MHD extension of
[Jiang & Wu (1999)](/sources/jiang-1999.md).

# Key claims

1. **Conservative finite-difference form** (§2, eqs. 2.2–2.3). The
   spatial operator is
   $L = -\frac{1}{\Delta x}(\hat f_{j+\frac12} - \hat f_{j-\frac12})$.
   The numerical flux $\hat f_{j+\frac12}$ approximates $h(x_{j+\frac12})$,
   where $h$ is defined implicitly by
   $f(u(x)) = \frac{1}{\Delta x}\int_{x-\Delta x/2}^{x+\Delta x/2} h(\xi)\,d\xi$.
   The scheme reconstructs from point values of $f$, not from cell
   averages: the Shu–Osher flux version of ENO.
2. **Flux splitting** (eqs. 2.4–2.6). $f = f^+ + f^-$ with
   $df^+/du \ge 0$, $df^-/du \le 0$. The global Lax–Friedrichs splitting is
   $f^\pm(u) = \frac12(f(u) \pm \alpha u)$, with $\alpha = \max|f'(u)|$
   "taken over the whole relevant range of $u$" (eq. 2.5). Roe splitting
   with entropy fix ("RF") is referenced to Shu & Osher. Local splitting is
   allowed in words ("either globally or locally", §2; §4 for systems),
   but every LF scheme tested is global LF.
3. **Candidate stencils and weighted flux** (eqs. 2.7–2.14, Tables 1–2).
   The $r$ stencils are $S_k = (x_{j+k-r+1},\dots,x_{j+k})$,
   $k = 0,\dots,r-1$, each giving $q_k^r = \sum_l a^r_{k,l} f_{j+k-r+1+l}$.
   The flux is $\hat f_{j+\frac12} = \sum_k \omega_k q_k^r$ (eq. 2.10).
   The optimal weights $C_k^r$ reproduce the $(2r-1)$th-order upstream
   central flux: $C^2 = (1/3, 2/3)$, $C^3 = (1/10, 6/10, 3/10)$ (Table 2).
   Order $2r-1$ requires $\omega_k = C_k^r + O(h^{r-1})$ (eq. 2.14).
4. **Nonlinear weights** (eqs. 2.15–2.17, 2.26–2.28).
   $\omega_k = \alpha_k / \sum_l \alpha_l$ with
   $\alpha_k = C_k^r / (\epsilon + IS_k)^p$. The paper takes
   $\epsilon = 10^{-6}$ ("in our later tests") and $p = 2$ in all tests,
   against the $p = r$ of Liu et al. (§2). A sufficient condition for order
   $2r-1$ is $IS_k = D(1 + O(h^{r-1}))$ with $D$ independent of $k$
   (eq. 2.17). At a discontinuity a non-smooth stencil has $IS_l = O(1)$, so
   $\omega_l = O(h^{2p})$ (eq. 2.28).
5. **The Liu–Osher–Chan indicator is sub-optimal** (eqs. 2.18–2.25). The
   sum of squared undivided differences gives $IS_k = (f'h)^2(1+O(h))$,
   hence $\omega_k = C_k^r + O(h)$: order $r+1$ in smooth monotone regions
   and third order at critical points. The super-convergence in their
   Tables 1–5 is superficial; it comes from large coarse-grid errors, and
   on fine grids the $IS_k$ fall below $\epsilon$ and the weights approach
   the optimal ones.
6. **The new indicator** (§3, eqs. 3.1–3.4):
   $IS_k = \sum_{l=1}^{r-1}\int_{x_{j-\frac12}}^{x_{j+\frac12}} h^{2l-1}(q_k^{(l)})^2\,dx$,
   motivated as a smoother analogue of minimizing total variation. For
   $r = 2$ it equals the Liu et al. indicator. For $r = 3$:
   $$\begin{aligned} IS_0 &= \tfrac{13}{12}(f_{j-2}-2f_{j-1}+f_j)^2 + \tfrac14(f_{j-2}-4f_{j-1}+3f_j)^2\\ IS_1 &= \tfrac{13}{12}(f_{j-1}-2f_j+f_{j+1})^2 + \tfrac14(f_{j-1}-f_{j+1})^2\\ IS_2 &= \tfrac{13}{12}(f_j-2f_{j+1}+f_{j+2})^2 + \tfrac14(3f_j-4f_{j+1}+f_{j+2})^2 \end{aligned}$$
7. **Accuracy of WENO5** (eqs. 3.5–3.9, §9). If $f' \ne 0$,
   $IS_k = (f'h)^2(1+O(h^2))$ (eq. 3.8), which meets eq. 2.17 for $r = 3$:
   fifth order. At critical points,
   $IS_k = \frac{13}{12}(f''h^2)^2(1+O(h^2))$ (eq. 3.9), and the paper
   concludes the weights "are also 5th order accurate at critical points".
   The §9 conclusion states only order $2r-1$ "in smooth regions" (for
   $r = 2, 3$) and order $r$ at discontinuities. No test isolates a
   critical point.
8. **Weight comparison** (Fig. 1, eq. 3.10). On a piecewise sine with a
   jump at $x = 1/2$ ($\Delta x = 1/40$) the original indicator departs
   from the optimal weights near the critical points $x = 1/4, 3/4$ and
   the new one does not. Both give the discontinuous stencil a near-zero
   weight. Just left of the jump $\omega_0 \approx 1/7$,
   $\omega_1 \approx 6/7$.
9. **Systems** (§4, eqs. 4.1–4.4). Fluxes are computed in the local
   characteristic fields of an interface Jacobian evaluated at the
   arithmetic mean $(u_j+u_{j+1})/2$ (eq. 4.1), or Roe's matrix for Euler.
   Scalar WENO acts on $l_s\cdot f$ per field (eq. 4.2), weights are
   computed field by field (eq. 4.3), and the result is projected back with
   the right eigenvectors (eq. 4.4). Multi-D is dimension by dimension. The
   projections dominate the flop count.
10. **Pressure/entropy weights, WENO-LF-5-PS** (§4, eqs. 4.5–4.6).
    Weights of the nonlinear fields come from pressure, those of the
    linearly degenerate fields from entropy, which cuts the projections to
    two forward and two inverse. About twice as fast as characteristic
    weights. It **fails** on the forward step and the double Mach
    reflection: pressure and entropy are symmetric across a reflective
    wall, cannot detect jumps in the normal velocity, and the density goes
    negative (§8.3, Remark). It is also poor on 2D shock–entropy
    interaction.
11. **Artificial compression, "-A"** (§5, eqs. 5.1–5.4). Yang's slope
    modification in the contact field only, with $\alpha = 33$. Up to
    +100% operations with the LF building block (§§7, 9).
12. **Convergence theorem** (§6, Theorem 6.1, Table 5). With a smooth
    splitting (global LF) the WENO operator is $C^\infty$ in its arguments.
    Its linearization at a constant state is a $(2r-2)$th-order central
    difference plus a $(2r-1)$th-order upwind-biased one, with spectrum in
    the left half-plane, so the first variation is $l_2$-stable under RK of
    order $\ge 3$. By Strang's theorem, smooth scalar solutions converge as
    $u = v + O(\Delta x^r)$ (eq. 6.5) with RK order $n \ge \max(r, 3)$.
    **The proven rate is $r$, not $2r-1$.** Linear-stability CFL numbers:
    $r = 2$: 1.625 (RK3), 1.745 (RK4); $r = 3$: 1.434 (RK3), 1.731 (RK4).
13. **Time stepping** (§1, eqs. 1.2–1.4). The Shu–Osher third-order TVD
    Runge–Kutta ("RK-3"):
    $$\begin{aligned} u^{(1)} &= u^n + \Delta t\,L(u^n)\\ u^{(2)} &= \tfrac34 u^n + \tfrac14 u^{(1)} + \tfrac14\Delta t\,L(u^{(1)})\\ u^{n+1} &= \tfrac13 u^n + \tfrac23 u^{(2)} + \tfrac23\Delta t\,L(u^{(2)}) \end{aligned}$$
    and the classical, non-TVD fourth-order RK ("RK-4", eq. 1.4). For the
    accuracy tables $\Delta t \propto (\Delta x)^{5/4}$, so RK-4 is
    effectively fifth order (§3, footnote 5).
14. **Efficiency** (§7, Tables 6–7). On the CRAY C-90, WENO-LF-4 and
    WENO-LF-5 are at least twice as fast as ENO-LF-4; WENO-LF-5-PS is 2.5×,
    3.2× and 3.9× faster than ENO-LF-4 in 1D, 2D and 3D. WENO runs at about
    500 MFlops, which the paper puts at 50% of peak. On workstations WENO
    is roughly as fast as ENO. The second-order TVD reference is about 10×
    faster than ENO-LF-4 on the C-90.

# Tests

All scalar or Euler; none is MHD, and no divergence is measured.

* **Linear advection accuracy** (§3, Tables 3–4). $u_t + u_x = 0$ on
  $[-1,1]$, periodic, $t = 1$. For $u_0 = \sin(\pi x)$, WENO-RF-5 reaches
  design order from about 40 points: $L^1$ orders 4.99, 4.95, 5.07, 5.03
  and $L^\infty$ 5.06, 5.01, 4.99, 5.00 from $N = 40$ to 320, $L^1$ error
  1.35e-9 at $N = 320$. WENO-RF-4 creeps from $L^1$ order 2.13 to 3.86.
  CENTRAL-5 gives 1.53e-10 at $N = 320$. For $u_0 = \sin^4(\pi x)$,
  WENO-RF-5 settles later ($L^1$ orders 4.80 and 5.48 at $N = 320$ and
  640). WENO-RF-4 is more accurate than WENO-RF-5 on the coarsest grid in
  both tables.
* **Composite-profile advection** (§8.1 Ex. 1; 200 points, $t = 8$, CFL
  0.4, 0.2 for -A, RK-3). WENO-Roe-4/5 beat ENO-Roe-4; WENO-Roe-5-A is
  best.
* **Buckley–Leverett** (§8.1 Ex. 2). WENO-RF-3 and WENO-RF-5 converge to
  the entropy solution.
* **Sod and Lax shock tubes** (§8.2 Ex. 1, $n = 101$). WENO-RF-5 >
  WENO-LF-5-PS > WENO-RF-3; -A much better at contacts. The Lax problem is
  called a tough case for non-characteristic schemes of order $\ge 3$.
* **1D shock–entropy interaction** (§8.2 Ex. 2; Mach 3, $\epsilon = 0.01$,
  $k = 13$, linear-theory amplitude 0.08690716). WENO-LF-4 is best at
  $N = 800$; WENO-LF-5 equals it at $N = 1200$ and overtakes it on finer
  grids.
* **Woodward–Colella blast waves** (§8.2 Ex. 3; 199, 399, 799 points,
  $t = 0.038$, reference ENO-RF-5 on 1600). WENO4 and WENO5 are much
  better than WENO3.
* **Quasi-1D nozzle** (§8.2 Ex. 4, 34 points). Residual to $10^{-7}$.
* **Oblique Sod** (§8.3 Ex. 1; $96\times16$, $t = 1.2$, RK-4,
  $\Delta t = 0.6\Delta x$). WENO deviates from 1D about as much as
  ENO-LF-4.
* **Mach 3 forward step** and **double Mach reflection** (§8.3 Exs. 2–3).
  WENO slightly better than ENO at the contact; PS fails on both.
* **2D shock–entropy interaction** (§8.3 Ex. 4; $800\times20$,
  amplitude 0.08744786). Unmodified ENO loses accuracy and WENO does not.
  The modified weights of eq. 8.2 ($\tilde\omega_k = C_k^r$ if any
  $IS_l < \alpha^{-1}$, $\alpha = 2$) give "WENO2" variants;
  WENO2-LF-4 becomes fifth order in smooth regions.
* **Shock–vortex interaction** (§8.3 Ex. 5) and **Mach 3 cylinder** on a
  curvilinear $60\times80$ grid (§8.3 Ex. 6, WENO-LF-5, RK-4).

# Notation map

| Jiang & Shu (1996) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta x$, $h$ | $h$ | the paper also uses $h(x)$ for the implicit flux primitive (eq. 2.3): an internal collision; concept pages say "flux primitive" |
| $L(u)$ | words | semi-discrete spatial operator; no registry symbol |
| $\hat f_{j+\frac12}$ | words | numerical flux at a face; the registry's $f^{x,*}$ is reserved for the magnetic base-scheme fluxes |
| $\alpha = \max|f'|$ (eq. 2.5) | $\alpha^{\mathrm{LF}}$ | global over the whole range, per direction |
| $r$ (stencil count and base ENO order) | words ("$r$-point stencils") | **collision**: registry $r$ is the refinement ratio |
| $S_k$, $q_k^r$, $a^r_{k,l}$ | words | candidate stencils and interpolants |
| $C_k^r$ | words ("linear weights") | |
| $\omega_k$, $\alpha_k$ | words ("nonlinear weights") | $\alpha_k$ collides with $\alpha^{\mathrm{LF}}$; the paper reuses $\alpha$ for Yang's constant (eq. 5.4) and the eq. 8.2 threshold |
| $IS_k$ | words ("smoothness indicator") | |
| $\epsilon$, $p$ | words | $p$ is close to the registry's $p_{\mathrm{obs}}$ |
| $l_s$, $r_s$, $A_{j+\frac12}$ | words | $l$ collides with the AMR level index |
| $u^{(1)}, u^{(2)}$; $\Delta t$; superscript $n$ | $\Delta t$; superscript $n$ | stage values need no symbol |
| $P$ (pressure) | words | **collision** with prolongation $P$ |
| $E$ (total energy) | words | **collision** with $E_h$ |
| $D$ (eq. 2.17), $D_{2r-2}$ (eq. 6.3) | words | **collision** with $D_h$ |

# Pages created or updated

* Created [WENO reconstruction](/methods/weno.md): the method from its primary source, and its role in the bundle's divergence-preserving and divergence-controlling schemes.
* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md): finite-difference against finite-volume WENO, and the meaning of "$r = 2, 3$".
* Updated [Constrained transport](/methods/constrained-transport.md): the base scheme of the high-order finite-difference CT.
* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): the WENO variants of the fourth-order and alternative-FD realizations.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): what the base scheme's own paper says about positivity.

# Citations

1. `~/papers/mosaic/div-free-amr/1996-JCP-Jiang-101006jcph19960130.pdf`.
   * **Version read.** The **authors' preprint**, not the typeset JCP
     article: 40 pages, an abstract page "i" and text pages 1–34 in LaTeX
     layout with no journal header or pagination (PDF produced 1997 by
     Acrobat Distiller). Section, equation, table and figure numbers on
     this page are the preprint's; they were not checked against the
     published pp. 202–228. Shu's footnote places him in residence at
     ICASE, NASA Langley; Jiang's current address is given as UCLA.
   * **Identity.** doi:10.1006/jcph.1996.0130, checked on Crossref: title
     and both authors match page 1; J. Comput. Phys. 126(1):202–228, June
     1996. Crossref deposits no reference list. The filename DOI agrees.
   * **How it was read.** Text extraction for the prose; the text layer
     garbles most equations. Eqs. 1.3, 2.2–2.6, 2.14–2.18, 3.1–3.9,
     5.1–5.4 and 6.1–6.2 were read from the rendered PDF pages 4, 5, 7, 9,
     10 and 15, and eq. 8.2 from page 35. Eqs. 6.3–6.5 and 8.3–8.8 were
     read from the text layer only and are not reproduced. Figures were
     read from captions and surrounding text only.
   * **Recorded as printed.**
     * Eq. 2.26 prints $IS_k = O(h^{2p})$ for a smooth stencil (confirmed
       on the render). By eq. 2.21 a smooth stencil has $IS_k = O(h^2)$,
       which with eq. 2.27 gives eq. 2.28; probably a typo for $O(h^2)$.
       Not corrected.
     * Reference [11] (Roe, "Approximate Riemann solvers, parameter
       vectors…") is printed with the venue of Sod's survey, J. Comput.
       Phys. 27:1 (1978).
     * Eq. 8.2 compares each indicator with the absolute threshold
       $\alpha^{-1} = 1/2$, so it is not scale-invariant (an observation
       of this reading, not a claim of the paper).
   * **Reference list.** 21 entries, all merged; none prints a DOI.
     Roe's paper, printed with Sod's venue, was merged into `roe-1981`.
     Liu & Lax, "Positive schemes…", printed without year as a preprint,
     was merged into `liu-lax-1996`. Shu, Zang et al. (Appl. Numer. Math.
     9:45) is `shu-1992-b`. The bibliography holds 3669 entries after this
     batch.
