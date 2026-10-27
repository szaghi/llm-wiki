---
type: Source
title: "Caban et al. (2026) — Analysis of the impact of numerically induced high-order filters and regularization on LES modelling of an incompressible 3D Taylor-Green vortex flow undergoing laminar-turbulent transition"
description: "Fourier analysis of the filters induced by compact derivative and interpolation schemes, and their use in approximate deconvolution, tested in LES of the transitional Taylor–Green vortex at Re=1600: ILES and the Layton–Lewandowski model beat ADM, which beats eddy-viscosity models; ADM needs added dissipation."
resource: "doi:10.1016/j.compfluid.2026.107015"
source_kind: paper
authors: [Caban L., Tyliszczak A., Geurts B.J.]
year: 2026
venue: "Comput. Fluids 312:107015"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Computers_amp_Fluids_Caban_Analysis_of_the_impact_of_numerically_induced_high-order_fil.pdf"
tags: [les, sgs-model, filtering, implicit-les, numerical-dissipation, discretization-consistent-closure]
timestamp: 2026-10-27T15:59:00Z
---

# Summary

Caban et al. (2026) study how the filters that a discretization induces
implicitly interact with LES subgrid models, in the incompressible
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$. They
use their half-staggered compact-difference code SAILOR, where the derivative
scheme (second-order central, sixth- and tenth-order compact) and the
interpolation between velocity and pressure nodes (spectral or compact, 4th to
10th order) can be switched. In Fourier space they write the transfer
functions of explicit compact and finite-difference filters, of the filters
induced by first- and second-derivative schemes, and of the
interpolation-induced filter, the induced filter $\mathcal F_h$ of a
[discretization-consistent closure](/definitions/discretization-consistent-closure.md).
The first-derivative filter changes only the phase speed; the
second-derivative filter lowers the viscous dissipation of small scales; two
interpolations act as a squared filter. A deconvolution-error analysis shows
what happens when the filter assumed in approximate deconvolution differs from
the true one, measured a priori on isotropic DNS data
([a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

In the laminar vortex, derivative-induced filtering leaves the effective
Reynolds number unchanged, while dissipative interpolation or an explicit
regularization filter (a compact filter times its approximate inverse; compare
[explicit modal filtering](/methods/explicit-modal-filtering.md)) lower it. In the
transitional vortex on $64^3$, runs with non-dissipative interpolation are
unstable without a model and with the [Smagorinsky](/methods/smagorinsky-model.md)
or [Vreman](/methods/vreman-model.md) model at $\Delta=2h$. Dissipative
interpolation or regularization stabilize them and act as
[implicit LES](/definitions/implicit-les.md), which beats the eddy-viscosity
models by about a factor two. The approximate deconvolution model (ADM) needs
added [numerical dissipation](/properties/numerical-dissipation.md) to stay
stable and ranks below ILES and below its $N_{\mathrm{AD}}=0$ case, the
Layton–Lewandowski [scale-similarity model](/methods/scale-similarity-model.md),
whose best run is 10% more accurate than the best ILES. Building the
numerically induced filter into the deconvolution helps only when the LES
filter is of low order.

# Version read

Version of record (Elsevier typeset; received 9 September 2025, accepted 16
February 2026, online 18 March 2026), 29 pages, all read; pp. 3–13, 17 and 23
checked visually for equations and tables. Page 1 matches Crossref; page 1
prints "B. J. Geurts", Crossref "Geurts B.". Locators are those of the
published article.

# Key claims

1. In the semi-discrete convection–diffusion equation with central schemes, the first-derivative induced filter scales only the phase speed $a_n$ and leaves the modulus of the Fourier coefficient $|\phi_{\boldsymbol k}(t)|$ unchanged; the second-derivative induced filter gives a numerical viscosity $\nu_n=\nu\hat G^{(2)}_{I,n}\le\nu$ ("non-dissipative and under-dissipative", §3.2.1, Eqs. 26–27). **Derived**
2. With time integration included, global spectral analysis gives an effective viscosity above $\nu$ in some wavenumber ranges, so central schemes can be over-dissipative (§3.2.1, citing GSA). **Stated**
3. The physical-space coefficients of the derivative-induced filters are nonzero over the whole stencil for the second-order, sixth- and tenth-order schemes alike, so every discretization-induced filter couples all nodes; the central coefficient dominates and the others decay with oscillating sign (Fig. 3c,d, 32 nodes). **Shown**
4. Two successive second-order interpolations (to the half nodes and back) equal the explicit trapezoidal filter, $\hat G_E=\tfrac12+\tfrac12\cos(kh)=\cos^2(kh/2)=\hat G_{I'}^2$; the authors state that this holds for higher-order finite and compact interpolations, so the interpolation-induced filter is $G_{I'}^2$ (§3.2.2, Eqs. 34–35). **Derived** (second order); **Stated** (higher order)
5. With 10th-order compact interpolation combined with the derivative filter, the combined transfer function at the point where $\hat G_I=0.5$ falls to 0.49, 0.22 and 0.13 for the second-order, sixth- and tenth-order derivative schemes: interpolation matters most when its order is close to that of the derivative scheme (§4.1, Fig. 5a). **Shown**
6. Deconvolution with a filter of higher order than the true filter $\mathcal H$ suppresses the deconvolved variable; with a lower-order filter it amplifies it, near $k_c$ rather than near the grid cutoff; the error does not vanish as $N_{\mathrm{AD}}\to\infty$ (§4.1, Eqs. 36–37, Fig. 6, $N_{\mathrm{AD}}=5$). **Derived**/**Shown**
7. A priori on isotropic DNS ($Re_\lambda=100$, $384^3$, LES grid 64, Gaussian filter $\Delta=2h$): the SGS-stress error is largest at high wavenumbers and of the order of the filtered product $\overline{uv}$ for every assumed filter, including the exact numerical filter; at low $k$ the largest error comes from the second-order finite-difference filter; with second- and fourth-order compact filters the low-$k$ errors are about two orders of magnitude below those of Layton–Lewandowski or the second-order finite-difference filter (§4.2, Fig. 8a). **Shown**
8. With the second-order finite-difference filter, raising $N_{\mathrm{AD}}$ raises the total SGS error; with second- and fourth-order compact filters the error falls up to $N_{\mathrm{AD}}=4$–6 and then stays constant; the authors advise keeping $N_{\mathrm{AD}}$ small (§4.2, Fig. 8b). **Shown**
9. Laminar vortex ($T_v=7$, $Re=1600$, $\Delta t=10^{-3}$, $t=3.772$, $16^3$–$128^3$): with spectral interpolation the sixth- and tenth-order errors approach the theoretical order; with compact interpolation the errors are much larger and nearly independent of the derivative scheme, 4th-order interpolation giving a large error constant on every grid; regularization by the 8th-order compact filter is less accurate than 8th-order interpolation, while the deconvolution-based regularization filter matters only on coarse grids (§5.1, Fig. 9). **Shown**
10. On $64^3$ with the sixth-order scheme, $Re_{\mathrm{eff}}/Re\approx1$ with spectral interpolation, while regularization and compact interpolation lower $Re_{\mathrm{eff}}$ markedly, 4th-order interpolation "several times"; $Re_{\mathrm{eff}}$ of Eq. 42 is nearly independent of time (§5.1, Figs. 10–11). **Shown**
11. Derivative-induced filtering has a negligible effect on $Re_{\mathrm{eff}}$ because the first-derivative filter is "only dissipative … (not diffusive)" and is compensated by the reduced viscous dissipation of the second-derivative filter (§5.1). **Stated**
12. Transitional DNS: spectral interpolation on $384^3$ and 10th-order compact interpolation on $256^3$ agree "very well" with Brachet et al., van Rees et al. and the $512^3$ pseudo-spectral reference of the first HiOCFD workshop; spectral interpolation on $256^3$ becomes unstable near $t=10$ (§5.2, Figs. 16–17). **Shown**
13. The DNS spectra of the two interpolation variants differ for $k>100$, but there the energy is at least four orders of magnitude below the energetic scales, so kinetic energy and $\varepsilon$ are unaffected (§5.2, Fig. 14). **Shown**
14. LES on $64^3$ with spectral interpolation and no model is unstable around $t=3.5$ (sudden drop of dissipation), the same time as Hickel et al.'s no-model run; on $256^3$ the instability comes near $t=10$ (§5.3.1, Fig. 18). **Shown**
15. Smagorinsky and Vreman with $\Delta=2h$ and spectral interpolation are also unstable (onset near $t\approx4$); with $\Delta=4h$ they are stable but inaccurate, with discrepancies like those of Hickel et al.'s Smagorinsky run with $C_s=0.18$; the authors attribute Hickel et al.'s stability to the larger $C_s$ (0.18 against 0.1) (§5.3.1). **Shown** (attribution a hypothesis)
16. ILES with the second-order derivative and regularization is unstable ($\varepsilon<0$ for $t=5.5$–7), attributed to the second-derivative filter damping viscous dissipation; 10th-order interpolation with the second-order derivative is stable but inaccurate; sixth- and tenth-order schemes with regularization are stable and more accurate than Hickel et al.'s ALDM (§5.3.1, Fig. 19). **Shown**
17. Eddy-viscosity models with dissipative interpolation or regularization ($\Delta=2h$) are stable but worse than ILES: the total dissipation is too large (§5.3.1, Fig. 20). **Shown**
18. Lowering the interpolation order from 10 to 4 increases dissipation; when the interpolation order is at or below the derivative order, $\varepsilon(t)$ resembles that of $\Delta=4h$ with spectral interpolation (§5.3.1, Fig. 22). **Shown**
19. Kinetic-energy error at $t_N=20$ (Eq. 45, Table 4): ILES with regularization $2.23\times10^{-2}$; ILES with 10th-order interpolation $2.23\times10^{-2}$, with 4th-order $2.84\times10^{-1}$; Vreman ($\Delta=2h$) with regularization $4.33\times10^{-2}$; Smagorinsky $4.76\times10^{-2}$; spectral-interpolation entries are blank (unstable) except at $\Delta=4h$; going from 10th to 4th-order interpolation is "an order-of-magnitude increase" for ILES and "approximately a fivefold increase" for the SGS models (§5.3.1, Table 4). **Shown**
20. The transition phase ($t\approx5$–12) contributes most of the error; the error curves flatten from $t\approx12$ (§5.3.1, Fig. 23b). **Shown**
21. With spectral interpolation the Layton–Lewandowski model is stable for every LES filter (finite-difference and compact, orders 2–6), unlike no-model and eddy-viscosity runs; $\varepsilon(t)$ oscillates near its maximum, especially with compact filters, because of excess energy between $k_c$ and $k=30$; dissipative interpolation and regularization damp the oscillations (§5.4.1, Figs. 24–26). **Shown**
22. Layton–Lewandowski with the second-order finite-difference filter is too dissipative early ($t<5$) because that filter acts at low wavenumbers; the best result, regularization with the 6th-order compact filter, is $2.03\times10^{-2}$, "10% lower" than the best ILES (§5.4.1, Table 5). **Shown**
23. ADM with spectral interpolation: with the derivative-induced filter as assumed filter and compact LES filters it is unstable shortly after the $\varepsilon$ peak, because deconvolution amplifies the subfilter energy and the aliasing of the deconvolved product; with finite-difference LES filters it is stable but slightly worse than Layton–Lewandowski; with the LES filter (alone or times the induced filter) as assumed filter it is stable only for the second-order finite-difference filter, and less accurate (§5.4.2, Fig. 29, Table 6). **Shown**
24. ADM with dissipative interpolation or regularization is stable for all filter combinations; ADM therefore "requires some level of numerical dissipation", in agreement with the relaxation term of Stolz and Adams (§5.4.2, §6, Tables 7–8). **Shown**
25. With dissipative interpolation, ADM built on the derivative-induced filter and on that filter times the squared interpolation filter gives virtually the same errors: the interpolation filter acts on low-energy scales; adding the LES filter improves only minimally on Layton–Lewandowski (§5.4.2, Table 8). **Shown**
26. With explicitly assumed filters: the 6th-order compact LES filter with 2nd- or 4th-order finite-difference assumed filters and regularization is unstable (low-order deconvolution amplifies resolved scales); otherwise the error falls as the order of the assumed filter rises; the best ADM (6th-order compact for both filters) is about twice as accurate as the best eddy-viscosity result (§5.4.2, Table 9). **Shown**
27. Ranking at $Re=1600$ on $64^3$: Layton–Lewandowski (regularized, 6th-order compact filter) $\lesssim$ ILES $<$ best ADM $<$ eddy-viscosity models; ADM "does not deliver the anticipated improvement" over Layton–Lewandowski or ILES (§5.4.2, §6). **Shown**
28. The interpolation results apply only to algorithms with explicit interpolation (staggered or half-staggered); collocated grids with discrete [kinetic-energy-conserving](/properties/kinetic-energy-preservation.md) schemes do not have this dissipation (§6). **Stated**

# Printed slips

- Eq. 16, middle rows: "$\sum_{l=0}^N j^2b_l$" and so on, with summation index $l$ but $j$ in the summand.
- Eq. 23, first row, printed $1+2\sum_ka_k=2\sum_ll^rb_l$ for $r=1,2$. Taylor expansion of Eq. 22's stencil $f_{j+l}-2f_j+f_{j-l}\approx l^2h^2f''$ gives $1+2\sum a_k=\sum l^2b_l$ for $r=2$, without the factor 2, and Table 2 satisfies that form (sixth-order: $\tfrac{12}{11}+4\cdot\tfrac{3}{44}=\tfrac{15}{11}=1+2\cdot\tfrac{2}{11}$) *(compiler check, not in the sources)*.
- Eq. 32, second row, printed exponent $(2l-1)^{2l}$; the exponent must be the order index $2j$: with $2j$, Table 3's 6th-order interpolation satisfies the $j=1$ row ($2^3\cdot\tfrac{3}{10}=2.4=\tfrac32+9\cdot\tfrac1{10}$), with $2l$ it does not ($\tfrac32+81\cdot\tfrac1{10}=9.6$) *(compiler check, not in the sources)*.
- Eq. 43 prints $w(t=0)=\frac{2}{\sqrt3}\sin\theta\cos x\sin y\cos z$; the field is solenoidal only with $\cos x\cos y\sin z$, since $\partial_xu+\partial_yv=-\frac{2}{\sqrt3}\sin\theta\cos x\cos y\cos z$ *(compiler check, not in the sources)*; harmless here because $\theta=0$.
- §5.1 prints $E_{d,a}(t)=\exp(-6T_v^2t/Re)/E_0$ although $E_d=E/E_0$ is already normalized, and Eq. 42 divides $E_d$ by $E_0$ again inside the logarithm.
- §5.3.1 and §5.4.1 point to "Table 7" for the ILES and eddy-viscosity errors, which are in Table 4.
- §5.4: "approachTable 4." (missing space).
- Table 9 caption "$\mathcal G_\Delta$ = FDF2, $\mathcal G_\Delta$ = CDF2", while the rows and §5.4.2 use CDF6.
- Fig. 28 caption labels two panels "(b)"; Fig. 27 caption has no "(a)"; Fig. 30 caption "N-DI (a) na N-DI-R (b)".
- §4.2: "$N_{\mathrm{ADM}}=4◦6$" for the range 4–6.
- §5.3.1: "see the TKE spectra in Fig. 1" (the spectra are in Fig. 14); §5.4.2: "(see 25)" without "Fig.".
- The interpolation filter is written $\mathcal G_{I'}^2$ in §3.2.2 and the Fig. 5 caption, but $\mathcal G_{N'}=\mathcal G_I\mathcal G_{I'}$ in §4.1 and Fig. 6 "with $\mathcal G_{I'}$ representing … (CDI10²)".
- The first-derivative filter is called "non-dissipative" (§1, §3.2.1) and "dissipative … without inducing numerical diffusion" (abstract, §5.1, §6).
- References [73] and [83] are the same work (Gullbrand & Chow 2003) printed twice; author lists of [40], [41], [70] and [80] are garbled.

# Notation map

| Caban et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f=\mathcal G_\Delta*f$ | $\bar\phi=G*\phi$ | agrees |
| $\hat{\mathcal G}(k)$, $\hat{\mathcal G}_E$ | $\hat G(k)$ | transfer function; **collision:** the source's hat is the transfer function, not a test filter |
| $\hat f_n$ | $\phi_{\boldsymbol k}$ | Fourier coefficient |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | positive trace, agrees |
| $\sqrt{2S_{lm}S_{lm}}$ | $\lvert\bar S\rvert$ | agrees (factor two printed) |
| $C_s=0.1$, $C_v=2.5C_s^2$ | $C_s$, (Vreman constant) | |
| $\Delta$, $h$, $h_g$ | $\Delta$, $h$, (largest grid spacing) | $\Delta=2h$ or $4h$ |
| $k_c$, $k_g$ | $k_c$, (grid cutoff $\pi/h_g$) | |
| $\omega$, $\omega_n=2\pi n/K$ | $kh$ (scaled wavenumber) | **collision:** $\omega$ is the specific dissipation rate in the registry |
| $\mathcal G_I^{(r)}$, $\mathcal G_{I'}$, $\mathcal G_{N'}$ | $\mathcal F_h$ (its derivative, interpolation and combined parts) | page-local subscripts |
| $\mathcal G_{QG}=Q_{N_{\rm ADM}}\mathcal G_E$ | (regularization filter) | from the 8th-order compact filter with $N_{\mathrm{AD}}=2$ |
| $\mathcal G_{EF}$, $\mathcal H$ | (filter assumed in deconvolution, true filter) | |
| $N_{\mathrm{ADM}}$, $u^*_i$ | $N_{\mathrm{AD}}$ (number of van Cittert terms, registry §11), $u^*_i$ (deconvolved velocity, page-local) | |
| $\hat{\mathcal E}$ | (deconvolution error, Eq. 36) | negative = amplification |
| $a_n$, $\nu_n$ | (numerical phase speed and numerical viscosity of mode $n$) | $a_n=a\hat G^{(1)}_{I,n}$, $\nu_n=\nu\hat G^{(2)}_{I,n}$ |
| $M$, $N$ | (stencil sizes of compact formulas) | **collision:** $N$ is the polynomial degree in the registry |
| $K$ | $N_x$ | nodes per direction |
| $p$ | (formal order) | |
| $Re_{\mathrm{eff}}$ | (effective Reynolds number from energy decay) | |
| $E$, $E_0$ | $K$ (kinetic energy) | spectral page convention; $E_0=0.1875$ |
| $T_v$, $\theta$ | (laminar-vortex wavenumber, initial phase) | |
| N-DI, DI, N-DI-R | (spectral interpolation; compact interpolation; spectral interpolation plus regularization) | |

# Reference list

114 printed references, numbered, Elsevier abbreviated style without titles in
quotes. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` this slug. [73] and [83] are one work printed twice and fold
into one entry. [99] (Li et al., J. Fluid Mech. 2024, jet mixing) is not the
ingested source li-2024 and takes the key `li-2024-d`. Author lists of [40], [41],
[70] and [80] are garbled in print; [93] has no venue; [100] no volume; [6],
[40], [81], [99] no pages.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Vreman model](/methods/vreman-model.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
