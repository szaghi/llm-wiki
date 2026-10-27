---
type: Property
title: "Dynamic alignment and intermittency in MHD turbulence"
description: "Dynamic alignment is the scale-dependent alignment of Elsasser increments that weakens the MHD nonlinearity and gives a k_perp^-3/2 spectrum; Schekochihin (2022) recasts it, to respect the RMHD rescaling symmetry, as an intermittency effect with sin(theta) ~ (lambda/lambda_CB)^(1/4)."
status: hypothesis
aliases: [Boldyrev alignment, scale-dependent alignment, aligned MHD turbulence, refined critical balance, three-dimensional anisotropy]
tags: [mhd, astrophysics, plasma, intermittency, anisotropy]
timestamp: 2026-10-27T15:48:00Z
---

# Dynamic alignment and intermittency in MHD turbulence

**Dynamic alignment** is the tendency of the Elsasser increments
$\delta\boldsymbol Z^+_\lambda$ and $\delta\boldsymbol Z^-_\lambda$ of
[reduced MHD](/definitions/reduced-mhd.md) to align with each other by an
angle $\theta_\lambda$ that shrinks as the perpendicular scale $\lambda$
decreases. Aligned fluctuations are sheet-like, with three scales
$l_\parallel\gg\xi\gg\lambda$ (along the local field, along the fluctuation,
and across both), and their nonlinear interaction is weakened by
$\sin\theta_\lambda$. [Schekochihin
(2022)](/sources/schekochihin-2022.md) (§6) credits the idea to Boldyrev (2006);
the review accepts Beresnyak's objection to its original form and replaces it
with an intermittency-based version (§6.4, after Mallet & Schekochihin 2017).
The page carries `status: hypothesis`: the review itself ranks alignment as
"hotly debated" (§8.2), in contrast to [critical
balance](/properties/critical-balance.md).

## Alignment weakens the nonlinearity

Following Schekochihin (2022, §6.1), the nonlinear term is estimated as
$\boldsymbol Z^\mp_\perp\cdot\nabla_\perp\boldsymbol Z^\pm_\perp\sim\delta Z^+_\lambda\delta Z^-_\lambda/\xi$
(Eq. 6.1), the gradient being taken along the advecting field. The identity

$$\boldsymbol Z^+_\perp\cdot\nabla_\perp\boldsymbol Z^-_\perp-\boldsymbol Z^-_\perp\cdot\nabla_\perp\boldsymbol Z^+_\perp=\nabla_\perp\times(\boldsymbol Z^+_\perp\times\boldsymbol Z^-_\perp)\sim\frac{\delta Z^+_\lambda\,\delta Z^-_\lambda\sin\theta_\lambda}{\lambda}$$

(Eq. 6.2) then gives $\lambda/\xi\sim\sin\theta_\lambda$ (Eq. 6.3) and the
nonlinear time

$$\tau^\pm_{\mathrm{nl}}\sim\frac{\xi}{\delta Z^\mp_\lambda}\sim\frac{\lambda}{\delta Z^\mp_\lambda\sin\theta_\lambda}$$

(Eq. 6.4). The review measures alignment between **Elsasser** increments, not
between $\delta\boldsymbol u$ and $\delta\boldsymbol b$ (App. B; see the
alignment diagnostics on [reduced MHD](/definitions/reduced-mhd.md)), and
attributes the mechanism to mutual shearing of the two Elsasser fields
(citing Chandran et al. 2015). It also notes (footnote 17, citing
Bowen et al. 2021) that alignment does not by itself imply $\lambda/\xi$
small.

## Boldyrev's theory and the symmetry objection

Boldyrev's conjecture, as the review states it (Eq. 6.5), is an "uncertainty principle"
$\sin\theta_\lambda\sim\delta b_\lambda/v_A$. With constant flux and
[critical balance](/properties/critical-balance.md) it gives

$$E(k_\perp)\sim(\varepsilon v_A)^{1/2}k_\perp^{-3/2},\qquad l_\parallel\sim v_A\varepsilon^{-1/2}\lambda^{1/2}$$

(Eqs. 6.8–6.9), and a dissipation cutoff
$\lambda_{\mathrm d}^{\mathrm B}\sim\eta_m^{2/3}(v_A/\varepsilon)^{1/3}$
(Eq. 6.10; page-local symbol, the "Boldyrev cutoff"), against the
Goldreich–Sridhar cutoff $\sim\eta_m^{3/4}\varepsilon^{-1/4}$ (Eq. 6.11). The
$-3/2$ exponent coincides with Iroshnikov–Kraichnan's, which the review
describes as IK being right "in a different sense".

The objection, credited to Beresnyak (2011, 2012), is that this scaling
violates the [RMHD rescaling symmetry](/definitions/reduced-mhd.md): under
amplitude factor $c$ and length factor $a$, $\delta Z_\lambda\to c\,\delta Z_\lambda$,
$\varepsilon\to(c^3/a)\varepsilon$, $v_A\to v_A$, $\lambda\to a\lambda$
(Eq. 6.12), the law $\delta Z_\lambda\sim(\varepsilon v_A\lambda)^{1/4}$
would transform into $c^{3/4}$ times itself, a contradiction (§6.3).
Equivalently, $\sin\theta_\lambda\sim\delta b_\lambda/v_A$ makes the angle
formally infinitesimal in the RMHD ordering, which would linearize the
system, and $l_\parallel$ in Eq. 6.9 does not contain $v_A$ only through
$l_\parallel/v_A$. With $\varepsilon$, $v_A$ and $\lambda$ as the only
parameters, the Goldreich–Sridhar scaling is the unique admissible one
(§6.4.1).

## The RMHD-consistent revision

Schekochihin (2022, §6.4.1) keeps alignment by letting the parallel outer
scale $L_\parallel$ enter the inertial-range scalings. With a free
intermittency exponent $q$ (page-local; the source writes $\delta$),
dimensional analysis and the symmetry give

$$\delta Z_\lambda\sim\varepsilon^{(1+q)/3}\left(\frac{L_\parallel}{v_A}\right)^{q}\lambda^{(1-2q)/3}$$

(Eq. 6.14), with a companion form for $l_\parallel$ (Eq. 6.15). Combining
critical balance with the [parallel
cascade](/properties/critical-balance.md) fixes the exponent of
$L_\parallel$ in $l_\parallel$ at $2q$ (Eq. 6.17) and gives
$\sin\theta_\lambda\sim(\lambda/\lambda_{CB})^{2q}$ (Eq. 6.18), where
$\lambda_{CB}$ is the critical-balance scale and the perpendicular outer
scale satisfies $L_\perp\sim\lambda_{CB}$ (Eq. 6.16). Boldyrev's
$\lambda$-scalings are recovered with $q=1/8$ (Eq. 6.19), so (Eqs. 6.20–6.22)

$$\delta Z_\lambda\sim\left(\frac{\varepsilon L_\parallel}{v_A}\right)^{1/2}\left(\frac{\lambda}{\lambda_{CB}}\right)^{1/4},\qquad\frac{l_\parallel}{L_\parallel}\sim\left(\frac{\lambda}{\lambda_{CB}}\right)^{1/2},\qquad\sin\theta_\lambda\sim\left(\frac{\lambda}{\lambda_{CB}}\right)^{1/4},$$

equivalently $E(k_\perp)\sim\varepsilon^{2/3}\lambda_{CB}^{1/6}k_\perp^{-3/2}$
(Eq. 6.25), the form the review cites as used by Perez et al. (2012, 2014). The
dissipation cutoff becomes
$\lambda_{\mathrm d}^{\mathrm B}/\lambda_{CB}\sim Re_{\mathrm{eff}}^{-2/3}$
(Eq. 6.24) with the effective Reynolds number (page-local)
$Re_{\mathrm{eff}}=\delta Z_{\lambda_{CB}}\lambda_{CB}/(\nu+\eta_m)$, equal
to $Rm/(1+Pm)$, where $Rm=\delta Z_{\lambda_{CB}}\lambda_{CB}/\eta_m\sim(\varepsilon/\eta_m)(L_\parallel/v_A)^2$
is based on $\lambda_{CB}$ (Eq. 6.23). The value $q=-1/4$ reproduces the
weak-turbulence spectrum (footnote 22).

The fluctuation-direction scale is
$\xi\sim\lambda_{CB}^{1/4}\lambda^{3/4}$, along which the scaling is always
Kolmogorov, $\delta Z_\xi\sim(\varepsilon\xi)^{1/3}$ (Eq. 6.31); $\xi$ is
also the field-line wandering distance, $\xi\sim l_\parallel\delta b_\lambda/v_A$
(Eq. 6.32). The resulting **three-dimensional anisotropy** has Elsasser
spectra with exponents $-2$ along $l_\parallel$, $-3/2$ along $\lambda$ and
$-5/3$ along $\xi$ (§6.5), reported as measured in simulations by Mallet et
al. (2016) and in the solar wind by Verdini et al. (2018) (Figs. 12–13).

## Alignment as intermittency

The value $q=1/8$ is derived from an intermittency model, "vulgarised" in
the review from Mallet & Schekochihin (2017) (§6.4.2). The ingredients
(conjectures of the model):

1. **Refined critical balance.** The ratio
   $\chi=\delta Z\,l_\parallel/(\xi v_A)\sim\tau_A/\tau_{\mathrm{nl}}$, with
   the alignment angle included in $\tau_{\mathrm{nl}}$, has a scale-invariant
   probability distribution (Eq. 6.28). The review cites Mallet et al. (2015)
   for a $1024^3$ RMHD simulation in which seventeen PDFs of $\chi^+$ collapse
   over about a decade of scales "to truly remarkable accuracy", while the
   collapse fails without the angle (Fig. 6).
2. **The most intense structures are sheets**, with filling fraction
   $\propto\lambda$ in the perpendicular plane and $\propto\xi l_\parallel$ in
   the sheet plane (Eqs. 6.26–6.27).
3. **The most intense structures have scale-independent amplitude**, which
   with refined critical balance gives $\xi\propto l_\parallel$ and a filling
   fraction $\propto l_\parallel^2$ (Eq. 6.29); this is consistent with the
   most intense dissipative structures that the review cites from Zhdankin
   et al. (2016).

Equating the two expressions of the filling fraction gives
$l_\parallel\propto\lambda^{1/2}$, hence the exponent $1/4$ of $L_\parallel$
in $l_\parallel$ and $q=1/8$ (Eq. 6.30). The full Mallet–Schekochihin theory
predicts structure functions of all orders from log-Poisson statistics (footnote 26
cites She & Leveque 1994 and Dubrulle 1994). The review
quotes Chandran et al. (2015) for $q\approx0.108$, i.e.
$\delta Z_\lambda\propto\lambda^{0.26}$, and notes that the magnetic field is
more intermittent than the Elsasser fields and those more than the velocity,
which it leaves unexplained (§6.4.2, Fig. 13).

In the review's account (§6.4.2), the aligned scalings are no longer a property
of every fluctuation (which the symmetry forbids) but a statistical property
of an intermittent ensemble in which $L_\parallel$ appears through the
filling fraction of the most intense structures.

## Limits of the aligned range

Alignment cannot continue indefinitely: the aligned sheets become unstable to
tearing below a disruption scale $\propto Rm^{-4/7}$, which ends the $-3/2$
range and restores a Kolmogorov-scaled cutoff — see [tearing-mediated MHD
turbulence](/results/tearing-mediated-mhd-turbulence.md). The review adds
that if an ideal instability (for instance Kelvin–Helmholtz) limited
alignment instead, the Goldreich–Sridhar scaling would return (§8.2). In
strongly imbalanced simulations the alignment angle is reported to scale as
$\lambda^{0.1}$ ($\lambda^{0.2\text{–}0.25}$ with rms definitions) (§9.2),
and Elsasser alignment is tied to the residual energy (§10.4; see [critical
balance](/properties/critical-balance.md)). Stochastic reconnection does not
destroy alignment in the review's analysis: shear inside an aligned layer
limits internal eddies to $\xi'/\lambda\sim(\lambda/\lambda_{CB})^{1/8}$
($\xi'$ page-local) and the reconnecting layer width comes out $\sim\lambda$
(§8.3.3, App. D.7.4, Eqs. D115–D116), against the view it cites from Lazarian
et al. (2020) that turbulent resistivity prevents alignment.

## Qualifications

- **Disputed asymptotics.** The review records a long dispute it does not
  settle by fiat: Beresnyak (2011–2019, as the review cites) argues from simulations
  rescaled to the Kolmogorov dissipation scale (best convergence
  $k_\perp^{-1.7}$, Beresnyak 2014, Fig. 10b) for an asymptotic $-5/3$, while
  Perez et al. (2012, 2014) report $-3/2$ (Fig. 10a). The review's synthesis
  is that "both are right, in a sense": an aligned $-3/2$ inertial range and a
  Kolmogorov cutoff produced by tearing (§1, §7.2.2). Both sides are
  un-ingested works cited by the review, so no bundle contradiction is
  opened here.
- Solar-wind conditional structure functions that the review cites from
  Wicks et al. (2013) give a Goldreich–Sridhar-like $-5/3$ for a balanced sub-population and
  $-3/2$ for imbalanced or aligned intervals (Fig. 16).
- The cited simulations use Laplacian viscosity or hyperviscosity; the
  $1024^3$ runs of Mallet et al. (2015, 2016) use hyperviscosity.

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §6 (Eqs. 6.1–6.32), §6.3, §6.4.1, §6.4.2, §6.5; §7.2.2; §8.2, §8.3.3; §9.2; §10.4; App. B; App. D.7.4 (Eqs. D115–D116); footnotes 17, 22, 26.
