---
type: Method
title: "α-damping viscous flux discretization"
description: "The α-damping viscous flux computes the interface gradient as the average of two cell-centre gradients plus a damping jump of extrapolated states; with sixth-order explicit or fourth-order compact cell gradients and damping coefficient 4 it is a fourth-order conservative viscous discretization free of odd–even decoupling, whose gradients are shared with the inviscid reconstruction."
status: established
aliases: [alpha-damping scheme, α-damping interface gradient, α-EG, α-IG, gradient sharing, interface-gradient viscous flux]
tags: [finite-difference, compact-scheme, low-dissipation, navier-stokes, gradient-based-reconstruction]
timestamp: 2026-10-24T06:00:00Z
---

# α-damping viscous flux discretization

The viscous terms of the compressible Navier–Stokes equations, discretized in conservative
form as differences of interface viscous fluxes, need velocity and temperature gradients at
the interfaces $x_{i+1/2}$. The **α-damping** interface gradient, due to Nishikawa as
recalled by [Chamarthi (2023a)](/sources/chamarthi-2023.md) (§3.1), writes this gradient as
a *consistent* term, the average of the two neighbouring cell-centre gradients, plus a
*damping* term proportional to the jump of the two states extrapolated to the interface. The
damping term suppresses the high-frequency (odd–even) modes that a conservative
discretization built from first derivatives alone leaves undamped. In the gradient-based
finite-difference schemes of Chamarthi and co-workers the cell-centre gradients are computed
once and reused in the inviscid [gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
and in the curvature of the [monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md)
("gradient sharing").

## The interface gradient

For a variable $v$ (a velocity component; the temperature $T$ is treated the same way), with
page-local cell-centre gradient $v'_i\approx(\partial_xv)_i$, damping coefficient
$\alpha_{\mathrm D}$ and curvature coefficient $\beta_{\mathrm D}$ (both page-local; the
sources write $\alpha$, $\alpha_v$, $\alpha_D$ and $\beta_D$),

$$\Big(\frac{\partial v}{\partial x}\Big)_{i+1/2}=\underbrace{\tfrac12\big(v'_i+v'_{i+1}\big)}_{\text{consistent}}+\underbrace{\frac{\alpha_{\mathrm D}}{2\Delta x}\big(v^{\mathrm R}_{i+1/2}-v^{\mathrm L}_{i+1/2}\big)}_{\text{damping}},$$

$$v^{\mathrm L}_{i+1/2}=v_i+\tfrac{\Delta x}{2}v'_i+\beta_{\mathrm D}\big(v_{i+1}-2v_i+v_{i-1}\big),\qquad
v^{\mathrm R}_{i+1/2}=v_{i+1}-\tfrac{\Delta x}{2}v'_{i+1}+\beta_{\mathrm D}\big(v_{i+2}-2v_{i+1}+v_i\big)$$

([Chamarthi (2023a)](/sources/chamarthi-2023.md), Eqs. (23)–(26), with $\beta_{\mathrm D}=0$;
[Chamarthi (2023b)](/sources/chamarthi-2023-b.md), Eq. (12);
[Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md), Eqs. (29)–(31), written in
computational coordinates with $\Delta\xi=1$). Here $v^{\mathrm L}$, $v^{\mathrm R}$ are the
page-local extrapolated states of the viscous gradient, not the reconstructed inviscid states
$u^\mp_{i+1/2}$. The interface velocity in the stress work is $\tfrac12(v^{\mathrm L}+v^{\mathrm R})$
(Chamarthi (2023a), Eq. (26)), and in 1D the viscous flux is
$\big(0,\,-\tau_{i+1/2},\,-\tau_{i+1/2}v_{i+1/2}+q_{i+1/2}\big)$ with
$\tau_{i+1/2}=\tfrac43\mu_{i+1/2}(\partial_xv)_{i+1/2}$ and the heat flux from
$(\partial_xT)_{i+1/2}$ (Eqs. (21)–(22); page-local $\tau_{i+1/2}$ the viscous stress, not the
global smoothness indicator, $q_{i+1/2}$ the heat flux and $\mu$ the dynamic viscosity).

All three sources use $\beta_{\mathrm D}=0$. As recalled by Chamarthi (2023a) (§3.1),
Nishikawa used second-order central cell gradients with $\alpha_{\mathrm D}=8/3$ and obtained
fourth-order diffusion fluxes, and Chamarthi et al. (2022) used fourth-order central
gradients, the curvature term $\beta_{\mathrm D}\neq0$ and an extra parameter in the damping
term, and obtained a sixth-order scheme.

## Cell-centre gradients and order

Chamarthi (2023a) (§3.1, Eqs. (27)–(28)) gives two choices of $v'_i$:

- **α-EG** (explicit), the sixth-order central difference
  $$v'_i=\frac1{60\,\Delta x}\big[45(v_{i+1}-v_{i-1})-9(v_{i+2}-v_{i-2})+(v_{i+3}-v_{i-3})\big];$$
- **α-IG** (implicit), the compact tridiagonal scheme
  $$\beta_{\mathrm c}v'_{i-1}+v'_i+\beta_{\mathrm c}v'_{i+1}=\frac{a_{\mathrm c}}{2\Delta x}(v_{i+1}-v_{i-1})+\frac{b_{\mathrm c}}{4\Delta x}(v_{i+2}-v_{i-2}),\qquad\beta_{\mathrm c}=\tfrac5{14},\ a_{\mathrm c}=\tfrac{11}7,\ b_{\mathrm c}=\tfrac17$$
  (page-local coefficients), solved with a tridiagonal solver.
  *(compiler check, not in the sources: these coefficients satisfy
  $a_{\mathrm c}=\tfrac23(\beta_{\mathrm c}+2)$ and $b_{\mathrm c}=\tfrac13(4\beta_{\mathrm c}-1)$,
  the one-parameter family of fourth-order tridiagonal first derivatives.)*

[Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) (Eqs. (17)–(18)) call the same
two gradient schemes E6 and IG4, and [Chamarthi (2023b)](/sources/chamarthi-2023-b.md)
(Eq. (13)) uses E6 only.

**Order.** Fourier analysis shows that with either gradient the viscous scheme is fourth
order for $\alpha_{\mathrm D}=4$ and second order for every other value (Chamarthi (2023a),
§3.1). For the second derivative the exact symbol is $-\vartheta^2$ in the reduced
wavenumber $\vartheta$ of registry §9, and the modified symbols are (Eqs. (33)–(36))

$$\text{α-IG: }-\vartheta^2+\frac{\vartheta^6}{240}-\frac{17\vartheta^8}{24192}+\dots,\qquad
\text{α-EG: }-\vartheta^2+\frac{\vartheta^6}{360}-\frac{73\vartheta^8}{10080}+\dots$$

With $\alpha_{\mathrm D}=4$ the conservative difference of the interface gradients is
(Remark 3.1, Eqs. (37)–(39))

$$\Big(\frac{\partial^2v}{\partial x^2}\Big)_i=\frac{2}{\Delta x^2}\big(v_{i+1}-2v_i+v_{i-1}\big)-\frac1{2\Delta x}\big(v'_{i+1}-v'_{i-1}\big),$$

the form of Adam (1977) as Chamarthi recalls it, although with different first derivatives.
*(compiler check, not in the sources: with $\alpha_{\mathrm D}=4$, $\beta_{\mathrm D}=0$ the
interface gradient is $\frac2{\Delta x}(v_{i+1}-v_i)-\tfrac12(v'_i+v'_{i+1})$, whose difference
divided by $\Delta x$ is the formula above.)* The code implements the flux form, not this
formula; the formula serves as the second derivative of the inviscid reconstruction
(Remark 3.2). Chandravamsi et al. (§5.2) state fourth order for both E6 and IG4 with
$\alpha_{\mathrm D}=4$; Chamarthi (2023b) (§2.1) states that the fourth-order viscous scheme
has better spectral properties than the sixth-order α-damping scheme of Chamarthi et al.
(2022), citing that work.

The same interface-gradient construction, with $(\alpha_{\mathrm D},\beta_{\mathrm D})$ as free
parameters, generates the second derivative of the seventh-order
[gradient-based reconstruction](/methods/gradient-based-reconstruction.md) of Chamarthi (2023b)
(Eqs. (18)–(21): $\alpha_{\mathrm D}=38/7$, $\beta_{\mathrm D}=3/190$); there it is an
interpolation device, not a viscous flux.

## High-frequency damping and odd–even decoupling

Chamarthi (2023a) (§1) contrasts two routes: Sandham et al. avoid odd–even decoupling by
writing the viscous terms in Laplacian (second-derivative, non-conservative) form, while a
conservative discretization built from first derivatives "is susceptible" to it; the damping
term keeps the conservative form and removes the problem. The plotted modified wavenumbers
(Fig. 1) show both fourth-order α-damping schemes closer to $-\vartheta^2$ at high
wavenumbers than the sixth-order α-damping scheme of Chamarthi et al. (2022) and than the
sixth-order scheme of Shen and Zha, which "does not resolve any of the high-frequency modes".

On the [viscous shock tube](/benchmarks/viscous-shock-tube.md) at $\mathrm{Re}=1000$ on
$1280\times640$ points, the Shen–Zha viscous scheme with TENO5 shows saw-tooth oscillations at
$t=0.5$, while all α-damping runs show no odd–even decoupling (Chamarthi (2023a), Ex. 4.1,
Figs. 4–5). Wall-clock times on that case (Table 1, hardware not printed): TENO5 with α-IG
58680 s, TENO5 with α-EG 50880 s, MEG6 with α-EG 48506 s, MIG4 with α-IG 51146 s.

## Time step

The explicit viscous limit, taken from Nishikawa, is
$\Delta t_{\mathrm{visc}}=\min\frac1{\alpha_{\mathrm D}}\frac{\Delta x^2}{\mu/\rho}$ with
$\alpha_{\mathrm D}=4$, "slightly more restrictive than the value 38/15" of Chamarthi et al.
(2022) (Chamarthi (2023a), Eq. (40)); Chamarthi (2023b) (Eq. (41)) takes the minimum of this
bound and the convective one, with CFL 0.2.

## Curvilinear and moving meshes

[Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) (§5.2, Eqs. (29)–(35), Fig. 5)
apply the formula in each computational direction to $(v_1,v_2,v_3,T)$, obtain Cartesian
gradients by the chain rule with interface metrics,
$(\partial_xv)_{i+1/2}=(\xi_x)_{i+1/2}(\partial_\xi v)_{i+1/2}+(\eta_x)_{i+1/2}(\partial_\eta v)_{i+1/2}+(\zeta_x)_{i+1/2}(\partial_\zeta v)_{i+1/2}$
(Eq. (32); $\xi,\eta,\zeta$ the computational coordinates), take
$T_{i+1/2}=\tfrac12(T^{\mathrm L}+T^{\mathrm R})$ and the viscosity from Sutherland's law, and reuse
the inviscid gradients without recomputation. The interface metrics are interpolated as in
their [free-stream-preserving](/properties/free-stream-preservation.md) procedure. The
viscous double shear layer at $\mathrm{Re}=10^4$ on a deforming $360^2$ grid reproduces the
kinetic energy and enstrophy of a stationary $512^2$ run (§8.2.3).

## Qualifications

- **Order for nonlinear problems.** "Fourth order" is the Fourier order of the linear
  constant-coefficient scheme. Chamarthi (2023b) (Remark 2.1) states that with Sutherland's
  viscosity the viscous discretization is only second order, yet gave better results than
  truly high-order schemes with poorer spectral properties, citing earlier work.
- **Printed slips.** Chamarthi (2023a) prints Eq. (28) as $\beta u'_{i-1}+u'_i+\beta u'_{i-1}$;
  the second term is $\beta u'_{i+1}$, as the symmetric scheme and its modified wavenumber
  (Eq. (33)) require. Chandravamsi et al. print the brackets of Eqs. (17)–(18) as sums
  $(u_{i+1}+u_{i-1})$, where the first-derivative schemes need the differences that
  Chamarthi (2023a) prints, and leave the viscous time-step factor
  $\alpha$ of Eq. (B.3) undefined. Chamarthi (2023a) writes the heat flux with
  $\mu/(\mathrm{Re}\,\mathrm{Pr}\,M(\gamma-1))$ in Eq. (6) but without $\mathrm{Re}$ and $M$ in
  Eq. (22); the paper does not say which scaling the code uses.
- The comparison with the Shen–Zha scheme is the only head-to-head test against another
  viscous discretization; no source compares α-damping with a Laplacian-form discretization.

# Citations

- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — §1, §3.1 (Eqs. (21)–(40), Remarks 3.1–3.2, Fig. 1), Ex. 4.1 (Figs. 4–5, Table 1) (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §2.1 (Eqs. (10)–(13), Remark 2.1), §2.2 (Eqs. (18)–(21)), Eq. (41) (arXiv v1).
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §5.1 (Eqs. (17)–(19)), §5.2 (Eqs. (29)–(35), Fig. 5), §8.2.3, App. B (arXiv v1).
