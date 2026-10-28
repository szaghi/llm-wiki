---
type: Method
title: "Actuator line and actuator disk models"
description: "Actuator line and actuator disk models replace rotor blades in an LES by body forces from tabulated airfoil polars, spread on the grid by a Gaussian kernel; this page gives the line and disk formulations, the kernel-width and grid rules, the filtered actuator line correction and its parallel algorithm, and the accuracy reported for wind turbines."
status: established
aliases: [actuator line model, ALM, actuator line method, filtered actuator line model, F-ALM, actuator disk model, actuator disc model, ADM, filtered actuator disk model, actuator-line tower model, actuator surface method]
tags: [les, implicit-les, wmles, numerical-dissipation, software]
timestamp: 2026-10-28T06:44:00Z
---

# Actuator line and actuator disk models

An **actuator line model (ALM)** represents each rotating blade of a rotor
in a [large-eddy simulation](/definitions/large-eddy-simulation.md) by a
line of actuator points instead of a body-fitted surface. At each point
the lift and drag per unit span are computed from the local relative
velocity and tabulated airfoil polars, and the force is spread onto the
grid as a body-force density with a Gaussian kernel. An **actuator disk
model (ADM)** goes one step further and spreads a thrust over the rotor
disk, azimuthally averaged, so that individual blades and tip vortices are
not represented. Both are subgrid models of the rotor, not of the
turbulence: the flow around the blade is never resolved, and the forcing
enters the momentum equations as a body force.
[Stanly et al. (2022)](/sources/stanly-2022.md) implement and parallelize
the filtered actuator line of Martínez-Tossas & Meneveau in a compressible
[implicit LES](/definitions/implicit-les.md) code, and
[Zhang et al. (2022e)](/sources/zhang-2022-i.md) use a filtered actuator
disk in a wall-modelled LES of wind-turbine wakes over hills.
[Taschner et al. (2024)](/sources/taschner-2024.md) couple a GPU-resident
atmospheric LES code with an aeroelastic turbine tool through the actuator
line and its filtered form, verify the line against four research LES
codes and test the filtered correction on a wing and a rotor. All three
sources are wind-energy applications; the rotor model is the shared
ingredient.

Page-local notation: $\Omega_{\mathrm{rot}}$ the rotor angular velocity
(registry clash list), $R_{\mathrm r}$ the rotor radius (registry §11)
and $D_{\mathrm r}=2R_{\mathrm r}$ its diameter, $r$ the radial position, $c$
the local chord; $V_z$, $V_\theta$ the axial and tangential velocity at an
actuator point and $V_{\mathrm{rel}}$ the relative velocity; $\phi_{\mathrm f}$
the flow angle, $\alpha_{\mathrm a}$ the angle of attack and $\gamma_{\mathrm t}$
the local twist plus blade pitch (the sources' $\phi$, $\alpha$, $\gamma$;
the registry's $\alpha$ is the DG blending factor and $\gamma$ the ratio
of specific heats); $\epsilon_{\mathrm G}$ the Gaussian kernel width (the
sources' $\epsilon$; the registry's $\varepsilon$ is the dissipation rate);
$h$ the grid spacing (registry §6; the sources write $\Delta$, which here
is never a filter width); $C_L$, $C_D$ the lift and drag coefficients of
the airfoil tables (registry §5); $C_{\mathrm{Th}}$ the thrust coefficient
(registry §11), $a_{\mathrm i}$ the axial induction factor, $A_{\mathrm D}$
the disk area; $N_{\mathrm{fp}}$, $N_{\mathrm{vp}}$ the numbers of force and
velocity actuator points of a blade (the source's $N_F$, $N_V$; not the
registry's modal-filter degree $N_f$), $C_{\mathrm{Pw}}$ the rotor power
coefficient (the registry's $C_p$ is the pressure coefficient) and
$f_{\mathrm u}$ an under-relaxation factor.

## The actuator line

Stanly et al. (2022, §2.2, Algorithm 1, Eqs. 10–16) give the baseline model
of Sørensen & Shen, which they cite. At each actuator point of a blade the
relative velocity and the flow angle are
$$V_{\mathrm{rel}}=\sqrt{V_z^2+(\Omega_{\mathrm{rot}}r-V_\theta)^2},\qquad \phi_{\mathrm f}=\tan^{-1}\frac{V_z}{\Omega_{\mathrm{rot}}r-V_\theta},\qquad \alpha_{\mathrm a}=\phi_{\mathrm f}-\gamma_{\mathrm t},$$
the lift and drag per unit span are
$$(L',D')=\tfrac12\rho V_{\mathrm{rel}}^2c\,\big(C_L(\alpha_{\mathrm a},Re)\,\boldsymbol e_L,\ C_D(\alpha_{\mathrm a},Re)\,\boldsymbol e_D\big)$$
with $\boldsymbol e_L$, $\boldsymbol e_D$ the unit vectors of lift and drag
(page-local), and the force is regularized with the isotropic Gaussian
kernel
$$g_\epsilon(d)=\frac{1}{\epsilon_{\mathrm G}^3\pi^{3/2}}\exp\!\Big[-\Big(\frac{d}{\epsilon_{\mathrm G}}\Big)^2\Big],\qquad \boldsymbol f_{\mathrm{ALM}}(\boldsymbol x)=\sum_{i=1}^{N_{\mathrm b}}\int_0^{R_{\mathrm r}}(L',D')(s)\,g_\epsilon\big(\lvert\boldsymbol x-s\boldsymbol e_i\rvert\big)\,ds,$$
where $d$ is the distance from a grid point to the actuator point, $s$ the
coordinate along line $i$ with unit vector $\boldsymbol e_i$, and $N_{\mathrm b}$
the number of blades ($g_\epsilon$, $\boldsymbol f_{\mathrm{ALM}}$, $N_{\mathrm b}$
page-local). $\boldsymbol f_{\mathrm{ALM}}$ is a force per unit volume.

**Variants named in the source.** Stanly et al. (§1) list tip and root
corrections (Shen et al.), a chord-scaled Gaussian width (Shives &
Crawford), an equivalent elliptic-planform chord (Jha et al.), an
airfoil-shaped projection (Churchfield et al.), actuator curve embedding
(Jha & Schmitz), an elastic actuator line (Meng et al.), and
implementations in [lattice Boltzmann](/methods/lattice-boltzmann-method.md)
and vortex particle-mesh solvers, all as cited there. The **actuator surface**
method adds chord-wise lines at each radial station to represent the blade
surface and near wake. They call the earlier tip corrections "mostly based
on empirical corrections or fits".

**The tower as an actuator line** (Stanly et al. 2022, §2.3, Eqs. 17–18,
after Sarlak et al.): drag coefficient 1.2 and a fluctuating lift
coefficient $C_L=A_{\mathrm s}\sin(2\pi f_{\mathrm s}t)+B_{\mathrm s}$, with
the shedding frequency $f_{\mathrm s}=0.2U_\infty/D_{\mathrm{cyl}}$, the local
tower diameter $D_{\mathrm{cyl}}$, $A_{\mathrm s}=0.3$ and a random offset
$B_{\mathrm s}$ (all page-local). The authors state that such a tower
disturbs the tip vortices less than a no-slip body-fitted tower because
the stagnation pressure in front of it is too low.

## Kernel width and grid spacing

The kernel width is the crux of the model. Stanly et al. (2022, §3–3.1,
Figs. 2–3) state, citing Martínez-Tossas et al. and Stevens et al.:

- the optimal width is $\epsilon_{\mathrm G}\approx0.25c$;
- smooth projection needs $\epsilon_{\mathrm G}/h\gtrsim2.8$ so that the
  force spreads over more than two grid points without oscillations, so
  the optimal width forces very fine grids;
- a wider kernel predicts the downstream wake well but gives thicker,
  weaker tip vortices; these induce too small a velocity at the blade, the
  angle of attack of neighbouring sections is too large, and torque and
  power are overpredicted, "sometimes even exceeding the Betz limit",
  most where the lift coefficient or the chord varies strongly.

Their own coarse run violates $\epsilon_{\mathrm G}/h>2$
($\epsilon_{\mathrm G}/h=1.85$) without spurious fluctuations (§5.2); fifty
actuator points per line sufficed (§5.2, results not shown).

Taschner et al. (2024, §1, §2.3, §3.3) cite the same rules with a sharper
statement of the upper end: the optimal width is about 25% of the local
chord, which makes the grids "infeasible" for wind farms;
$\epsilon_{\mathrm G}/h>2$ avoids numerical oscillations;
$\epsilon_{\mathrm G}/h=5$ has been found necessary for fully converged
results; and a width above the optimum underestimates the induced
velocity, raising the angle of attack and overpredicting torque and power,
as in Stanly et al. Their own GPU runs are limited by the memory of one
A100 (40 GB) to $\epsilon_{\mathrm G}/h\approx3.39$ in the rotor
cross-verification and about 3 in the filtered-line rotor runs, below the
$\approx5$ of the reference codes (§3.1, §3.3, §4.1). Only grid points where
the kernel exceeds 0.1% of its centre value receive the projected force
(§2.3).

## The filtered actuator line

The **filtered actuator line model (F-ALM)** of Martínez-Tossas & Meneveau,
which Stanly et al. (2022, §3.2, Algorithm 2, Eqs. 19–21) implement,
corrects the velocity that a coarse kernel samples instead of the kernel
itself. With $\tilde{\boldsymbol u}(\boldsymbol x_i)$ the LES velocity
sampled at actuator point $\boldsymbol x_i$ (the tilde as printed, not a
Favre filter), $\boldsymbol j$ the lift direction and $u_y(z_i;\epsilon_{\mathrm G})$
the induced velocity at spanwise position $z_i$ for kernel width
$\epsilon_{\mathrm G}$ (page-local), the corrected velocity is
$$\boldsymbol u_{\mathrm{corr}}(\boldsymbol x_i)=\tilde{\boldsymbol u}(\boldsymbol x_i)+\big[u_y(z_i;\epsilon_{\mathrm G}^{\mathrm{opt}})-u_y(z_i;\epsilon_{\mathrm G}^{\mathrm{LES}})\big]\,\boldsymbol j,$$
the bracket being the "subfilter velocity model". The induced velocity
follows from filtered lifting-line theory,
$$u_y(z_i;\epsilon_{\mathrm G})=-\int_{-\infty}^{\infty}\frac{1}{U_\infty(z_i)}\frac{\mathrm d\Gamma_U(z_j)}{\mathrm dz_j}\,\frac{1}{4\pi(z_i-z_j)}\Big(1-e^{-(z_i-z_j)^2/\epsilon_{\mathrm G}^2}\Big)\,dz_j,\qquad \Gamma_U=\tfrac12cU_\infty^2C_L,$$
with $U_\infty(z_i)$ the unperturbed inflow at the point estimated from the
previous step ($\Gamma_U$ page-local, the bound circulation times the
inflow speed). Lift and drag are then applied perpendicular and parallel
to $\boldsymbol u_{\mathrm{corr}}$. The projected force field is unchanged:
F-ALM corrects only the velocity "felt" by the actuator points, so a coarse
kernel ($\epsilon_{\mathrm G}=2c$ in their illustration) recovers the
induced velocity of the optimal one. The authors call it a "well-derived
subgrid-scale model" and a more theoretically consistent version of the
model of Dağ & Sørensen; the "subgrid" here is the rotor's induced flow,
not turbulence.

**Parallel algorithm** (Stanly et al. 2022, §4.3, Algorithm 3; their
contribution). The correction couples all points of a line through the
integral, and the processor that owns a point changes as the line rotates,
so fixed point-to-point messages are, as stated, not feasible. Each step
splits the global communicator into one communicator per blade, gathers the
line data on one rank, computes the non-local correction there, broadcasts
it, and continues with the local steps. The authors state that the scheme
carries over to other non-local actuator lines.

**Discrete form with separate force and velocity points** (Taschner et
al. 2024, §2.3, Eqs. 12–20, App. A, Algorithm 1; the vector-form
implementation is their contribution, the model that of Martínez-Tossas &
Meneveau, which they cite). The aeroelastic tool carries $N_{\mathrm{fp}}$
force points and $N_{\mathrm{vp}}$ velocity points per blade, generally
different ($N_{\mathrm{vp}}$ fixed by the blade stations of the
aerodynamic module). The correction is computed at the force points: the
inflow is estimated as the sampled velocity minus the induced velocity of
the LES kernel, $\Gamma_U$ at each point is recovered from the previous
step's force as its component normal to that inflow per unit span and
density (Eq. 14), and the spanwise derivative becomes a central difference,
$\Delta\Gamma_{U,k}=\tfrac12(\Gamma_{U,k+1}-\Gamma_{U,k-1})$, with
$\Delta\Gamma_{U,1}=\Gamma_{U,1}$ at the first point and the value
$-\Gamma_{U,N_{\mathrm{fp}}}$ at the last (Eqs. 15–17; the printed
left-hand side of Eq. 17 is under Qualifications). In the spanwise notation of the integral above,
the induced velocity becomes the sum

$$u_y(z_k;\epsilon_{\mathrm G})\approx-\sum_{l=1}^{N_{\mathrm{fp}}}\frac{\Delta\Gamma_{U,l}}{U_\infty(z_l)}\,\frac{1}{4\pi(z_k-z_l)}\Big(1-e^{-(z_k-z_l)^2/\epsilon_{\mathrm G}^2}\Big)$$

(Eq. 18, printed in vector form per actuator point), evaluated for
$\epsilon_{\mathrm G}^{\mathrm{opt}}$ and $\epsilon_{\mathrm G}^{\mathrm{LES}}$.
The correction is under-relaxed in time,
$\Delta u^n=f_{\mathrm u}[u_y(\epsilon_{\mathrm G}^{\mathrm{opt}})-u_y(\epsilon_{\mathrm G}^{\mathrm{LES}})]^n+(1-f_{\mathrm u})[\,\cdots]^{n-1}$
with $f_{\mathrm u}=0.1$ as recommended by the model's authors (Eq. 19),
added to the sampled velocity (Eq. 20) and interpolated to the velocity
points; the force is still projected with the coarse kernel, so the
resolved vorticity differs little between the line and its filtered form
(§4.2).

**Accuracy and convergence of the filtered line.**

- *Translating wing* (Taschner et al. 2024, §3.2, Table 2, §4.2, Figs.
  8–9): a constant-chord NACA64A17 wing at $\alpha_{\mathrm a}=6^\circ$ and
  span $12.5c$, with $\epsilon_{\mathrm G}/c=1$, 2, 4 and
  $\epsilon_{\mathrm G}/h=4$, 8. The correction is converged already at
  $\epsilon_{\mathrm G}/h=4$, in line with the convergence for
  $\epsilon_{\mathrm G}/h>2.8$ reported by the model's authors, and the
  lift distribution is independent of the kernel width "even for widths
  exceeding the optimum by a factor of 16", matching an actuator line run
  with $\epsilon_{\mathrm G}=\epsilon_{\mathrm G}^{\mathrm{opt}}=0.25c$.
  This agrees with Stanly et al.'s illustration, where a kernel of $2c$
  recovers the optimal induced velocity. The accuracy rests on the
  numerically differenced lift gradient: $N_{\mathrm{fp}}=300$ points were
  needed, and the authors suggest clustering the points at the tips.
- *NREL 5-MW rotor* (§3.3, Table 3, §4.3, Table 4, Figs. 11–13): with
  $N_{\mathrm{fp}}=N_{\mathrm{vp}}=307$ and $\epsilon_{\mathrm G}/D_{\mathrm r}=0.079$,
  the filtered line lowers $C_{\mathrm{Pw}}$ from 0.569 to 0.514 and
  $C_{\mathrm{Th}}$ from 0.838 to 0.805, and widening the kernel to
  $\epsilon_{\mathrm G}/D_{\mathrm r}=0.11$ raises $C_{\mathrm{Pw}}$ by
  3.51% with the plain line and 1.56% with the filtered one ($C_{\mathrm{Th}}$
  by 1.31% and 0.50%). The correction acts for $r/R_{\mathrm r}>0.75$, where
  the ratio of optimal to resolved induced velocity reaches about 12 near
  the tip, and the optimal induced velocity changes sign at
  $r/R_{\mathrm r}\approx0.16$. Unlike the wing, the rotor result is not
  independent of $\epsilon_{\mathrm G}$ and $h$ at $\epsilon_{\mathrm G}/h\approx3$,
  which the authors find consistent with Blaylock et al. at
  $\epsilon_{\mathrm G}/h=2$ (cited) and expect to improve with larger
  $\epsilon_{\mathrm G}/h$. The reduced normal loading weakens the
  induction and the shear layer and delays the laminar–turbulent
  transition of the wake, a conclusion they restrict to laminar inflow.
- *Actuator-point count* (App. C, Fig. C2): the filtered line needs at
  least $N_{\mathrm{fp}}=163$ points to capture the magnitude of the tip
  lift drop and about 300 for a converged lift profile, against 55 for the
  plain line; between 55 and 307 points $C_{\mathrm{Pw}}$ and
  $C_{\mathrm{Th}}$ change by about 1.8% and 0.7% with the filtered line
  and 0.014% and 0.011% with the plain one. The tip blade data (zero-chord
  interpolation against extrapolation from the two inner points) change
  the tip lift and are named as a source of inter-code deviation (§3.1,
  §4.1, §4.3).

## Actuator disk

Zhang et al. (2022e, §II A–B, Eqs. 7–11) use the filtered actuator disk of
Shapiro, Gayme & Meneveau, which they cite. With the upstream velocity
$u_\infty$ and $A_{\mathrm D}=\tfrac14\pi D_{\mathrm r}^2$, the thrust is
$F_{\mathrm t}=-\tfrac12\rho C_{\mathrm{Th}}A_{\mathrm D}u_\infty^2$; since
$u_\infty$ is not known inside a wind farm, it is rewritten with the
disk-averaged, time-filtered velocity $u_{\mathrm d}$ (page-local) as
$$F_{\mathrm t}=-\tfrac12\rho\,C'_{\mathrm{Th}}A_{\mathrm D}u_{\mathrm d}^2,\qquad C'_{\mathrm{Th}}=\frac{C_{\mathrm{Th}}}{(1-a_{\mathrm i})^2},\qquad P_{\mathrm T}=-F_{\mathrm t}u_{\mathrm d},$$
with $P_{\mathrm T}$ the power (page-local). With $a_{\mathrm i}=1/4$:
$C_{\mathrm{Th}}=3/4$ and $C'_{\mathrm{Th}}=4/3$. Because
$C'_{\mathrm{Th}}$ is constant, the authors estimate the power of a turbine
at any site without simulating it, from the turbine-free flow (§III C,
Eq. 19):
$$\frac{P_{\mathrm T}}{P_{\mathrm T,0}}\approx\left(\frac{\int_{A_{\mathrm D}}\langle u\rangle_{\mathrm{nw}}\,dA}{\int_{A_{\mathrm D}}\langle u\rangle_{\mathrm{nw},0}\,dA}\right)^3,$$
with $\langle u\rangle_{\mathrm{nw}}$ the time-averaged turbine-free velocity
and subscript 0 the flat-terrain case (page-local); the actuator-disk runs
collapse on this curve (Fig. 11a).

Stanly et al. (2022, §1) state the disk's drawback: it sheds a vortex sheet
instead of distinct tip vortices. The two sources thus sit at the two ends
of the trade-off: blade-level loads and tip vortices with the line, wake
and power at wind-farm scale with the disk.

## Host LES and results

| | Stanly et al. (2022) | Zhang et al. (2022e) |
|---|---|---|
| Rotor model | ALM and F-ALM, actuator-line tower, no nacelle | filtered ADM, $C'_{\mathrm{Th}}=4/3$ |
| Host solver | MIRACLES, compressible: fourth-order summation-by-parts differences, eighth-order artificial dissipation as the only closure ([implicit LES](/definitions/implicit-les.md), [numerical dissipation](/properties/numerical-dissipation.md)), RK4 | modified [LESGO](/software/lesgo.md): pseudo-spectral in $x$, $z$, second-order differences in $y$, AB2; [Smagorinsky](/methods/smagorinsky-model.md) with Mason–Thomson damping ($C_{\mathrm{MT}}=0.16$, the source's $C_0$, exponent 2); log-law [wall stress](/methods/equilibrium-wall-model.md); [immersed boundary](/methods/immersed-boundary-method.md) terrain |
| Case | NREL Phase VI two-bladed turbine, sequence H, $U_\infty=7$ m/s, tip-speed ratio 5.35 as printed, $R_{\mathrm r}=5.029$ m, tip Mach number 0.1, uniform laminar inflow | wind-tunnel-scale neutral boundary layer, $D_{\mathrm r}=40$ mm at hub height $D_{\mathrm r}$, flat ground and two-dimensional $\cos^2$ hills of slope 0.2 and 0.4 |
| Grid | about 15 million points on 729 CPUs, $\epsilon_{\mathrm G}=0.5c$ (twice optimal), mean $\epsilon_{\mathrm G}/h=3.6$ in the rotor plane | $192\times64\times97$ over $30D_{\mathrm r}\times6D_{\mathrm r}\times6D_{\mathrm r}$ (streamwise, spanwise, vertical as printed; 6.4, 10.7, 16.2 points per diameter) |
| Result | power 6.06 kW (F-ALM) and 6.778 kW (ALM) against 6.0 kW measured, errors 1% and 12.96%; F-ALM lowers the tangential force near tip and root; flow fields and wakes indistinguishable; cost per step 3.039 against 3.0098 s on 8 cores | power peaks at the hill crest (1.8 and 2.6 times flat terrain for the gentle and steep hill) and collapses in the steep-hill wake; the wake centre deflects downward behind the steep hill crest; wake deficit not Gaussian until $x/D_{\mathrm r}\gtrsim7.5$ |

(Stanly et al. 2022, §5, Tables 2–3, 6–7, Figs. 12–17; Zhang et al. 2022e,
§II B, §III B–C, Figs. 7–11.)

**A GPU-resident host coupled to an aeroelastic tool** (Taschner et al.
2024, §2.1–2.3, §3.1, §4.1, App. B). The host is GRASP, an anelastic
atmospheric LES code derived from DALES that runs entirely on the GPU:
second-order central advection on a staggered (Arakawa C) grid,
third-order Runge–Kutta time stepping, an FFT pressure solver, and the
[Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.16$ and
$\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$. A new plugin of its interface
(AspFAST, on the CPU) exchanges sampled velocities (linear interpolation),
blade positions and forces each step with OpenFAST, whose AeroDyn module
computes the blade-element loads with its own induction model disabled,
ElastoDyn the structural dynamics and ServoDyn the controller. In the
cross-verification of Martínez-Tossas et al. (cited) — NREL 5-MW turbine,
$D_{\mathrm r}=126$ m, uniform laminar inflow of 8 m/s at 9.155 rpm,
$N_{\mathrm{fp}}=64$, $N_{\mathrm{vp}}=19$, $\epsilon_{\mathrm G}/D_{\mathrm r}=0.079$ —
blade loads and the near wake agree with [LESGO](/software/lesgo.md),
SOWFA, SP-Wind and EllipSys3D; the far-wake Reynolds stresses are lower,
which the authors attribute to the coarser $\epsilon_{\mathrm G}/h$, and
the vertical velocity profile at $x/D_{\mathrm r}=15$ is slightly
asymmetric, attributed as a hypothesis to the lack of a zero-shear bottom
boundary. Wake transition begins earliest in SP-Wind ($x/D_{\mathrm r}\approx5.5$)
and furthest downstream in SOWFA and GRASP (about 10); the authors cite
earlier transition in the pseudo-spectral codes and expected it from the
staggered grid, a gain the coarse resolution cancels (see
[numerical dissipation](/properties/numerical-dissipation.md)). The
outflow fringe forcing affects wake recovery and the transition location,
and the domain was lengthened from $24D_{\mathrm r}$ to $53.25D_{\mathrm r}$
to mitigate it. On one A100, two-way coupling is about ten times slower
than the standalone LES for medium and large grids and one-way coupling
about twice as fast as two-way; the filtered correction itself costs
little, but its larger $N_{\mathrm{fp}}$ (163 against 55) lowers the time
steps per wall-clock second by about 25%. The closure here is explicit,
the kind of LES for which Stanly et al. judge the filtered line better
suited than their implicit LES.

**What each source attributes its errors to.** Stanly et al. attribute the
small differences from the reference translating-wing results to running
their implicit LES on a grid built with the explicit-LES criterion
$\epsilon_{\mathrm G}/h=2.8$ of the reference (§4.2), the wake differences
$2R_{\mathrm r}$ downstream from a published reference to the missing nacelle and the
actuator-line tower (§5.3.1), and the overshoot of both models near the
root to three-dimensional rotational effects that two-dimensional airfoil
tables do not capture (§5.3.2). They judge that because F-ALM allows coarse
grids it is "more suitable for LES simulations having explicit
subgrid-scale models … rather than the currently used implicit LES" (§6).
Zhang et al. attribute the underpredicted streamwise turbulence intensity in
the recirculating wake of the bare steep hill to the equilibrium log-law
wall model (§III A, Fig. 4b).

## Qualifications

- **One operating point, laminar inflow.** Stanly et al.'s 1% power error
  is one tip-speed ratio, one kernel width ($\epsilon_{\mathrm G}/c=0.5$)
  and non-turbulent inflow; they attribute the insensitivity of the
  averages beyond one flow-through to the laminar inflow (§5.2).
- **Grid study run with the baseline model.** Their three-grid study
  (3,466,008, 6,993,756 and 13,002,444 points, GCI 6% on the fine grid,
  Table 5) prints a fine-grid power of 6.778 kW, equal to the ALM power of
  Table 6, so the GCI applies to ALM, and the printed powers 6.675, 6.557
  and 6.778 kW are non-monotone in refinement *(compiler check, not in the
  sources)*.
- **Printed slips in Stanly et al. (2022)** *(compiler checks from the
  printed numbers, not in the sources)*. The text gives about 15 million
  points ($25\times25\times33$ per CPU on 729 CPUs, which is 15,035,625),
  while the fine grid of Table 5, said to be used for both runs, has
  13,002,444. The printed fine-to-medium refinement ratio 1.44 matches the
  edge lengths ($0.0219/0.0152$) but not the point counts
  ($(13{,}002{,}444/6{,}993{,}756)^{1/3}=1.23$). With
  $\epsilon_{\mathrm G}=0.5\times0.1095R_{\mathrm r}$, the edge lengths give
  $\epsilon_{\mathrm G}/h=3.60$, 2.50 and 1.98, against the printed 3.60,
  2.33 and 1.85. With 71.9 rpm and $R_{\mathrm r}=5.029$ m the tip speed is
  37.87 m/s (printed 37.86) and the tip-speed ratio 5.41, against the
  printed 5.35; the mean chord 0.5475 m is $0.1089R_{\mathrm r}$, printed
  $0.1095R_{\mathrm r}$. Table 3 leaves its grid-size cells empty. In
  Eq. (21) the left side carries the kernel $\epsilon_k$ and the integrand
  $\epsilon_i$, and $\gamma$ denotes both the grid-stretching parameter and
  the twist.
- **Printed labels in Zhang et al. (2022e).** The text discusses turbines at
  $x_t/D_{\mathrm r}=-5$, 0 and 1.25 ($x_t$ the turbine position), while the legend of
  Fig. 8 reads $x_t=3.5$, 8.5 and 9.75; both are recorded as printed.
- Neither source couples the rotor model with an explicit turbulence
  closure study: the closure is held fixed (implicit LES in one, Smagorinsky
  in the other). The same holds for Taschner et al. (2024), whose
  Smagorinsky constant is fixed at 0.16 "to be consistent with the
  reference" (§3.1).
- **Printed slips in Taschner et al. (2024).** The last-point case of the
  spanwise difference (Eq. 17) prints the left-hand argument as the first
  point, $x^1_i$, where the pattern of Eqs. (15)–(16) has the last point.
  Appendix B gives $\epsilon_{\mathrm G}/h=5$ for the run of §3.1, where
  Table 1 and §4.1 give 3.39 and attribute $\approx5$ to the reference
  codes. Appendix B quotes Appendix C as requiring at least 150 force
  points, Appendix C prints 163. The caption of Table 3 repeats that of
  Table 1 (the cross-verification case) for the filtered-line rotor case.
- The filtered-line results of Taschner et al. are for uniform laminar
  inflow; the wing and rotor convergence statements are at
  $\epsilon_{\mathrm G}/h$ between 3 and 8.

# Citations

- [Stanly et al. (2022)](/sources/stanly-2022.md) — §1 (variants, actuator disc and surface, tip corrections); §2.1 (MIRACLES implicit LES); §2.2, Algorithm 1, Eqs. (10)–(16) (actuator line); §2.3, Eqs. (17)–(18) (actuator-line tower); §3–3.2, Algorithm 2, Eqs. (19)–(21), Figs. 2–3 (kernel width, F-ALM); §4.2, Table 1, Fig. 6 (translating wing); §4.3, Algorithm 3, Figs. 7–8 (parallel F-ALM); §5–5.3, Tables 2–7, Figs. 12–17 (NREL Phase VI: grid study, flow fields, loads, power, cost); §6.
- [Zhang et al. (2022e)](/sources/zhang-2022-i.md) — §II A–B, Eqs. (1)–(11) (LESGO, Smagorinsky with wall damping, log-law wall stress, immersed-boundary terrain, filtered actuator disk, grid); §III A, Fig. 4 (hill validation, wall-model attribution); §III B–C, Eq. (19), Figs. 7–11 (wakes, power estimate without a turbine); App. A, Table I (grid study).
- [Taschner et al. (2024)](/sources/taschner-2024.md) — §1; §2.1, Eqs. (1)–(4) (GRASP, Smagorinsky); §2.3, Eqs. (5)–(20), Fig. 1 (actuator line, Gaussian projection, filtered line with force and velocity points, under-relaxation); §3.1–3.3, Tables 1–3; §4.1, Figs. 2–6 (cross-verification against four LES codes, wake transition, fringe); §4.2, Figs. 8–9 (translating wing); §4.3, Table 4, Figs. 11–13 (NREL 5-MW, power and thrust, wake transition); App. A, Algorithm 1; App. B, Fig. B1 (GPU performance); App. C, Fig. C2 (actuator-point convergence).
