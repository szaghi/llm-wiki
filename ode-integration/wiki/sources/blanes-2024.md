---
type: Source
title: "Blanes et al. (2024) — Splitting methods for differential equations"
description: "Acta Numerica survey of splitting and composition methods: Lie–Trotter and Strang, four characterisations of the order conditions, the negative-coefficient barrier, RKN and near-integrable methods, stability, backward error analysis, processing, PDE and complex-coefficient splittings, and a catalogue of recommended methods."
resource: "doi:10.1017/S0962492923000077"
source_kind: paper
authors: [Blanes S., Casas F., Murua A.]
year: 2024
venue: "Acta Numer. 33:1-161"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Acta_Numerica_Blanes_Splitting_methods_for_differential_equations.pdf"
tags: [splitting, order-conditions, geometric-integration, structure-preserving, stability]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The survey treats [splitting](/methods/operator-splitting.md) and [composition](/methods/composition-methods.md) methods for $y'=f^{[1]}(y)+\dots+f^{[m]}(y)$, where each sub-flow is cheap or exact.

- **§1** introduces Lie–Trotter and Strang, flows and Lie operators, adjoint and conjugate methods, and the pendulum, outer-Solar-System and split-step Fourier examples.
- **§2** raises the order by composition (triple and quintuple jump, compositions of a first-order method and its adjoint). It gives four characterisations of the [order conditions](/results/splitting-order-conditions.md): Baker–Campbell–Hausdorff in a Lyndon basis, words and shuffle algebra, Lyndon multi-indices in $(b_j,c_j)$, and odd-index Lyndon multi-indices for compositions. It ends with the [negative-coefficient barrier](/results/negative-coefficient-barrier.md).
- **§3** covers special structures: Runge–Kutta–Nyström problems, commutator flows (modified potentials), near-integrable systems with generalized order, linear systems, non-autonomous problems.
- **§4** gives the qualitative theory: linear stability on the harmonic oscillator, [backward error analysis](/methods/backward-error-analysis.md) with energy errors $O(h^p)$ over exponentially long times for [symplectic](/properties/symplecticity.md) splittings, and [processing and effective order](/methods/processing-and-effective-order.md).
- **§5** is a self-contained second-order analysis for highly oscillatory problems, valid uniformly in $\omega h$, with an explicit processor for Strang.
- **§6** treats PDEs. Marchuk–Yanenko, Yanenko–Crank–Nicolson, Peaceman–Rachford and Douglas–Rachford are written as compositions of explicit and implicit Euler, and [IMEX](/methods/imex-runge-kutta.md) schemes are recast as splittings. It also covers boundary-induced [order reduction](/definitions/order-reduction.md), Schrödinger equations with Magnus and commutator-free [exponential integrators](/methods/exponential-integrators.md), and the order-2 barrier for positive coefficients on parabolic problems.
- **§7** treats [complex coefficients](/methods/complex-coefficient-splitting.md).
- **§8** catalogues more than 80 methods in five tables, with recommended methods boxed.
- **§9** covers applications, among them extrapolation, [positivity](/properties/positivity-preservation.md), molecular dynamics, Hamiltonian Monte Carlo and Trotterization.
- **Appendix A** compares the methods on random matrix exponentials.

Results are mostly recalled with proofs sketched; the order-condition algebra is derived in full. The new material is the Lyndon multi-index characterisation of composition order conditions (§2.5) and the oscillatory analysis and processor of §5. The page is linked from the [B-series](/definitions/b-series.md) page for the word-series and BCH counterparts of B-series.

# Version read

arXiv:2401.01722v3 [math.NA], 7 May 2024, typeset in the Acta Numerica class, dated 8 May 2024 and carrying "© The Author(s), 2024. Published by Cambridge University Press": an author version, not the version of record. Page 1 prints the placeholder DOI `10.1017/S09624929XXXXXXXX` and the range "pp. 1–160"; the file has 160 pages against 161 in Crossref. All 160 pages were read (main text pp. 1–141, Appendix A pp. 142–146, references pp. 146–160); Tables 8.1–8.5 and pp. 37, 77, 83, 107–108 were checked visually. Title and authors match Crossref. Numbering cited here is that of the arXiv v3. Method coefficients and the Appendix A tests are on the authors' web site (gicas.uji.es/SplittingMethods.html).

# Key claims

Notation: $f=f^{[1]}+f^{[2]}$; $\varphi^{[i]}_h$ sub-flows; $F^{[i]}$ the Lie operator $f^{[i]}\cdot\nabla$ (exponentials of Lie operators appear in reverse order relative to the maps); $\chi_h$ Lie–Trotter; $S^{[2]}_h$ Strang; $a_j,b_j$ splitting coefficients; $\gamma_j$ composition weights; $p$ the order (the source's $r$) (see the notation map).

1. Lie–Trotter $e^{hF^{[2]}}e^{hF^{[1]}}$ has local error $\tfrac12h^2[F^{[1]},F^{[2]}]+O(h^3)$ and is first order. Strang $e^{hF^{[1]}/2}e^{hF^{[2]}}e^{hF^{[1]}/2}$ satisfies $e^{h(F^{[1]}+F^{[2]})}-\text{Strang}=Ch^3+O(h^4)$ with $C=\tfrac1{24}([F^{[1]},[F^{[1]},F^{[2]}]]+2[F^{[2]},[F^{[1]},F^{[2]}]])$. (§1.1, Eqs. 1.6–1.9) **Derived**
2. Lie–Trotter and Strang are conjugate: $S^{[2]}_h=\pi_h^{-1}\circ\chi^*_h\circ\pi_h$ with $\pi_h=\varphi^{[1]}_{h/2}$, so $n$ Strang steps equal $n$ Lie–Trotter steps plus an initial and a final transformation. (§1.3, Eq. 1.18) **Derived**
3. Symmetric (self-adjoint) methods have even order; a map is time-symmetric iff $-Y(-h)\equiv Y(h)$ for its generator, i.e. $Y(h)=hY_1+h^3Y_3+\dots$. (§2.1.1, statement (2)) **Proved**
4. The composition $\psi_h=S^{[2]}_{\gamma_sh}\circ\dots\circ S^{[2]}_{\gamma_1h}$ of a time-symmetric second-order map has order $\ge3$ iff $\sum\gamma_j=1$ and $\sum\gamma_j^3=0$; the smallest $s$ with real solutions is 3, and the symmetric choice is the fourth-order triple jump $\gamma_1=\gamma_3=1/(2-2^{1/3})$, $\gamma_2=1-2\gamma_1$. (§2.1.1, Eqs. 2.1–2.3) **Derived**
5. Numbers of independent order conditions at order $n=1,\dots,11$: general splitting $c_n$: 2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186; RKN splitting $d_n$: 2, 1, 2, 2, 4, 5, 10, 14, 25, 39, 69; compositions of a second-order symmetric method $m_n$: 1, 0, 1, 1, 2, 2, 4, 5, 8, 11, 17. (Table 2.1) **Stated**
6. For a consistent splitting method, an independent set of order conditions for order $p$ is Eq. (2.38) restricted to Lyndon multi-indices $(i_1,\dots,i_k)$ with $1<i_1+\dots+i_k\le p$; for time-symmetric methods only those of odd weight are needed. (§2.4) **Proved** (via shuffle relations of iterated integrals)
7. The order of compositions (2.1) of Strang maps is characterised by $\gamma_1+\dots+\gamma_s=1$ and $u_{i_1,\dots,i_m}(\gamma)=0$ for Lyndon multi-indices with odd indices and $1<$ weight $\le p$; symmetric compositions of even order $p$ need only those of odd weight $<p$: 7 conditions for order 8. (§2.5.2) **Derived**
8. Negative-coefficient barrier: every splitting or composition method of order $p\ge3$ with real coefficients has at least one negative $a_j$ and at least one negative $b_j$. The proof uses $w_3=\sum_j(\alpha_{2j}^3+\alpha_{2j-1}^3)=0$ with "$x^3+y^3<0\Rightarrow x+y<0$". (§2.6, Eq. 2.56; credited to Sheng 1989, Suzuki 1991, Goldman & Kaper 1996; proof from Blanes & Casas 2005) **Proved**
9. For RKN problems ($y''=g(y)$), $[F^{[1]},[F^{[1]},[F^{[1]},F^{[2]}]]]=0$, so $C_k=0$ for $k\ge4$; multi-indices with an index $\ge4$ drop out, and $[C_3,[C_2,C_3]]=0$ removes (2,3,3) at order 8. (§3.1) **Derived**
10. Including the flow of $[F^{[1]},[F^{[1]},F^{[2]}]]$ (a modified potential) evades the barrier: the fourth-order scheme (3.4)–(3.5) of Koseleff (1993) and Chin (1997) has the positive coefficients $a_1=1/6$, $b_1=1/2$, $a_2=1/3$ and the commutator weight $d_2=-1/72$. Order six with positive coefficients in general requires negative coefficients (Chin 2005), but a sixth-order processed method with all $a_j,b_j>0$ exists for cubic potentials (Blanes et al. 2023). (§3.2) **Derived** (order of 3.4) / **Stated** (rest)
11. For near-integrable $y'=f^{[1]}+\varepsilon f^{[2]}$ there are, at each power $h^k$, one error term of order $\varepsilon h^k$, $\tfrac12(k-1)$ terms of order $\varepsilon^2h^k$ and $\tfrac16(k-1)(k-2)$ of order $\varepsilon^3h^k$; generalized order $(p_1,\dots,p_m)$ means local error $O(\varepsilon h^{p_1+1}+\dots+\varepsilon^mh^{p_m+1})$. (§3.3, Table 3.1; McLachlan 1995a) **Stated**
12. For the linear systems $q'=Hp$, $p'=-Hq$ arising from the Schrödinger equation, orders $2,4,6,8,10,12$ are reached with as many exponentials as the order, against at least 15 and 31 exponentials in general for orders 8 and 10. (§3.4; Gray & Manolopoulos 1996, Blanes et al. 2008a) **Stated**
13. The Störmer–Verlet stability interval on the harmonic oscillator is $z^*=2$ ($z=h\omega$); $k$ concatenated Störmer–Verlet steps give $(0,2k)$, the longest possible for any $k$-stage splitting method (2.17). (§4.2; proof in Bou-Rabee & Sanz-Serna 2018) **Stated**
14. For the perturbed oscillator $y''=-y-\varepsilon y$, $k$ concatenated Strang rotation/kick integrators (4.10) have strictly larger stability regions on each line $h=h^*<h_k$ ($h^*\ne\pi,\dots,(k-1)\pi$) than any other $k$-stage rotation/kick splitting. (§4.2; Casas, Sanz-Serna & Shaw 2023) **Stated**
15. Backward error analysis: the numerical solution is exponentially close, $\lVert\psi_h(y_0)-\tilde\varphi^{[N]}_h(y_0)\rVert\le h\gamma Ke^{-h_0/h}$, to the flow of the optimally truncated modified equation; for an order-$p$ splitting of a Hamiltonian system on a compact set, $\mathcal H(y_n)=\mathcal H(y_0)+O(h^p)$ for $nh\le e^{h_0/2h}$; for integrable systems the global error grows at most linearly, $\le Cth^p$ for $t\le h^{-p}$, whereas non-symplectic methods give $\mathcal H(y_n)-\mathcal H(y_0)=O(th^p)$ and quadratic error growth. (§4.4, Eq. 4.16; Hairer et al. 2006, Moan 2004, Calvo & Hairer 1995) **Stated**
16. Variable step size destroys these long-time properties, because the modified equation depends on $h$. (§4.4, §9.10) **Stated**
17. Processing: if $\pi_h^{-1}\circ\psi_h\circ\pi_h$ is more accurate, long-run accuracy is governed by the processed method's local error, not by that of $\psi_h$; many order conditions can be met by the processor, so the kernel needs far fewer. (§4.5) **Derived**
18. Oscillatory splitting: for $y'=Ay+f^{[2]}(y)$ with $e^{tA}$ $2\pi/\omega$-periodic and polynomial $f^{[2]}$ there is a second-order-in-$h$ expansion valid uniformly in $\omega$; Strang has a modified Hamiltonian (5.40) under the non-resonance conditions (5.31); an explicit processor (5.49)–(5.50) built from $2m+1$ rotations by $2\pi/(2m+1)$ and $2m$ kicks makes the processed Strang's local error $O(h^2)$ only in the $g'g$ terms, with modified Hamiltonian $\mathcal H+O(h)$ (5.47). (§5) **Derived**
19. On the pendulum (initial state $(1/10,0)$, $h=5/6$, $t\in[0,500]$) the processed Strang P(2,2) has a far smaller energy error than Strang (2,2) away from resonant steps; spikes appear at $k\omega h/2\pi\in\mathbb Z$ for $k=2,4$, plus $3h/2\pi\in\mathbb Z$ for the processed method. (§5.7, Figs. 5.1–5.2) **Shown**
20. The PDE schemes are compositions of explicit and implicit Euler sub-steps: Marchuk–Yanenko (6.2) is first order; Yanenko's Crank–Nicolson (6.3) is first order but conjugate to a second-order symmetric method; Peaceman–Rachford (6.4) is the symmetric composition $\phi^{3*}_{h/2}\circ\phi^3_{h/2}$, second order, and the only symmetric second-order Euler composition that captures steady states exactly; Douglas–Rachford (6.5) is first order and a splitting in an enlarged space (6.12). (§6.1) **Derived**
21. Boundary conditions hold for $f$ but not for the sub-operators; for reaction–diffusion with Dirichlet or Neumann conditions this causes order reduction, "one in the infinity norm" for Strang; remedies are boundary correction functions (Einkemmer & Ostermann 2015, 2016) and boundary-only corrections (Alonso-Mallo et al. 2018, 2019). (§6.1; Hansen & Ostermann 2009b, Hundsdorfer & Verwer 2003) **Stated**
22. Strang applied to the pseudo-spectral Schrödinger equation with $V\in C^5$ periodic and bounded has local error $\le C_1\lvert h\rvert^3\lVert u_0\rVert_{H^2}$ and global error $\le C_2\lvert h\rvert^2\lVert u_0\rVert_{H^2}$ in $L^2$, independent of the number of grid points; order-$p$ splittings satisfy $\lVert u_n-u(t_n)\rVert\le C\lVert u(0)-u_0\rVert+C\lvert h\rvert^p\lVert u(0)\rVert_{H^p}$. (§6.3, Eqs. 6.23, 6.25; Jahnke & Lubich 2000, Thalhammer 2008) **Stated**
23. The splitting algorithm of Blanes et al. (2015) for $e^{-ihH}v$ is 1.4–2 times faster than Chebyshev at equal accuracy, and Chebyshev is 2–3 times faster than Taylor; polynomial methods of degree $m$ need $h/(m\Delta x^2)\le C$. (§6.3) **Stated**
24. For the parabolic problem $u'=(A+B)u$ ($A$, $B$ operators generating $C_0$ semigroups), an order-$p$ splitting with all $a_j,b_j\ge0$ retains order $p$ (6.44) under regularity assumptions (Hansen & Ostermann 2009a), but positivity limits it to order 2 unless double commutators $[B,[A,B]]$ are included (Kieri 2015); with complex coefficients in a sector $\Sigma_\theta$ (analytic semigroups) the classical order is retained (6.47), also after projecting onto the real part. (§6.4) **Stated**
25. Complex-coefficient order barriers with $\operatorname{Re}>0$: iterated compositions of a first-order method, order 3; Strang-based recursive two-stage compositions (7.5), order 6; triple-jump palindromic compositions, order 8; quadruple jump, order 14. (§7.1; proved in Blanes et al. 2013a, Hansen & Ostermann 2009b) **Stated**
26. Symmetric-conjugate methods ($a_{s+2-j}=\bar a_j$, $b_{s+1-j}=\bar b_j$) satisfy $\bar\psi_h=\psi_h^{-1}$ for problems reversible under complex conjugation; on $iu'=(H_1+H_2)u$ with real $H$ having simple real eigenvalues they are similar to unitary maps for small $h$, nearly preserving norm and energy over long times, whereas palindromic complex methods lose unitarity (Fig. 7.1). (§7.2; Bernier et al. 2023) **Stated** / **Shown** (two-level system)
27. Projecting onto the real part, $R_h=\tfrac12(\psi_h+\bar\psi_h)$, raises the order from $p$ to $p+1$ when $\psi_h$ is symmetric-conjugate and $p$ is odd; a five-stage symmetric-conjugate Strang composition then gives an order-6 $R_h$ (palindromic needs 7 stages) and nine stages give order 8 (palindromic needs 15). Time-symmetry and symplecticity are preserved to orders $4k-1$ (odd $p=2k-1$), $4k+3$ (symmetric-conjugate $p=2k$) and $4k+1$ (palindromic $p=2k$). (§7.3; Blanes et al. 2022c, Chambers 2003) **Stated**
28. On the two-level system the leading error coefficient $E_5=\lvert\sum_j\gamma_j^5\rvert$ of the complex fourth-order compositions (7.8)/(7.9) is about 200 times smaller than that of the real triple jump. (§7.1; Blanes et al. 2022a) **Stated**, illustrated in Fig. 7.1 **Shown**
29. Multi-product expansions $\sum_ic_i(S^{[2]}_{h/k_i})^{k_i}$ with $c_i=\prod_{j\ne i}k_i^2/(k_i^2-k_j^2)$ reach order $2m$; starting from a symmetric geometric method of order $2n$ they reach order $2n+2\ell$, $\ell=1,\dots,n$, and preserve the geometric properties up to order $4n+1$ or higher. (§9.1.2; Blanes et al. 1999a, Chan & Murua 2000) **Stated**
30. Runge–Kutta and multistep methods that unconditionally preserve positivity are at most first order (Bolley & Crouzeix 1978); a Strang splitting of the doubled system $y'=A(z)y$, $z'=A(y)z$ gives second-order positivity- and mass-preserving approximations for $h>0$. (§9.2.1) **Stated** / **Derived**
31. Outer Solar System over $2\times10^5$ days: near-integrable splittings of generalized order (2,2), (8,2) and (10,6,4) beat extrapolation of orders 2–12 and MATLAB ode23/ode45/ode113 at all accuracies, in energy and position error per force evaluation. (§9.4, Fig. 9.1) **Shown**
32. Appendix A: no single method is best; the authors recommend symmetric compositions with $s=5,13,19,35$ for orders 4, 6, 8, 10 and processed kernels with $s=13,19,23$ for orders 6, 8, 10; for small $\varepsilon$ the near-integrable methods dominate everything else. (Figs. A.1–A.5) **Shown** — Table 8.1 boxes different stage counts (printed slips, item 11)

# Printed slips

1. (7.10), p. 108 (visual): $b_1=\tfrac12\pm i\tfrac{\sqrt3}2$ is printed; consistency with (7.4) ($\gamma_1=\tfrac12\pm i\tfrac{\sqrt3}6$, $b_1=\gamma_1$, $a_1=\gamma_1/2$ as printed) and with $\gamma_1^3+\bar\gamma_1^3=0$ requires $b_1=\tfrac12\pm i\tfrac{\sqrt3}6$.
2. (7.8), p. 108 (visual): "$\gamma_2=1-2\alpha_1$" for $1-2\gamma_1$.
3. (7.6), p. 107 (visual): left side "$\gamma_{k,1}$", right side $\gamma_{r,2}$; the index should be $r$.
4. (5.24)–(5.25), pp. 77–78: the second sum "$\sum_{1\le j\le r}\tfrac12b_j^2e^{\dots}$" should run to $s$ (stages).
5. (5.52), p. 83 (visual): the first exponential $e^{2\pi(jk+n\ell)/(2m+1)}$ lacks the factor $i$ present in (5.51) and in the second term.
6. §3.1, p. 51: the extra Lyndon multi-indices for RKN order 7 list "(1,1,2,3)" twice and omit (1,1,2,1,2); the ten weight-7 words with entries $\le3$ are (1,1,1,1,1,2), (1,1,1,1,3), (1,1,1,2,2), (1,1,2,1,2), (1,1,2,3), (1,1,3,2), (1,2,1,3), (1,2,2,2), (1,3,3), (2,2,3), consistent with $d_7=10$.
7. §2.6, p. 50: the regrouped sum $\sum_{i=0}^{s}(\alpha_{2j}^3+\alpha_{2j+1}^3)$ has summation index $i$ but summand in $j$.
8. Fig. 6.1 caption, p. 105: "N = 256 and repeated with N = 510", while the text says $M=256$ and $M=512$.
9. §9.6, p. 134: "$h<2$, independently of $h$" should read "independently of $d$" (the dimension).
10. §1.6, p. 19: the periodic grid $x_j=-\pi+j\cdot2\pi/(M-1)$, $j=0,\dots,M-1$, includes both endpoints; the standard spacing is $2\pi/M$.
11. Appendix A against Table 8.1: the appendix recommends $s=5,13,19,35$ (orders 4–10) and processed $s=13,19,23$ (orders 6–10), while Table 8.1 boxes 21-SS05 at order 8 (19 unboxed) and processed P:11 (order 6) and P:13 (order 8).
12. Table 8.5 labels WHT96 "P:1(17,2)" while the text says "(k,2) method with k = 16 and s = 1".
13. Typos: "Stömer–Verlet" (p. 15), "toay's" (p. 27), "Baker–Cambpell–Hausdorff" (p. 34), "spitting methods" (p. 87), "3th-order" (p. 109), "Schödinger" (p. 111); in the references "Handook" (twice), "Huges" for Hughes, a garbled second author "J. A. F. Jr." of Feit et al. 1982, "spliting" in the Blanes et al. 2023 title, and Ruth 1983 pages "26–69".

# Notation map

| Blanes et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x'=f(x)=f_1+\dots+f_m$ | $y'=f(y)=f^{[1]}+\dots+f^{[m]}$ | autonomous throughout |
| $h$; $\Delta t$ (§6); $\tau=-ih$ (Schrödinger) | $h$ | |
| $\varphi^{[f]}_t$, $\varphi^{[j]}_t$ | $\varphi_t$, $\varphi^{[j]}_t$ | also $\varphi^{[T]},\varphi^{[V]},\varphi^{[A]},\varphi^{[B]},\varphi^{[R]},\varphi^{[K]},\varphi^{[O]}$ |
| $F$, $F_j$ | $F^{[j]}$ | Lie operator $f^{[j]}\cdot\nabla$ — **not in the registry, and not the elementary differential $F(\tau)$**; exponentials appear in reverse order relative to maps |
| $[F,G]$, $F_{12}$, $F_{112}$, $F_{122}$ | $[X,Y]$ | Lie brackets in Lyndon convention |
| $\chi_h$, $\chi^*_h$ | $\chi_h$, $\chi_h^*$ | Lie–Trotter and adjoint; **the source flips its ordering between §2.1.2 and §7.1** |
| $S^{[2]}_h$, $S^{[2k]}_h$ | kept | Strang / symmetric map of order $2k$ |
| $\psi_h$, $\psi^*_h=(\psi_{-h})^{-1}$, $\Psi(h)$ | $\psi_h$, $\psi_h^*$ | $\Psi(h)$ the Lie transform of the map |
| $a_j,b_j$ ($a_{s+1}$ included) | $a_j,b_j$ | the source's form (2.17) ends with $\varphi^{[1]}_{a_{s+1}h}$ |
| $c_i=\sum_{j\le i}a_j$ | kept | **not the Runge–Kutta abscissae** |
| $\gamma_j$ | $\gamma_j$ | composition weights; the source reuses $\gamma$ in §4.3 and §5 |
| $\alpha_j$ | kept | weights of adjoint compositions (2.15); **collides with the Shu–Osher $\alpha$**; also $\alpha_k(h)$ and $\alpha=2\pi/(2m+1)$ in §5 |
| $r$ (order); $(r_1,\dots,r_m)$ | $p$; $(p_1,\dots,p_m)$ | classical and generalized order |
| $s$ | $s$ | number of $f^{[2]}$ flows (≈ force evaluations for RKN) |
| $z=h\omega$, $\tilde M_z$, $p(z)=\tfrac12\operatorname{tr}\tilde M_z$ | $z=h\omega$; $\tilde M_z$, half-trace kept | **"stability polynomial" of a splitting on the oscillator: not the registry $P(z)$ nor $R(z)$; the oscillator, not Dahlquist's equation, is the test** |
| $f_h$, $f^{[j]}$ (modified-equation terms) | $\tilde f$ | **the source's $f^{[j]}$ in (4.13) are modified-equation coefficients, not split parts** |
| $H$, $\tilde H$ | $\mathcal H$, $\tilde{\mathcal H}$ | Hamiltonian and modified Hamiltonian; $H$ is also a matrix in §3.4 |
| $\pi_h$, $\hat\psi_h$ | $\pi_h$ | processor, processed method; "kernel" $=\psi_h$ |
| $q$, $p$ | kept locally | position and momentum; **$q$ and $p$ are stage order and order in the registry** |
| $M$ (grid points, §1.6, §6.3) | $M_x$ | **the registry's $M$ is the mass matrix** |
| $\mathbb C_+$, $\Sigma_\theta$ | kept | positive-real-part half plane; sector |
| $\psi^{ke},\psi^{ki}$, $\phi^\ell_h$ | kept | explicit/implicit Euler on $f^{[k]}$ and their compositions (6.10) |
| $\gamma$, $K$, $h_0$ in (4.16) | kept | constants of the backward-error estimate; **not the composition weights $\gamma_j$ nor the registry $K$ (correction iterations)** |
| $m$, $\ell$, $n$ in (9.8) | kept | number of terms, order increment and half-order of the basic method of a multi-product expansion; **$\ell$ is not the registry micro-step index, $m$ not the multirate ratio** |
| $m$ in $h/(m\Delta x^2)\le C$ (§6.3) | kept | degree of the polynomial approximation (6.28) |
| AB, BA, ABA, BAB; S/N; P: | kept | RKN families; symmetric/non-symmetric; processed; in RKN tables $A$ is kinetic and $B$ potential |

# Reference list

268 printed references, author–year style with letters a–d for same-author-year items. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` blanes-2024. Same-key collisions take suffixes in printed order. Bader, Blanes & Casas 2013 prints no volume; Blanes et al. 2023 is "in press"; Bréhier, Cohen & Giordano 2023a prints only a DOI, the single printed DOI of the list. Preprints (Alberdi 2019, Bou-Rabee 2017, del Valle 2023, Foster 2022, Skeel 2020) stay distinct entries. Feit et al. 1982 has a garbled second author; Suris 1988 is in Russian without publisher; four edited volumes carry their editors as authors. No unparseable item.

# Pages created or updated

Chunk 1 (2026-10-19). This source is cited on:

* [B-series, composition and substitution laws](/definitions/b-series.md)
* [Backward error analysis, modified equations and modifying integrators](/methods/backward-error-analysis.md)
* [Composition methods and Runge–Kutta–Nyström splittings](/methods/composition-methods.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Exponential integrators and φ-functions](/methods/exponential-integrators.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Negative-coefficient barrier for splitting methods](/results/negative-coefficient-barrier.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Order conditions of splitting and composition methods](/results/splitting-order-conditions.md)
* [Order reduction](/definitions/order-reduction.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Processing and effective order](/methods/processing-and-effective-order.md)
* [Splitting and composition with complex coefficients](/methods/complex-coefficient-splitting.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
