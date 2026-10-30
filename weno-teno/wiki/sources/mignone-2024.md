---
type: Source
title: "Mignone et al. (2024) — A fourth-order accurate finite volume scheme for resistive relativistic MHD"
description: "Fourth-order finite-volume scheme for resistive relativistic MHD in PLUTO: constrained transport for face-averaged B, pointwise WENO-Z and the MHLLC solver, and IMEX Runge–Kutta stages whose explicit part acts on cell averages and whose stiff implicit part acts on point values, solved by Newton–Broyden."
resource: "doi:10.1093/mnras/stae1729"
source_kind: paper
authors: [Mignone A., Berta V., Rossazza M., Bugli M., Mattia G., Del Zanna L., Pareschi L.]
year: 2024
venue: "Mon. Not. R. Astron. Soc. 533:1670-1686"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Monthly_Notices_of_the_Royal_Astronomical_Society_Mignone_A_fourth-order_accurate_finite_volume_scheme_for_resistive_r.pdf"
tags: [finite-volume, mhd, relativistic, imex, stiff-source, very-high-order]
timestamp: 2026-10-23T15:19:00Z
---

# Summary

Mignone et al. (2024) build a finite-volume method for resistive
[relativistic MHD](/definitions/relativistic-hydrodynamics.md) in Cartesian
coordinates that they call "genuinely fourth-order". It extends their "Paper II",
Berta et al. (2024), from ideal to resistive MHD. The stiff relaxation term
$-\tilde{\mathcal E}/\eta_{\mathrm m}$ of Ampère's law needs implicit time
integration. The authors use [IMEX Runge–Kutta](/methods/imex-runge-kutta.md)
methods, Pareschi & Russo's SSP3(4,3,3) and Kennedy & Carpenter's fourth-order
ARK4(3)7L[2]SA1, and print both double tableaux.

The magnetic field is evolved as face averages by
[constrained transport](/methods/constrained-transport.md), which keeps
[$\nabla\cdot B=0$](/properties/divergence-free-magnetic-field.md). Density, momentum,
energy and the electric field are evolved as cell averages. Unlike their Paper I,
$\nabla\cdot\mathcal E$ is not constrained: the charge is a fourth-order central
divergence of $\mathcal E$. The explicit stages act on cell averages and the
implicit stage on point values at the cell centres. The two are linked by the
$1\mp\Delta/24$ [average–point conversion](/operators/cell-average-point-value-conversion.md).
The implicit update reduces to a $3\times3$ nonlinear system for the four-velocity,
solved by Newton–Broyden with an analytic Jacobian, and it also performs the
conservative-to-primitive conversion. The authors stress that the pointwise
treatment of the stiff source is what allows accuracy beyond second order.

Interface states come from fifth-order WENO-Z on point values. The fluxes come from
the MHLLC solver, a combination of Maxwell jump conditions with the relativistic HLLC
of the [HLL family](/methods/hll-riemann-solvers.md). Edge electric fields are formed
by an upwind "CT-Maxwell" average. A derivative-ratio detector triggers a fallback
to WENO3 or linear reconstruction near discontinuities. The scheme needs three ghost
zones and two boundary calls per stage.

The tests are run in [PLUTO](/software/pluto.md). They are a telegraph equation,
a stationary charged [vortex](/benchmarks/magnetized-vortex.md), a resistive rotor
and a 3D [blast wave](/benchmarks/mhd-blast-wave.md), the
[ideal tearing mode](/benchmarks/tearing-mode-instability.md) and a 3D relativistic
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md). They
show fourth order, errors two orders of magnitude below the second-order scheme of
Paper I in the charge, and the tearing growth rate reached at about half the resolution.
SSP3(4,3,3) proves more robust than ARK4 for small resistivity.

# Version read

The archive file is the typeset version of record (OUP, CC BY 4.0), deposited on HAL
as hal-04661926v1 (submitted 21 October 2024) behind a one-page HAL cover sheet: 18
PDF pages, journal pp. 1670–1686, all read; pp. 4–8, 10–13 and 17 were checked on
the page images. The HAL cover prints a variant title, "A Fourth-Order Finite
Volume Scheme for Resistive Relativistic Magnetohydrodynamics"; the journal title
above matches Crossref. Page 1 matches the Crossref record for authors, venue,
pages and DOI.

# Key claims

Registry notation. Page-local: $\bar u_c$ and $u_c$ the cell average and the
cell-centre point value of the conserved vector, $v_c$ the primitive point value;
$\Delta=\Delta^x+\Delta^y+\Delta^z$ the undivided three-point Laplacian;
$\mathcal E$ the electric field (registry §10) and
$\tilde{\mathcal E}=W\mathcal E+Wv\times B-W(\mathcal E\cdot v)v$; $\eta_{\mathrm m}$
the resistivity and $\tilde\eta_{\mathrm m}=\eta_{\mathrm m}/(a_{kk}\Delta t)$;
$\mathfrak q=\nabla\cdot\mathcal E$ the charge density; $h_{\mathrm e}$ the specific
enthalpy; $\kappa_\gamma=\gamma/(\gamma-1)$; $h_\Delta$ the grid spacing (see the
Notation map).

1. The scheme is a finite-volume, "genuinely fourth-order accurate" method for resistive relativistic MHD in Cartesian coordinates; $B$ is evolved as face averages by constrained transport, $D$, the momentum, the energy and $\mathcal E$ as cell averages (Abstract, §3.1). **Stated** (order **Shown** in §4.1–4.2)
2. Unlike Paper I, the electric field is cell-centred, not staggered, and its divergence is not enforced: $\mathfrak q$ is replaced by $\nabla\cdot\mathcal E$ where needed. The authors found no "appreciable evidence of loss of accuracy or stability", citing "extensive testing (not part of this work)" (§1, §3.1). **Stated**
3. Pointwise reconstruction is "crucial to achieve accuracy beyond the second order when evaluating the implicit stiff source terms within the IMEX formulation" (§1, citing Boscarino, Russo & Semplice 2018). **Stated**
4. The explicit stages are applied to cell averages and the implicit stage to point values, through the two-step stage update (24) (§3.2). **Derived**
5. Point values are recovered by $u_c=(1-\Delta/24)\bar u_c+O(h_\Delta^4)$ (Eq. 25); face point values of $B$ use only the transverse Laplacian (Eq. 28), and cell-centre $B$ the unlimited fourth-order interpolation $-\tfrac1{16}(\cdot)+\tfrac9{16}(\cdot)$ of Felker & Stone (2018) (Eq. 29) (§3.3). **Stated** (background)
6. The primitive recovery follows Palenzuela et al. (2009): the electromagnetic parts are subtracted from momentum and energy, then the relativistic-hydrodynamics inversion of Mignone, Plewa & Bodo (2005) is used; this differs from Paper I (§3.3). **Stated**
7. The implicit electric-field update (30) reduces to an explicit function $\mathcal E(Wv)$ (Eq. 32), and momentum conservation, $f(Wv)=m-Dh_{\mathrm e}Wv-\mathcal E\times B=0$ (Eq. 33), is a $3\times3$ nonlinear system for $Wv$, solved by Newton–Broyden with the analytic Jacobian (38)–(40) (§3.4). **Derived**
8. The Newton–Broyden iteration "converges in 2–5 iterations given a relative tolerance of $10^{-11}$" in standard applications (§3.4). **Stated**
9. Because the implicit step also performs the conversion to primitives, it runs on a layer of ghost zones ("three for a five-point stencil") to avoid extra communication (§3.4). **Stated**
10. Interface values come from fifth-order WENO-Z on point values (Eqs. 41–42), with $d_k=\{1/16,5/8,5/16\}$, $\epsilon=10^{-40}$ and $\alpha_k=d_k\big(1+\lvert\beta_0-\beta_2\rvert/(\beta_k+\epsilon)\big)$ (§3.5). **Stated** (background, Paper II)
11. The flux is MHLLC (Paper I): Maxwell jump conditions for the transverse $\mathcal E$ and $B$ (Eq. 43), relativistic HLLC for the gas (Eqs. 44–46) and their sum (Eq. 47); the face average is $\hat f=(1+(\Delta^y+\Delta^z)/24)f$, $f$ the point flux (Eq. 48) (§3.6). **Stated**
12. The edge field $\mathcal E_z$ is reconstructed from the face centres to the edge along the transverse directions, from one value per face, the average of the two sides (Eq. 50); the four values are combined by the CT-Maxwell upwind average (Eq. 52) and converted to a line average by $1+\Delta^z/24$ (Eq. 53). This "differs from the one employed in Paper I", which started from the cell centre with linear interpolation (§3.7, footnote 1). **Stated**
13. "A typo is present in equation (48) of Paper I, since the arithmetic average operator $\langle.\rangle_z$ is not needed" (§3.7, footnote 1). **Stated** (correction of earlier work)
14. The explicit source $-\mathfrak qv$ is added as the average $(1+\Delta/24)\mathfrak q_{\mathrm c}v_c$ (Eq. 54), with $\mathfrak q_{\mathrm c}$ a fourth-order central divergence (Eqs. 55–56); these unlimited differences "may lead to the appearance of spurious oscillations in the presence of strong gradients", which does not affect the tests shown (§3.8). **Stated**
15. Order reduction ("fallback"): Paper II's derivative-ratio sensor flags cells, where the Laplacian corrections (25) and (48) are dropped and the reconstruction switches to WENO3 or linear; the detector uses five zones and "does not require additional ghost zones" (§3.9). **Stated**
16. The algorithm needs two boundary calls per stage, $\bar u_c$ on one ghost layer and $v_c$ on three; "unlike previous works, our formulation does not require more than three ghost zones", "a more compact stencil when compared to its previous version (Paper II)" (§3.10, §5). **Stated**
17. On the rotated 2D telegraph equation (ARK4) fourth order is recovered for conductivity $\sigma_{\mathrm c}=1,10,20$ and polarization angles $30^\circ$, $90^\circ$, in both $B$ and $\mathcal E$ (§4.1, Fig. 2). **Shown**
18. On the stationary charged vortex the fourth-order scheme "is able to reduce the error by two orders of magnitude" in charge relative to Paper I; SSP3(4,3,3) and ARK4 "yield nearly identical results", "however, the ARK4 method becomes unstable" for $\eta_{\mathrm m}\lesssim10^{-4}$; the pressure errors show fourth order for both (§4.2, Fig. 3). **Shown**
19. On the resistive rotor ($400^2$, WENO3 fallback) only SSP3(4,3,3) completes the run at $\eta_{\mathrm m}=10^{-6}$, confirming "the reduced stability of the fourth-order method, which is not SSP"; at $\eta_{\mathrm m}=10^{-1}$ spurious $m=4$ modes appear, an artefact of Cartesian coordinates more evident with MHLLC than with a more diffusive solver (§4.3, Fig. 4). **Shown**
20. On the 3D blast wave ($\eta_{\mathrm m}=10^{-6}$, SSP3(4,3,3), linear fallback) the forward shock moves almost radially, with maximum Lorentz factor about 5.4 (§4.4, Fig. 5). **Shown**
21. Ideal tearing mode ($S_{\mathrm L}=10^6$, $k_w=12$, expected growth rate about 0.27): from $256\times64$ to $2048\times512$ the measured rates are 1.19, 0.89, 0.58, 0.38 at second order and 0.75, 0.44, 0.30, 0.27 at fourth order; the fourth-order scheme "requires approximately half of the resolution (or less)" (§4.5, Table 1). **Shown**
22. 3D relativistic Kelvin–Helmholtz ($\eta_{\mathrm m}=10^{-5}$, SSP3(4,3,3), linear fallback): growth rates about 2.94 and 2.14 for the second-order scheme (low and high resolution) and about 2.17 and 2.31 for the fourth-order one; the latter at $N_x=128$ "already outperforms" the second-order scheme at twice the resolution, and large-scale modes are better resolved (§4.6, Figs. 7–8). **Shown**
23. ARK4 keeps fourth order in time for smooth problems; the third-order SSP scheme "is more robust for lower values of the resistivity", $\eta_{\mathrm m}\lesssim10^{-5}$, "and thus preferable for highly stiff problems" (§5). **Shown** (the threshold is $10^{-4}$ in §4.2 and $10^{-5}$ in §5)
24. The paper is "one of the few contributions addressing the design of the fourth-order methods based on an IMEX approach for multidimensional PDEs with stiff terms" (§5). **Stated**
25. The CFL number is 0.4 in 2D and 0.3 in 3D; smooth initial data are averaged with four-point Gauss quadrature; the error is $\epsilon_1(Q)=\sum_i\lvert Q(x_i)-Q_{\mathrm{ref}}(x_i)\rvert/N_{\mathrm z}$, $N_{\mathrm z}$ the number of zones (§4). **Stated**

*(Compiler check, not in the sources.)* The three candidates of Eq. (41) combined
with $d_k=(1/16,5/8,5/16)$ give the fifth-order point interpolant
$(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2})/128$. The tearing parameters are
consistent: $v_A=1/\sqrt{1+1+2}=0.5$, $\eta_{\mathrm m}=v_AL/S_{\mathrm L}=5\times10^{-7}$,
$1.4S_{\mathrm L}^{1/6}=14$ and $2\pi/12=0.523599$, the printed $y$-period.

# Printed slips

- **Eq. (52):** "$-\frac{B^N_x-B^S_y}{2}$": the second term should be $B^S_x$, the quantity Eq. (51) defines; no $B^S_y$ exists.
- **Eq. (51):** "$B^W_{y,z_e}=\mathcal R^+_y(B_{y,y_f})$, $B^E_{y,z_e}=\mathcal R^-_y(B_{y,y_f+\hat e_x})$": by Fig. 1 and the parallel Eq. (49), $E^W_{z,z_e}=\mathcal R^+_x(E_{z,y_f})$, the operator on $y$-faces is $\mathcal R_x$.
- **Eq. (61):** "$(1\cdots f_t(r))$", a dot glyph for the minus of $(1-f_t(r))$.
- **Eq. (68):** the density prints $\rho_h$ in both terms, "$\frac{1+\tanh\phi}{2}\rho_h+\frac{1-\tanh\phi}{2}\rho_h$"; no density values are given, and $p$, $\sigma$ in $B=(\sqrt{2p\sigma\mu_p},0,\sqrt{2p\sigma\mu_t})$ are not specified, while $\sigma$ is $1/\eta$ in the same section.
- **Eqs. (21), (24):** the stage formula prints $\tilde a_{kj}\hat R_c$ without the stage superscript $(j)$.
- **3D blast wave (§4.4):** the inner and outer density and pressure are not given.
- **Fig. 3:** the caption says "1D horizontal cuts, at y = 0, of charge at t = 3", the panel title reads "t=2"; the caption says "pressure" maps where the panel label reads "ρ", and "the expected second-order scaling" where the panel carries lines labelled $N^{-2}$ and $N^{-4}$. **Fig. 4:** the caption says "gas pressure p (upper panels)", the colour-bar label reads "ρ".
- **§4.5:** the text calls the Paper I data "dotted lines"; the Fig. 6 caption says "solid (dashed) lines for the fourth-order (second-order) data". **§4.6:** colours code the resolution ("blue and red colours, respectively"), then "clearly visible with the second-order method (red lines)".
- **§4.6:** the text says higher resolution or accuracy gives "a gradual reduction of the growth rate", while the printed fourth-order rates rise from about 2.17 to about 2.31.
- Typos: "Newton–Brodyen" (§3.4), "implcit" (§3.10), "neglection" (§4.5). $\eta$ is also an SSP3(4,3,3) coefficient (App. A), $\kappa$ both the Newton index and the ARK4 diagonal.

# Notation map

| Mignone et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\langle U\rangle_c$, $U_c$, $V_c$ | $\bar u_c$, $u_c$, $v_c$ (local) | cell average, point values of conserved and primitive variables; **collision** of $v_c$ with the velocity |
| $\hat B_{x,x_f}$, $B_{x,x_f}$ | face average and face point value of $B_1$ | staggered constrained-transport variable |
| $\bar E_{z,z_e}$ | $\bar{\mathcal E}_3$ | line-averaged edge field, as on [constrained transport](/methods/constrained-transport.md) |
| $\boldsymbol E$, $\tilde{\boldsymbol E}$ | $\mathcal E$, $\tilde{\mathcal E}$ | electric field; **collision**: registry $E$ is the total energy |
| $D$, $\boldsymbol m$, $\mathcal E$ | $D$, $m$, $E$ | lab density, total momentum, total energy; **collision** of the source's $\mathcal E$ with the electric field |
| $\rho$, $\boldsymbol v$, $p$ | $\rho$, $v$, $p$ | agree |
| $\gamma$, $\boldsymbol u=\gamma\boldsymbol v$ | $W$, $Wv$ | Lorentz factor, spatial four-velocity |
| $\Gamma$, $\Gamma_1=\Gamma/(\Gamma-1)$ | $\gamma$, $\kappa_\gamma$ (local) | $\gamma=4/3$ |
| $h$, $w=\rho h$ | $h_{\mathrm e}$, $\rho h_{\mathrm e}$ (local) | specific enthalpy; **collision** with the numerical flux $h$ and the entropy variables $w$ |
| $q$ | $\mathfrak q$ (local) | charge density; **collision** with the weight exponent $q$ |
| $\eta$, $\tilde\eta$ | $\eta_{\mathrm m}$, $\tilde\eta_{\mathrm m}$ (local) | resistivity; **collision** with the entropy $\eta$ |
| $\sigma$ (telegraph, KH) | $\sigma_{\mathrm c}=1/\eta_{\mathrm m}$ (local) | conductivity; **collision** with the affine $\sigma$ |
| $\Sigma$ | $\sigma_{\mathrm m}$ (local) | magnetisation $B_0^2/\rho_0$ |
| $\Delta$, $\Delta^x$ | local | undivided Laplacian, no $1/\Delta x^2$ |
| $\delta_x$ | local | fourth-order central derivative (56) |
| $\mathcal R^\pm_x$, $\mathcal R^\pm_y$ | local | 1D reconstruction to an edge |
| $\hat F$, $\mathcal F$ | $\hat f$, $f$ (point flux) | face-averaged and point numerical flux |
| $d_l$, $\beta_l$, $\alpha_l$, $\omega_l$, $\epsilon$ | $d_k$, $\beta_k$, $\alpha_k$, $\omega_k$, $\epsilon$ | point-value WENO-Z, $\tau_5=\lvert\beta_0-\beta_2\rvert$, exponent 1 |
| $V^L_{i+1/2}$ | $v^-_{i+1/2}$ | left interface state |
| $\lambda_L$, $\lambda_R$, $\lambda^*$ | $s^-$, $s^+$, contact speed | HLLC speeds |
| $\mathcal H$, $\mathcal W$ | local | gas flux and state of the HLLC part |
| $\tilde A,\tilde w,\tilde c$; $A,w,c$; $a_{kk}$; $\nu$ | local | explicit and implicit Butcher coefficients and stage count; **collision** of $\nu$ with the CFL number |
| $S$, $k$ (tearing) | $S_{\mathrm L}$, $k_w$ (local) | Lundquist number and wavenumber |
| $v_a$, $L$ (tearing) | $v_A$, $L$ (local) | Alfvén speed and reference length |
| $\gamma_{TM}$ | tearing growth rate (local) | **collision** with $\gamma$ |

# Reference list

The paper prints 48 references in MNRAS author-year style, alphabetical, without
titles. The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `mignone-2024`. The cited Paper II is the ingested source
Berta et al. (2024). Mignone & Bodo (2005, MNRAS 364:126) and Mignone, Plewa & Bodo
(2005, ApJS 160:199) take suffixes in printed order, matching the existing keys.
Pareschi & Russo (2003) is a chapter of *Hyperbolic Problems: Theory, Numerics,
Applications*. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunks 10–12 (2026-10-23/30). This source is cited on:

* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)
* [Constrained transport for the induction equation](/methods/constrained-transport.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [GLM divergence cleaning](/methods/glm-divergence-cleaning.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Magnetized (MHD) vortex](/benchmarks/magnetized-vortex.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [PLUTO](/software/pluto.md)
* [Special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
* [Tearing-mode instability](/benchmarks/tearing-mode-instability.md)
