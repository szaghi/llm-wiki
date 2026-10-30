---
type: Source
title: "Charles & Ray (2025) — Learning WENO for Entropy Stable Schemes to Solve Conservation Laws"
description: "DSP-WENO: a third-order sign-preserving WENO reconstruction for entropy-stable TeCNO schemes whose weight perturbations are convex combinations, chosen by a small network, of the vertices of a hand-built feasible polygon, so that consistency, the sign property and third order hold by construction."
resource: "doi:10.1137/24m1697566"
source_kind: paper
authors: [Charles P., Ray D.]
year: 2025
venue: "SIAM J. Sci. Comput. 47:C1196-C1222"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_SIAM_Journal_on_Scientific_Computing_Charles_Learning_WENO_for_Entropy_Stable_Schemes_to_Solve_Conservati.pdf"
tags: [entropy-stable, weno, machine-learning, finite-difference, sign-property]
timestamp: 2026-10-23T20:30:00Z
---

# Summary

Charles & Ray (2025) work with [TeCNO schemes](/methods/tecno-scheme.md): high-order
[entropy-conservative fluxes](/methods/entropy-conservative-flux.md) plus a numerical
diffusion acting on the reconstructed interface jump of scaled entropy variables.
These are [entropy stable](/properties/entropy-stability.md) when the reconstruction
has the sign property, the reconstructed jump having the sign of the undivided jump.
ENO has it, and two third-order WENO variants were built to have it:
[SP-WENO](/methods/sign-preserving-weno.md) (Fjordholm & Ray 2016) and SP-WENOc (Ray
2018). The authors show that both overshoot at shocks, because their reconstructed
jump vanishes, or nearly so, in most cases near a discontinuity, so the scheme adds
almost no diffusion there.

The contribution is DSP-WENO (Deep Sign-Preserving WENO). It keeps the SP-WENO
third-order form, two two-point candidates on a four-point stencil whose linear weights
are perturbed by two parameters $(C_1,C_2)$. For each stencil a hand-derived vertex
selection algorithm builds a convex polygon of at most five vertices in the
$(C_1,C_2)$ plane, on which consistency, the sign property and third-order accuracy
hold. A small network (three hidden layers of five ReLU neurons, softmax output, 120
parameters) returns five convex weights, and $(C_1,C_2)$ is the corresponding
combination of the vertices, so every output satisfies the constraints by construction.
Training uses interface values of synthetic smooth and piecewise-linear functions only,
and one trained network serves every conservation law of the paper: this is
[learned WENO weights](/methods/learned-weno-weights.md) with the structure imposed
strongly rather than by a penalty.

With a fourth-order entropy-conservative flux, Roe-type diffusion and
[SSP-RK3](/methods/ssp-runge-kutta.md), DSP-WENO keeps third order on linear advection
and the [isentropic vortex](/benchmarks/isentropic-vortex.md), where ENO3 loses order,
which the authors attribute to its linear instability. It is more dissipative than
SP-WENO and SP-WENOc in smooth regions but largely removes their overshoots on Burgers,
modified Sod, Shu–Osher, Lax, 2D Riemann and Kelvin–Helmholtz tests, at up to about
five times the cost per reconstruction. In Configuration 3, SP-WENO and DSP-WENO show
a [carbuncle](/definitions/carbuncle-phenomenon.md)-like artefact, weakened by
Rusanov-type diffusion. The one proof is a jump bound for DSP-WENO.

# Version read

The archive file is arXiv:2403.14848v2 [math.NA], 3 June 2025, 37 pages (main text and
references pp. 1–25, Supplementary Materials pp. SM1–SM12), all read; pp. 5–8, 15 and
SM1–SM6 checked on the page images. It is the authors' preprint, not the SIAM version
of record; the DOI is not printed on it. Title (capitalized differently on Crossref)
and authors match the Crossref record. Code: github.com/pmcharles/DSP-WENO. Every
claim, equation and number on this page is that of arXiv v2.

# Key claims

Registry notation: point values $u_i$ of a conservative finite-difference scheme,
spacing $\Delta x$ (source $h$), entropy $\eta$, entropy flux $F_\eta$ (source $q$),
entropy variables $w=\eta'(u)$ (source $v$), entropy-flux potential $\psi$ (source
$\Psi$), right eigenvectors $R$, entropy-conservative flux $f^{\mathrm{ec}}$ (source
$\tilde f$). Page-local: $z=R^\top_{i+1/2}w$ the scaled entropy variables,
$z^\pm_{i+1/2}$ their reconstructed interface values, $[\![z]\!]_{i+1/2}=z^+-z^-$ the
reconstructed jump, $\Delta z_{i+1/2}=z_{i+1}-z_i$ the undivided jump; $\omega_0$,
$\omega_1$ (left) and $\tilde\omega_0$, $\tilde\omega_1$ (right) the nonlinear weights
(source $w$); $(C_1,C_2)$ the perturbations; $\vartheta^-_i=\Delta z_{i+1/2}/\Delta z_{i-1/2}$,
$\vartheta^+_i=1/\vartheta^-_i$ the jump ratios (source $\theta^\pm$) and
$\psi^\pm_{\mathrm{SP}}$ the SP-WENO ratio (source $\psi^\pm$).

1. TeCNO schemes are entropy stable when the reconstruction of $z$ satisfies the sign property $\mathrm{sign}([\![z]\!]_{i+1/2})=\mathrm{sign}(\Delta z_{i+1/2})$ componentwise, with flux $\hat f_{i+1/2}=f^{\mathrm{ec},p}_{i+1/2}-\tfrac12R\Lambda[\![z]\!]_{i+1/2}$ (Lemma 1, Eqs. (10)–(11), quoting Fjordholm, Mishra & Tadmor). **Stated**
2. With the dissipation $\tfrac12D_{i+1/2}\Delta w_{i+1/2}$, $D\succeq0$, the scheme satisfies the discrete entropy inequality (8), but the unreconstructed jump $\Delta w=O(\Delta x)$ limits it to first order (§2). **Stated**
3. Only a handful of sign-property reconstructions exist: ENO, SP-WENO, SP-WENOc and two others; an alternative replaces the sign property by a special diffusion operator usable with any reconstruction (§1). **Stated**
4. For SP-WENO, $[\![z]\!]=\tfrac12\big[\tilde\omega_0(1-\vartheta^-_{i+1})+\omega_1(1-\vartheta^+_i)\big]\Delta z_{i+1/2}$, so the sign property is equivalent to $\tilde\omega_0(1-\vartheta^-_{i+1})+\omega_1(1-\vartheta^+_i)\ge0$ (Eqs. (15)–(16)). **Derived**
5. SP-WENO satisfies consistency ($-\tfrac38\le C_1,C_2\le\tfrac18$), the sign property, negation symmetry, the mirror property, the inner jump condition and the jump bound $\lvert[\![z]\!]\rvert\le2\lvert\Delta z_{i+1/2}\rvert$ (§3.1, Eq. (20), from Fjordholm & Ray). **Stated**
6. SP-WENO performs poorly at discontinuities because its reconstructed jump is zero in most cases there (the "C-region", $\vartheta^+_i<1<\vartheta^-_{i+1}$ or $\vartheta^-_{i+1}<1<\vartheta^+_i$), giving no numerical diffusion (§3.2, citing Ray 2018). **Stated** (and **Shown** in §5)
7. SP-WENOc adds a perturbation $\mathcal G$ (Eq. (21)) that makes the jump non-zero in the C-region and keeps every SP-WENO property except the jump bound (20) (§3.2). **Stated**
8. DSP-WENO restricts $(C_1,C_2)$ to a convex polygon of at most five vertices, built case by case over six subdomains of the $(\vartheta^+_i,\vartheta^-_{i+1})$ plane; any convex combination gives consistent weights, the sign property and third order for smooth data (§4, §4.1, SM1–SM2, Algorithm SM1). **Derived**
9. DSP-WENO satisfies all SP-WENO properties except the mirror property, which the vertex algorithm and the network break (§4.4). **Stated**
10. Jump bound: $\lvert[\![z]\!]_{i+1/2}\rvert\le\tfrac12\lvert\Delta z_{i-1/2}\rvert+\lvert\Delta z_{i+1/2}\rvert+\tfrac12\lvert\Delta z_{i+3/2}\rvert$ (Eq. (32), Lemma SM1); the original SP-WENO satisfies a sharper bound (Remark SM5). **Proved**
11. DSP-WENO is not positivity preserving for Euler, since no constraint enforces it (Remark 5). **Stated**
12. Network: MLP with three hidden layers of five neurons, ReLU, softmax output, 120 parameters; Adam ($\beta_1=0.5$, $\beta_2=0.9$, learning rate $10^{-3}$, weight decay $10^{-5}$), split 0.6/0.2/0.2, mini-batches of 500, 50 epochs, under 30 s per training on a laptop CPU; the best of five initializations on the test set is kept (§4.3). **Stated**
13. Dataset: 100,000 four-point samples, half smooth (cubics, sines) and half piecewise linear with a jump, at $\Delta x=1/40,1/100,1/200$ (§4.2, Table 1); no conservation-law solutions are used (Remark 3). **Stated**
14. Reconstruction of $\sin(10\pi x)+x$: all methods converge at third order or better, SP-WENO and SP-WENOc super-converge (rates up to 3.82); at $N_x=1280$ the errors are $1.22\cdot10^{-6}$ (DSP-WENO), $1.17\cdot10^{-6}$ (ENO3) and $1.68\cdot10^{-7}$ (SP-WENO) (§5.1, Table 2). **Shown**
15. Linear advection of $\sin^4x$: the $L^1$ rate of ENO3 drops to 1.99 and 1.32 at $N_x=800,1000$, which the authors attribute to the linear instability of ENO; the SP variants and DSP-WENO keep about third order (DSP-WENO 3.04 at $N_x=1000$) (§5.2.1, Table 3). **Shown**
16. In $L^\infty$ all rates deteriorate somewhat; ENO3 falls to 0.43 on the $\sin^4x$ test at $N_x=1000$ (§SM4.2, Table SM3). **Shown**
17. On 100,000 random stencils reconstruction takes 0.852 s (DSP-WENO), 0.178 s (SP-WENO), 0.192 s (SP-WENOc) and 0.839 s (ENO3); 95% of the DSP-WENO cost is the vertex search, and inside the solver DSP-WENO is 2–3 times more expensive at fine resolution, which the authors attribute to unbatched network queries (§5.2.2). **Shown**
18. Burgers with Riemann data $3/-1$: all methods oscillate, "a fundamental problem" of high-order TeCNO schemes that persists with minmod, which also has the sign property (Remark 6); DSP-WENO reduces the oscillations leading up to the overshoot (§5.2.3, Fig. 4). **Shown**
19. Modified Sod, [Shu–Osher](/benchmarks/shu-osher-problem.md) and Lax tests: SP-WENO and SP-WENOc overshoot significantly at the shock; DSP-WENO overshoots only slightly and resolves shocks about as ENO3 does, with a sharper contact in modified Sod, and is the most dissipative in the Shu–Osher oscillatory region, comparable to ENO3 (§5.3, Figs. 6–8). **Shown**
20. Isentropic vortex: $L^1$ density rates about 2.2 for ENO3, 3.6–3.9 for SP-WENO and SP-WENOc, 3.13–3.30 for DSP-WENO with larger errors (Table 4). **Shown**
21. 2D Riemann Configuration 3: SP-WENO and DSP-WENO show a carbuncle-like protrusion, stronger for SP-WENO and absent for SP-WENOc; entropy stability does not preclude it, and a Rusanov-type dissipation $\Lambda=(\lvert v\rvert+c)I$ weakens it (§5.3, Fig. 10, Figs. SM4–SM5). **Shown**
22. The authors relate the carbuncle to a scheme's ability to resolve contacts, citing Chandrashekar's empirical results (§5.3, §6). **Stated**
23. Kelvin–Helmholtz: a single deterministic sample does not converge under refinement; only statistics converge, in the measure-valued sense (§5.3, Fig. 11). **Stated** (cited)
24. Strong imposition of the constraints is preferred to a weak, PINN-type penalty, which cannot guarantee the sign property and hence entropy stability, and networks trained at one resolution rarely show mesh convergence (§6). **Stated**
25. The ENO3 interface reconstruction uses six points, the third-order SP-WENO variants four (§6). **Stated**
26. One trained DSP-WENO network is used for scalar advection, Burgers and the 1D and 2D Euler equations, applied to scaled entropy variables (§1, §6). **Shown**

*(Compiler check, not in the sources: from Eqs. (12)–(13),
$[\![z]\!]_{i+1/2}=(C_1-\tfrac18)\Delta z_{i-1/2}+(\tfrac14-C_1-C_2)\Delta z_{i+1/2}+(C_2-\tfrac18)\Delta z_{i+3/2}$
identically. The consistency bounds $-\tfrac38\le C_k\le\tfrac18$ alone give
$\lvert C_k-\tfrac18\rvert\le\tfrac12$ and $\lvert\tfrac14-C_1-C_2\rvert\le1$, hence the
bound of claim 10 for every weight choice of this form, sign-preserving or not.)*

# Printed slips

- **Entropy variables for Euler** (p. 15): printed $w=\big[-\beta\lvert v\rvert^2-\frac{\gamma-s}{\gamma-1},\ 2\beta v^\top,\ -2\beta\big]^\top$, $\beta=\rho/(2p)$, for $\eta=-\rho s/(\gamma-1)$, $s=\ln p-\gamma\ln\rho$. *(Compiler check, not in the sources: differentiating $\eta$ at fixed momentum and energy gives $\partial\eta/\partial\rho=\frac{\gamma-s}{\gamma-1}-\beta\lvert v\rvert^2$; the second and third components agree, so the first should carry $+\frac{\gamma-s}{\gamma-1}$.)*
- **"About an order of magnitude"** (§5.2.1, p. 11): the text says the DSP-WENO errors in the advection tests are "about an order of magnitude larger than those of SP-WENO and SP-WENOc". Table 3 prints, at $N_x=1000$, $1.66\cdot10^{-6}$ against $8.94\cdot10^{-7}$ ($\sin^4x$) and $5.02\cdot10^{-8}$ against $4.22\cdot10^{-8}$ ($\sin x$). *(Compiler check, not in the sources: ratios 1.9 and 1.2; the reconstruction test of Table 2 gives 7.3 at $N_x=1280$.)*
- **Remark SM5 against its proof**: the remark calls the bound (SM3) "a consequence of the sign property constraint (16)", but the proof uses only the consistency bounds (see the compiler check above).
- **§4.4 property list**: DSP-WENO is said to satisfy all SP-WENO properties except the mirror property, a list that includes the jump bound (20), while only the weaker bound (32) is proved.
- **Case 4a** (SM2, p. SM3): the text describes the segment $C_1=\tfrac18$, $-\tfrac38\le C_2\le\tfrac18$, but gives the endpoints $(\tfrac18,\tfrac18)$, $(-\tfrac38,\tfrac18)$ and midpoint $(-\tfrac18,\tfrac18)$, which lie on $C_2=\tfrac18$ (the Case 5a points); Algorithm SM1 gives the consistent $(\tfrac18,-\tfrac38)$, $(\tfrac18,\tfrac18)$, $(\tfrac18,-\tfrac18)$.
- §3, p. 5: WENO is said to combine "the $2k-1$ candidate polynomials considered in the $k$th-order ENO reconstruction"; ENO of order $k$ has $k$ candidates, and the paper's own third-order form (12) combines two.
- Loss (31) is called mean squared error but printed as the unsquared $\lVert\hat Y-Y\rVert_2$.
- The scalar flux (33) has no factor $\tfrac12$ in front of the dissipation, unlike (11); the coefficient $a_{i+1/2}$ is the mean of $\lvert f'\rvert$. The paper does not comment.
- Configuration 12: "The reference solution is once again generated using ENO3" with no earlier reference solution; the quadrant states are defined only after Configuration 3.
- "peridoc" (p. 12); "While is was not the focus" (Remark 5); "There are not constraints" (SM2); "is solved on the domain is [0, 1]" (p. 15); ref. [12] prints the author Dafermos twice.

# Notation map

| Charles & Ray (arXiv v2) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $h$, $I_i$ | $u_i$, $\Delta x$, $I_i$ | point values (finite difference) |
| $\Delta(\cdot)_{i+1/2}$, $\overline{(\cdot)}_{i+1/2}$ | undivided jump, $\{\!\{\cdot\}\!\}$ | |
| $\eta$, $q$ | $\eta$, $F_\eta$ | **collision**: source $q$ is the entropy flux |
| $v=\nabla_u\eta$ | $w$ | **collision**: source $v$ is not velocity |
| $\Psi=v^\top f-q$ | $\psi$ | **collision** with the source's own $\psi^\pm$ |
| $\tilde f_{i+1/2}$, $\tilde f^p$ | $f^{\mathrm{ec}}$, order-$p$ entropy-conservative flux | |
| $D=R\Lambda R^\top$, $\Lambda$ | dissipation matrix, $\mathrm{diag}(\lvert\lambda_l\rvert)$ | |
| $z=R^\top v$, $z^\mp_{i+1/2}$, $\llbracket z\rrbracket$ | page-local; $[\![z]\!]=z^+-z^-$ | $-$ from cell $i$; agrees with the registry jump |
| $w_0,w_1$, $\tilde w_0,\tilde w_1$ | $\omega_0,\omega_1$, $\tilde\omega_0,\tilde\omega_1$ | **collision** of $w$ with the entropy variables; linear weights $d=\tfrac34,\tfrac14$ |
| $C_1$, $C_2$ | page-local | not the TENO constant $C$ |
| $\theta^\pm_i$ | $\vartheta^\pm_i$ (local) | **collision** with the Zhang–Shu factor $\theta$; not the reduced wavenumber $\vartheta$ |
| $\psi^\pm_{i+1/2}$, $\kappa^\pm$, $\mathcal G$, $\mathcal L$ | $\psi^\pm_{\mathrm{SP}}$, page-local | $\mathcal G$ not the flux-globalization integral |
| $\alpha$, $\nu$ (network output, vertices) | page-local | **collision** with $\alpha_k$ and the CFL number $\nu$ |
| $\mathbf u$, $a$ | $v$, $c$ | **collision**: source $a$ is the sound speed and, in (33), a dissipation coefficient |
| $\beta=\rho/(2p)$, $\hat\rho$, $\hat\beta$ | page-local; $\{\!\{\cdot\}\!\}_{\log}$ | **collision** of $\beta$ with $\beta_k$ |
| $\Gamma$ (vortex strength) | $\mathcal E$ | |

# Reference list

The arXiv v2 prints 66 references, numbered [1]–[66], alphabetical by first author. The
list is merged complete into the [bibliography](/bibliography.md), with `citedby`
including `charles-2025`. Five items are arXiv preprints and keep preprint keys ([8]
Chertock, Chu & Kurganov; [26] Huang, Nelsen & Trautner; [30] Kingma & Ba; [38] Li,
Fu & Adams, NENO6; [39] Li et al., Fourier neural operator). Several printed-order keys
name different works than the bibliography entries of the same key and are matched by
venue: [1] (Abgrall & Han Veiga, neural limiter), [65] (Yu & Shu, La Matematica), the
two Ray 2018 items ([50] proceedings, [51] Ray & Hesthaven) and the two Ismail 2009
items ([27] proceedings, [28] Ismail & Roe), and the Fjordholm & Ray, Cheng, Harten
1983, Lu, Sun and Yang items. Ref. [12] prints its author twice. No item is
unparseable.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunks 11–12 (2026-10-24/30). This source is cited on:

* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Learned WENO weights](/methods/learned-weno-weights.md)
* [Logarithmic mean](/operators/logarithmic-mean.md)
* [Sign-preserving WENO](/methods/sign-preserving-weno.md)
* [TeCNO schemes — entropy-stable reconstruction with the sign property](/methods/tecno-scheme.md)
