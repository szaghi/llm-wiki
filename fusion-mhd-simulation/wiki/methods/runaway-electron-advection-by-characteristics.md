---
type: Method
title: "Runaway-electron advection by the method of characteristics"
description: "Semi-Lagrangian solution of the runaway-electron continuity equation in M3D-C1: the convective part is rewritten exactly as advection of the runaway density divided by the field strength, massless pseudo-particles at every quadrature point are traced backwards along the parallel-streaming plus E×B velocity by a massless-limit Boris integrator, and the pulled-back values are L2-projected onto the finite-element basis, removing the CFL and matrix-conditioning limits of an implicit Galerkin solve."
status: established
aliases: [method of characteristics for runaway electrons, semi-Lagrangian RE advection, pseudo-particle RE advection, modified Boris algorithm]
tags: [runaway-electrons, numerics, time-integration, particles, finite-elements, gpu, code]
timestamp: 2026-10-16T20:00:00Z
---

# Runaway-electron advection by the method of characteristics

In a [runaway-electron fluid model](/methods/runaway-electron-fluid-model.md)
the runaway density $n_{\mathrm{RE}}$ streams along $\mathbf b$ at a speed
close to $c$, far above the Alfvén speed. [Liu et al. (2021)](/sources/liu-2021.md)
replace the θ-implicit Galerkin solve of the runaway continuity equation in
[M3D-C1](/software/m3d-c1.md) by a semi-Lagrangian scheme: the equation is
rewritten as a pure advection with a slow source, its characteristics are
traced backwards from every quadrature point, and the values found are
projected back onto the finite-element space (§3, §4, App. A).

## Why an implicit Galerkin solve fails

The runaway continuity equation of the M3D-C1 model is
$$\partial_tn_{\mathrm{RE}}+\nabla\cdot\big[n_{\mathrm{RE}}\big(c_{\mathrm{RE}}\mathbf b+\mathbf v_E\big)\big]=S_{\mathrm{RE}},\qquad \mathbf v_E=\frac{\mathbf E\times\mathbf B}{B^2},$$
with $c_{\mathrm{RE}}\le c$ a numerical convection speed and $S_{\mathrm{RE}}$
the runaway sources (Eq. 3; $S_{\mathrm{RE}}$ is a page-local symbol). Solved with GMRES and a block-Jacobi preconditioner whose
blocks are the toroidal planes, the system becomes ill-conditioned when
$c_{\mathrm{RE}}\gg v_A$. The toroidal derivative $\partial_\phi n_{\mathrm{RE}}$
then sits in off-diagonal blocks that "can dominate the matrix" at Alfvénic
time steps (§3, pp. 6–7). The earlier remedies were subcycling, a reduced
$c_{\mathrm{RE}}$ and artificial diffusion. Liu et al. call them costly or
say they "can possibly reduce the MHD mode growth or even suppress unstable
modes" (§3, p. 7). The paper states this suppression but does not demonstrate
it (see the Contradictions section of the
[fluid-model page](/methods/runaway-electron-fluid-model.md)).

## Advective form

Using $\nabla\cdot\mathbf B=0$, Faraday's law
($\mathbf b\cdot\nabla\times\mathbf E=-\partial_tB$) and
$\nabla\cdot(\mathbf E\times\mathbf b)=\mathbf b\cdot\nabla\times\mathbf E-\mathbf E\cdot\nabla\times\mathbf b$,
the convective part becomes an exact advection of $n_{\mathrm{RE}}/B$
(Eq. 11, App. A):
$$\frac{\partial}{\partial t}\Big(\frac{n_{\mathrm{RE}}}{B}\Big)+\big(c_{\mathrm{RE}}\mathbf b+\mathbf v_E\big)\cdot\nabla\Big(\frac{n_{\mathrm{RE}}}{B}\Big)=\frac{n_{\mathrm{RE}}}{B^2}\,\mathbf E\cdot(\nabla\times\mathbf b).$$
The paper calls this the "divergence-free form", although it is the
advective (non-conservative) form. The right-hand side acts on the resistive
time scale and is treated as an extra source (§3, p. 7). The reader of the
source rechecked App. A and found the algebra correct with $\mu_0=1$; the
compiler repeated the step from the conservative form, and the identity holds
for $S_{\mathrm{RE}}=0$.

## Algorithm

One MHD step $\Delta t$ proceeds as follows (§3, p. 8):

1. Place a pseudo-particle at every quadrature point $\mathbf x_m$ of every
   3D element (125 per element).
2. Integrate each characteristic backwards over $\Delta t$,
   $\mathrm d\mathbf x/\mathrm dt=c_{\mathrm{RE}}\mathbf b+\mathbf v_E$ (Eq. 12),
   with substeps $\Delta t_p<\Delta t$ and the fields frozen during the
   substeps. Subcycling is kept for orbit accuracy, not for stability.
3. Pull back $n_{\mathrm{RE}}/B$ from the foot of the characteristic.
4. Recover the finite-element coefficients by an $L^2$ projection,
   $\sum_k\big(\int\Lambda_j\Lambda_k\,dV\big)C_k=\sum_m\Lambda_j(\mathbf x_m)\,\frac{n_{\mathrm{RE}}}{B}(\mathbf x_m)\,J(\mathbf x_m)$
   with $J(\mathbf x_m)$ the quadrature weight times the Jacobian (Eq. 14;
   see [particle-to-mesh projection](/methods/particle-to-mesh-projection.md)).
5. Add the source.

Unlike particle-in-cell, $n_{\mathrm{RE}}$ stays a field: there is no marker
re-seeding and no particle noise. The scheme has no CFL limit and needs no
artificial diffusion (§3, p. 8). A characteristic whose foot leaves the mesh
sets $n_{\mathrm{RE}}=0$ at its origin. That is an absorbing boundary for the
runaways, and the mesh boundary counts as the wall for loss diagnostics
(pp. 15–16).

## Massless-limit ("modified") Boris integrator

The characteristics are traced with a Boris-type scheme in which the
$\mathbf E\times\mathbf B$ velocity is subtracted before the rotation and
restored after it (§4, Eqs. 15–18):
$$\mathbf x_p^{l+1}=\mathbf x_p^{l}+\mathbf v_p^{l+1/2}\Delta t_p,\qquad \mathbf v'^{\,l+1/2}=\mathbf v_p^{l+1/2}-\mathbf v_E^{l+1},\qquad \mathbf v_p^{l+3/2}=\mathbf v'^{\,l+3/2}+\mathbf v_E^{l+1}.$$
In the massless limit the Boris rotation degenerates to
$(\mathbf v'^{\,l+3/2}+\mathbf v'^{\,l+1/2})\times\mathbf B^{l+1}=0$ with
$|\mathbf v'^{\,l+3/2}|=|\mathbf v'^{\,l+1/2}|$ (Eq. 19). In the authors'
words, the field acts "like a reflection mirror" that reverses only the
component normal to it. Eq. 19 has two roots. The intended one is
$\mathbf v'^{\,l+3/2}=2(\mathbf v'^{\,l+1/2}\cdot\mathbf b^{l+1})\mathbf b^{l+1}-\mathbf v'^{\,l+1/2}$,
which keeps the parallel part and reverses the perpendicular part. The paper
does not mention excluding the trivial root
$\mathbf v'^{\,l+3/2}=-\mathbf v'^{\,l+1/2}$ (compiler's remark). As for the
slow-manifold Boris scheme, one RK4 step from $\mathbf x_p^0$ to
$\mathbf x_p^1$ starts the integrator on the slow manifold, and the substep
may exceed the electron gyro-period (§4; see
[particle pushers](/methods/particle-pushers.md)).

**Conservation test** (§4, Fig. 2). The test uses the static DIII-D 177040
field with $c_{\mathrm{RE}}=32v_A$, no source and $\mathbf J=\mathbf J_{\mathrm{RE}}$,
at equal cost: the Boris step is one quarter of the RK4 step. The total
runaway current should stay constant.

- RK4 drifts from about 0.75 to 0.90 MA in 0.2 ms.
- The modified Boris scheme stays at about 0.745 MA.
- For a single pseudo-particle the RK4 error in $\psi$ grows secularly to
  about $3\times10^{-4}$ of the reference flux in 0.65 μs, while the Boris
  error oscillates within about $\pm1.5\times10^{-4}$.

All values are read from the figure. The authors attribute the difference to
the structure-preserving property of the Boris scheme.

## Performance

The paper times one advance of the runaway equation over
$\Delta t=0.65\,\mu$s on Summit (§3, Fig. 1). The case has
$c_{\mathrm{RE}}=8v_A$, 16 planes of 6454 elements and
$\Delta t_p=\tau_A/32$.

- θ-implicit Galerkin on CPUs: 126 s.
- Characteristics on CPUs: 39 s, an algorithmic gain of about 3.2.
- Characteristics on GPUs: 3.8 s, about 33 times faster than the Galerkin
  baseline.

The CPU runs use 32 POWER9 CPUs and the GPU run 96 V100 GPUs, so the GPU
comparison is not like-for-like. The quoted 1 290 800 pseudo-particles is ten
times fewer than 16 × 6454 × 125 (recorded on the
[Source page](/sources/liu-2021.md)). No GPU programming model is named.

## Use

The scheme carries the nonlinear M3D-C1 simulations of the (2,1) resistive
kink that ends a DIII-D runaway plateau. In those runs more than 95% of the
runaways reach the wall within about 0.06 ms, and the loss fraction converges
only with at least 16 toroidal planes
([Liu et al. (2021)](/sources/liu-2021.md), §5.3; see
[runaway reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)).
Because it removes the CFL constraint, $c_{\mathrm{RE}}$ can be raised to
$8$–$32\,v_A$. The nonlinear saturation needs such values: at
$c_{\mathrm{RE}}/v_A=2$ the saturated $W_{\mathrm{mag}}^{(1)}$ is about twice
its value at 8 or 32 (Fig. 14b).

# Citations

- [Liu et al. (2021)](/sources/liu-2021.md): §3 and App. A (Eqs. 3, 10–14); §4 (Eqs. 15–19, Fig. 2); Fig. 1; §5.3 (Fig. 14).
