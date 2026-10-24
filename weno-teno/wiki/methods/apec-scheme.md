---
type: Method
title: "APEC flux for approximate pressure equilibrium"
description: "APEC is a fully conservative kinetic-energy-preserving central flux for multi-species and real-fluid Euler equations whose internal-energy half-point value adds a correction to the arithmetic mean, so pressure equilibrium holds to second order for any equation of state; the page gives the derivation, error analysis, PEqC variant and tests."
status: established
aliases: [APEC, approximately pressure-equilibrium-preserving with conservation, PEqC, pressure equilibrium with quasi-conservation, FC-NPE]
tags: [kinetic-energy-preserving, central-scheme, finite-difference, multiphase, numerical-flux]
timestamp: 2026-10-24T06:00:00Z
---

# APEC flux for approximate pressure equilibrium

**APEC** (approximate pressure equilibrium preserving with conservation) is
a fully conservative central finite-difference flux for the inviscid
multi-species Euler equations in $(\rho Y_k,\rho v,E)$ form, with an
arbitrary equation of state. It is due to
[Terashima, Ly & Ihme (2025)](/sources/terashima-2025.md). Species mass,
momentum and total energy are all in flux form. Constant velocity and
pressure are kept constant
([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md))
only approximately, with a residual of second order in $\Delta x$. The
new ingredient is the interface ("half-point") value of the internal
energy $\rho e$: the arithmetic mean minus a correction built from the
jumps of the partial densities and of an equation-of-state derivative.
Every other flux is the kinetic-energy-preserving split form of
[split convective forms](/methods/split-convective-forms.md).

## Setting and the discrete equilibrium condition

Terashima et al. use the conservative central scheme with nodes $x_i$,
uniform $\Delta x$ and interface values $(\cdot)_{i+1/2}$ (the source's
index $m$). The total-energy flux is split into internal-energy,
kinetic-energy and pressure-work parts, each with its own half-point value
(§2.2, Eqs. (6)–(8)). The equation of state is written in conservative
variables, $p=p(\rho Y_1,\dots,\rho Y_{N_{\mathrm s}},\rho v,E)$, with
page-local $N_{\mathrm s}$ the number of species.

Setting $\partial_tp=0$ in the chain rule gives the flux form of the
equilibrium condition (Eq. (11)). For uniform initial $p_0$ and $v_0$ the
velocity condition holds automatically (Eq. (12), §2.5). The discrete
pressure condition then reduces to a condition on half-point values only
(Eq. (19)):

$$(\rho e)_{i+1/2}-(\rho e)_{i-1/2}=\sum_{k=1}^{N_{\mathrm s}}\mathsf e_k\big|_i\,\Big((\rho Y_k)_{i+1/2}-(\rho Y_k)_{i-1/2}\Big),\qquad \mathsf e_k=\Big(\frac{\partial\rho e}{\partial\rho Y_k}\Big)_{\rho Y_{j\ne k},\,p},$$

with page-local $\mathsf e_k$ (the source's $\epsilon_i$). The authors say
it "corresponds to" the compatibility condition of
[Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md), which is
recorded on the pressure-equilibrium page. Because $\mathsf e_k$ is
evaluated at node $i$, the condition is asymmetric between the two
interfaces of a cell. The authors argue that "no locally-defined
half-point values satisfy Eq. (19) for all cells, and thereby no
conservative schemes may be constructed" for a general equation of state
(§2.5–2.6). The paper gives no proof of it. For the calorically perfect
mixture, Fujiwara et al. do construct exact local half-point values, and
Terashima et al. acknowledge this (§1, §3.1).

## Construction

The authors replace Eq. (19) by the sufficient pair of half-cell relations
(Eqs. (20)–(21)):

$$(\rho e)_{i+1/2}-(\rho e)_i=\sum_k\mathsf e_k|_i\big((\rho Y_k)_{i+1/2}-(\rho Y_k)_i\big),\qquad (\rho e)_i-(\rho e)_{i-1/2}=\sum_k\mathsf e_k|_i\big((\rho Y_k)_i-(\rho Y_k)_{i-1/2}\big).$$

They shift the second relation by one node and subtract it from the
first. Fujiwara et al. eliminated $(\rho e)_{i+1/2}$; Terashima et al.
solve for it, which gives a symmetric formula (Eq. (23)). The species
half-point value is left free, and the authors take the arithmetic mean
$(\rho Y_k)_{i+1/2}=\overline{\rho Y_k}$ (Eq. (24)). The internal-energy
half-point value is then (Eq. (25))

$$(\rho e)_{i+1/2}=\overline{\rho e}-\sum_{k=1}^{N_{\mathrm s}}\frac{\mathsf e_k|_{i+1}-\mathsf e_k|_i}{2}\,\frac{(\rho Y_k)_{i+1}-(\rho Y_k)_i}{2},$$

where $\overline a=\tfrac12(a_i+a_{i+1})$. The authors say the second term
"serves as a sensor to approximately preserve the PE condition" (§2.6).
The APEC fluxes are the KEP split-form fluxes of Eqs. (35)–(39) plus this
internal-energy flux (Eq. (40)):

| face flux | APEC (Eqs. (35)–(40)) |
|---|---|
| species mass | $\overline{\rho Y_k}\,\overline v$ |
| momentum (convective) | $\overline\rho\,\overline v\,\overline v$ |
| pressure | $\overline p$ |
| kinetic energy | $\overline\rho\,\tfrac12v_iv_{i+1}\,\overline v$ |
| pressure work | $\tfrac12(p_{i+1}v_i+p_iv_{i+1})$ |
| internal energy | $(\rho e)_{i+1/2}\,\overline v$ with $(\rho e)_{i+1/2}$ from Eq. (25) |

The comparison scheme **FC-NPE** ("fully-conservation but no
pressure-equilibrium preserving") is the same split form with the plain
mean $\overline{\rho e}$ (§3.1). The species flux of APEC is therefore that of FC-NPE. The abstract
states that "the numerical fluxes of internal energy and species-mass are
newly constructed"; §2.8 calls only Eq. (40) "the newly proposed internal
energy flux".

**Any equation of state.** The method needs only $\mathsf e_k$, which
follows from temperature derivatives (Eq. (48), App. B):

$$\mathsf e_k=-\frac{\rho C_v}{(\partial p/\partial T)_{\rho Y_j}}\Big(\frac{\partial p}{\partial\rho Y_k}\Big)_{\rho Y_{j\ne k},T}+\Big(\frac{\partial\rho e}{\partial\rho Y_k}\Big)_{\rho Y_{j\ne k},T},$$

with page-local temperature $T$ and specific heat $C_v$. The paper
evaluates it for the Soave–Redlich–Kwong cubic equation of state with
mixing rules (Eqs. (41)–(52)) and for the calorically perfect mixture
(Eq. (59)).

## Error of the equilibrium residual

The authors define the residual of Eq. (19) divided by $\Delta x$
(Eq. (26)). A modified-equation expansion at a state that satisfies the
continuous condition $\partial_x(\rho e)=\sum_k\mathsf e_k\partial_x(\rho Y_k)$
gives leading terms (§2.7, Eqs. (32)–(33)):

$$\text{APEC: }\ \Delta x^2\sum_k\Big(\tfrac1{12}\,\mathsf e_k'(\rho Y_k)''-\tfrac1{12}\,\mathsf e_k''(\rho Y_k)'\Big),\qquad \text{FC-NPE: }\ \Delta x^2\sum_k\Big(\tfrac13\,\mathsf e_k'(\rho Y_k)''+\tfrac16\,\mathsf e_k''(\rho Y_k)'\Big).$$

Primes denote $x$-derivatives. Both residuals are second order; only the
coefficients differ. The authors note that ranking the two errors "is
configuration dependent" (§2.7). The APEC term vanishes when
$\sum_k\mathsf e_k'(\rho Y_k)''=\sum_k\mathsf e_k''(\rho Y_k)'$ (Eq. (34)).
The order refers to the equilibrium residual, not to the scheme.

## Variants

- **PEqC** (pressure equilibrium with quasi-conservation, §2.11). Under
  velocity equilibrium the energy equation is modified to
  $\partial_tE+\partial_x\big((E+p)v\big)=\partial_x(\rho ev)-\sum_k\mathsf e_k\,\partial_x(\rho Y_kv)$
  (Eq. (54)). The right-hand side is discretized with $\mathsf e_k|_i$ and
  the species fluxes (Eqs. (55)–(56)). Pressure equilibrium then holds
  exactly, without a pressure evolution equation, but total energy is no
  longer conserved. The same trade is made by the quasi-conservative and
  [double-flux](/methods/double-flux-method.md) approaches, which the
  authors cite as non-energy-conserving (§1).
- **Upwind form** (App. A). The same half-cell argument applied to the
  physical fluxes gives an energy flux (Eq. (A.4)). It takes the species
  and momentum fluxes from an upwind solver such as HLLC
  ([HLL-type solvers](/methods/hll-riemann-solvers.md)). It is derived
  but not tested.
- **Relation to Fujiwara et al.** APEC "does not reduce to Fujiwara's
  half-point values in the calorically perfect gas case" (§3.1).
  Substituting Fujiwara's weighted species half-point value into Eq. (23)
  recovers Fujiwara's arithmetic internal-energy value (§3.1, Eqs.
  (60)–(61)). The authors "speculate" that Fujiwara's species value makes
  the scheme solve Abgrall's $\gamma$-transport implicitly.

## Evidence

All runs use third-order TVD (SSP) Runge–Kutta at CFL 0.6
([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)) and smooth tanh profiles
advected periodically
([material-interface advection](/benchmarks/material-interface-advection.md)).

- **Two ideal gases, 1D** ($\gamma=1.4$, molar mass 28, against
  $\gamma=1.66$, molar mass 4; 501 points; $v_0=1$, $p_0=0.9$; §3.1, Figs.
  1–5). FC-NPE produces pressure and velocity oscillations. Its
  equilibrium error diverges from $t\approx4$, and it blows up after
  $t=9$. APEC keeps the error at $10^{-5}$–$10^{-4}$ without growth.
  Fujiwara's exact scheme has a smaller error. All three schemes conserve
  total energy. The APEC residual converges at second order.
- **Transcritical CH$_4$/N$_2$ with the cubic equation of state, 1D**
  (ambient pressure 5 MPa, velocity 100 m/s, 501 to 4001 points; §3.2.1, Figs.
  6–11). FC-NPE blows up after $t=0.09$ s. Refinement does not cure it:
  with 4001 points it blows up around $t=0.11$ s. APEC is stable over
  twenty flow-through times. PEqC keeps the pressure error at $10^{-8}$,
  but its energy error grows. Fujiwara's scheme does not apply to this
  equation of state. At $t=0$ the maximum APEC error term is about a
  quarter of FC-NPE's. The authors attribute this to the coefficient
  $\tfrac1{12}$ against $\tfrac13$.
- **2D, CH$_4$/N$_2$** ($501^2$, diagonal advection to $t=0.09$ s, §3.2.2,
  Fig. 12). FC-NPE reaches about 10 % pressure error, 5 % velocity error
  and a 10 % temperature overshoot before blowing up near $t=0.1$ s. APEC
  stays at about 0.02 % in pressure and 0.01 % in velocity.
- **2D with a tangential shear velocity** ($2001^2$, §3.2.3, Fig. 14).
  FC-NPE fails before $t=0.044$ s, and at $3001^2$ it still oscillates
  near $t=0.03$ s. APEC keeps pressure and transverse velocity and
  conserves energy. It eventually becomes unstable as the shear thins the
  interface. The authors attribute this to under-resolved species density
  and temperature, "not oscillations driven by PE errors".

## Qualifications

- The method is non-dissipative and is tested only on smooth interfaces.
  The authors leave discontinuities to future work. They state that the
  remaining second-order error "could lead to numerical instabilities if
  the grid resolution is insufficient", especially at large density
  ratios (§3.2.3, §4).
- The impossibility statement for exact, locally defined, fully
  conservative fluxes is argued from the asymmetry of Eq. (19). It is not
  proved, and the paper restricts it to general equations of state.
  Fujiwara et al.'s FC/PE scheme is exact for the calorically perfect
  mixture. Terashima et al. call it "the first one in which the full
  conservation and pressure equilibrium properties are both preserved"
  (§1).
- Terashima et al. print the subscript of $\mathsf e_k$ as
  $\rho Y_{j\ne j}$ after Eqs. (21) and (40); Eqs. (17), (19) and (48)
  hold the other species fixed, as in the definition above. They print the energy-conservation
  error with a leading sum over time, although Fig. 2(a) plots it as a
  time history (§3.1).

# Citations

- [Terashima, Ly & Ihme (2025)](/sources/terashima-2025.md) — §1, §2.2–2.8 Eqs. (6)–(40), §2.10 Eq. (48), §2.11 Eqs. (53)–(56), §3.1 Eqs. (57)–(61) Figs. 1–5, §3.2 Figs. 6–14, §4, App. A Eq. (A.4), App. B.
- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — §2.3, §3 (the compatibility condition and the exact ideal-gas half-point values APEC is compared with).
