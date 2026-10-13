---
type: Source
title: "Shu & Osher (1989) — Efficient Implementation of Essentially Non-oscillatory Shock-Capturing Schemes, II"
description: "ENO II: the point-value flux ENO scheme rebuilt on the primitive of an implicit function whose cell averages are the point fluxes, the ENO-Roe, local Lax–Friedrichs (ENO-LLF) and Roe-with-entropy-fix (ENO-RF) variants, contact sharpening in flux form, local characteristic decomposition, and the 1D shock–density-wave test; no divergence content."
resource: "doi:10.1016/0021-9991(89)90222-2"
source_kind: paper
authors: [Shu C.-W., Osher S.]
year: 1989
venue: "J. Comput. Phys. 83:32-78"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1989-JCP-Shu-1010160021-99918990222-2.pdf"
tags: [eno, finite-difference, high-order, shock-capturing, lax-friedrichs, riemann-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The sequel to [Shu & Osher (1988)](/sources/shu-osher-1988.md), which
built ENO schemes in a conservative finite-difference, numerical-flux
framework on point values, with TVD Runge–Kutta time stepping. This paper
changes four things.

1. It replaces the 1988 flux formula, which corrects the interface flux
   with even derivatives, by an equivalent and simpler construction:
   Newton divided differences of the primitive of an implicit function
   whose cell averages are the point fluxes (Lemma 2.1, eqs. 2.1–2.3).
   This is the "flux-primitive" form of FD-ENO/WENO.
2. It introduces three upwinding and splitting variants that stay
   uniformly high order at sonic points: **ENO-Roe** (Alg. 2.1),
   **ENO-LLF**, with a local Lax–Friedrichs coefficient per interface
   (Alg. 2.2), and **ENO-RF**, Roe with the LLF entropy fix only where the
   characteristic speed changes sign (Alg. 2.3).
3. It recasts two contact-sharpening devices in the flux/RK framework:
   Harten's subcell resolution (Alg. 3.1, 1D only) and Yang's artificial
   compression (Alg. 3.2).
4. It implements systems by local characteristic decomposition at a mean
   or Roe-averaged state (Alg. 4.1), and multidimensions dimension by
   dimension.

The tests include the 1D Mach 3 shock–density-wave interaction (Example
8, eq. 5.11), the problem later literature calls the "Shu–Osher problem",
and a 2D Mach 8 shock–vorticity-wave interaction (Example 9).

**The paper contains no divergence constraint.** Scalar laws and the
Euler equations only: no MHD, no $\nabla\cdot\mathbf B$, no
incompressibility. It enters this bundle as the source of the FD flux form,
of LLF and RF splitting and of the shock–entropy test that the bundle's
finite-difference MHD codes build on ([WENO reconstruction](/methods/weno.md)).

# Key claims

1. **TVD Runge–Kutta restated** (§I, eqs. 1.6–1.7, Table I).
   $u^{(i)} = \sum_{k<i}[\alpha_{ik}u^{(k)} + \beta_{ik}\Delta t\,L(u^{(k)})]$,
   $i = 1,\dots,\bar r$, TVD under $\lambda \le c_r\lambda_0$ when the
   forward-Euler step is TVD under $\lambda \le \lambda_0$. CFL
   coefficients (p. 34): $c_2 = c_3 = 1$, $c_4 = 2/3$ ($\bar r = r$ for
   $r \le 4$); $c_5 = 7/30$ with $\bar r = 6$. For $r \ge 4$ some
   $\beta_{ik} < 0$ and the adjoint operator $\tilde L$ is needed. Table I:
   * order 2: $\alpha$ rows $(1)$, $(\frac12, \frac12)$; $\beta$ rows
     $(1)$, $(0, \frac12)$; CFL 1;
   * order 3: $\alpha$ rows $(1)$, $(\frac34, \frac14)$,
     $(\frac13, 0, \frac23)$; $\beta$ rows $(1)$, $(0, \frac14)$,
     $(0, 0, \frac23)$; CFL 1;
   * order 4: $\alpha$ rows $(1)$, $(\frac12, \frac12)$,
     $(\frac19, \frac29, \frac23)$, $(0, \frac13, \frac13, \frac13)$;
     $\beta$ rows $(\frac12)$, $(-\frac14, \frac12)$,
     $(-\frac19, -\frac13, 1)$, $(0, \frac16, 0, \frac16)$; CFL $\frac23$.

   The schemes were constructed in the 1988 paper; this one only lists
   them.
2. **Conservative form** (eqs. 1.8–1.9).
   $L(u)_j = -\frac{1}{\Delta x}(\hat f_{j+1/2} - \hat f_{j-1/2})$. The
   1988 accuracy condition is restated with $a_2 = -\frac1{24}$,
   $a_4 = \frac{7}{5760}$.
3. **Lemma 2.1, the flux-primitive principle** (eqs. 2.1–2.3). If
   $f(u(x)) = \frac{1}{\Delta x}\int_{x-\Delta x/2}^{x+\Delta x/2} h(\xi)\,d\xi$,
   then $f(u(x))_x = (h(x+\Delta x/2) - h(x-\Delta x/2))/\Delta x$, so
   $\hat f_{j+1/2}$ must approximate $h(x_{j+1/2})$. The primitive
   $H(x_{j+1/2}) = \Delta x\sum_{k\le j} f(u_k)$ is interpolated in ENO
   fashion and differentiated at $x_{j+1/2}$. Its divided differences of
   order $k+1$ are the $k$-th divided differences of $f$, so the sum is
   never formed (p. 36). The scheme equals cell-average ENO (Harten et
   al.) **for linear 1D equations only** (p. 36).
4. **The upwind start is essential** (p. 36). Starting the stencil
   downwind is unstable for Burgers "even if the stencil is chosen in an
   ENO fashion up to third order".
5. **Criticism of the 1988 splitting** (p. 37). Global $f^\pm$ splitting
   smears shocks; an E-flux building block loses accuracy at sonic points,
   where most E-fluxes are only Lipschitz or $C^1$.
6. **ENO-Roe** (Alg. 2.1, eqs. 2.4–2.10). The first stencil point is
   chosen by the sign of the Roe speed
   $\bar a_{j+1/2} = (f(u_{j+1}) - f(u_j))/(u_{j+1} - u_j)$: $j$ if
   $\bar a_{j+1/2} \ge 0$, else $j+1$ (2.6). The divided differences of
   $H$ follow from those of $f$ (2.5); the stencil grows toward the
   smaller divided difference (2.7–2.8); Newton form (2.9);
   $\hat f_{j+1/2} = \frac{d}{dx}Q_{j+1/2}(x_{j+1/2})$ (2.10). Remark 2.1:
   uniformly high order even at sonic points; order $r+1$, perhaps $r$ at
   isolated zeros of derivatives of $f(u(x))$. Being built on first-order
   Roe, it admits stationary entropy-violating expansion shocks (p. 38).
7. **ENO-LLF** (Alg. 2.2, eqs. 2.11–2.15). $H^\pm$ are built from
   $\frac12(f[\cdot] \pm \alpha_{j+1/2}u[\cdot])$ with the **local**
   coefficient $\alpha_{j+1/2} = \max_{u_j \le u \le u_{j+1}}|f'(u)|$
   (2.12), $\max(|f'(u_j)|, |f'(u_{j+1})|)$ for convex $f$ (2.14). $H^+$
   starts at $j$, $H^-$ at $j+1$ (2.13). The first-order LLF flux
   $h^{LLF}_{j+1/2} = \frac12[f(u_j) + f(u_{j+1}) - \alpha_{j+1/2}(u_{j+1} - u_j)]$
   (2.15) is monotone. Alg. 2.2 is not ENO with $h^{LLF}$ as a building
   block (Remark 2.2b).
8. **Cost and viscosity** (Remark 2.2c–e). ENO-LLF costs as much as the
   1988 global scheme ("ENO-LF"), two divided-difference tables; ENO-Roe
   half as much. Viscosity, hence shock smearing, decreases from ENO-LF to
   ENO-LLF to ENO-Roe. With minmod (2.16) and $r = 1$, Alg. 2.1 reduces to
   a familiar second-order TVD scheme.
9. **ENO-RF** (Alg. 2.3, eq. 2.17). ENO-Roe where $f'$ keeps its sign
   between $u_j$ and $u_{j+1}$, ENO-LLF otherwise; for convex $f$ only in
   expansion-shock cells, $f'(u_j) < 0 < f'(u_{j+1})$ (Remark 2.3). Cost
   close to ENO-Roe. "Numerically we observe that Algorithm 2.3 always
   yields the correct entropy solution even for nonconvex $f$" (p. 40):
   observed, not proved.
10. **Subcell resolution in flux form** (Alg. 3.1, eq. 3.1), for linear
    advection with $a > 0$. Critical cells are detected by minmod slopes;
    the discontinuity position inside the cell is located; the flux
    blends a left and a right flux with weight
    $\xi_j = \min((1-\theta_j)\Delta x/(a\Delta t), 1)$. Simpler than
    Harten's, less accurate in theoretical resolution; its naive 2D
    extension fails (Remark 3.1e, Example 5).
11. **Artificial compression in flux form** (Alg. 3.2, eqs. 3.2–3.3). A
    minmod-limited correction $c_{j+1/2}$ is added to the flux;
    monotonicity is preserved for any compression coefficient, typically
    $2 \le \alpha \le 5$ with "no general rule"; an adaptive coefficient is
    eq. 3.3. For Euler it is applied only in the linearly degenerate fields
    (p. 42).
12. **Multidimensions** (p. 42). §II applied to each $f_i(u)_{x_i}$; CFL
    condition $\Delta t\max_u\sum_i(1/\Delta x_i)|f_i'(u)| \le \lambda_0$.
13. **Local characteristic decomposition** (Alg. 4.1, eqs. 4.1–4.4).
    Jacobian at $\frac12(u_j + u_{j+1})$ or, for Euler, at the Roe
    average; biorthonormal eigenvectors; project (4.1), run the scalar
    algorithm per field with $\bar a_{j+1/2} = \lambda^{(p)}_{j+1/2}$,
    recompose (4.2). The LLF coefficient per field is a maximum of
    $|\lambda^{(p)}|$ along a phase-space curve (4.3); for Euler
    $\max(|\lambda^{(p)}(u_j)|, |\lambda^{(p)}(u_{j+1})|)$ (4.4). Third
    order costs about $\frac{16}{9}$ times the vector multiplications of
    second order (p. 44).
14. **Conclusion** (§VI). ENO-RF is preferred: half the cost of ENO-LLF or
    ENO-LF, better resolution, and it "seems always to converge to the
    correct entropy solution". Open: rarefaction corners and a stability
    proof.

# Tests

Naming ENO-X-(Y)-$r$: X ∈ {Roe, LLF, RF, LF}, Y ∈ {S (Alg. 3.1), A
(Alg. 3.2)}. Mostly third order is shown (§V).

1. **Nonconvex scalar Riemann problems** (Ex. 1, eqs. 5.1–5.2, Fig. 1).
   Data $u_l = 2$, $u_r = -2$; $u_l = -3$, $u_r = 3$; and a
   Buckley–Leverett-type flux with $u^0 = -1$ on $[-\frac12, 0]$, 0
   elsewhere. ENO-RF-3 converges to the entropy solution, a "considerable"
   improvement over Figs. 14, 18 and 22 of the 1988 paper. The flux
   formulas were not verified on the page.
2. **Linear advection, contact sharpening** (Ex. 2, eqs. 5.3–5.4, Figs.
   2–5). $u_t + u_x = 0$ on $[-1,1]$, periodic, 100 points: Zalesak's
   square wave (800 steps, CFL 0.2), Gaussian $e^{-300x^2}$ and half-ellipse
   (600 steps, CFL 0.1), and Harten's composite profile at $t = 8$.
   ENO-Roe-S-3 and ENO-Roe-A-3 improve on ENO-Roe-3 in all cases.
3. **2D Burgers Riemann problems** (Ex. 3, eq. 5.5, Figs. 6–7). Four
   quadrants, eight solution types (Wagner). ENO-RF-3 gives the entropy
   solution in all; on $20\times20$ it matches first-order Engquist–Osher
   on $80\times80$.
4. **Steady 2D "boundary layer"** (Ex. 4, eq. 5.6, Fig. 8).
   $u_t + (u^2/2)_x + u_y = 0$, ENO-RF-3 on $30\times30$.
5. **Rotated advection on an anisotropic grid** (Ex. 5, eq. 5.7, Fig. 9).
   A disc advected diagonally, $\Delta y = 2\Delta x = \frac1{20}$,
   $t = 2$. ENO-Roe-A-3 much better than ENO-Roe-3; naive 2D subcell
   resolution "does not work well".
6. **Sod and Lax shock tubes** (Ex. 6, eqs. 5.8–5.9, Figs. 10–11).
   $\gamma = 1.4$; Sod data $(\rho, q, P) = (1, 0, 1)$ and
   $(0.125, 0, 0.1)$, ENO-RF-3 on 100 points, output time printed $t = 2$;
   Lax data $(0.445, 0.698, 3.528)$ and $(0.5, 0, 0.571)$, 100 points,
   $t = 1.3$. S and A variants sharpen contacts; rarefaction corners are
   poorly resolved and "still under investigation".
7. **Woodward–Colella interacting blast waves** (Ex. 7, eq. 5.10, Figs.
   12–13). Pressures $10^3$, $10^{-2}$, $10^2$, reflecting walls,
   $t = 0.038$; reference ENO-RF-S-3 on 800 points. On 400 points ENO-RF-3
   has converged in velocity and pressure, not in density; ENO-RF-S-3 and
   ENO-RF-A-3 on 200 points beat ENO-RF-3 on 400 in density.
8. **1D shock–density-wave interaction** (Ex. 8, eq. 5.11, Figs. 14–15).
   $\gamma = 1.4$. $(\rho, q, P) = (3.857143, 2.629369, 10.33333)$ for
   $x < -4$; $\rho = 1 + \varepsilon\sin 5x$, $q = 0$, $P = 1$ for
   $x \ge -4$; a Mach 3 shock moving right, $\varepsilon = 0.2$, output at
   $t = 1.8$. Reference ENO-RF-3 on 1600 points. ENO-RF-3 on 200 points
   matches a second-order MUSCL-type TVD scheme on 800 in density (Fig.
   14); little gain in velocity and pressure (Fig. 15). Domain, boundary
   conditions and CFL number are not printed; the figure axes span about
   $[-5, 5]$.
9. **2D shock–vorticity-wave interaction** (Ex. 9, eqs. 5.12–5.13, Fig.
   16). A Mach 8 shock at $x = -1$ moving into $P_R = \rho_R = 1$ with a
   sinusoidal velocity perturbation, $k_R = 2\pi$, $\theta_R = \pi/6$;
   $t = 0.20$; ENO-RF-3 on $60\times40$ and $120\times80$. Earlier results
   used shock fitting; "A small spurious oscillation will be enough to
   kill any resolution of the specified small fluctuations" (p. 71).

No MHD test and no divergence measurement.

# Notation map

| Shu & Osher (1989) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_j$, $u_j^n$ | $w_j$, time level $n$ | **collision:** $u_h$ is the velocity field |
| $\Delta x$, $\Delta x_i$ | $h$ | |
| $\hat f_{j+1/2}$ | words: numerical flux | used on [WENO](/methods/weno.md) without registration |
| $h(x)$ (Lemma 2.1) | words: implicit function whose cell averages are the point fluxes | **collision:** $h$ fine grid spacing |
| $H(x)$ | words: flux primitive | **collision:** $H$ coarse grid spacing |
| $r$, $\bar r$, $c_r$ | words: order, stage count, CFL coefficient | **collision:** refinement ratio $r$ |
| $\lambda = \Delta t/\Delta x$, $\lambda_0$ | words: CFL number | **collision:** $\lambda_k$ characteristic speed |
| $\lambda^{(p)}_{j+1/2}$; $l^{(p)}$, $r^{(p)}$ | $\lambda_k$; words: left and right eigenvectors | field index $p \to k$ |
| $\bar a_{j+1/2}$ | words: Roe speed | |
| $\alpha_{j+1/2}$ (eq. 2.12) | $\alpha^{\mathrm{LF}}$ with a face index | local, per interface |
| $\alpha$, $\alpha_0$, $\beta$ (eqs. 3.2–3.3) | words: compression coefficients | **collision:** $\beta$ plasma beta, $\alpha^{\mathrm{LF}}$ |
| $\alpha_{ik}$, $\beta_{ik}$ | words: convex stage weights, Euler-step weights | **collision:** as above |
| $q$, $q_x$, $q_y$ | words: velocity | **collision:** $q$ ghost-fill order |
| $P$ | words: pressure | **collision:** $P$ prolongation |
| $m(\cdot)$ (minmod) | words: minmod | **collision:** $m(E)$ SFC index |
| $L(u)$ | words: spatial operator | not registered |
| $\gamma$ | $\gamma$ | adiabatic index |

# Pages created or updated

* Updated [SSP Runge–Kutta methods](/methods/ssp-runge-kutta.md) (created
  in this batch): Table I, multidimensional CFL condition.
* Updated [WENO reconstruction](/methods/weno.md): the flux-primitive form
  (Lemma 2.1), local Lax–Friedrichs splitting as ENO-LLF, RF splitting.
* Updated [Constrained transport](/methods/constrained-transport.md).
* Updated Source pages of [Jiang & Shu (1996)](/sources/jiang-shu-1996.md) and
  [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md).

# Citations

1. `~/papers/mosaic/div-free-amr/1989-JCP-Shu-1010160021-99918990222-2.pdf`
   (copied from a sibling archive, D17).
   * **Version read.** The published journal version (Academic Press
     typeset pages 32–78, 47 PDF pages; journal page = PDF page + 31).
     Received April 15, 1988; revised August 2, 1988.
   * **Identity.** doi:10.1016/0021-9991(89)90222-2, checked on Crossref
     (2026-10-13): "Efficient implementation of essentially
     non-oscillatory shock-capturing schemes, II", Shu & Osher, J. Comput.
     Phys. 83(1):32–78, issued July 1989. Matches page 1.
   * **How it was read.** A scan with an OCR layer that garbles equations;
     every equation quoted was read from page renders at 110–250 dpi.
     Not rendered and not reproduced: eqs. 5.1–5.2 (nonconvex fluxes),
     5.5 (2D Burgers data), 5.8 (1D Euler flux), 5.12c and 5.13a–b
     (eigenvalues and right eigenvectors), and the explicit form of 1.5.
   * **Recorded as printed.**
     * Eq. 5.4d, third piece, printed "$2x = 1 - \sin(3\pi x)/6$" on
       $\frac13 < x < 1$; the "=" is evidently a typesetting error for "−"
       (reader's reading).
     * Example 9: the velocity amplitude is printed $c_R/P_R$ (checked at
       250 dpi); with $P_R = \rho_R = 1$ it equals $c_R$. Not checked
       against Zang et al.
     * Examples 8 and 9 print no computational domain and no boundary
       conditions; Example 8 prints no CFL number.
   * **Reference list.** 18 entries, all merged. Harten's ICASE Report
     87-56 is `harten-1989` (NTRS 19870018924, "ENO schemes with subcell
     resolution"); Harten's "in preparation" is `harten-1989-b`. Ref. 12 is
     the ingested [Shu & Osher (1988)](/sources/shu-osher-1988.md).
     Bibliography key renamed `shu-1989` → `shu-osher-1989`; its DOI was
     corrected to 10.1016/0021-9991(89)90222-2 (the stored string lacked
     the hyphen and returned 404 on Crossref). The bibliography holds 3779
     entries after this batch.
