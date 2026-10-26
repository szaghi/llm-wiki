---
type: Method
title: "Autonomous eddy-viscosity model"
description: "Domaradzki's autonomous LES derives the eddy viscosity at every step from the resolved field itself: in spectral space from the subgrid transfer across a test cutoff, in physical space from the filtered dissipation of a similarity stress, with no postulated functional form and no adjustable constant."
status: established
aliases: [autonomous LES, autonomous large-eddy simulation, similarity-derived eddy viscosity]
tags: [les, sgs-model, eddy-viscosity, backscatter]
timestamp: 2026-10-26T10:27:00Z
---

# Autonomous eddy-viscosity model

The **autonomous eddy-viscosity model** of
[Domaradzki (2024)](/sources/domaradzki-2024.md) computes the subgrid
eddy viscosity at each time step from the energy transfer among the
resolved scales of the LES field, instead of postulating a functional form
with a model constant as the
[Smagorinsky model](/methods/smagorinsky-model.md) does. The physical-space
version, the paper's contribution (§2.4), takes the energy flux of a
[scale-similarity](/methods/scale-similarity-model.md) stress built from the
LES velocity, filters it once more in place of the shell average of
spectral theory, and turns it into an eddy viscosity applied in Boussinesq
form, $\tau^d_{ij}=-2\nu_t\bar S_{ij}$. No constant enters ("fully
autonomous", an implicit coefficient of 1). The same author's earlier
spectral version (Domaradzki 2021a,b, 2022, recalled in §2.2) is the origin
of the idea.

**Notation on this page.** Domaradzki writes the LES field as $u^<$ (the
DNS field projected on the LES mesh, sharp cutoff $k_c=\pi/\Delta x$) and a
graded (Gaussian or box) filter of width $2\Delta x$ applied to it as an
overbar. Here, following the registry, the LES field is $\bar u_i$ and the
graded filter applied to it is written as the test filter, a hat, with
width $\hat\Delta=2\Delta x$. The paper's sign convention for the subgrid
dissipation, $\epsilon_{SGS}=\tau_{ij}\bar S_{ij}$, negative for forward
transfer, is the opposite of the registry's $\Pi=-\tau_{ij}\bar S_{ij}$;
every formula below is translated to $\Pi$. Page-local symbols: $C_{\mathrm A}$
the non-dimensional constant of the constant variant (the paper's $C$, Eq.
3.3; not the Smagorinsky $C_s$), $u_{\mathrm{rms}}$ the rms velocity (the
paper's $u'$), $U_0t/M$ the time of the Comte-Bellot–Corrsin experiment in
units of the grid-mesh size $M$ over the tunnel speed $U_0$.

## Spectral origin

In the spectral version (§2.2, steps i–ix), the shell-averaged subgrid
transfer across a sharp test cutoff $ak_c$, $a=1/2$ recommended, is
computed from the LES field at each step. Kraichnan's definition (Eq. 2.24),
$\nu_t(k\mid ak_c)=-T_>(k\mid ak_c)/(2k^2\bar E(k))$ (the
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)), gives a
resolved eddy viscosity, which is rescaled to the real cutoff $k_c$ in the
similarity variable $k/k_c$. Its total level is then fixed by the
ultraviolet-flux relation (Eq. 2.26), derived in Domaradzki (2021b) from
Kraichnan's scaling of the ultraviolet flux (Eq. 2.27): the total subgrid
transfer across $k_c$ equals the resolved transfer across $ak_c$ divided
by $1-a^{4/3}$, a factor $D=1.66$ for $a=1/2$
($1/(1-2^{-4/3})=1.658$, *compiler check, not in the sources*, consistent
with the printed value). The same paper states that the actual transfer at
$k_c$ is therefore at most 1.66 times the resolved transfer at $k_c/2$
(§3.3). Under-predicting this total transfer led in the spectral method to
a gradual loss of accuracy, "reminiscent of the similarity model" (§3.2).

## Physical-space model

The Leonard-type stress of the LES field under the graded filter,
$$L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j,$$
is what Domaradzki calls the resolved (similarity-like) SGS stress
$\tau^{\mathrm{res}}_{ij}$ (Eq. 2.36): the part of the full stress on the
LES mesh that contains no true subgrid scales, the remainder
$\tau^{\mathrm{phy}}_{ij}$ (Eq. 2.37) holding all interactions with modes
beyond $k_c$ (after Domaradzki et al. 2002, as recalled in §2.3). Its local
energy flux, written here $\Pi_L=-L_{ij}\hat{\bar S}_{ij}$ (page-local; the
paper's $\epsilon^{\mathrm{res}}_{SGS}$ with the opposite sign, Eq. 2.40),
is the physical-space analogue of the resolved spectral transfer: with a
sharp spectral filter at $k_c/2$ its domain average equals the resolved
spectral transfer across $k_c/2$ (Eq. 2.41).

Inverting $\Pi_L=2\nu_t\hat{\bar S}_{ij}\hat{\bar S}_{ij}$ point by point
(Eq. 2.46) gives negative viscosities wherever $\Pi_L<0$ and is stated to
cause numerical instability. The model replaces shell averaging by one more
application of the same filter (Eq. 2.47):

$$\nu_t(\boldsymbol x)=\frac{\widehat{\Pi_L}(\boldsymbol x)}{2\,\hat{\bar S}_{ij}(\boldsymbol x)\hat{\bar S}_{ij}(\boldsymbol x)}
=\frac{\widehat{\Pi_L}}{\lvert\hat{\bar S}\rvert^2},\qquad
\tau_{ij}=-2\nu_t\bar S_{ij}\quad(\text{Eq. 2.42}).$$

The viscosity is computed from the filtered field and applied unchanged to
the unfiltered LES field; the paper assumes, rather than proves, that "for
two similar fields … the eddy viscosities are similar, here assumed to be
the same", and needs no rescaling to $k_c$ because a graded filter keeps
the spectral support of the field (§2.4). The trace of the model stress is
ignored, since only energy equations are used (§2.4). Domaradzki reads
$L_{ij}$ either as a generalized similarity model (no true subgrid scales
enter) or as a deconvolution model, the Gaussian filter being exactly
invertible (§3.1). The filters are the tensor products of the 1-D Gaussian
$G(r)=\sqrt{6/(\pi\hat\Delta^2)}\exp(-6r^2/\hat\Delta^2)$ and the 1-D box of
width $\hat\Delta$ (Eqs. 2.28–2.30).

### Constant variant

Multiplying Eq. (2.47) by a non-dimensional $C_{\mathrm A}$ (Eq. 3.3) enforces the
global transfer constraint of the spectral steps viii–ix; $C_{\mathrm A}=1$ is the
autonomous model. For graded filters no scaling law fixes the total
transfer, so $C_{\mathrm A}$ depends on filter and spectrum; comparing the domain
average of $\Pi_L$ with the spectral subgrid transfer gives $C_{\mathrm A}\approx0.8$
for the Gaussian with $\hat\Delta=2\Delta x$, for both inertial-range and
Comte-Bellot–Corrsin fields (§3.2). Unlike the dimensional coefficient of
the spectral model, this $C_{\mathrm A}$ is non-dimensional.

### Dynamic determination of $C_{\mathrm A}$ fails

A [dynamic procedure](/methods/dynamic-procedure.md) for $C_{\mathrm A}$, from
Germano's identity in energy form (Eqs. 3.4–3.6), gives wildly fluctuating
local values and a domain-averaged $C_{\mathrm A}=-3.9$ with standard deviation of
order $10^3$ (§3.3). With constant $C_{\mathrm A}$ the domain-averaged identity reads
(Eq. 3.7, translated to $\Pi$)

$$\langle\Pi_L\rangle=C_{\mathrm A}\Big(\langle\widehat{\Pi_L}\rangle-\Big\langle\widehat{\big(\widehat{\Pi_L}/\hat{\bar S}_{kl}\hat{\bar S}_{kl}\big)\bar S_{ij}}\,\hat{\bar S}_{ij}\Big\rangle\Big),$$

where $\langle\cdot\rangle$ is the average over all mesh points; the two
bracketed terms are comparable in value (confirmed by direct calculation),
so a large $C_{\mathrm A}$, and an excessive dissipation, would be needed. Domaradzki
judges the dynamic procedure unsuited to the method: it chooses a model
first and fits its coefficient, so its subgrid transfer depends on the
model chosen for the same velocity field (§3.3).

## A posteriori results

Tests use a de-aliased pseudo-spectral code (Rogallo) in a $2\pi$-periodic
box, which the author states makes numerical dissipation negligible, so the
observed effects are those of the model (§3.3; see
[numerical dissipation](/properties/numerical-dissipation.md)).

- **Forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)**
  at nominal $Re_\lambda>10^4$ ($\nu=2.5\times10^{-7}$), $64^3$, Gaussian
  filter, $k^{-5/3}$ initial spectrum, about 10 large-eddy turnover times:
  late-time slopes agree with $-5/3$ and the compensated Kolmogorov
  function stays between 1.4 and 2.1 outside the forcing band, with minor
  departures near $k_c$ (§3.1, Fig. 1). Halving the resolution to $32^3$
  causes "no visible deterioration" (Fig. 2a); the box filter slightly
  over-damps the highest wavenumbers (Fig. 2b); a pulse initial spectrum
  settles at a higher energy level with nearly the same Kolmogorov function
  (Fig. 3). The method assumes neither the inertial-range exponent nor the
  Kolmogorov constant: both are predictions (§3.1, §3.3).
- **Decaying grid turbulence of Comte-Bellot & Corrsin** ($64^3$,
  $k_c=30$): under-resolved DNS without a model fails, while the autonomous
  LES follows the measured spectra over $U_0t/M\in[42,98]$ and $[98,171]$
  (Figs. 4b, 5). At $U_0t/M=171$ it gives $u_{\mathrm{rms}}=0.865$ (experiment 0.895),
  $\varepsilon=1.73$ (1.74), $\lambda=0.099$ (0.102), $L=0.48$ (0.490),
  $Re_\lambda=57.2$ (60.7) (Table 2).
- **Correlation and backscatter.** The planar correlation between the
  subgrid transfer of the eddy-viscosity model and that of the similarity
  stress is 0.81 (above 0.8 in 3-D), against "around 0.4" quoted for the
  standard Smagorinsky model (§3.1, Fig. 6). The derived viscosity has
  negative regions, local [backscatter](/definitions/energy-backscatter.md),
  yet no run showed "any hints of instability"; the forward transfer
  exceeded backscatter by at least an order of magnitude, which the author
  suspects explains the stability (§3.1).
- **The $C_{\mathrm A}=0.8$ variant** keeps the $-5/3$ range but its Kolmogorov
  function rises steeply near $k_c$, consistent with too little subgrid
  dissipation there; against Comte-Bellot–Corrsin it dissipates less near
  the cutoff than the spectral method (§3.2, Figs. 7–9). Compared with
  three spectral eddy viscosities it practically overlaps a
  $k$-independent one: in practice a time-dependent, spatially near-uniform
  viscosity (§3.3, Fig. 10).

## Qualifications

- The physical-space method is not universal: it must depend on filter
  type and width, unlike the sharp-spectral method whose constants follow
  from LES data and analytical theory (§4).
- Evidence is limited to isotropic turbulence at $32^3$ and $64^3$;
  channel flow up to $Re_\tau=2000$ is announced for future work (§3.3).
- Domaradzki prints a Taylor microscale in Table 1 (and in the first LES
  row of Table 2) that deviates by up to about 6% (7%) from the paper's own
  definition $\lambda=(15u_{\mathrm{rms}}^2\nu/\varepsilon)^{1/2}$ evaluated on the
  tabulated values, while the printed $Re_\lambda=u_{\mathrm{rms}}\lambda/\nu$
  is consistent with the printed $\lambda$ *(compiler check, not in the
  sources)*.

# Citations

- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §2.2, Eqs. (2.24)–(2.27); §2.3, Eqs. (2.28)–(2.41); §2.4, Eqs. (2.42)–(2.47); §3.1, Figs. 1–6, Tables 1–2; §3.2, Eq. (3.3), Figs. 7–9; §3.3, Eqs. (3.4)–(3.7), Fig. 10; §4.
