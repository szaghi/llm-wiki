---
type: Property
title: "Stationary contact preservation"
description: "A scheme preserves stationary contacts when an isolated discontinuity of a linearly degenerate field with zero speed stays exactly on the mesh; Balsara et al. obtain it in FD-WENO through HLLI anti-diffusion, Renac in multicomponent DGSEM through contact-resolving fluxes, Lax–Friedrichs-type FD-WENO and central-upwind schemes lack it, and for moving interfaces the weaker interface equilibrium condition applies."
status: established
aliases: [exact capture of stationary contact discontinuities, preservation of stationary linearly degenerate discontinuities, stationary discontinuity preservation]
tags: [riemann-solver, finite-difference, well-balanced, multiphase, dg]
timestamp: 2026-10-23T10:00:00Z
---

# Stationary contact preservation

A discretization **preserves stationary contacts** if initial data consisting of an isolated
jump in a linearly degenerate field whose wave speed is zero — a stationary contact or, in
systems with non-conservative products, any stationary linearly degenerate wave — remain
exactly unchanged on the mesh for all time, up to round-off. The property is stated in these
terms by [Balsara et al. (2024)](/sources/balsara-2024.md) (§III, §IV), who require it for
"any wave family".

## Why it matters

Balsara et al. (§III) argue that in systems with non-conservative products these products
usually couple to linearly degenerate fields, whose waves do not self-steepen; with a
"plain-vanilla" scheme such waves "diffuse ever so slowly even when a very high order scheme
is used". With discontinuous bathymetry in a shallow-water-type model, a scheme that does not
preserve isolated stationary contacts "might never achieve steady state"; preserving them is
stated to be crucial for the lake-at-rest property and for well-balanced schemes, as several
works they cite also stress ([well-balancing](/properties/well-balancing.md)).

## Which schemes have it

- **Lax–Friedrichs-type FD-WENO: no.** The high-order upwind FD scheme with
  $A^\pm=\tfrac12(A\pm aI)$, equivalent to Lax–Friedrichs FD-WENO for linear fluxes, "will not
  preserve a stationary contact discontinuity exactly", nor will its naive nonlinear upgrade
  (Balsara et al., §II, Eqs. (2.3), (2.6)). The isotropic dissipation $a\,[\![u]\!]$ acts on
  every field regardless of its speed ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).
- **HLL with anti-diffusion: yes.** The single-state [HLL](/methods/hll-riemann-solvers.md)
  solver does not resolve intermediate waves; the anti-diffusive term of Dumbser & Balsara
  (2016), restricted to linearly degenerate fields and giving the most anti-diffusion to
  stationary waves, "will exactly preserve a stationary discontinuity in any wave family"
  and is conservative (§III, Eqs. (3.7)–(3.9)). Inside the
  [fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md) it gives the property at
  every order (§IV).
- **Central-upwind schemes: improved, not exact.**
  [Chertock et al. (2023)](/sources/chertock-2023.md) test a stationary contact with a
  travelling shock and rarefaction, $(\rho,v,p)=(1,-19.59745,1000)$ for $x<0.8$ and
  $(1,-19.59745,0.01)$ otherwise on $[-1,1]$, $t=0.03$, $\Delta x=1/100$ (Ex. 3). Both the
  original and the [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md) are
  non-oscillatory and the LCD scheme resolves the contact better, but neither is claimed to
  keep it exact. *(compiler check, not in the sources: for a constant-coefficient linear
  system the LCD scheme is exactly upwind (Lemma 3.1), and the upwind flux carries no
  contribution of a field with zero eigenvalue, so a stationary jump of that field stays
  fixed in the linear case.)*
- **Entropy-stable DGSEM with contact-resolving fluxes: yes, for material interfaces.**
  [Renac (2021)](/sources/renac-2021.md) proves exact preservation of stationary material
  interfaces in his [DGSEM](/methods/dgsem.md) for the
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
  (Theorem 6.1, proof p. 16). Take nodal states that differ in mass fractions and density,
  with $v=0$ and the same pressure $p$ everywhere. Both his entropy-conservative volume flux
  and his relaxation surface flux then reduce to $(0,0,p\,n,0)$, the pure pressure flux,
  so the nodal residuals vanish and the data stay fixed at the interpolation points. If the
  interface lies on a mesh interface, the relaxation solver returns the exact solution.
  The relaxation solver is an HLLC-like three-wave solver with a contact wave
  ([HLL-family solvers](/methods/hll-riemann-solvers.md)), which is why, unlike an
  isotropic Lax–Friedrichs dissipation, it adds nothing at a stationary contact
  *(compiler check, not in the sources: Renac shows the reduction, not this comparison)*.

## Evidence

On Balsara et al.'s tests (§VIII):

- Debris-flow Riemann problem 1 (three superposed stationary jumps in linearly degenerate
  fields, plus two shear waves): "exactly preserved on the mesh at all orders", HLL and
  Lax–Friedrichs-limit results identical, $x$-velocity fluctuations below $1.4\times10^{-14}$
  (§VIII.a, Fig. 2).
- Two-layer shallow-water Riemann problem 1: the stationary intermediate-field jumps are
  preserved, higher orders and the Lax–Friedrichs limit identical (§VIII.c, Fig. 7).
- Abgrall test for Baer–Nunziato (uniform $p$ and $v$ across a volume-fraction jump):
  pressure deviation below $9\times10^{-13}$, velocities below $2\times10^{-13}$, HLL and
  Lax–Friedrichs profiles "entirely comparable" thanks to the anti-diffusion (§VIII.b,
  Fig. 5).

Renac's tests (§7.2, Fig. 4; $N=3$, 100 cells, $t=0.08$, two gases with
$\gamma_1=1.6$, $\gamma_2=1.4$): the stationary interface (mass fraction 1 to 0, density 1
to 0.1, $v=0$, $p=1$) is resolved exactly. The same interface moving at $v=1$ produces
spurious pressure and velocity oscillations, which Renac calls inherent to discretely
conservative schemes, after Abgrall and Abgrall–Karni.

## Moving contacts: interface equilibrium and resolution

For a contact or material interface in motion the analogous requirement is weaker: velocity
and pressure, uniform across it, must stay uniform, while the jump itself is transported and
smeared. [Jain & Moin (2022)](/sources/jain-2022.md) (§3.3, after Abgrall 1996) call this the
**interface equilibrium condition**: a scheme satisfies it if $v=v_0$ and $p=p_0$ at every
point at step $k$ imply the same at step $k+1$. For their second-order central
finite-volume discretization of the five-equation model with a conservative diffuse-interface
regularization, Lemma 3.1 (proof App. B, stiffened-gas phases) states that it holds when the
internal-energy face flux uses the same split form as the mass flux (and the volume-fraction
flux), and the regularization enthalpy flux the same as the regularization mass flux
([split convective forms](/methods/split-convective-forms.md),
[five-equation model](/definitions/five-equation-model.md)). The two split forms of the
internal-energy flux that violate it (cubic, and cubic in enthalpy) cause "spurious mixing of
internal energy at the interface" and diverge in the two-phase Taylor–Green vortex at density
ratio 10, while all three are stable in single phase (§4.1, Figs. 4–5). Their stationary-slab
test ($u=v=0$, $p=1$, density ratio 1000, $64^2$, to $t=10$) shows the regularization's
entropy production instead: small positive relative changes of the two phase entropies,
plotted on axes scaled by $10^{-7}$ and $10^{-8}$, for interface widths off the equilibrium one
(App. A, Fig. 12).

Sharpness of a moving contact is a matter of the flux's dissipation on the contact field.
[Hu et al. (2022)](/sources/hu-2022.md) (§5.1, Eq. (5.1), Fig. 5.1) advect an isolated contact,
$(\rho,v,p)=(1.4,0.1,1)$ to $(1,0.1,1)$, over 100 cells at CFL 0.9 to $t=2$: their RHLLEM-LD, which keeps the HLLEM
anti-diffusion on the contact field and selects a THINC density in the dissipation term,
captures "a sharper contact discontinuity than the HLLE and HLLEM solvers"; on a 2D
interface-only problem (a density disc advected diagonally, $100\times100$) it gives "a
significant improvement" over both (§5.4; [HLL-family solvers](/methods/hll-riemann-solvers.md)).

## Qualifications

- Stationary and moving interfaces behave differently in Renac (2021). The property is
  exact at rest and lost in motion, so it does not imply pressure-equilibrium preservation
  for moving material interfaces. Renac accepts the oscillations to keep species mass
  conservation, and notes that quasi-conservative alternatives remove them at the cost of
  conservation (§1.2).
- **A moving interface kept in equilibrium.** [Nguyen et al. (2022)](/sources/nguyen-2022.md)
  advect a water–air interface at uniform $v=150$ m/s, $p=101325$ Pa, $T=293.15$ K in their
  $N$-phase model with velocity, pressure and temperature equilibrium (one mass equation per
  phase, mixture momentum and energy; stiffened-gas phases in $(p,T)$ form) and report
  velocity, pressure and temperature errors at the interface "on the order of $10^{-14}$",
  with the interface about three cells thick under compressive limiters (§3.1, Fig. 1). The
  scheme reconstructs the primitive variables $(p,v,T,\phi_2,\dots,\phi_N)$ with MUSCL and
  advances them through $[\partial u/\partial w]^{-1}$ of the conservative-to-primitive Jacobian
  (Eqs. (7), (26)–(30); page-local primitive vector $w$), while the paper states that the
  model "is always mass conservative for each phase". No conservation error is reported.
  *(compiler check, not in the sources: for the printed update
  $w^{n+1}=w^n-\Delta t\,[\partial u/\partial w]^{-1}\nabla\cdot f$ (Eq. (29), sign restored),
  $u(w^{n+1})-u(w^n)=-\Delta t\,\nabla\cdot f+O(\Delta t^2)$, and the $O(\Delta t^2)$
  remainder, from the curvature of $u(w)$ (e.g. $\phi_1\rho_1(p,T)$), is not a flux
  difference, so the cell sums of $u$ are not conserved to round-off unless the scheme
  recovers $u$ in some way the paper does not describe. The result therefore does not clearly
  test the statement, recalled by Renac, that discretely conservative schemes oscillate at
  moving material interfaces; see [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md).)*
- In the Baer–Nunziato Riemann problems 1–6 the anti-diffusion is switched off for lack of a
  good flattener (§VIII.b), so the property is not used there.
- The anti-diffusion needs the eigenvectors of the linearly degenerate fields only; for
  Pitman–Le debris flow these are analytic while the genuinely nonlinear ones are not
  (§III, §VII.c).

# Citations

- [Balsara et al. (2024)](/sources/balsara-2024.md) — §II (Eqs. (2.3), (2.6)), §III (Eqs. (3.7)–(3.9)), §IV, §VIII.a–c (Figs. 2, 5, 7) (accepted manuscript).
- [Chertock et al. (2023)](/sources/chertock-2023.md) — Ex. 3 (Fig. 5.3), Lemma 3.1 (arXiv v2).
- [Renac (2021)](/sources/renac-2021.md) — §1.2, Theorem 6.1 (proof p. 16), §7.2 Fig. 4 (RP4, RP5) (arXiv v3).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.1 (Eqs. (2), (7)), §2.3 (Eqs. (26)–(30)), §3.1 (Fig. 1).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §3.3 (Lemma 3.1), §4.1 (Figs. 4–5), Apps. A–B.
- [Hu et al. (2022)](/sources/hu-2022.md) — §5.1 (Eq. (5.1), Fig. 5.1), §5.4.
