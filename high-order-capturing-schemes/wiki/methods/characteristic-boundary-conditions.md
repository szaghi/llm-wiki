---
type: Method
title: "Navier–Stokes characteristic boundary conditions"
description: "Poinsot–Lele NSCBC: at a boundary, the normal-derivative terms of the conservation equations are rewritten through characteristic wave-amplitude variations; outgoing ones come from one-sided interior differences, incoming ones from local one-dimensional inviscid (LODI) relations matched to the physical conditions, and the boundary values are advanced by the remaining equations with no extrapolation; a partially reflecting outflow relaxation removes the mean-pressure drift of perfectly non-reflecting conditions."
status: established
aliases: [NSCBC, LODI, local one-dimensional inviscid relations, characteristic boundary conditions, Thompson boundary conditions, non-reflecting boundary conditions, partially reflecting outflow]
tags: [boundary-treatment, navier-stokes, finite-difference, compact-scheme]
timestamp: 2026-10-13T00:00:00Z
---

# Navier–Stokes characteristic boundary conditions

[Poinsot & Lele (1992)](/sources/poinsot-1992.md) extend Thompson's
characteristic boundary conditions for the Euler equations to
Navier–Stokes, for direct simulations with low-dissipation, high-order
interior schemes. The design criteria (§1) are that the method handles
Euler and Navier–Stokes alike, and that it "does not use any
extrapolation procedure".

## Physical and soft conditions

(§2.1, Table I.) A *physical* boundary condition specifies known physical
behaviour and does not depend on the scheme; a *soft* (numerical)
condition is anything else the discretization needs. In 3D the number of
physical conditions for well-posedness is (Euler / Navier–Stokes):
supersonic inflow 5 / 5, subsonic inflow 4 / 5, supersonic outflow 0 / 4,
subsonic outflow 1 / 4 (from Oliger–Sundström, Dutt and Strikwerda).
* **Extrapolation over-specifies.** Extrapolating a variable, for
  instance the pressure at a subsonic inlet, "acts as an additional
  physical condition imposing a zero pressure gradient and therefore
  overspecifies the boundary conditions". Soft values must come instead
  from the conservation equations solved on the boundary itself.
* **Incoming waves need data** (quoting Thompson). Outgoing waves are
  fixed by the interior and computed with one-sided (upwind) differences;
  incoming waves would need downwind differences, which are unstable, so
  they come from the physical conditions, written in terms of the
  outgoing ones.
* **One-sided accuracy** (§§2.1–2.2). Boundary derivatives one order
  below the scheme do not affect the overall accuracy, a result the paper
  attributes to Gustafsson. In the authors' code, third-order one-sided
  derivatives turn the formally fourth- or sixth-order compact scheme into
  a fourth-order one.

## Characteristic form at a boundary

(§2.2, eqs. 9–23, read from the page images.) Take the boundary normal
along $x$, at $x = L_x$. Each conservation equation keeps its transverse
and viscous terms; its $x$-derivative terms are replaced by combinations
of the wave-amplitude variations $\mathscr L^{(1)},\dots,\mathscr L^{(5)}$,
attached to the eigenvalues $\lambda^{(1)} = v_x - c$,
$\lambda^{(2)} = \lambda^{(3)} = \lambda^{(4)} = v_x$,
$\lambda^{(5)} = v_x + c$:
$$\begin{aligned}
\mathscr L^{(1)} &= \lambda^{(1)}\left(\partial_x p - \rho c\,\partial_x v_x\right), &
\mathscr L^{(2)} &= \lambda^{(2)}\left(c^2\partial_x\rho - \partial_x p\right), &
\mathscr L^{(3)} &= \lambda^{(3)}\,\partial_x v_y,\\
\mathscr L^{(4)} &= \lambda^{(4)}\,\partial_x v_z, &
\mathscr L^{(5)} &= \lambda^{(5)}\left(\partial_x p + \rho c\,\partial_x v_x\right).
\end{aligned}$$
In the mass equation the normal terms become
$\frac1{c^2}\left[\mathscr L^{(2)} + \tfrac12(\mathscr L^{(5)} + \mathscr L^{(1)})\right]$;
in the energy (pressure) equation $\tfrac12(\mathscr L^{(5)} + \mathscr L^{(1)})$;
in the normal momentum equation $\frac{1}{2\rho c}(\mathscr L^{(5)} - \mathscr L^{(1)})$;
in the two transverse momentum equations $\mathscr L^{(3)}$ and
$\mathscr L^{(4)}$. $-\mathscr L^{(1)}$ is the time variation, at a fixed
point, of the acoustic amplitude $p' - \rho c\,v_x'$ (p. 109). Viscous
terms are deliberately left out of the $\mathscr L^{(p)}$: the waves of
the Navier–Stokes problem are approximated by inviscid ones. This is the
time-derivative form of the split used in
[characteristic decomposition](/methods/characteristic-decomposition.md).

**LODI relations** (§2.3, eqs. 24–36). Dropping transverse and viscous
terms gives
$$\partial_t\rho + \frac1{c^2}\left[\mathscr L^{(2)} + \tfrac12(\mathscr L^{(5)} + \mathscr L^{(1)})\right] = 0,\quad
\partial_t p + \tfrac12(\mathscr L^{(5)} + \mathscr L^{(1)}) = 0,\quad
\partial_t v_x + \frac{1}{2\rho c}(\mathscr L^{(5)} - \mathscr L^{(1)}) = 0,\quad
\partial_t v_y + \mathscr L^{(3)} = 0,\quad
\partial_t v_z + \mathscr L^{(4)} = 0,$$
with analogous forms for temperature, momentum, entropy and enthalpy.
They serve only to set the incoming $\mathscr L^{(p)}$, never to compute
boundary values (p. 111). Constant entropy, for example, means
$\mathscr L^{(2)} = 0$; a constant pressure means
$\mathscr L^{(5)} = -\mathscr L^{(1)}$. LODI with $\mathscr L^{(1)} = 0$
alone gives $\partial_t p - \rho c\,\partial_t v_x = 0$ (eq. 37), the
classical non-reflecting condition of Hedström, Bayliss–Turkel and
Rudy–Strikwerda, and the first Engquist–Majda approximation.

## The procedure

(§2.4, Table II.)
1. For each inviscid physical condition, drop the conservation equation
   it replaces: imposed pressure drops the energy equation, imposed
   density the mass equation, imposed $v_x$ or $\rho v_x$ the normal
   momentum equation.
2. Set the incoming $\mathscr L^{(p)}$ from the LODI relations; the
   outgoing ones come from one-sided interior differences.
3. Advance the remaining unknowns with the remaining conservation
   equations, transverse terms included.

For Navier–Stokes (§2.5), the viscous conditions enter only through the
viscous terms of step 3 and are "not strictly enforced".

**Condition counts against theory** (§2.5, Tables III–IV). NSCBC matches
Strikwerda's Navier–Stokes count except in two cases:
* subsonic inflow with $v_x, v_y, v_z, T$ imposed uses 4 conditions where
  5 are required, because $\rho$ comes from the mass equation, which has
  no viscous term;
* supersonic outflow uses 3 viscous conditions where 4 are required:
  "We have no explanation for this difference".

The only inflow set proved well-posed for Navier–Stokes (Riemann
invariant $v_x - 2c/(\gamma-1)$, $v_y$, $v_z$ and entropy imposed) "did
not work (unstable)" with NSCBC. A non-reflecting inflow
($\mathscr L^{(2)} = \mathscr L^{(3)} = \mathscr L^{(4)} = \mathscr L^{(5)} = 0$)
has no proof. Outflow viscous conditions are zero normal derivatives of
the tangential stresses and of the normal heat flux, close to Dutt's
proposal. Walls: isothermal no-slip ($\mathbf v = 0$, $T$ imposed),
adiabatic slip ($v_x = 0$, zero tangential stress and normal heat flux),
adiabatic no-slip ($\mathbf v = 0$, zero normal heat flux).

**Specific boundaries** (§3).
* *Subsonic inflow* with imposed velocity and temperature (eq. 39): the
  incoming amplitudes follow from the time derivatives of the data;
  $\rho$ comes from the mass equation.
* *Walls* (§§3.4–3.6): $\mathscr L^{(1)} = \mathscr L^{(5)}$, and
  $\mathscr L^{(2)} = \mathscr L^{(3)} = \mathscr L^{(4)} = 0$ because
  $v_x = 0$.
* *Reflecting outflow* with imposed pressure (§3.3): $\mathscr L^{(1)}$
  from $\mathscr L^{(5)}$ and the time derivative of the imposed
  pressure.
* *Edges and corners* (§2.6). A second LODI system replaces the
  transverse terms by characteristic amplitudes, which the authors found
  *necessary* with a centred low-dissipation scheme. At a corner where a
  no-slip wall meets a fixed-pressure outlet the corner pressure is left
  to float. A general theory "remains to be given".

## Partially reflecting outflow

(§3.2, eq. 40.) A perfectly non-reflecting outflow,
$\mathscr L^{(1)} = 0$, never feeds the mean pressure back from
infinity, so a problem with imposed inlet velocity and temperature has
no reference pressure. Perfectly non-reflecting Euler conditions were
"well-posed in one-dimensional cases and ill-posed in most
two-dimensional situations" (tests not shown). The fix relaxes toward a
target pressure $p_\infty$:
$$\mathscr L^{(1)} = K_{\mathrm{NR}}\,(p - p_\infty),\qquad K_{\mathrm{NR}} = \sigma_{\mathrm{NR}}\left(1 - \mathrm{Ma}_{\max}^2\right)\frac{c}{L_x},$$
with $\mathrm{Ma}_{\max}$ the maximum Mach number, $L_x$ a domain size and
$\sigma_{\mathrm{NR}} = 0.25$ in the tests; $\sigma_{\mathrm{NR}} = 0$ is
Thompson's perfectly non-reflecting condition. A known incoming wave is
added as an exact $\mathscr L^{(1)}$ term. In multi-D the treatment is
exact only at normal incidence, with "small levels of reflection"
otherwise.

## Evidence

(§§4–6; interior scheme: Lele's sixth-order compact ("Padé") finite
differences with a third-order explicit Runge–Kutta. NSCBC at inlets and
walls throughout; only the outlet varies: an extrapolation reference
after Rudy–Strikwerda (zeroth-order extrapolation of $v_x$, $v_y$,
$\rho$, pressure from a relaxed non-reflecting relation with constant
0.58), and NSCBC perfectly non-reflecting, partially non-reflecting
($\sigma_{\mathrm{NR}} = 0.25$) and reflecting.)
* **Ducted shear layer** (2D steady, 41×41, $\mathrm{Re} = 2000$, stream
  speeds $0.81c$ and $0.9c$). The extrapolation outlet oscillates without
  a steady state after $ct/L_x \approx 30$; the authors attribute
  Rudy–Strikwerda's own success to MacCormack's artificial dissipation.
  The perfectly non-reflecting outlet lets the mean pressure fall
  linearly. The reflecting outlet traps the first longitudinal acoustic
  mode. Only $\sigma_{\mathrm{NR}} = 0.25$ (and 0.4) reaches a steady
  state; 0.1 drifts, about 0.7 and above oscillates.
* **Vortex leaving a supersonic outlet** (2D, Mach 1.1 plug flow,
  81×81). The extrapolation outlet distorts the vortex, and its spurious
  waves reach the inlet and spawn a new vortex of about 0.15 of the
  initial peak vorticity. With NSCBC the vortex leaves smoothly, with a
  residual of $10^{-4}$ (§5). This vortex is a transmission test, not the
  [isentropic vortex](/benchmarks/isentropic-vortex.md).
* **Poiseuille flow** (2D, $\mathrm{Re} = 15$, 121×81). The extrapolation
  outlet distorts the outlet profiles; the partially reflecting NSCBC
  gives a pressure gradient of 0.998 times the exact one.
* **Spurious upstream waves** (§5, after Vichnevetsky). A boundary
  treatment generates short-wavelength numerical waves with negative group
  velocity: $-1$, $-3$ and $-13/3$ times the flow speed for second-order
  central, fourth-order and sixth-order Padé schemes. They travel upstream
  even in supersonic flow, reflect at the inlet as physical waves and
  close a feedback loop: "Using supersonic outlets cannot be viewed as a
  general simple solution." For a 1D acoustic pulse at normal incidence
  the numerical reflection is about $10^{-4}$ and the physical one below
  $10^{-6}$ of the incident amplitude.

No well-posedness proof is given (abstract, §8).

## Relation to ghost-point boundary treatments

[Inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) and
[weighted extrapolation](/methods/weighted-extrapolation.md) fill ghost
points for upwind-biased WENO and take outflow values by high-order,
possibly nonlinear, extrapolation. NSCBC needs no ghost points: it
modifies the equations solved at the boundary point. Its argument
against extrapolation is general: extrapolating a variable adds a
physical condition and over-specifies the boundary, whatever the scheme
or extrapolation order (§2.1). Its evidence is narrow: zeroth-order
extrapolation of primitive variables with a centred compact scheme
(§§4–6). The argument conflicts with the ghost-point methods' reports of
stable, accurate outflow extrapolation; see Contradictions. Both build
Navier–Stokes conditions as inviscid conditions plus viscous ones,
following Strikwerda.

## Contradictions

* **Does outflow extrapolation over-specify the boundary?** *Open.*
  [Poinsot & Lele (1992)](/sources/poinsot-1992.md), §2.1: extrapolating
  a variable at a boundary acts as an additional physical condition, so
  the boundary is over-specified; their tests use zeroth-order
  extrapolation with a sixth-order compact scheme and find no steady
  state and spurious upstream waves (§§4–6).
  [Li, Shu & Zhang (2016)](/sources/li-2016.md) report outflow
  extrapolation as stable (Goldberg's theorem, one-dimensional), and
  [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §§5.2, 6, use
  high-order (weighted) extrapolation at outflow with WENO in accurate
  tests (see [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)).
  The evidence on the two sides differs in extrapolation order and
  scheme dissipation; no source tests high-order extrapolation with a
  centred low-dissipation scheme, or NSCBC with upwind WENO, on a common
  problem.


# Citations

1. [Poinsot & Lele (1992)](/sources/poinsot-1992.md), §§1–6, Tables I–VI (equations and Tables I–IV read from the page images).
2. [Li, Shu & Zhang (2016)](/sources/li-2016.md), stability of outflow extrapolation (as recorded on the ILW page).
3. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §§5.2, 6.
