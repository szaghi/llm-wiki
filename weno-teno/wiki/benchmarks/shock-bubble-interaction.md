---
type: Benchmark
title: "Shock–bubble interaction"
description: "A planar shock hitting a circular or spherical region of different density or material: one-dimensional analogues, the Mach 1.22 air–helium and air–R22 experiments of Haas and Sturtevant, a helium–R22 three-phase bubble, stronger air–helium and air–hydrogen cases, gas bubbles in water or stiffened gas, a relativistic version, Baer–Nunziato and shallow-water variants; tests interface sharpness, robustness and roll-up."
status: established
aliases: [shock–bubble, shock-bubble interaction, shocked bubble, shock–helium bubble, shock–R22 bubble, Haas–Sturtevant experiment, shock-induced bubble collapse]
tags: [benchmark, multiphase, interface-capturing, central-scheme, finite-volume]
timestamp: 2026-10-23T20:30:00Z
---

# Shock–bubble interaction

A planar shock travels through a uniform medium and hits a circular
(in one dimension, an interval; in three, spherical) region whose
density, and in multiphase versions whose material, differs from its
surroundings. The waves refracted and reflected at the interface deform
the bubble and roll it up; the benchmark tests how sharply a scheme
keeps the interface, whether it survives the material contrast, and how
much of the roll-up it resolves. It is the one test of this family with
an experiment behind it: the Mach 1.22 air–helium case of Haas &
Sturtevant, against which two sources measure feature or interface
velocities; others compare interface trajectories or shadowgraph-like
contours with the experiment or with published computations of the same
case.
The sources use the geometry in four quite different settings.

Throughout, $\phi_k$ denotes the volume fraction of component $k$ and
$(\gamma_k,p_{\infty,k})$ its [stiffened-gas](/definitions/stiffened-gas-equation-of-state.md)
constants (page-local symbols). States are listed in the variables the
source prints.

## Euler and two-material Euler versions

**One-dimensional analogue.** [Chertock et al. (2023)](/sources/chertock-2023.md)
Ex. 1 run, on $[-1,1]$ with $\gamma=1.4$, a left-moving shock at
$x=0.75$ hitting a heavy "bubble" of radius $0.25$ at the origin:

$$
(\rho,v,p)(x,0)=\begin{cases}
(13.1538,\ 0,\ 1), & \lvert x\rvert<0.25,\\
(1.3333,\ -0.3535,\ 1.5), & x>0.75,\\
(1,\ 0,\ 1), & \text{otherwise},
\end{cases}
$$

solid wall on the left, free boundary on the right, $t=3$,
$\Delta x=1/100$, reference on $\Delta x=1/2000$, after a work they
list as in preparation. Their [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
is "sharper and less oscillatory" than the earlier
[central-upwind scheme](/methods/central-upwind-scheme.md), which has
lower shock resolution and an oscillation at the contact (Fig. 5.1).
[Chu et al. (2025b)](/sources/chu-2025-b.md) Example 1 make the same
data two-material: the bubble gas has $\gamma=5/3$, the surrounding gas
$\gamma=1.4$ (the $\gamma$-based multifluid system with advected
$1/(\gamma-1)$ and $\gamma p_\infty/(\gamma-1)$, $p_\infty=0$ here), on
$[-1,2]$ with solid walls, $t=3$, $\Delta x=1/50$ to $1/200$, reference
on $1/1000$. Their Example 2 is a water–air analogue: air
$(\rho,v,p;\gamma,p_\infty)=(0.05,0,1;1.4,0)$ for $\lvert x-6\rvert<3$,
shocked water $(1.325,-68.525,19153;4.4,6000)$ for $x>11.4$, water
$(1,0,1;4.4,6000)$ otherwise, on $[0,18]$ with free boundaries,
$t=0.045$, $\Delta x=1/10$ to $1/40$. Their
[LCD-based path-conservative central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
(second order, generalized minmod with parameter 1.3, SSP-RK3 at CFL
0.45) has the lower $L^1$ density errors on every grid: $8.53\times10^{-1}$,
$4.21\times10^{-1}$, $1.96\times10^{-1}$ against $1.16$, $6.65\times10^{-1}$,
$3.39\times10^{-1}$ for the scalar
[path-conservative central-upwind](/methods/path-conservative-scheme.md)
scheme in Example 1, and $1.93\times10^{-1}$, $1.05\times10^{-1}$,
$5.70\times10^{-2}$ against $4.06\times10^{-1}$, $2.57\times10^{-1}$,
$1.53\times10^{-1}$ in Example 2, with observed rates near 1 (Tables
5.1–5.2), and a sharper contact near $x\approx3$ in the water–air case.

**One-dimensional two-material slabs.** [Bai & Li (2022)](/sources/bai-2022.md)
§3.1.3–3.1.4 run slab versions with two materials, as strips
$[-10,10]\times[0,1]$ m. Air–helium (after Quirk & Karni): post-shock air
$(\rho,v,p,T)=(1.6863\ \mathrm{kg/m^3},\ 113.515\ \mathrm{m/s},\ 1.5906\ \mathrm{bar},\ 328.54\ \mathrm K)$
for $x<-1.4$, a helium slab $[-1,1]$ ($0.223$ kg/m³, $\gamma=1.648$)
in air at 1.01 bar, $t=9.74$ ms. Water–gas: shocked water
$(1125.61\ \mathrm{kg/m^3},\ 220.87\ \mathrm{m/s},\ 0.4304\ \mathrm{GPa})$
($\gamma=4.4$, $p_\infty=6\times10^8$ Pa) for $x<-2.2$, a gas slab
$[-2,2]$ ($\gamma=2.4$) at 1.03 bar in water at rest, $t\approx8.27$ ms.
Their DG solution converges under refinement (25, 50, 100 elements/m)
to a finite-volume cut-cell reference; at equal element count degrees
1 and 3 beat degree 0 but look alike, and at equal degrees of freedom
the three agree up to slight differences, which the authors attribute
to the piecewise-constant structure of the solution (Figs. 10–13).

**The Quirk–Karni helium slab.** Two sources run the one-dimensional
air–helium problem of Quirk & Karni in non-dimensional form, a shocked
air state $(\rho,v_1,p)=(1.3765,0.3948,1.57)$ on the left, a helium slab
$\rho=0.138$ at rest with $p=1$ in air $(1,0,1)$, to $t=0.35$.
[Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.2.1 (arXiv v1)
place the shock at $x\le0.2$ and the slab on $[0.4,0.6]$ in a strip
$[0,1]\times[0,0.05]$ and carry a material marker $\chi$ (page-local),
$5/(3\gamma)$ in the helium; their $\mathbb P_2$ ADER-DG scheme in
primitive variables on $h=1/270$ "perfectly agree[s]" with a reference
Kapila-model solution on 20000 cells, while a conservative second-order
finite-volume scheme produces spurious pressure oscillations at the
interfaces even on $h=1/2690$ (Fig. 7).
[Trojak & Dzanic (2024)](/sources/trojak-2024.md) §5.1.3, Table 3 (arXiv
v1) place the shock at $x\le0.25$ and the slab on $(0.4,0.6]$
(helium $\gamma=1.67$, $c_v=2.52$; air $1.4$, $0.72$); their
conservative multi-species DG with entropy filtering ($\mathbb P_3$,
$N=50$, 100, 200) is in "excellent agreement" at $N=200$ with a
first-order Godunov reference on $5\cdot10^4$ elements, and the
pressure-equilibrium oscillations of conservative schemes "were not
visually noticeable" (Fig. 5). The left states are the Mach 1.22
post-shock state of the right one with $\gamma=1.4$
($\rho=1.3764$, $p=1.5698$, $v_1=0.3947$) *(compiler check, not in the
sources)*.

**Mach 1.22 air–helium (Haas & Sturtevant).** A Mach 1.22 shock in air
hits a helium bubble of diameter 5 cm. Nineteen sources run it, in several
models:

| Source | Model and scheme | Setup as printed | Grid |
|---|---|---|---|
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §5.1 | five-equation model, FV-WENO5 + HLLC ([MFC](/software/mfc.md)) | spherical bubble, axisymmetric; grid, CFL, $\gamma$ deferred to an earlier MFC paper | not printed |
| [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.6 | [five-equation model](/definitions/five-equation-model.md), unstructured CWENO5 + HLLC | $(\phi_1\rho_1,\phi_2\rho_2,v_1,v_2,p,\phi_1)$: pre-shock air $(0,1.204,0,0,101325,0)$, post-shock $(0,1.658,-114.49,0,159060,0)$, bubble $(0.158,0.061,0,0,101325,0.95)$, helium "contaminated by 28% air"; $\gamma=1.4$ (air), $1.66$ (helium); shock moving right to left | 2D mixed meshes $D_b/35$, $D_b/120$, $D_b/400$; 3D $D_b/50$; to $t=1000\,\mu$s |
| [Renac (2021)](/sources/renac-2021.md) §7.3 | [multicomponent Euler](/definitions/multicomponent-euler-equations.md), entropy-stable [DGSEM](/methods/dgsem.md), $N=3$ | $[0,6.5]\times[0,0.89]$ (unit = bubble diameter), shock at $x=4.5$ moving left, bubble at $(3.5,0)$, symmetry boundaries top and bottom; helium $\gamma=1.648$, $C_v=6.89$; air $\gamma=1.4$, $C_v=1.7857$; regularized initial interface | 238,673 unstructured elements |
| [Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.8, 5.10 | multicomponent Euler, entropy-stable FD on an [adaptive moving mesh](/methods/adaptive-moving-mesh.md) | $[0,445]\times[-44.5,44.5]$, bubble radius 25 at $(225,0)$, shock at $x=275$ moving left (speed $-415.16$); helium with 28 % air; air $(1.225,0,0,101325)$, post-shock $(1.6861,-113.5243,0,159060)$; $\gamma=1.4$, $1.647$ | 2D: $800\times160$ moving vs $2400\times480$ uniform; 3D: $400\times80\times80$ moving vs $800\times160\times160$ uniform |
| [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 10 | sharp interface: level set, conservative A-WENO | non-dimensional; pre-shock air $(\rho,v_1,v_2,p)=(1,0,0,1)$, post-shock $(1.3764,0.394,0,1.5698)$ for $x<-1.2$, helium $\rho=0.138$, $\gamma=5/3$ inside the unit circle | $280\times240$ |
| [Bai & Li (2022)](/sources/bai-2022.md) §3.4 | sharp interface: level set, ghost fluid and cut cells, DG of degree 2 with HLLC–HLL flux, adaptive quadtree | diameter 5 cm, upper half domain (symmetry); air $\rho=1.225$ kg/m³, $p=1.01325$ bar, $\gamma=1.4$; helium $\rho=0.2228$ kg/m³, $\gamma=1.648$ | background $720\times40$, two to four levels (AMR1–AMR4); to $983\,\mu$s |
| [Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) §5.2.5 | sharp interface: level set of Hu et al. in the finite-volume [JAX-Fluids](/software/jax-fluids.md); scheme settings not restated for this case | helium bubble of diameter 50 mm at the origin, shock 5 mm to its left, moving right; domain $[-90,266]\times[-44.5,44.5]$ mm; gas states not printed | not printed (arXiv v1) |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.16 | [five-equation model](/definitions/five-equation-model.md), finite-difference [gradient-based reconstruction](/methods/gradient-based-reconstruction.md) (MEG6, MIG4) and TENO5, HLLC | $(\rho,v_1,v_2,p,\gamma)$: post-shock air $(1.3764,-0.3336,0,1.5698/1.4,1.4)$, helium $(0.1819,0,0,1/1.4,1.648)$, pre-shock air $(1,0,0,1/1.4,1.4)$; $[0,6.5]\times[0,1.78]$ in diameters, bubble at $(3.5,0.89)$, shock at $x=4.5$ moving left; slip walls top and bottom; CFL 0.1 | $1300\times356$, $2600\times712$ (arXiv v2) |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.8 | two-species Euler with the double-flux method, six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) (WCNS-SA, WCNS-LD, ONL6) + HLLC | the same three states and geometry as Chamarthi, after Shankar et al.; zeroth-order extrapolation left and right, slip walls top and bottom, an artificial diffusion layer at the interface; CFL 0.5 | $\Delta x=D/150$ |
| [Huang & Johnsen (2023)](/sources/huang-2023.md) §4.4 | [five-equation model](/definitions/five-equation-model.md) with a [phase-field](/methods/phase-field-method.md) term, MUSCL–minmod + HLLC | $(\rho_1,\rho_2,v_1,v_2,p,\phi_1)$, phase 1 helium: pre-shock air and bubble moving at $v_1=114.49$, $(0.166,1.204,114.49,0,101325,\phi_1)$ with $\phi_1=10^{-15}$ outside and $1-10^{-15}$ in the bubble; air at rest $(0.166,1.658,0,0,159060,10^{-15})$ for $x>30$ mm; $[-44.5,44.5]^2$ mm, bubble radius 25 mm; $\gamma=1.67$ (helium), $1.40$ (air); zero-gradient left and right, reflecting top and bottom; CFL 0.4 | upper half, $200\times100$; to $983\,\mu$s |
| [Paula et al. (2023)](/sources/paula-2023.md) §7.6 | Baer–Nunziato model, [discrete equations method](/methods/discrete-equations-method.md) (RDEMIC) with time-averaged [THINC](/methods/thinc-reconstruction.md), WENO3, HLLC, multiresolution | half domain of height 44.5 mm and length 356 mm, shock at $x=40$ mm, bubble of diameter 50 mm at $x=90$ mm; post-shock air $(\rho,v_1,p)=(1.6573,114.5,159056)$, air $(1.2041,0,101325)$, helium $\rho=0.166$, $\gamma=5/3$ (Table 3); symmetry at axis and top, zero-gradient left and right | $8192\times1024$ effective, about 1150 cells per diameter |
| [Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.2.2 | two-gas Euler with marker $\chi$, ADER-DG $\mathbb P_2$ in primitive variables with a posteriori subcell FV limiting, conservative MUSCL–Hancock in shock-triggered subcells; polygonal meshes | $(\rho,v_1,v_2,p,\chi)$: pre-shock air $(1,0,0,1/\gamma,1)$, post-shock $(1.3764,-0.3336,0,1.5698/\gamma,1)$, helium $(0.1819,0,0,1/\gamma,1.648/\gamma)$, $\gamma=1.4$; $[0,7D]\times[-0.89D,0.89D]$, shock at $x=4.5D$ moving left, bubble at $(3.5D,0)$, radius printed $r_b=0.05$ with $D=1$ m; walls top and bottom | $h=1/30$, $1/75$, $1/150$ (arXiv v1) |
| [Jiao et al. (2024)](/sources/jiao-2024.md) §4.2, Table 4.3 | four-equation mass-fraction model, second-order compact FV, all-Mach flux, THINC on the gas mass fraction with EOS-consistent face density (THINC-TDU) | pre-shock air $(p,v_1,\rho)=(101325\ \mathrm{Pa},0,1.225\ \mathrm{kg/m^3})$, post-shock $(159059,\ 113.5\ \mathrm{m/s},\ 1.686)$, helium $(101325,0,0.169)$; air $\gamma=1.4$, helium $1.67$; $M=1.22$; walls top and bottom, zero gradient left and right | $14400\times1600$, cell $0.055625$ mm |
| [Trojak & Dzanic (2024)](/sources/trojak-2024.md) §5.1.4, Table 4 | conservative multi-species Euler, nodal DG $\mathbb P_3$ with positivity-preserving [entropy filtering](/methods/entropy-filtering.md) and a pressure-jump entropy switch ([PyFR](/software/pyfr.md)) | half of $[0,1]\times[-0.1,0.1]$ with symmetry; bubble radius $5/89$ at $(0.8,0)$, helium with 28 % air by mass; shock $M=1.22$ at $x=0.9$ moving left; air $(\rho,v_1,p)=(1,0,1)$, $\gamma=1.3986$; shocked air $(1.37636,-0.55957,1.5698)$; bubble $\rho=0.18187$, $\gamma=1.6467$ | unstructured triangles at three edge lengths (arXiv v1) |
| [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) §3.1 | multi-species Navier–Stokes in [OpenFOAM](/software/openfoam.md), kinetic-energy-preserving central flux plus Ducros-switched AUSM$^+$-up dissipation | helium circle $d=50$ mm in N$_2$ at $101325$ Pa, 273 K, shock moving right to left; shock Mach number not printed | three hexahedral grids, sizes not printed for this case |
| [Chen & Fu (2024)](/sources/chen-2024.md) §9.8 | single-material Euler ($\gamma=1.4$ throughout), [spectral differences](/methods/spectral-difference-method.md) of third and fourth order with TENO-A and WENO limiters | $(\rho,v_1,v_2,p)$: $(1,0,0,1)$ outside, bubble $(0.1819,0,0,1)$ of radius 0.5 at $(3.5,0.89)$, post-shock $(1.3764,-0.3947,0,1.5698)$ for $x\ge4.5$; $[0,6.5]\times[0,1.78]$; inflow and outflow left and right, reflective top and bottom; $t=2.5$ | $1300\times356$ |
| [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) Ex. 4.11 | Kapila [five-equation model](/definitions/five-equation-model.md), bound-preserving [OEDG](/methods/oedg.md) $\mathbb P^2$, $\mathbb P^3$, HLL, SSP-RK3, CFL $1/(2N+1)$ | $(\rho_1,\rho_2,v_1,v_2,p,\phi_1)$, phase 1 air ($\gamma_1=1.4$), phase 2 helium with 28 % air ($\gamma_2=1.648$): helium $(1.4,0.25463,0,0,10^5,10^{-6})$, pre-shock air $(1.4,0.25463,0,0,10^5,1-10^{-6})$, post-shock air $(1.92691,0.25463,-113.5,0,1.5698\times10^5,1-10^{-6})$; Mach 1.22 moving left; Haas–Sturtevant geometry in mm; walls top and bottom | $900\times267$; 32 to 983 µs after impact |
| [Chu et al. (2025b)](/sources/chu-2025-b.md) Example 3 | $\gamma$-based multifluid Euler in non-conservative form, LCD path-conservative central-upwind, second order, SSP-RK3, CFL 0.45 | $(\rho,v_1,v_2,p;\gamma,p_\infty)$: helium $(4/29,0,0,1;5/3,0)$, air $(1,0,0,1;1.4,0)$, shocked air $(4/3,-0.3535,0,1.5;1.4,0)$; $[-3,1]\times[-0.5,0.5]$, walls top and bottom, free left and right; $t=3$ | $\Delta x=\Delta y=1/500$ |
| [Nguyen et al. (2022)](/sources/nguyen-2022.md) §3.4 | multicomponent Euler in $p$–$T$ equilibrium, MUSCL with overbee limiter on volume fractions, HLLC | $325\times89$ mm; shock 25 mm from the bubble, moving right to left; pre-shock air $(\rho,p)=(1.4,10^5)$, post-shock $(1.92691,\ v_1=-114.42,\ 156{,}980)$; helium $\rho=0.25463$, $\gamma=1.648$ (SI values of their Table 3, whose column headers are misaligned with the rows) | $325\times90$, $650\times180$, $1300\times360$ (about 50, 100, 200 cells per diameter) |

The post-shock pressure ratio $1.5698$ of Zheng et al. is that of a
Mach 1.22 shock in air, $1+\frac{2\gamma}{\gamma+1}(M^2-1)$ with
$\gamma=1.4$ *(compiler check, not in the sources)*, and Tsoutsanis et al.'s and
Li et al. (2022c)'s $159060/101325=1.5698$ is the same, so these sources run
the same shock strength; they differ in the helium contamination, the
air state and the non-dimensionalization. Nguyen et al.'s post-shock
ratios, $156{,}980/10^5=1.5698$ and $1.92691/1.4=1.3764$, are the same
*(compiler check, not in the sources)*; Bai & Li print the pre-shock
states only. So are Paula et al.'s, $159{,}056/101{,}325=1.5698$ and
$1.6573/1.2041=1.3764$, and Huang & Johnsen's pressure ratio
$159060/101325$; their density ratio $1.658/1.204=1.3771$ differs from the
Mach 1.22 value $1.3764$ in the fourth digit *(compiler check, not in the
sources)*. Huang & Johnsen's frame has the pre-shock air and the bubble
moving at $114.49$ m/s towards gas at rest. Paula et al.'s shock reaches
the bubble at $59.7\,\mu$s, which equals the 25 mm gap divided by
$1.22\sqrt{1.4\cdot101325/1.2041}$ m/s *(compiler check, not in the
sources)*.

Chu et al. (2025b)'s shocked air, $(4/3,-0.3535,1.5)$ into $(1,0,1)$
with $\gamma=1.4$, is the Rankine–Hugoniot state of a Mach 1.195 shock
(pressure ratio 1.5 gives $M^2=1.4286$, and with it density ratio
$1.3333$ and speed $0.3535$), weaker than Haas & Sturtevant's Mach 1.22;
their helium density $4/29=0.1379$ is Zheng et al.'s $0.138$
*(compiler check, not in the sources)*. Yan, Abgrall & Wu's post-shock
density and pressure ratios, $1.92691/1.4=1.3764$ and $1.5698$, are the
Mach 1.22 values, while their speed $113.5$ is that of a Mach 1.22 shock
into air at $\rho=1.225$, $p=101325$ (their R22 case below), not into
their $\rho=1.4$, $p=10^5$, which gives $105.5$; Nguyen et al. print
$114.42$ for the same pre-shock state *(compiler check, not in the
sources)*.

Gaburro et al.'s non-dimensional states, with pressure $1/\gamma$ and
unit sound speed, are Zheng et al.'s with velocities scaled by the air
sound speed: $0.3947/\sqrt{1.4}=0.3336$ *(compiler check, not in the
sources)*; their helium state is Chamarthi (2023a)'s.

**A square N$_2$ bubble in SF$_6$.** Duronio & Di Mascio §3.1 also run a
square nitrogen bubble of edge $56.6$ mm in SF$_6$ on $[0,45]\times[0,14]$ cm
(three grids, $450\times140$ to $1800\times560$), against the
experiments of Zhai et al.; the shock Mach number is not printed. The
wave sequence (transmitted, free precursor and secondary shocks, Mach
stem, corner vortices, jet) matches the experiment from 82 to 1334 µs,
the interface width agrees "excellent[ly]" and the height is slightly
high after 0.75 ms (Figs. 4–5); see
[Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md).

**Mach 1.22 air–R22.** Bai & Li §3.4 also run Haas & Sturtevant's
heavy-gas case: an R22 cylinder ($\rho=3.8635$ kg/m³, $\gamma=1.249$)
of the same diameter in the same air, background $1600\times80$ with
four levels, times 55–1020 µs. The pressure contours and the positions
of the interfaces and of the incident, refracted and transmitted shocks
"almost coincide" with a front-tracking computation of Ullah et al.;
the interface carries a richer vortex head, secondary vortex and jet,
which the authors attribute to higher resolution (Figs. 27–30).
Paula et al. §7.6.2 run the R22 case (R22 $\rho=3.7975$ kg/m³,
$\gamma=1.249$) on the setup of their helium row. The feature trajectories
agree "excellent[ly]" with the experiment and with two computations,
except the late downstream centreline jet, which runs ahead of the
experiment; they attribute this to the missing viscous dissipation
(Fig. 22).

Yan, Abgrall & Wu (2024) Ex. 4.12 run the R22 case in the Kapila model
with phase 1 R22 and phase 2 air: R22 bubble
$(\rho_1,\rho_2,v_1,v_2,p,\phi_1)=(3.863,1.225,0,0,1.01325\times10^5,1-10^{-6})$,
pre-shock air $(3.863,1.225,0,0,1.01325\times10^5,10^{-6})$, post-shock
air $(3.863,1.686,-113.5,0,1.59\times10^5,10^{-6})$, Mach 1.22, on
$900\times267$ cells to $1020\,\mu$s; their result agrees with the
one-stage gas-kinetic computation they cite (Fig. 18). They print
"$\gamma_1=1.249$ and $\gamma_2=1.4$ for air and R22 bubble,
respectively", while in their data phase 1 is R22 and phase 2 air; the
values belong to R22 ($1.249$) and air ($1.4$) as in Bai & Li and Paula
et al. Chu et al. (2025b) Example 4 run R22 on their helium setup, with
bubble $(3.1538,0,0,1;1.249,0)$ at $t=3$.

[Huang et al. (2025b)](/sources/huang-2025-b.md) §4.3.2 run the R22
case in a five-equation model, with phase 1 R22 ($\gamma_1=1.249$) and
phase 2 air ($\gamma_2=1.4$): in $(\rho_1,\rho_2,v_1,v_2,p,\phi_1)$, the
bubble $(3.869,1.225,0,0,1.01325\times10^5,1-10^{-8})$ of radius 25 mm
about $(225,44.5)$ mm, pre-shock air the same with $\phi_1=10^{-8}$, and
post-shock air $(3.869,1.686,-113.5,0,1.59\times10^5,10^{-8})$ behind a
leftward Mach 1.22 shock at $x=275$ mm; $\Delta x=\Delta y=1/8$ mm, 400
cells per diameter, reflective top and bottom, schlieren of
$\log(1+\lvert\nabla\rho\rvert)$ (Figs. 15–18). Their deepMTBVD, which
replaces the [BVD](/definitions/boundary-variation-diminishing.md) selection
between MUSCL and [THINC](/methods/thinc-reconstruction.md) by a small
neural-network classifier, is comparable to MUSCL-THINC-BVD and sharper
than MUSCL; it classifies fewer cells as THINC than the BVD rule but
gives very similar results (§4.3.2). The states are Yan, Abgrall & Wu's
with the R22 density $3.869$ for $3.863$ and the volume-fraction floor
$10^{-8}$ for $10^{-6}$.

**Three-phase bubble.** Paula et al. §7.6.3–7.6.4 put a helium core of
diameter 30 mm inside an R22 shell of diameter 50 mm, in 2D and in 3D on a
quarter domain of $3072\times384\times384$ cells (431 and 259 cells per
outer and inner diameter). The global shape agrees with Pelanti &
Shyue's computation with much finer structure; like Pelanti & Shyue, they
find it notably different from Billaud Friess & Kokh's. In 3D the R22 jet
is faster and longer and the upstream wall moves more slowly than in 2D
(Figs. 23–25).

**Mach 6 air–helium interaction.** [Huang et al. (2026)](/sources/huang-2026.md)
§6.12, Eqs. (6.11)–(6.12), after a cited multiphase work: in
$(\rho,v_1,v_2,p,\gamma)$, pre-shock air $(1,0,0,1,1.4)$, post-shock air
$(5.268,5.752,0,41.83,1.4)$, helium $(0.138,0,0,1,1.667)$; the helium
bubble is given by the level set
$-0.025+\sqrt{(x-0.15)^2+(y-0.0445)^2}$, a circle of radius $0.025$
about $(0.15,0.0445)$; the shock starts at $x=0.1$;
domain $[0,0.356]\times[0,0.089]$, walls top and bottom, inflow left
and outflow right; multi-resolution grid with $L_{\max}=3$ levels and
finest $1024\times256$; snapshots at $t=0.006$, $0.012$, $0.018$,
$0.024$. [ROUND and LD-ROUND](/methods/round-scheme.md) are comparable to
WENO5-JS; ROUND is slightly more dissipative at the two later times and
LD-ROUND develops more complex vortical structures than WENO5-JS
(Fig. 17). The test is presented as evidence of robustness in
multiphase flow.

**Mach 2 air–hydrogen.** Renac §7.5 runs a Mach 2 shock in air
(pre-shock $T=1000$ K, $p=1$ atm, $v_1=1240$ m/s) on a hydrogen bubble
of diameter 5.6 centred at $(4,0)$ in $[0,22.5]\times[0,7.5]$ (unit
1 mm); hydrogen $\gamma=1.41$, $C_v=7.424$, air $\gamma=1.353$,
$C_v=0.523$; 74,504 unstructured elements, $t$ up to $13.6\,\mu$s. The
results "compare well" with three earlier computations, and the case is
offered as evidence of robustness on unstructured meshes (Fig. 8).

**Three-dimensional air–helium at 640 cells per diameter.**
[Wilfong et al. (2026)](/sources/wilfong-2026.md) §5.2 run a shock on a
helium bubble in air in 3D with [MFC](/software/mfc.md) on
$[0,20D]\times[-5D,5D]^2$ with $3200\times1600\times1600$ cells (more than
$8\times10^9$), 640 cells per diameter, to $t^*=tU/D=5.0$, in 16 h on 144
H200 GPUs (Fig. 20); the shock Mach number is not printed. The run is a
capability demonstration: the authors state that validation rests on
earlier work (§5.5).

**A strong shock on a light bubble across block interfaces.**
[Qin et al. (2023)](/sources/qin-2023.md) (§3.5.2, Eq. (41), Fig. 11) run a rightward strong shock with $(\rho,v_1,v_2,p)=(3.81,2.85,0,10)$ in $[-0.1,0]\times[-0.5,0.5]$. It
hits a light bubble $(0.1,0,0,1)$ of radius $0.2$ centred at $(0.3,0)$ in a gas $(1,0,0,1)$. The
domain is $[-0.1,1.6]\times[-0.5,0.5]$, with reflective walls top and bottom, a Dirichlet inlet and
supersonic outflow. It is split into four blocks of $270\times150$, $320\times150$, $270\times200$
and $320\times200$ points, with interfaces at $y=0$ and $x=0.8$. The test exercises their
[shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md) for a
multi-resolution WCNS. Contacts and small scales are "well resolved" at $t=0.2$ and $0.4$ across the
interfaces. The contours are not completely symmetric, because the grid spacing differs between
blocks.
[Fan et al. (2025b)](/sources/fan-2025-b.md) Eq. (54), after Čada &
Torrilhon, run the same data on a single $680\times400$ grid to $t=0.4$
(Fig. 16): their three-point WCNS3-MR-NN, whose nonlinear weights come
from a network trained to reproduce the weights of a multi-resolution
WCNS ([learned WENO weights](/methods/learned-weno-weights.md)), resolves
the bubble better than WCNS3-JS and WCNS3-MR (§4.4).

## Gas bubbles in liquids and stiffened gases

The heavy medium is now a liquid (water) or a stiffened gas and the
bubble a light ideal gas: the shock collapses the bubble instead of
being refracted by it.

- **Gas bubble collapse in water.** Tsoutsanis et al. §4.4, after two
  earlier computations: a Mach 1.72 shock in water,
  $(\rho,v_1,v_2,p,\gamma,p_\infty,\phi_1)$ post-shock
  $(1323.65,681.058,0,1.9\times10^9,4.4,6\times10^8,0)$, pre-shock
  $(1000,0,0,10^5,4.4,6\times10^8,0)$, air bubble
  $(1,0,0,10^5,1.4,0,1)$ of diameter $D_b=6$ mm at the centre of
  $[0,0.024]^2$ m, shock at $x=0.0066$ m; about $10^6$ quadrilaterals,
  edge $\approx D_b/250$, CWENO5, $t=6.2\,\mu$s. Peak pressure 7.7 GPa
  and peak temperature about 15,670 K; the earlier computations report
  10.1 GPa at $D_b/800$ and 7.8 GPa at $D_b/300$, a spread the authors
  attribute to resolution (Figs. 6–8).
  Bai & Li §3.5 run the same geometry (6 mm bubble, Mach 1.72 shock;
  water $\gamma=4.4$, $p_\infty=6\times10^8$ Pa) in a 12 mm square with
  post-shock water $(\rho,v_1,p)=(1322.47\ \mathrm{kg/m^3},\ 685.86\ \mathrm{m/s},\ 1.915\ \mathrm{GPa})$,
  four levels and 80 cells per diameter: the water jet forms at about
  $2.86\,\mu$s, hits the downstream bubble wall at about $3.053\,\mu$s
  and sends out a water-hammer shock at about $3.28\,\mu$s; the bubble
  height and width histories agree with Shukla's computation
  (Figs. 31–33). The two sources' post-shock states differ slightly
  ($1.9$ against $1.915$ GPa, $681.058$ against $685.86$ m/s).
  Paula et al. §7.7 run the same problem with a Mach 1.715 shock:
  post-shock water $(\rho,v_1,p)=(1323.65\ \mathrm{kg/m^3},\ 681.58\ \mathrm{m/s},\ 1.9\times10^9\ \mathrm{Pa})$,
  water at rest $(1000,0,10^5)$, air $(1,0,10^5)$, bubble of diameter
  6 mm at $x=12$ mm, shock at $x=6.6$ mm, domain of height 12 mm and
  length 24 mm, $4096\times2048$ cells (1024 per diameter), zero-gradient
  boundaries except at the axis (Table 4). HLLC develops shock
  instabilities in the gas inside the bubble, where the Mach number
  exceeds 2. HLLC-LM, applied only to the air–air Riemann problems,
  removes them; the authors read this as evidence that the discrete
  equations method can combine different Riemann solvers (Fig. 26; see
  [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)). The water
  jet hits the downstream bubble wall about $2.83\,\mu$s after the shock
  reaches the bubble ($3.69\,\mu$s absolute), "which agrees perfectly"
  with an earlier computation.
- **Mach 10 air-bubble collapse in water.** [Zhang et al. (2024a)](/sources/zhang-2024.md)
  §4.8 (Table 9) run the same geometry as Tsoutsanis et al. with a much stronger shock:
  domain $[0,0.03]\times[0,0.015]$ m, air bubble of diameter 6 mm at $(0.012,0.0075)$ m,
  shock at $x=0.0066$ m; post-shock water $(\phi_1\rho_1,v_1,p)=(1579,\ 5958.1\ \mathrm{m/s},\ 9.68\times10^{10}\ \mathrm{Pa})$
  ("approximately 100 GPa"), water at rest $(1000,0,10^5)$, air $1.2$ kg/m³; water
  $(\gamma,p_\infty)=(4.4,\ 6\times10^8\ \mathrm{Pa})$; extrapolation boundaries;
  $3840\times1920$ cells, $0.34$–$1.0\,\mu$s. *(Compiler check, not in the sources: mass and
  momentum balance give the shock speed $1579\cdot5958.1/579=16249$ m/s, ten times the water
  sound speed $1625$ m/s, and the jump $1000\cdot16249\cdot5958.1=9.68\times10^{10}$ Pa.)*
  Their WENO5IS-THINC scheme ([THINC](/methods/thinc-reconstruction.md)) reproduces the
  jet, the water-hammer shock and sheet jetting; the bubble outline converges over
  $960\times480$ to $3840\times1920$; the bubble mass over the domain is conserved exactly
  and the mass inside $\phi_1\le0.5$ converges towards zero error (Figs. 14–16(a)). The
  positivity- and boundedness-preserving limiter fires in more than 1 % of the cells with
  WENO-JS5 as base scheme, much less with TENO5, and never above 0.04 % with WENO5IS
  (Fig. 16(b)). They call the agreement with an earlier computation qualitatively good,
  describing their ref. [58] as a "front-tracking method"; that reference is the paper of
  the ALPACA level-set sharp-interface solver.
- **Underwater shock on a gas bubble.** Zheng et al. Ex. 11: pre-shock
  water $(\rho,v_1,v_2,p,\gamma,p_\infty)=(1000,0,0,1,7.15,3309)$,
  post-shock $(1176.3576,1.1692,0,9120,7.15,3309)$ for $x<-1.2$, gas
  $(1,0,0,1,1.4,0)$ in the unit circle; $280\times240$ cells; density at
  $t=0.06$, $0.19$, $0.357$, $0.471$, stopped before collapse (Fig. 15).
- **Ideal-gas bubble in a stiffened gas, Mach 10.** Li et al. (2022c) Ex. 5.9
  and 5.11 (3D): bubble $(\rho_1,\rho_2,v_1,v_2,p)=(0.05,4.95,0,0,100)$
  in a stiffened gas $(0.95,0.05,0,0,100)$, post-shock
  $(1.930198,0.05,-121.2497,0,29800)$ (Li et al. (2022c) write the trace
  partial density $0.05$ as a symbol and subtract it from the main one);
  stiffened gas $\gamma_1=3$, $p_{\infty,1}=100$, bubble gas
  $\gamma_2=1.4$; $t=0.8$ (2D), $0.64$ (3D).

- **A cloud of 75 bubbles.** Wilfong et al. (2026) §5.1 collapse 75
  randomly placed 3 mm air bubbles in water with a shock, on
  $[-9D,9D]\times[0,10D]^2$, $2000\times1000\times1000$ cells (about
  $2\times10^9$) stretched to 100 points per diameter, in about 30 min on
  1024 MI250X GCDs (Fig. 19), also as a demonstration.

[Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §6.1 show a
related illustration rather than a benchmark: a 40 MPa shock collapsing
a 20 µm air bubble inside a water-filled vessel in gelatin, with
qualitative claims only.

## Relativistic version

[Duan & Tang (2022)](/sources/duan-2022.md) Ex. 6.9 run a
three-dimensional shock–bubble problem for
[special relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)
with $\gamma=5/3$, after He & Tang: on $[0,325]\times[-45,45]^2$,
pre-shock $(\rho,v_1,v_2,v_3,p)=(1,0,0,0,0.05)$ for $x_1<265$,
post-shock $(1.865225080631180,\ -0.196781107378299,\ 0,\ 0,\ 0.15)$
for $x_1>265$, and a light bubble $(0.1358,0,0,0,0.05)$ in
$(x_1-215)^2+x_2^2+x_3^2\le25$; outputs at $t=90$ to $450$. Their
fifth-order entropy-stable scheme on an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) with
$325\times90\times90$ cells (2h14m44s) is comparable to the same scheme
on a uniform $650\times180\times180$ mesh (12h34m43s, so 17.8 % of the
CPU time), and gives sharper bubble interfaces than the second-order
moving-mesh scheme, "since the high-order accurate scheme has lower
dissipation" (Table 6.2).

## Non-conservative multiphase and shallow-water versions

[Balsara et al. (2024)](/sources/balsara-2024.md) §IX use the geometry
for systems with non-conservative products, computed with their
[FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md):

- **Baer–Nunziato shock–bubble** (§IX.a, Table IX, Fig. 11; after
  Dumbser and co-workers): domain $[-0.5,3]\times[-0.75,0.75]$,
  $700\times300$ zones, CFL 0.4, $t=0.025$; phases with stiffened-gas
  parameters $(\gamma_1,p_{\infty,1})=(3,100)$ and $(\gamma_2,p_{\infty,2})=(1.4,0)$;
  bubble of radius $0.25$ at $(0.5,0)$ with solid volume fraction 0.25
  against 0.75 outside; shock at $x=0$, left state
  $(\rho_1,v_1,p_1,\rho_2,v_2,p_2,\phi_1)=(1999.939402,\ 49.998485,\ 4999849.5,\ 1,\ 0,\ 1,\ 0.75)$,
  right and bubble states $(1000,0,1,1,0,1,\phi_1)$; Dirichlet left and
  right, periodic top and bottom ($\phi_1$ is the solid volume
  fraction).
- **Two-layer shallow-water shock–"bubble"** (§IX.c, Fig. 13) and
  **debris-flow shock–"bubble"** (§IX.e, Fig. 15), both new: the
  "bubble" is a smooth depression of the bottom,
  $b(r)=-0.25+0.25\tanh\big((r-0.25)/(2\Delta x)\big)$ (debris flow:
  amplitude 0.5) centred at $(0.5,0)$, hit by a bore at $x=0$;
  $700\times300$ (debris flow $700\times500$) zones, CFL 0.4, $t=0.30$.

Fifth and seventh order resolve the structures "much more crisply" than
third order, and the authors present the shallow-water and debris-flow
cases as genuinely new multidimensional tests (§IX).

## Findings across sources

**Agreement with the Haas–Sturtevant experiment.** Bryngelson et al.
report that the simulated velocities of the incident, reflected and
transmitted shocks, of the upstream and downstream interfaces and of
the jets are within 10 % of the measured ones, and generally within
about 5 % of the experimental means, with no spurious oscillations in
numerical schlieren (§5.1, Fig. 1). Tsoutsanis et al. average three
interface velocities (m/s) and find all within the experimental
variation (Table 2):

| Interface velocity | 2D fine | 3D | WENO5 of Coralic & Colonius (as quoted) | Experiment |
|---|---|---|---|---|
| upstream | 181.242 | 178.402 | 173 | $170\pm17$ |
| jet | 237.086 | 228.375 | 230 | $230\pm23$ |
| downstream | 145.895 | 144.197 | 145 | $145\pm15$ |

Bai & Li compare the space–time diagrams of the upstream, downstream
and jet points of the helium bubble, which converge over their four
adaptive grids, and density contours, which agree with the Haas &
Sturtevant shadowgraphs and with two computations (Figs. 22–24). Their
earlier zero-order cut-cell mixing and a DG cut-cell method with cell
merging and a Lax–Friedrichs flux give an interface evolution
"obviously delayed at later stage", and the latter fails at
$983\,\mu$s because cell merging cannot follow the topology change
(Fig. 25); the upstream and jet curves of Terashima & Tryggvason's
front-tracking/ghost-fluid computation are delayed with respect to
theirs as well (Fig. 26). Nguyen et al. find their upstream, jet and
downstream interface positions nearly identical on three grids and in
good agreement with the same Terashima & Tryggvason computation, and
the wave patterns in agreement with the shadowgraphs (Figs. 18–19);
they pick overbee over superbee on interface thickness and smoothness
(Fig. 17). The two sources thus place Terashima & Tryggvason's curves
differently relative to their own; neither measures against the
experimental velocities.

[Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) (§5.2.5, Figs. 17–18) find their
upstream, jet and downstream interface points "in very good quantitative agreement" with the same
Terashima & Tryggvason computation. Their schlieren images agree qualitatively with the
Haas–Sturtevant images and with a computation by the ALPACA code.
Three sources thus compare with Terashima & Tryggvason: Nguyen et al. and Bezgin et al. agree with it,
and Bai & Li find it delayed. Paula et al. find good agreement of the
helium case with the experiment and with three computations (§7.6.1,
Fig. 20).

**Four further codes against experiment or references.** Gaburro et
al. find that a second-order conservative ENO finite-volume scheme on
$h=1/750$ emits circular spurious pressure waves from the interface,
while their quasi-conservative $\mathbb P_2$ scheme on $h=1/150$
"completely avoids any spurious oscillations"; since both use the same
ENO reconstruction at limiter level, they ascribe the waves to the
conservative fluxes at the material interface, "not related to
Gibbs-like oscillations" (Fig. 8). The limiter acts at the interface and
the shock, the conservative update only in shock-triggered cells, and
the main structures converge over $h=1/30$ to $1/150$ (Figs. 9–10); see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md).
Jiao et al. find their THINC-sharpened interface in good agreement with
Quirk & Karni's results, including the space–time diagram of interface
points (Figs. 4.5–4.7), and use the case for their scaling tests.
Trojak & Dzanic find "very good agreement" of schlieren images at
$t=0.25$ and $0.39$ (426 and 674 µs) with Kundu's ninth-order upwind
finite-difference solution at roughly equal solution-point spacing
(Fig. 9). Duronio & Di Mascio's upstream and downstream interface
trajectories agree with the Haas–Sturtevant measurements ("excellent
agreement", Figs. 6–7); a three-grid Roache analysis along the axis gives
observed orders 1.35 ($p$) and 1.46 ($\rho$) and grid-convergence
indices of 1.1 % and 0.77 % for this bubble, 1.53 and 1.46 with 0.92 %
and 0.97 % for the square one (Table 1).

**Two-phase DG with bound preservation and LCD central-upwind
schemes.** Yan, Abgrall & Wu's $\mathbb P^2$ and $\mathbb P^3$ runs show
the jet, the vortex ring and the Kelvin–Helmholtz roll-up of the helium
interface (Figs. 15–17). Their scheme proves the cell averages of the
partial densities and internal energy positive and $\phi_1\in[0,1]$, and
preserves constant velocity and pressure across an isolated interface;
see [bound preservation](/properties/bound-preservation.md) and
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md).
Chu et al. (2025b) find the LCD scheme resolving the bubble interface
and its instabilities better than the scalar path-conservative
central-upwind scheme at all output times, in agreement with the
experiment and with the computations they cite (Figs. 5.4–5.5); they
state that the scheme satisfies Abgrall's principle on the
non-conservative multifluid system ("as one can easily prove",
Remark 5.2) and that the conservative form with $\rho/(\gamma-1)$ and
$\rho\gamma p_\infty/(\gamma-1)$ produces spurious oscillations at
interfaces.

**Limited spectral differences.** Chen & Fu's TENO-A limiter resolves more of the
single-material roll-up than the WENO limiter at third order, but the fourth-order TENO-A
does not significantly improve on the third-order result; their TENO troubled-cell
indicator marks only the fronts and tails of the interfaces and leaves the high-wavenumber
centre unmarked, and they judge it better than the KXRCF indicator here (§9.8, Figs. 23–25;
[adaptive TENO](/methods/adaptive-teno.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). *(Compiler check, not
in the sources: their states are Chamarthi (2023a)'s above with the pressures multiplied by $1.4$
and the velocity by $\sqrt{1.4}$, $0.3336\sqrt{1.4}=0.3947$, with a single $\gamma=1.4$, so
the "bubble" differs from its surroundings in density only.)*

**Holding a diffuse interface thin.** Huang & Johnsen's phase-field term
keeps the helium–air interface 4–5 cells thick for the whole run, with
the thickness parameter equal to $\Delta x$ (§4.4, Figs. 8–9). Without
it, a non-negligible amount of air diffuses into the helium bubble.
Initializing the volume fraction exactly at 0 and 1 produces negative
round-off volume fractions after a few steps, with or without the
phase-field term; the bounds $[10^{-15},1-10^{-15}]$ avoid it. Violating
their consistent reconstruction or flux computation of mass and volume
fraction creates mass spikes near the interface, up to $40\%$ in the second
case (§5.1, Figs. 10–12).

**Interface thickness at fixed grid.** Two chunk-5 sources run the same non-dimensional setup and
compare schemes on one grid. Chamarthi (2023a) (Ex. 4.16, Figs. 20–21) finds no noticeable spurious
oscillations with the author's gradient-based schemes, and a material interface thinner with MIG4 than with
MEG6 and TENO5. On $2600\times712$, more secondary instabilities appear at late times. Chamarthi (2023a) states that
TENO "for the 5-equation model, is not presented in the open literature"
([targeted ENO](/methods/targeted-eno.md)). Zhou et al. (§5.8, Figs. 19–20) find that WCNS-SA and
WCNS-LD capture more small-scale structures along the bubble than ONL6. *(Compiler check, not in the
sources: in both, the post-shock to pre-shock pressure ratio is $1.5698$ and the density ratio
$1.3764$, the Mach 1.22 values noted above; the helium density $0.1819$ differs from Zheng et al.'s
$0.138$.)*

Renac compares the space–time trajectories of three interface points
with the high-order computation of Kawai & Terashima, not with the
experiment, and finds "close agreement", without significant spurious
oscillations (Figs. 5–6). Bryngelson et al. and Tsoutsanis et al. thus
find their diffuse-interface schemes within the experimental scatter of
the measured kinematics; Renac's conservative multicomponent scheme
agrees with a reference computation.

**Resolution of the roll-up and symmetry.** In two dimensions the
Kelvin–Helmholtz roll-up of the interface sharpens with refinement from
$D_b/35$ to $D_b/400$, while the 3D mesh at $D_b/50$ does not capture it
(Tsoutsanis et al., Figs. 16–18). On the medium and fine unstructured
meshes the 2D solution loses its symmetry at late times, which the
authors attribute to the multidimensional reconstruction and the
arbitrary elements in the interaction zone; see
[symmetry preservation](/properties/symmetry-preservation.md).

**Cost of resolution.** Li et al. (2022c) find their moving-mesh runs better
than, or comparable to, uniform-mesh runs with three times (2D) or
twice (3D) as many cells per direction, at 26.2 % (2D helium), 23.6 %
(2D stiffened), 29.2 % (3D helium) and 18.0 % (3D stiffened) of their
CPU time; per step the moving mesh costs roughly 4.3–7 times the
uniform mesh with the same cell count, as their Table 5.3 shows (e.g.
1h4m against 9m12s on $800\times160$).

**Mass loss of a sharp interface.** Bai & Li delete isolated
structures smaller than half a cell, followed by reinitialization, and
record the resulting mass loss for helium and R22 at 180 and 360 cells
per diameter, which they call "weak" because deletion is rare (§2.5.3,
Fig. 6; see [level-set methods](/methods/level-set-method.md)).

**Sharp-interface start-up.** Zheng et al. first run the pure shock
until it settles into a "numerical shock" before it reaches the bubble,
to avoid the start-up error of a shock initialized as a discontinuity;
the main features are "correctly captured" with "high resolution", a
qualitative claim with no reference comparison (Figs. 13–15).

## Qualifications

- The settings share only the geometry; neither the equations nor the
  measures of success (interface sharpness in one dimension,
  interface kinematics against experiment, roll-up in two-material
  Euler, bubble collapse pressures in water, order comparisons for
  non-conservative systems) carry over between them.
- The Haas–Sturtevant setups differ in the helium state: Tsoutsanis et
  al. and Li et al. (2022c) model the contamination with air (28 % air), while
  Renac and Zheng et al. use a single helium gas with their own
  constants ($\gamma=1.648$ and $5/3$). Interface-velocity agreement is
  therefore model-dependent within the experimental scatter.
- Balsara et al. print the post-shock two-layer state with labels
  "$h_{1L},u_{1L},v_{1L},h_{1R},u_{1R},v_{1R}$" for what are the left
  states of both layers.
- Tsoutsanis et al.'s quoted Coralic & Colonius velocities come from a
  different code and are reproduced here as quoted, not as read.
- Qin et al.'s inflow state is not a Rankine–Hugoniot post-shock state of a $\gamma=1.4$ gas
  moving into $(1,0,0,1)$ *(compiler check, not in the sources: the mass and momentum jumps give
  shock speeds $3.86$ and $3.68$, and with the printed $\rho$ and $p$ a single shock would carry
  $v_1\approx2.58$, with $\gamma=1.4$, the value the paper fixes for its Euler tests in §3.4)*.
  The paper does not comment on the inflow state.
- Huang et al. (2025b) print inflow on the left and outflow on the right
  for a leftward shock whose post-shock state ($v_1=-113.5$ m/s) lies on
  the right, and call it "Example 6" in the Fig. 15 caption. Fan et al.
  (2025b) take Qin et al.'s inflow state unchanged, so the remark on it
  above applies to their run too *(compiler check, not in the sources)*.
- Trojak & Dzanic's Table 4 prints the shocked-air velocity as
  $-0.55957$; a Mach 1.22 shock into their quiescent air gives
  $\lvert v_1\rvert=0.3948$ ($\gamma=1.3986$) or $0.3947$ ($\gamma=1.4$),
  the value their own Quirk–Karni Table 3 uses, and their printed
  $\rho=1.37636$, $p=1.5698$ are the $\gamma=1.4$ values, not those of
  their $\gamma=1.3986$ *(compiler check, not in the sources)*. Their text
  also names the unit state "post-shock" and the Rankine–Hugoniot state
  "pre-shock", the reverse of the table and of the bubble's stated
  equilibrium with the surrounding air at $p=1$.
- Jiao et al.'s Table 4.3 prints the post-shock velocity as $+113.5$ m/s
  and its non-dimensional value as $-0.394$; $113.5/\sqrt{101325/1.225}=0.3946$,
  so only the sign differs *(compiler check, not in the sources)*.
- Gaburro et al. print the air density as $1.29\cdot10^{-3}$ kg/m³, which
  with $p=101325$ Pa gives a sound speed of about $10^4$ m/s instead of
  their $331.6$ m/s, which $1.29$ kg/m³ gives *(compiler check, not in
  the sources)*. Their output times are listed as
  $T^*+[0.584,\dots,5.754]$ for $t^*+[32,\dots,983]$ µs; the ratio
  $(t^*+\Delta t)/T$ is constant at about 183 µs while
  $\Delta t/\Delta T$ is not, so the list holds absolute dimensionless
  times, and their time scale $r_b/(cM)$ with the printed $r_b$, $c$ and
  $M$ gives 123.6 µs *(compiler check, not in the sources)*: one of the
  printed parameters is inconsistent, and the paper does not show which.
  Their Quirk–Karni "otherwise" state has six entries for a
  five-component vector.
- Gaburro et al. state that conservative schemes oscillate at material
  interfaces "even if run on a very fine mesh"; Trojak & Dzanic find the
  oscillations of their conservative DG "not visually noticeable" and
  expect them to reduce with resolution. The schemes differ (second-order
  finite volumes against entropy-filtered $\mathbb P_3$ DG), so the
  statements are not recorded as a contradiction.
- Duronio & Di Mascio's observed orders measure grid convergence of a
  solution with shocks and interfaces, not the design order of the
  scheme.
- The helium constants differ again: Huang & Johnsen take
  $\gamma=1.67$ and Paula et al. $5/3$. The post-shock water velocity of
  the bubble-in-water problem is printed as $681.058$ m/s by Tsoutsanis
  et al. and $681.58$ m/s by Paula et al., with the same density and
  pressure, and the shock Mach number as $1.72$ and $1.715$.
- Apart from the interface velocities of Tsoutsanis et al. and the
  feature velocities of Bryngelson et al., the evidence is from contour
  plots; no source reports an error norm.

# Citations

- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §5.2.1–5.2.2, Eq. (75), Figs. 7–10 (arXiv v1).
- [Jiao et al. (2024)](/sources/jiao-2024.md) — §4.2, Tables 4.3–4.4, Figs. 4.4–4.7.
- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §5.1.3–5.1.4, Tables 3–4, Figs. 5–9 (arXiv v1).
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — §3.1, Table 1, Figs. 1–7.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.1, Ex. 1, Fig. 5.1 (arXiv v2).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.12, Eqs. (6.11)–(6.12), Fig. 17.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.a, §IX.c, §IX.e, Table IX, Figs. 11, 13, 15.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §5.1, Fig. 1; §6.1 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.4, Figs. 6–8; §4.6, Table 2, Figs. 15–18.
- [Renac (2021)](/sources/renac-2021.md) — §7.3, Figs. 5–6; §7.5, Fig. 8 (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.8–5.11, Table 5.3 (arXiv v1).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §4, Ex. 10–11, Figs. 13–15.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.5.3, Fig. 6; §3.1.3–3.1.4, Figs. 10–13; §3.4, Table 4, Figs. 20–30; §3.5, Figs. 31–33.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §3.4, Table 3, Figs. 16–20.
- [Duan & Tang (2022)](/sources/duan-2022.md) — §6, Ex. 6.9, Table 6.2 (arXiv v1).
- [Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) — §5.2.5, Figs. 17–18 (arXiv v1).
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.16, Figs. 20–21 (arXiv v2).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.8, Eq. (43), Figs. 19–20.
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.5.2, Eq. (41), Fig. 11.
- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §4.4, Eq. (51), Figs. 8–9; §5.1, Figs. 10–12.
- [Paula et al. (2023)](/sources/paula-2023.md) — §7.6, Table 3, Figs. 20–25; §7.7, Table 4, Fig. 26.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §9.8, Figs. 23–25: single-material shock–bubble interaction with limited spectral differences.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §4.8, Table 9, Figs. 14–16: Mach 10 air-bubble collapse in water, mass conservation, limiter frequency.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Exs. 4.11–4.12, Figs. 14–18.
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — §5.1, Examples 1–4, Remark 5.2, Tables 5.1–5.2, Figs. 5.4–5.5.
- [Huang et al. (2025b)](/sources/huang-2025-b.md) — §4.3.2, Figs. 15–18.
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §4.4, Eq. (54), Fig. 16.
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §§5.1–5.2, 5.5, Figs. 19–20.
