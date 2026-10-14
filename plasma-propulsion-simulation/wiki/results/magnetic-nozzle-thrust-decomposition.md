---
type: Result
title: "Thrust decomposition of a magnetic nozzle"
description: "The thrust of a magnetic-nozzle rf thruster splits into the source electron-pressure force on the back wall, the Lorentz force of the azimuthal electron-diamagnetic current on the nozzle field and the axial momentum lost to the radial wall, each measured separately and matched by integrals of measured electron-pressure profiles within 20-30%."
status: established
aliases: [F = F_s + F_B + F_w, magnetic nozzle thrust components, diamagnetic thrust]
tags: [magnetic-nozzle, helicon, fluid]
timestamp: 2026-10-14T00:00:00Z
---

# Thrust decomposition of a magnetic nozzle

[Takahashi (2019)](/sources/takahashi-2019.md), §4, Eqs. 8–23, derives,
after Takahashi et al. (2011b, 2012), the thrust of a
[magnetic nozzle](/definitions/magnetic-nozzle.md) rf thruster from a steady
axisymmetric two-fluid momentum balance with cold ions, inertialess
electrons, quasi-neutrality and the radial ion inertia neglected.

## Statement

The thrust is the axial momentum flux through a plasma cross section
(Eq. 8):
$$F=2\pi\int\left(p_e+m_in_iu_{i,z}^2\right)r\,dr .$$
It splits as $F=F_s+F_B+F_w$ (Eqs. 17–20), with
$$\begin{aligned}
F_s&=2\pi\int r\,p_e\,dr\quad\text{(over the source radius, at the axial position of maximum electron pressure)},\\
F_B&=-2\pi\iint r\,\frac{B_r}{B_z}\,\frac{\partial p_e}{\partial r}\,dr\,dz\quad\text{(over the plasma in the nozzle)},\\
F_w&=-2\pi\iint\frac{\partial}{\partial r}\left(r\,m_in_iu_{i,r}u_{i,z}\right)dr\,dz ,
\end{aligned}$$
where $u_{i,r}$, $u_{i,z}$ are the components of $\mathbf u_i$, and
$u_{i,z}=0$ is assumed where the electron pressure peaks. The reaction
forces act respectively on the source back wall, on the field coils or
magnets, and on the radial source wall. On the wall, $F_w$ reduces to
$-2\pi\int r\,m_in_iu_{i,r}u_{i,z}\,dz$ evaluated at the source radius
(Eq. 23).

$F_B$ is the Lorentz force between $B_r$ and the azimuthal
electron-diamagnetic current $B_z^{-1}\partial p_e/\partial r$: the radial
electron pressure is turned into axial momentum. The current sits at the
nozzle surface, where the radial density gradient is, by analogy with the
wall of a solid nozzle (Fig. 6a–b).

**1D reduction** (Fruchtman et al. 2012; Eqs. 21–22). With the product of
$B_z$ and the plasma cross-section area constant along the nozzle, and a
radially uniform field,
$F_B$ becomes an axial integral of the area-weighted mean electron pressure
times the logarithmic axial derivative of $B_z$. With measured parameters
it differs from the 2D integral by 15–25%, attributed to the
radially-uniform-field approximation (Fig. 6c). The isothermal, loss-free
version of it is the ideal-nozzle limit.

## Measurements

All are experiments reviewed by the author, mostly his own
([Takahashi (2019)](/sources/takahashi-2019.md), §5.5):

* **Source term alone.** The first direct thrust measurements (2011) gave a
  few mN at several hundred W, close to the maximum source electron
  pressure, so $F_s$ dominated; an ICP thruster with no magnetic field
  confirms it. Consistent with Fruchtman (2006), ambipolar and double-layer
  fields impart no significant net momentum (§5.5.1).
* **Nozzle term.** Mounting only the solenoids on the balance measured $F_B$
  alone (solenoid displacement about 10 µm). In the mode without a double
  layer, $F_B$ is about half of the total and the nozzle density an order of
  magnitude higher than in the mode with one. $F_s$ and $F_B$ computed from
  measured 2D electron-pressure profiles, with $F_w$ set to zero, agree with
  the measured forces (up to about 6 mN, rf power up to about 800 W) within
  20–30% (§5.5.2, Figs. 12–13).
* **All three separately** (HPT-I, Fig. 14): with $B$ at the antenna kept
  below 0.02 T (printed as 200 G), $F_s$ stays constant, $F_w$ is negligible in argon, and $F_B$
  grows with $B$ towards the ideal-nozzle limit. With pulsed fields up to
  0.6 T (printed as 6 kG) the thrust saturates, which the review attributes to cross-field
  diffusion (§5.5.2).
* **Wall loss.** In Kr and Xe a non-negligible negative $F_w$ was measured,
  down to about $-6$ mN for Xe (read from Fig. 16), together with a rapid
  axial density decay from neutral depletion; PIC with artificially
  depleted neutrals confirmed it (Takao & Takahashi 2015) (§5.5.3). The
  review lists models that neglect $F_w$ (Fruchtman 2006, 2008; Ahedo &
  Merino 2010; Ahedo & Navarro-Cavallé 2013; Lafleur 2014), none ingested
  in this bundle.
* **Which azimuthal current.** The measured plasma-induced decrease of
  $B_z$ gives $j_\theta$ through Ampère's law (Eq. 25). It agrees with
  $j_\theta=B_z^{-1}\partial p_e/\partial r+e\,n_eE_r/B_z$ (Eq. 26, as
  printed) and is dominated by the diamagnetic (first) term over the
  $\mathbf E\times\mathbf B$ Hall (second) term, in HPT-I up to about
  $\pm1$ kA/m$^2$ (§5.5.2, Fig. 15). The review takes this as support for
  the diamagnetic models against the conclusion of Ahedo & Merino (2010)
  that the main nozzle force comes from the electron Hall current.

## Limits

The model neglects radial ion inertia, and the cancellation of the electron
Hall current by the ion $\mathbf E\times\mathbf B$ drift assumes magnetized
ions; Ahedo & Merino (2010) keep the ion inertia
([Takahashi (2019)](/sources/takahashi-2019.md), §5.5.2). The integrals are
evaluated with measured, not computed, electron-pressure profiles.

# Citations

1. [Takahashi (2019)](/sources/takahashi-2019.md), §4, Eqs. 8–23, §5.5, Figs. 6, 12–16.
