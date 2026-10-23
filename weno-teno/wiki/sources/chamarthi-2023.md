---
type: Source
title: "Chamarthi (2023) — Gradient based reconstruction: Inviscid and viscous flux discretizations, shock capturing, and its application to single and multicomponent flows"
description: "Point-value finite-difference scheme that computes high-order cell-centre gradients once and reuses them in an α-damping viscous flux, a κ = 1/3 gradient-based interface reconstruction and the curvature of a monotonicity-preserving limiter (MEG6, MIG4), tested against TENO5 on single- and two-species flows."
resource: "doi:10.1016/j.compfluid.2022.105706"
source_kind: paper
authors: [Chamarthi A.S.]
year: 2023
venue: "Comput. Fluids 250:105706"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_Chamarthi_Gradient_based_reconstruction_Inviscid_and_viscous_flux_disc.pdf"
tags: [reconstruction, finite-difference, limiting, multiphase, low-dissipation]
timestamp: 2026-10-23T16:00:00Z
---

# Summary

A single-author paper that builds a
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
on point values $u_i$ for the compressible Navier–Stokes equations, single-species
and two-species (the quasi-conservative
[five-equation model](/definitions/five-equation-model.md) of Allaire et al.).
One idea organizes it: high-order cell-centre first derivatives of the
primitive variables are computed once and reused three times.

1. **Viscous fluxes.** The [α-damping interface gradient](/methods/alpha-damping-viscous-flux.md)
   of Nishikawa (the average of the two cell gradients plus a jump term
   $\tfrac{\alpha_{\mathrm D}}{2\Delta x}(v^{\mathrm R}_{i+1/2}-v^{\mathrm L}_{i+1/2})$ of the extrapolated states) is fed by explicit
   sixth-order (α-EG) or compact fourth-order (α-IG) gradients. Fourier analysis
   shows that it is fourth order for $\alpha_{\mathrm D}=4$ only and that it damps high
   frequencies.
2. **Inviscid fluxes.** The [gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
   (GBR) is van Leer's κ-scheme with $\kappa=1/3$, applied to point values,
   with a second derivative built from values and first derivatives. It is
   fourth order for linear problems (EG6 with explicit, IG4H with compact
   gradients). An [HLLC flux](/methods/hll-riemann-solvers.md) closes the scheme.
3. **Shock capturing.** The Suresh–Huynh
   [monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md)
   is applied to the GBR state, with its curvature replaced by the high-order
   second derivative (schemes MEG6 and MIG4). Optionally the limiting is done
   in [characteristic variables](/methods/characteristic-decomposition.md),
   projecting the gradients with the same frozen $L$.

[Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
analysis favours MIG4 over MEG6 and [TENO5](/methods/targeted-eno.md). The
schemes are fourth order on linear advection, but second order on the
nonlinear [isentropic vortex](/benchmarks/isentropic-vortex.md), as is TENO5.
The paper attributes this to the reconstruction of primitive variables. The
test set covers a [viscous shock tube](/benchmarks/viscous-shock-tube.md) with
timings, [shock–mixing-layer interaction](/benchmarks/shock-mixing-layer-interaction.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md), the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), the 2D and 1D
[Shu–Osher problems](/benchmarks/shu-osher-problem.md) and Titarev–Toro, a
[2D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md), the
[Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md),
[Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
[LeBlanc](/benchmarks/leblanc-shock-tube.md) and the
[blast waves](/benchmarks/woodward-colella-blast-wave.md), then two-fluid shock
tubes ([gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
page), a [shock–helium bubble](/benchmarks/shock-bubble-interaction.md), the
[multi-material triple point](/benchmarks/triple-point-problem.md) and a
viscous air–SF$_6$ RMI. MIG4 is reported less dissipative than MEG6, which in
turn beats TENO5. TENO5 is reported oscillatory in DMR, the 2D shock–entropy
wave and LeBlanc.

# Version read

arXiv preprint arXiv:2205.01034v2 [physics.flu-dyn], stamped 28 Oct 2022
(footer "Preprint submitted to Elsevier, October 31, 2022"), 40 pages, all
read; it is not the Computers & Fluids version of record. Page 1 title and
author match Crossref; no DOI is printed. The text calls the method both
"gradient-based reconstruction" and "GRB". Equation, table, figure and
reference numbers on this page are those of v2.

# Key claims

Registry notation (see the notation map): left and right interface states
$u^\mp_{i+1/2}$; the source's damping coefficient $\alpha$ is written
$\alpha_{\mathrm D}$ (page-local, as on the α-damping page); $u'_i$, $u''_i$ are the
cell-centre first and second derivatives; the first-derivative symbol of a
reconstruction is $\mathrm i\tilde\vartheta$ (the source's $k'$).

1. Sharing derivatives between the inviscid and viscous discretizations is the paper's novelty: the gradients of the primitive variables are computed once and reused for the viscous fluxes, the inviscid reconstruction and the MP curvature (Abstract, §1, §3.2). **Stated**
2. With explicit sixth-order or compact fourth-order cell-centre gradients, the α-damping viscous scheme is fourth-order accurate for $\alpha_{\mathrm D}=4$ and second order for any other $\alpha_{\mathrm D}$ (§3.1, Eqs. 28, 33–36). **Derived**
3. The α-IG modified wavenumber of the second derivative is $\sin^2\tfrac{\vartheta}{2}\,(-16\cos\vartheta+\cos2\vartheta-33)/(5\cos\vartheta+7)=-\vartheta^2+\vartheta^6/240-17\vartheta^8/24192+\dots$ (Eqs. 33–34). **Derived**
4. The α-EG modified wavenumber is $\tfrac1{15}\sin^2\tfrac{\vartheta}{2}(29\cos\vartheta-7\cos2\vartheta+\cos3\vartheta-83)=-\vartheta^2+\vartheta^6/360-73\vartheta^8/10080+\dots$ (Eqs. 35–36). **Derived**
5. The fourth-order α-damping schemes resolve high-frequency modes and stay closer to $-\vartheta^2$ than the sixth-order α-damping scheme of Chamarthi et al. and the sixth-order scheme of Shen & Zha; the latter resolves none of the high-frequency modes (Fig. 1, §3.1). **Shown**
6. With $\alpha_{\mathrm D}=4$ the α-damping second derivative reduces to $u''_i=\tfrac{2}{\Delta x^2}(u_{i+1}-2u_i+u_{i-1})-\tfrac{1}{2\Delta x}(u'_{i+1}-u'_{i-1})$, the form of Adam (1977) (Remark 3.1, Eqs. 37–39). **Derived**
7. The explicit viscous step is $\Delta t_{\mathrm{visc}}=\min\tfrac1{\alpha_{\mathrm D}}\tfrac{\Delta x^2}{\nu_{\mathrm{kin}}}$ with $\alpha_{\mathrm D}=4$ (from Nishikawa), "slightly more restrictive than the value 38/15 obtained in [3]" (Eq. 40). **Stated**
8. GBR with $\kappa=1/3$ on point values, $u^-_{i+1/2}=u_i+\tfrac{\Delta x}{2}u'_i+\tfrac{\Delta x^2}{12}u''_i$, is fourth-order accurate: EG6 has $\mathrm i\tilde\vartheta=\mathrm i\vartheta+\mathrm i\vartheta^5/720+\vartheta^6/1440+\dots$ and IG4H $\mathrm i\tilde\vartheta=\mathrm i\vartheta+\mathrm i\vartheta^5/720+\mathrm i\vartheta^7/2016+\dots$ (Eqs. 43–49). The author calls this "contrary to expectations that the κ-scheme can be only at most third accurate", an "unexpected outcome" due to the point-value interpretation (§3.2). **Derived**
9. The fifth-order linear upwind U5 has $\mathrm i\tilde\vartheta=\mathrm i\vartheta+\vartheta^6/60-\dots$ (Eqs. 50–52); IG4H has better dispersion than EG6 and U5, and both GBR schemes have "superior dissipation" to U5 (Fig. 2). **Derived**/**Shown**
10. $\kappa=1/2$ in place of $1/3$ "will lead to anti-dissipation properties (not shown here)" (Remark 3.3). **Stated**
11. Optimized linear schemes in the literature often give up formal order (six-point third-order Weirs–Candler, six-point fourth-order Sun et al., improved five/six-point TENO only third/fourth order), so a formally fourth-order scheme is acceptable (Remark 3.3). **Stated**
12. Reusing the high-order second derivative as the MP curvature (Eq. 60) with the two-argument minmod for the limited curvature (Eq. 61) improves the ADR dispersion of MIG4 over MIG4-base; the improvement is "marginal" for MEG6 (Fig. 3, §3.3). **Shown**
13. In ADR, MIG4 has better dispersion and dissipation than MEG6 and TENO5 (Fig. 3); Table 5 rates dissipation error "Medium" for MIG4 and MEG6 and "Low" for TENO5, dispersion error Low/Medium/High. **Shown** (see Printed slips)
14. Viscous shock tube, $\mathrm{Re}=1000$, $1280\times640$: the Shen–Zha scheme with TENO5 shows saw-tooth oscillations at $t=0.5$ because it lacks high-frequency damping, while no α-damping run shows odd–even decoupling; MIG4 comes closest to the fine-grid main vortex (Ex. 4.1, Figs. 4–5). **Shown**
15. Cost on Ex. 4.1 (Table 1, no hardware printed): TENO5+α-IG 58680 s (ratio 1.147), TENO5+α-EG 50880 s (0.994), MEG6+α-EG 48506 s (0.948), MIG4+α-IG 51146 s (1). **Shown**
16. Linear advection (Table 2, $\Delta t=\nu\Delta x^2$, $t=2$): MIG4 and MEG6 about fourth order, TENO5 fifth order, with almost equal errors on the finest grid ($N=802$: TENO5 $2.21\times10^{-7}$, MIG4 $3.37\times10^{-7}$, MEG6 $2.35\times10^{-7}$). **Shown**
17. Nonlinear isentropic vortex (Table 3): every scheme, TENO5 included, is only second order, with equal errors at $N=2002$ ($4.10\times10^{-5}$); this is attributed to the primitive-variable, midpoint-type reconstruction (citing Zhang, Zhang & Shu), and BVD, P4T2 and Fu's conservative-variable TENO are said to be likewise second order and not to have "formally compute[d] the order of accuracy" (Ex. 4.3, §5). **Shown**/**Stated**
18. TENO5 oscillates near the Mach stem in DMR ($768\times256$); MIG4 resolves the slip-line roll-ups better than MEG6 and TENO5 (Ex. 4.4, Fig. 7). **Shown**
19. Inviscid Taylor–Green vortex at $64^3$: IG4H and EG6 preserve kinetic energy better than U5 and IG4H gives the highest enstrophy, which is computed from the gradients already available (Ex. 4.5, Fig. 8). **Shown**
20. 2D shock–entropy wave at $400\times80$: MIG4 resolves the high-frequency density waves best and beats MIG4-base at the peaks; TENO5 shows oscillations, which "may indicate insufficient dissipation" (Ex. 4.6, Fig. 9). **Shown**
21. 2D Riemann problem at $400\times400$: MIG4 > MEG6 > TENO5 in vortical structures, and MIG4 > MIG4-base (Ex. 4.7, Fig. 10). **Shown**
22. Single-gas RMI at $320\times80$: TENO5 shows "no roll-up vortices at all", MEG6 some, MIG4 the most (Ex. 4.8, Fig. 11). **Shown**
23. LeBlanc, $N=900$, $t=6$: TENO5 density oscillates with larger amplitude, matching a figure of Li, Fu & Adams where MP filters TENO8-A; MIG4 captures the velocity discontinuity at $x=8$ within one cell (Ex. 4.10, Fig. 14). **Shown**
24. Titarev–Toro ($N=1000$): TENO5 "severely under-resolves" the fluctuations, MEG6 and MIG4 resolve them (Ex. 4.12, Fig. 16). **Shown**
25. Multi-species tests (five-equation model with HLLC and an HLLC-consistent interface velocity in the $\phi_1\nabla\cdot v$ source): no oscillations at material interfaces, and MIG4 gives the thinnest interface in the two-fluid shock tube, shock–curtain, shock–helium cylinder, triple point and viscous RMI (Exs. 4.14–4.18). **Shown**
26. "To the best of the authors' knowledge, the implementation of the TENO scheme for the multi-component flows, specifically for the 5-equation model, is not presented in the open literature" (Ex. 4.16). **Stated**
27. Triple point at $1792\times768$: MIG4 vorticity is comparable to, and in places "much more enhanced than", Pan et al. on $3584\times1536$ (Ex. 4.17, Fig. 23). **Shown**
28. Limitations and future work: genuine fourth order for nonlinear problems needs flux reconstruction; seventh-order κ-type reconstruction "is also possible"; conservative-variable reconstruction, curvilinear free-stream preservation, gradient sharing with KEEP split forms and reacting flows are left open (§5). **Stated**

# Printed slips

- Eq. (28): printed "$\beta u'_{i-1}+u'_i+\beta u'_{i-1}$"; the symmetric tridiagonal scheme needs $\beta u'_{i+1}$ in the third term, and only the symmetric form reproduces Eq. (33).
- Table 2, MIG4 orders printed 3.89, 3.91, 3.97; the printed MIG4 errors $1.19\times10^{-3}$, $7.82\times10^{-5}$, $4.97\times10^{-6}$, $3.37\times10^{-7}$ give $\log_2$ ratios 3.93, 3.98, 3.88, whereas the TENO5 and MEG6 orders match their errors (4.92/4.99/5.00 and 4.23/4.02/4.00). Either the MIG4 orders or the MIG4 errors are misprinted. *(compiler check, not in the sources: $\log_2$ of successive printed error ratios.)*
- Table 5 rates TENO5 dissipation "Low" and MIG4 "Medium", against the text near Fig. 3, "MIG4 has superior dispersion and dissipation properties than the MEG6 and TENO5 scheme".
- Ex. 4.17, Eq. (84): second sub-domain printed "$[1,1]\times[0,1.5]$"; with the domain $[0,7]\times[0,3]$ and the third region $[1,7]\times[1.5,3]$ it must be $[1,7]\times[0,1.5]$.
- Ex. 4.4: the reflecting wall is applied for "$0.1667<x\le4.0$" on a domain $[0,3]\times[0,1]$.
- Ex. 4.12, Eq. (79): domain $[0,10]$ with the jump at $x=0.5$ and $\sin(20\pi(x-5))$, but the axes of Fig. 16 run from about $-4$ to $4$.
- Eq. (6) carries $\mathrm{Re}$ and $M$ in the heat flux while Eq. (22) carries neither; the two scalings are inconsistent as printed.
- §2.1 says "two-dimensional (2-D) Cartesian coordinate system" while Eq. (1) includes the $z$ fluxes.
- Fig. 4(e) caption "MEG4, α-IG" (no such scheme; MIG4 is meant). Ex. 4.1: "Fig. 5(a) and 5(a)"; and "TENO5 scheme with α-EG viscous fluxes takes nearly the same time as the MIG4 scheme despite computing the gradients using a tridiagonal solver" misattributes the tridiagonal solver, which belongs to MIG4/α-IG.
- $\alpha$ denotes the damping coefficient, the MP parameter of $U^{UL}$ (Eq. 58, value never stated) and the volume fraction; $\beta$ denotes the compact coefficient $5/14$, the MP parameter $7$ (Eq. 55) and the vortex strength $5$. In Suresh–Huynh the Eq. (55) and Eq. (58) parameters are one constant.
- Acronym "GRB" for "Gradient-based reconstruction"; Appendix A refers to §3.3 for the Riemann solver introduced in §3.2; Eqs. (93)–(94) use lowercase $s_L$, $s_R$.
- Figs. 2–3: the text says the plots show the imaginary and real parts as dispersion and dissipation, while panel (a) is labelled "Real" and (b) "Imag".
- Ref. [1] (Jiang & Shu) printed "126 (126) (1995)".

# Notation map

| Chamarthi (2023a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\hat Q_i$, $\hat U_i$ | $u_i$ (conservative), primitive vector kept as $U$ | cell-centre **point values**, not cell averages, although the text speaks of cells |
| $U^L_{i+1/2}$, $U^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | interface states |
| $u'_i$, $U''_i$ | $u'_i$, $u''_i$ | cell-centre first and second derivatives (Eqs. 27/28 and 39) |
| $\kappa$ | $\kappa_{\mathrm M}$ | van Leer κ parameter, $1/3$; **$\kappa$ is the kinetic energy in the registry** |
| $\alpha$ (§3.1) | $\alpha_{\mathrm D}$ (page-local on [α-damping viscous flux](/methods/alpha-damping-viscous-flux.md)) | damping coefficient, $4$; **the bare $\alpha$ collides with the DG–FV blending coefficient and with $\alpha_k$** |
| $\alpha$ (Eq. 58), $\beta$ (Eq. 55) | $\xi_{\mathrm{MP}}$ (page-local on the [MP limiter](/methods/monotonicity-preserving-limiter.md)) | one constant in Suresh–Huynh, $7$ here; **$\beta$ collides with $\beta_k$** |
| $\alpha_1$, $\alpha_2$ | $\phi_1$, $\phi_2$ | volume fractions |
| $\beta$ (Eq. 28) | kept, page-local | compact-scheme coefficient $5/14$ |
| $\beta$ (Eq. 69) | $\mathcal E$ | vortex strength, $5$ |
| $d_i$, $d^M_{i+1/2}$ | kept, page-local | MP curvature ($=\Delta x^2u''_i$ in Eq. 60) and limited curvature |
| $k$, $k'$ | $\vartheta$, $\mathrm i\tilde\vartheta$ | reduced wavenumber and first-derivative symbol; for the second derivative $k'$ is kept as the symbol approximating $-\vartheta^2$ |
| $L^n$, $R^n$ | $L_{i+1/2}$, $R_{i+1/2}$ | arithmetic or Roe averages |
| $\hat W$, $W'$ | $\zeta$ and $\zeta'$ | characteristic values and gradients |
| $S_L$, $S_R$, $S_*$ | $s^-$, $s^+$, $s^*$ (page-local) | HLLC speeds (Einfeldt, Batten et al.) |
| $\nu$ (Eq. 40) | $\nu_{\mathrm{kin}}$ | kinematic viscosity; **$\nu$ is the CFL number in the registry** |
| $Ma$, $Re$, $Pr$ | $M$, $\mathrm{Re}$, $\mathrm{Pr}$ | |
| EG6, IG4H, MEG6, MIG4 | kept | the digit is the order of the gradient scheme, not of the reconstruction (fourth order for all) |

# Reference list

86 printed references in numbered style ([1]–[86], order of first citation),
merged complete into the [bibliography](/bibliography.md) with `citedby`
`chamarthi-2023`. Ref. [10] (Liu, Osher & Chan 1994) prints no venue and the
author as "X. X.-D. Liu"; refs. [3], [43], [85] print only an article number;
ref. [78] (Wong & Lele 2017) prints no journal name but a DOI; ref. [44] prints
its authors twice; ref. [1] (Jiang & Shu) is printed with year 1995. No
printed duplicates were found.

# Pages created or updated

Chunk 5 (2026-10-23), cited further in chunk 6 (2026-10-23). This source is cited on:

* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [Gradient-based reconstruction (MEG/MIG schemes)](/methods/gradient-based-reconstruction.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md)
* [Monotonicity-preserving (MP) limiter](/methods/monotonicity-preserving-limiter.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shock–mixing-layer interaction](/benchmarks/shock-mixing-layer-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Triple-point problem](/benchmarks/triple-point-problem.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [Viscous shock tube (Daru–Tenaud)](/benchmarks/viscous-shock-tube.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
* [α-damping viscous flux discretization](/methods/alpha-damping-viscous-flux.md)
