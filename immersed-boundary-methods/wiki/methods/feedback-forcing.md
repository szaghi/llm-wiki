---
type: Method
title: "Feedback forcing"
description: "Continuous-forcing immersed boundary method that drives the fluid velocity at boundary points to the prescribed boundary velocity with a proportional–integral controller; a damped-oscillator interpretation fixes the gains, which make the equations stiff and limit the time step."
status: established
aliases: [virtual boundary method, Goldstein forcing, proportional-integral forcing, two-mode controller forcing]
tags: [immersed-boundary, continuous-forcing, stiffness, diffuse-interface, spectral]
timestamp: 2026-11-08T18:08:00Z
---

# Feedback forcing

[Goldstein et al. (1993)](/sources/goldstein-1993.md) prescribe the location
of the boundary points $\mathbf X_\ell$ instead of the forces between them,
and let the force at each point adapt to the local flow:

$$\mathbf f(\mathbf X_\ell,t)=\alpha_f\int_0^t\big(\mathbf u(\mathbf X_\ell,t')-\mathbf u_\Gamma\big)\,dt'+\beta_f\big(\mathbf u(\mathbf X_\ell,t)-\mathbf u_\Gamma\big),\qquad \alpha_f,\beta_f<0 .$$

In control terms this is a two-mode (proportional–integral) controller. The
integral term alone brings the flow to rest on $\Gamma$; the proportional term
is the Stokes drag of an unresolved obstacle at $\mathbf X_\ell$. Keeping
only $\partial_t\mathbf u=\mathbf f/\rho$ shows a damped harmonic oscillator of natural
frequency $(2\pi)^{-1}\sqrt{|\alpha_f|}$ and damping ratio
$-\beta_f/(2\sqrt{|\alpha_f|})$ (per unit density): the integral term tethers a
small fluid volume to $\mathbf X_\ell$ by an elastic string. The natural frequency
must exceed the energetic frequencies of the flow for the force to track it.

## Stiffness and time step

With an explicit (Adams–Bashforth) treatment the stability limit is
$\Delta t<\big(-\beta_f-\sqrt{\beta_f^2-2\alpha_f k}\big)/\alpha_f$, $k$ a
problem-dependent constant of order one (Goldstein et al. 1993;
[Fadlun et al. 2000](/sources/fadlun-2000.md), §2.1). Goldstein et al. ran
the start-up cylinder at CFL $O(10^{-3}$–$10^{-2})$; in the turbulent-channel
case the time step was "only limited by the Courant condition" for moderate
gains ($\alpha_f=-200$, $\beta_f=-1.5$). Fadlun et al. (2000, §2.1) make the
proportional term implicit and reach CFL $0.025$–$0.1$ (up to $0.5$ for smooth
geometries), but sharp corners force large gains, and the gains are flow
dependent with no general rule. [Kim et al. (2001)](/sources/kim-2001.md),
§1, add that feedback forcing induces spurious oscillations.

## In a spectral code

Point forces on grid points produce global Gibbs-type spatial oscillations in
a Fourier–Chebyshev pseudo-spectral method. Goldstein et al. (1993) counter
them by spreading each force with a narrow Gaussian over a few points (not in
the Chebyshev direction), by mild spectral smoothing of
$\mathbf u\times\boldsymbol\omega+\mathbf f$, and by a "back force" that drives a flow
inside the body to remove kinks in the velocity profile.

## Results reported

Impulsively started cylinder ($Re\approx550$, 576 surface points) whose
body forms within $O(10^2)$ steps; turbulent channel at $Re_\tau=125$ with one
wall replaced by a virtual plate, mean, rms and Reynolds-stress profiles
matching a no-slip simulation; riblet-covered wall with 21 triangular ribs
(Goldstein et al. 1993, examples).

## Relation to other methods

[Direct forcing](/methods/direct-forcing.md) removes the gains and the
stability penalty by solving the discrete momentum equation for the force
([Fadlun et al. 2000](/sources/fadlun-2000.md), §2.2). [Angot et al. (1999)](/sources/angot-1999.md),
§1, read the Peskin–Goldstein point forcing as a penalization of the surface
that must be extended to the volume of the body at high Reynolds numbers
([volume penalization](/methods/volume-penalization.md)).

## Later assessments

[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) view the spring model of
rigid bodies, $\mathbf F=-k_s(\mathbf X-\mathbf X_e)$ with an equilibrium position $\mathbf X_e$,
as a special case of feedback forcing and the latter, after Iaccarino and
Verzicco, as a damped oscillator: promising at low Reynolds numbers, but large
$\alpha_f$, $\beta_f$ bring stability problems in highly unsteady flows.
[Uhlmann (2005)](/sources/uhlmann-2005.md), §1, calls it the "virtual
boundary method": virtual springs and dampers whose stiffness and damping are
problem dependent and whose time scales must be resolved. Taira and Colonius
(2007, §4.1) quote CFL numbers of $O(10^{-3})$ to $O(10^{-1})$ for cylinders
with such forcing.

# Citations

- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — introduction, formulation, spectral implementation, examples (the OCR text carries no section numbers).
- [Angot et al. (1999)](/sources/angot-1999.md) — §1.
- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §1, §2.1, §2.4.
- [Kim et al. (2001)](/sources/kim-2001.md) — §1.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — continuous-forcing section (rigid boundaries).
- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §1.
- [Taira & Colonius (2007)](/sources/taira-2007.md) — §4.1.
