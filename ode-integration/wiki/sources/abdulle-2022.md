---
type: Source
title: "Abdulle et al. (2022) — Explicit stabilized multirate method for stiff differential equations"
description: "Introduces the multirate Runge–Kutta–Chebyshev (mRKC) method: an outer RKC discretizes a modified equation whose averaged force, computed by a short inner RKC run on the cheap stiff part, has a spectrum bounded by the slow part; proves stability and first order without scale separation."
resource: "doi:10.1090/mcom/3753"
source_kind: paper
authors: [Abdulle A., Grote M.J., Rosilho de Souza G.]
year: 2022
venue: "Math. Comp. 91:2681-2714"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Mathematics_of_Computation_Abdulle_Explicit_stabilized_multirate_method_for_stiff_differential.pdf"
tags: [multirate, stabilized, explicit, stiff, stability, local-time-stepping]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper treats stiff systems $y'=f(y)=f^{\{\mathrm f\}}(y)+f^{\{\mathrm s\}}(y)$
in which an expensive, mildly stiff part $f^{\{\mathrm s\}}$ coexists with a
cheap, severely stiff part $f^{\{\mathrm f\}}$ acting on few degrees of
freedom; the canonical case is a parabolic problem on a locally refined mesh.
A standard [stabilized Runge–Kutta–Chebyshev method](/methods/stabilized-explicit-runge-kutta.md)
takes its stage number from the full spectral radius, so the few stiff
components force every expensive $f^{\{\mathrm s\}}$ evaluation to be repeated.

The remedy is a modified equation $y_\eta'=f_\eta(y_\eta)$ with the
**averaged force** $f_\eta(y)=(u(\eta)-y)/\eta$, where $u$ solves
$u'=f^{\{\mathrm f\}}(u)+f^{\{\mathrm s\}}(y)$, $u(0)=y$, on $[0,\eta]$ with
$f^{\{\mathrm s\}}$ frozen. For linear $f^{\{\mathrm f\}}=L^{\{\mathrm f\}}y$,
$f_\eta=\phi_1(\eta L^{\{\mathrm f\}})f$, which compresses the fast spectrum.
The authors prove a smoothing bound, contractivity and an $O(\eta)$ error bound
independent of the stiffness of $f^{\{\mathrm f\}}$ (under commuting
Jacobians), and show that on the scalar multirate test equation the spectrum
of $f_\eta$ is bounded by the slow eigenvalue iff $\eta\ge2/\lvert\lambda^{\{\mathrm s\}}\rvert$,
with no scale-separation assumption.

The [multirate RKC method (mRKC)](/methods/multirate-runge-kutta-chebyshev.md)
discretizes the modified equation by an $s$-stage RKC whose stage count is set
by $\rho^{\{\mathrm s\}}$, and evaluates $f_\eta$ by one step of size $\eta$ of an
$m$-stage RKC set by $\rho^{\{\mathrm f\}}$. Stability on the
[multirate test equation](/definitions/multirate-linear-stability.md) and first
order are proved; a $2\times2$ non-commuting model shows the condition on
$\eta$ is needed even for weak coupling. Experiments cover the
[Robertson problem](/benchmarks/robertson-problem.md), the
[heat equation](/benchmarks/heat-equation.md) with
[local mesh refinement](/methods/local-time-stepping.md), diffusion through a
narrow channel (speed-up up to about 40 over RKC and 70 over second-order RKC,
on par with implicit Euler), and a nonlinear integro-differential problem.

# Version read

The file is the arXiv preprint arXiv:2006.00744v6 (4 April 2022), 31 pages,
all read; it is not the Math. Comp. typeset, so it carries no journal page
numbers. It is the revised text: it records that Abdulle died on 1 September
2021 during the revision. Title and authors on page 1 match Crossref. The
file was re-downloaded on 2026-10-19 after the original download error (bundle
law, Corpus). Numbering cited here is that of arXiv v6.

# Key claims

1. When stiffness comes from a few components (local mesh refinement), any standard stabilized Runge–Kutta method takes its stage number from the stiffest part $f^{\{\mathrm f\}}$ and loses efficiency (§1, p. 2). **Stated**
2. Lemma 2.2: if $f^{\{\mathrm f\}}$ satisfies a one-sided Lipschitz condition with constant $\mu^{\{\mathrm f\}}$ (Eq. 2.4), then $\lVert f_\eta(y)\rVert\le\phi_1(\eta\mu^{\{\mathrm f\}})\lVert f(y)\rVert$; if $f^{\{\mathrm f\}}=L^{\{\mathrm f\}}y$, then $f_\eta(y)=\phi_1(\eta L^{\{\mathrm f\}})f(y)$ exactly (Eqs. 2.5–2.6). **Proved**
3. For linear $f^{\{\mathrm f\}}$ the auxiliary solution $u(\eta)=e^{\eta L^{\{\mathrm f\}}}y+\eta\phi_1(\eta L^{\{\mathrm f\}})f^{\{\mathrm s\}}(y)$ is one exponential-Euler step of the full problem (Eq. 2.7, Remark 2.3); mRKC never computes $\phi_1(\eta L^{\{\mathrm f\}})$, and $\eta$ is not a step size. **Derived**
4. Thm 2.4: if $L^{\{\mathrm f\}}$ is symmetric, the Jacobian of $f$ satisfies the one-sided bound (2.8) with $\mu\le0$, and $L^{\{\mathrm f\}}$ commutes with $\partial f^{\{\mathrm s\}}/\partial y$, then $f_\eta$ is one-sided Lipschitz with $\mu_\eta=\mu\min_{\lambda\in\sigma(L^{\{\mathrm f\}})}\phi_1(\eta\lambda)\le0$ (contractivity preserved). **Proved**
5. Thm 2.5: under the same hypotheses, $\lVert y(t)-y_\eta(t)\rVert\le\max_\lambda\lvert1-\phi_1(\eta\lambda)\rvert\int_0^te^{\mu_\eta(t-\theta)}\lVert f(y(\theta))\rVert\,d\theta$ (Eq. 2.9), a bound independent of the stiffness of $f^{\{\mathrm f\}}$ and $O(\eta)$ as $\eta\to0$. **Proved**
6. Thm 2.7: for $\lambda^{\{\mathrm s\}}<0$, $\phi_1(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})\in[\lambda^{\{\mathrm s\}},0]$ for all $\lambda^{\{\mathrm f\}}\le0$ iff $\eta\ge2/\lvert\lambda^{\{\mathrm s\}}\rvert$; no scale separation is needed, since the bound holds for every $\lambda^{\{\mathrm f\}}\le0$ (§2.3, via Lemma 2.6: $\phi_1(z)(z+w)\in[w,0]$ for all $z\le0$ iff $\lvert w\rvert\ge2=1/\phi_1'(0)$). **Proved**
7. mRKC parameter selection (3.4): $h\rho^{\{\mathrm s\}}\le\beta_{\mathrm d}s^2$, $\eta\rho^{\{\mathrm f\}}\le\beta_{\mathrm d}m^2$, $\eta=6hm^2/(\beta_{\mathrm d}s^2(m^2-1))$ with $\beta_{\mathrm d}=2-4\varepsilon_{\mathrm d}/3$, $\varepsilon_{\mathrm d}=0.05$; $m$ from $6h\rho^{\{\mathrm f\}}\le\beta_{\mathrm d}^2s^2(m^2-1)$ (3.9). **Stated** (justified by Thm 4.5)
8. Cost model ($\varepsilon_{\mathrm d}=0$, real $s,m$, $\rho=\rho^{\{\mathrm f\}}+\rho^{\{\mathrm s\}}$): speed-up $S=\sqrt{1+r_\rho}/\big(1+c_{\mathrm f}(\sqrt{1+3r_\rho}-1)\big)$ with $r_\rho=\rho^{\{\mathrm f\}}/\rho^{\{\mathrm s\}}$ and $c_{\mathrm f}$ the relative cost of $f^{\{\mathrm f\}}$ (3.12); $S>1$ iff $c_{\mathrm f}<(\sqrt{1+r_\rho}-1)/(\sqrt{1+3r_\rho}-1)$, a bound above $0.5$ for $r_\rho>8$ (Fig. 5b). **Derived**
9. Relaxed conditions (3.13) under scale separation: $\eta=2h/(\beta_{\mathrm d}s^2)$ and $\eta\rho^{\{\mathrm f\}}\le\bar\beta_{\mathrm d}m^2$ with $\bar\beta_{\mathrm d}\approx1.86$ ($\bar\varepsilon_{\mathrm d}=0.1$); the speed-up $\bar S$ exceeds 1 for all $c_{\mathrm f}\in[0,1)$ and exceeds $S$ for all $c_{\mathrm f}$ (Fig. 6). **Derived** (justified in Remark 4.4)
10. On $y'=\lambda^{\{\mathrm f\}}y+\lambda^{\{\mathrm s\}}y$ the inner $m$-stage RKC gives $u_\eta=\big(P_m(\eta\lambda^{\{\mathrm f\}})+\Phi_m(\eta\lambda^{\{\mathrm f\}})\eta\lambda^{\{\mathrm s\}}\big)y$ with $\Phi_m(z)=(P_m(z)-1)/z$ (Lemma 4.1), so $\bar f_\eta(y)=\Phi_m(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})y$ (4.4) and the mRKC stability polynomial is $P_{s,m}=P_s\big(h\Phi_m(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})\big)$ (Def. 4.2). **Proved**
11. Lemma 4.3 (discrete analogue of Lemma 2.6): for damping $\varepsilon_{\mathrm d}\le\bar\varepsilon_m$, $\Phi_m(z)(z+w)\in[w,0]$ for all $z\in[-\ell_m,0]$ iff $\lvert w\rvert\ge2/P_m''(0)$; for $\varepsilon_{\mathrm d}=0$, $2/P_m''(0)=6m^2/(m^2-1)>6$, against $\lvert w\rvert\ge2$ in the continuous case (pp. 13–14, proof in App. A). **Proved**
12. Thm 4.5: for $\lambda^{\{\mathrm f\}}\le0$, $\lambda^{\{\mathrm s\}}<0$, $h\lvert\lambda^{\{\mathrm s\}}\rvert\le\ell_s$, $\eta\lvert\lambda^{\{\mathrm f\}}\rvert\le\ell_m$ and $\eta\ge\frac{6h}{\ell_s}\frac{m^2}{m^2-1}$ (4.5), $\lvert P_{s,m}\rvert\le1$. **Proved**
13. The restriction $\varepsilon_{\mathrm d}\le\bar\varepsilon_m$ is "probably not needed in practice": the equivalence of Lemma 4.3 is verified numerically for any $\varepsilon_{\mathrm d}\ge0$, which justifies replacing $\ell_s,\ell_m$ by $\beta_{\mathrm d}s^2,\beta_{\mathrm d}m^2$ in (3.4) (p. 15, Fig. 8 for $s=5$, $m=3$, $\varepsilon_{\mathrm d}=0.05$ and $1$). **Shown**
14. In the discrete method $\eta$ depends on $f^{\{\mathrm s\}}$ only through $s$, a "protective buffer" that prevents $\eta\to\infty$ as $\lambda^{\{\mathrm s\}}\to0$, since $\ell_s\ge2$ (p. 15). **Stated**
15. $2\times2$ model (4.6)–(4.7) with non-simultaneously-triangularizable fast and slow matrices and weak coupling $\sigma_{\mathrm c}=0.1\sqrt{\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}}$ ($s=10$, $m=8$, $h=1$): (4.5) gives stability; with $\eta=0.9\bar\eta$ an instability region appears near $z=0$, and similarly for coupling $0.01$ and $0.001$ times $\sqrt{\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}}$ with $\eta=0.95\bar\eta$; condition (4.5) is therefore necessary even for weak coupling (§4.1, Fig. 9). **Shown**
16. Thm 4.6: mRKC is first-order accurate, with local error $O(\eta h+h^2)$ and $\eta\le8h$ from (3.4). **Proved**
17. Robertson (5.1), $t\in[0,100]$, $h=2^{-k}$, $k=0,\dots,7$: RKC and mRKC are both first order with nearly equal errors and mean $\eta\ll h$ (Fig. 10); with $h=1$, $\rho^{\{\mathrm s\}}$ decreases in time, so mRKC's $s$ decreases while RKC's $s$ grows with $\rho$ (Fig. 11). **Shown**
18. Heat equation on the unit square, two levels of local refinement in $(1/4,3/4)^2$, first-order DG, $h=2^{-j}$, $j=2,\dots,5$, parameters (3.13): first-order space-time convergence in $H^1$, similar errors; mRKC's $s$ much smaller, $m$ constant (Fig. 12). **Shown**
19. Narrow channel (5.4), channel width $\delta_{\mathrm c}=2^{-k}$, $k=0,\dots,15$, $h=0.01$: the CPU-time speed-up of mRKC over RKC is always $\ge1$ and reaches about 40; the relative $L^2$/$H^1$ difference between the two solutions is at most $3\cdot10^{-4}$; for $m=1$ they coincide to machine precision; $\rho,\rho^{\{\mathrm f\}}\sim\delta_{\mathrm c}^{-2}$ while $\rho^{\{\mathrm s\}}$ stays almost constant (Fig. 15). **Shown**
20. Narrow channel, work–precision ($h=T/2^j$, $j=0,\dots,16$): at $\delta_{\mathrm c}=2^{-6}$ mRKC beats second-order RKC (RKC2) at most step sizes but not at high accuracy, and implicit Euler (IE) and mRKC are about equally efficient; at $\delta_{\mathrm c}=2^{-12}$ mRKC is 10 to 70 times faster than RKC2 and IE stays slightly faster than mRKC (Fig. 16). **Shown**
21. Integro-differential problem (5.5), $N=100$: IE is always faster than RKC and comparable to mRKC at large $h$, mRKC is clearly more efficient as $h$ decreases, and RKC2 beats mRKC only at high accuracy; $N=3200$: mRKC is fastest, IE is dominated by its direct solver, and RKC and RKC2 "could not be run to completion" (Fig. 17). **Shown**
22. Reaction–convection–diffusion, three settings (refined half-domain diffusion; convection–reaction with three refinements; discontinuous diffusivity with corner refinement): $h\rho_\eta\le\beta_{\mathrm d}s^2$ iff $\lvert w(\eta)\rvert\ge2$, so the relaxed condition (3.13) is necessary and sufficient here even without scale separation (§5.5, Figs. 18–19). **Shown**
23. The modified-equation strategy needs no scale separation (unlike heterogeneous multiscale and projective methods) and, unlike MIS methods, discretizes the fast part with a compressed spectrum and comes with a fully discrete stability analysis (§2.1, pp. 4–5). **Stated**
24. Interpolation-based multirate RKC with AMR uses time interpolation of missing stage values, which "can cause numerical instabilities"; mRKC needs no interpolation or extrapolation between stages (§1, §6). **Stated**
25. Conclusion: mRKC is up to forty times faster than RKC and up to seventy times cheaper than RKC2 "for moderately high error tolerances", and "in all our numerical experiments, mRKC performed similarly, or even better, than IE" (§6). **Shown** (summary of §5; Fig. 16b has IE slightly faster)

# Printed slips

- Fig. 13 caption (p. 20): "Numerical solutions of (5.4) at t = 1", while the problem has $T=0.1$.
- Eq. (4.8): "$A_\eta=\Phi_m(\eta A_F)Ay$" carries a stray $y$; §5.5 (p. 24) restates it correctly as $\Phi_m(\eta A_F)A$.
- Proof of Thm 2.4 (p. 6): the last line minimizes over "$\lambda\in\lambda(A)$", while the statement uses the spectrum of $A_F$.
- App. A (p. 27): "$z_2=-2m^2\sin(\pi/m)$" drops a square; $1-\cos(2\pi/m)=2\sin^2(\pi/m)$ gives $z_2=-2m^2\sin^2(\pi/m)$, the form the next line uses *(compiler check, not in the sources)*.
- Ref. [9] prints "C. N. Dawson, D. Qiang, and T. F. Dupont" (given and family name of Qiang Du inverted; the text says "Dawson, Du and Dupont"); ref. [19] prints "C. W. Gear, G. Ioannis, and G. Kevrekidis", splitting I. G. Kevrekidis into two authors.
- Ref. [43] "J. Sci. Comput., 87(4), 2021" has no article number or pages.
- (3.4) has $m^2-1$ in a denominator and is undefined for $m=1$; §5.3 treats $m=1$ (mRKC equals RKC) outside it.
- The Robertson initial data $y(0)=(1,2\cdot10^{-5},10^{-1})$ differ from the standard $(1,0,0)$ without comment.
- Typos: "severly" (p. 3), "detemine" (p. 7).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f=f_F+f_S$ | $f=f^{\{\mathrm f\}}+f^{\{\mathrm s\}}$ | fast (cheap, very stiff) and slow (expensive, mildly stiff) parts |
| $\tau$ | $h$ | outer step |
| $H$, $h=H/4$ | — | coarse and fine **mesh** sizes; **collision**: $h$ is not the step, $H$ not a macro step |
| **$\eta$** | $\eta$ (page-local) | averaging length = inner step; **collides with the entropy $\eta$** |
| $f_\eta$, $\bar f_\eta$ | $f_\eta$, $\bar f_\eta$ | exact and numerical averaged force |
| $u$, $u(\eta)$, $u_\eta$, $y_\eta$ | — | auxiliary solution, its exact and RKC value; solution of the modified equation |
| $\varphi(z)=(e^z-1)/z$ | $\phi_1(z)$ | agrees with the registry normalization |
| $A_F$, $A_S$ | $L^{\{\mathrm f\}}$, $L^{\{\mathrm s\}}$ (page-local) | **collision** with the Butcher matrix $A$ |
| $\mu_F$, $\mu$, $\mu_\eta$ | $\mu^{\{\mathrm f\}}$, $\mu$, $\mu_\eta$ (page-local) | one-sided Lipschitz constants; distinct from the multipliers $\mu_j$ |
| $\lambda$, $\zeta$ | $\lambda^{\{\mathrm f\}}$, $\lambda^{\{\mathrm s\}}$ | real nonpositive fast and slow eigenvalues of the scalar multirate test equation |
| $\sigma$ | $\sigma_{\mathrm c}$ (page-local) | coupling of the $2\times2$ model |
| $\rho$, $\rho_F$, $\rho_S$ | $\rho$, $\rho^{\{\mathrm f\}}$, $\rho^{\{\mathrm s\}}$ (page-local) | spectral radii, by nonlinear power method |
| $s$, $m$ | $s$, $m$ | outer and inner RKC stage numbers; **$m$ collides with the multirate ratio**, which mRKC does not have |
| $\varepsilon$, $\bar\varepsilon$ | $\varepsilon_{\mathrm d}$, $\bar\varepsilon_{\mathrm d}$ | RKC damping; **collides with the stiffness parameter $\varepsilon$** |
| $\beta=2-4\varepsilon/3$, $\bar\beta$ | $\beta_{\mathrm d}$, $\bar\beta_{\mathrm d}$ (page-local) | $\beta_{\mathrm d}s^2\le\ell_s$; **collides** with PID and multistep $\beta$ and with the convection vector $\beta$ of §5.5 |
| $\ell_s^\varepsilon=2\omega_0/\omega_1$ | $\ell_s$ (page-local) | length of the real stability interval |
| $R_s(z)$, $P_m(z)$ | $P_s(z)$, $P_m(z)$ | outer and inner RKC stability polynomials, $z=h\lambda$ |
| $\Phi_m(z)=(P_m(z)-1)/z$ | $\Phi_m$ (page-local) | discrete $\phi_1$; **collides** with the elementary weight $\Phi(\tau)$ |
| $R_{s,m}$ | $P_{s,m}$ (page-local) | mRKC stability polynomial |
| $\mu_j,\nu_j,\kappa_j$; $\alpha_j,\beta_j,\gamma_j$; $\omega_0,\omega_1,b_j$; $\upsilon_0,\upsilon_1,a_j$ | — | outer and inner RKC recurrence coefficients; **collide** with registry $\nu$, $\alpha_j$, $\beta_j$, $\gamma$, $a_j$, $b_j$ |
| $T_j$ | — | Chebyshev polynomial; **collides** with the tree set $T$ |
| $w$, $w(\eta)=-\eta\ell_s/\tau$ | $w$, $w(\eta)$ (page-local) | scaled slow eigenvalue |
| $c_F$, $c_S$, $r_\rho$, $S$, $\bar S$ | $c_{\mathrm f}$, $c_{\mathrm s}$, $r_\rho$, $S$, $\bar S$ (page-local) | relative costs, stiffness ratio, speed-ups |
| $\delta$ | $\delta_{\mathrm c}$ (page-local) | channel width |
| $D$ | — | 0/1 selector of fast degrees of freedom |
| $A$, $b$ (inner RKC) | $A$, $b$ | Butcher coefficients; agree |

# Reference list

The paper prints 66 references in numbered style ([1]–[66]), ordered
alphabetically. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. Ref. [4] (Abdulle
& Rosilho de Souza, stiff stochastic differential equations, printed "in
Press" with no year) takes the citing year and the key `abdulle-2022-b`, so
that it is not confused with this source. Ref. [5] is an EPFL report (2020) on
instabilities of interpolation-based multirate RKC, `abdulle-2020-b`, a
different work from `abdulle-2020`, the in-press form of this paper that the
bibliography holds from
[Croci & Rosilho de Souza (2022)](/sources/croci-2022.md). Ref. [35] (Kværnø,
printed 1999) is merged into `kvaerno-2000`, and ref. [51] (Sexton & Reynolds,
an arXiv preprint printed with year 2019 and its later title) into the arXiv
entry `sexton-2018`. Ref. [12] has the single-letter surname E (`e-2003-b`).
Ref. [22] is the Eigen web page. DOIs are printed for three items. No printed
duplicates; all items parsed.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Heat equation](/benchmarks/heat-equation.md)
* [Linear stability of multirate methods and joint stability regions](/definitions/multirate-linear-stability.md)
* [Local time stepping](/methods/local-time-stepping.md)
* [Multirate infinitesimal methods (MIS, MRI-GARK)](/methods/multirate-infinitesimal-methods.md)
* [Multirate Runge–Kutta–Chebyshev (mRKC) methods and the averaged-force modified equation](/methods/multirate-runge-kutta-chebyshev.md)
* [Robertson problem](/benchmarks/robertson-problem.md)
* [Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping](/methods/stabilized-explicit-runge-kutta.md)
