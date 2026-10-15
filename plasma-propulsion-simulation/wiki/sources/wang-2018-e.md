---
type: Source
title: "Wang et al. (2018) — Form-finding of deployable mesh reflectors using dynamic relaxation method"
description: "Proposes a dynamic-relaxation form-finding procedure with kinetic damping for the cable nets of AstroMesh-type deployable reflectors, holding prescribed member forces constant so that the converged net has a uniform force distribution by construction, shown on a symmetric and an asymmetric 10 m reflector in MATLAB."
resource: "doi:10.1016/j.actaastro.2018.06.017"
source_kind: paper
authors: [Wang X., Cai J., Yang R., Feng J.]
year: 2018
venue: "Acta Astronaut. 151:380–388"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Form-finding_of_deployable_mesh_reflectors_using_dynamic_rel.pdf"
tags: [context, deployable-structures, mesh-reflector, form-finding, dynamic-relaxation]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper proposes a form-finding procedure for the cable nets of
deployable mesh reflectors of AstroMesh type (two parabolic triangular
nets joined by vertical tension ties, on a fixed boundary ring), based
on dynamic relaxation (DR) with kinetic damping. Its distinctive choice
is to prescribe the member forces and hold them constant during the
iterations (§3.2), so that the converged net has a perfectly uniform
force distribution by construction; the unknowns are the nodal
coordinates. The fictitious nodal masses are scaled from a maximum
nodal stiffness by a "coefficient of mass" $\lambda$ (Eq. 13), tuned by
trial and error. Two MATLAB examples (symmetric and asymmetric 10 m
reflectors, §5) converge to near-parabolic surfaces in 0.58 s and
1.33 s and are compared, by force ratio, with earlier optimisation and
force-density methods [1,27,31,32,33]. The paper has no plasma or
propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Dynamic relaxation** (§1, §6): DR turns the static equilibrium
   problem into a pseudo-dynamic one with fictitious mass and damping;
   it needs no tangent stiffness matrix and handles boundary
   constraints easily. Stated, attributed to [18–20].
2. **Equations** (Eqs. 1–3): $\mathbf M^t\dot{\mathbf v}^t+\mathbf C^t\mathbf v^t=\mathbf R^t$,
   with residual $\mathbf R^t=-\mathbf A^t\mathbf F^t$, nodally
   $\sum_{j\in\varphi}\frac{x_i-x_k}{l_j}F_j=R_{i,x}$ (likewise in $y$,
   $z$).
3. **Kinetic damping** (§3.1, Eqs. 10–12): undamped leapfrog velocity
   update (Eq. 11) and kinetic energy (Eq. 12); velocities are reset to
   zero at each kinetic-energy peak. The standard method, attributed to
   [20,25,30].
4. **Fictitious mass** (Eqs. 7, 9, 13): maximum nodal stiffness
   $S_i^t=\sum_{j\in\varphi}\left((E_jA_j)^t/L_j^0+F_j^t/L_j^t\right)$
   and mass $\Delta t^2S_i^t/2$, modified to $\lambda\Delta t^2S_i/2$
   with $\lambda$ chosen by trial and error (§3.2). The paper's stated
   modification.
5. **Constant forces** (§3.2–3.3): member forces are not updated by
   Eq. 8 during the iterations; axial stiffness is set to realistic
   values ("case (b)" of Zhang et al. [26]). The max/min force ratio is
   therefore exactly 1 in both nets (§5.1–5.2): imposed by construction,
   not an emergent property.
6. **Peak correction** (§4, Step 3.1): coordinates are corrected at a
   kinetic-energy peak by
   $x_i^{t+\Delta t}-\frac32\Delta t\,v_{i,x}^{t+\Delta t}+\frac12\Delta t^2R_{i,x}^t/M_{i,x}^t$,
   and the restart velocity is
   $R_{i,x}^{t+\Delta t}\Delta t/(2M_{i,x}^t)$ (Step 3.4).
7. **Symmetric example** (§5.1): converged in 0.58 s against 29.853 s
   for the authors' own implementation of the optimisation formulation
   of [27,32]; force ratio 1 against 1.24 and 1.38 with [27] and [32];
   force standard deviation 0.87 N for the comparison method against
   zero. Shown by single-run MATLAB timings.
8. **Asymmetric example** (§5.2): force ratio 1 in both nets against
   1.241 (front) and 1.240 (back) in [33] and 1 and 1.07 in [31]. The
   comparison values are quoted from, or re-run on, the cited methods.

# Methods

* Structural model (§2.1): pin-jointed cable members, no external load,
  slackening and yielding ignored, boundary-ring nodes fixed, topology
  given in advance.
* DR (§2.2): central-difference integration (Eqs. 4–6); the viscous form
  (Eq. 5) replaced by kinetic damping (Eqs. 10–12); fictitious masses
  from the maximum nodal stiffness with the mass coefficient (Eqs. 7,
  13). The force update Eq. 8 is written but not used.
* Algorithm (§4, Steps 0–7): initialise lengths, equilibrium matrix,
  residual, stiffness, masses and the initial half-step velocity;
  residual tolerance 0.01; loop over velocity, coordinate and
  kinetic-energy updates; at an energy peak correct the coordinates,
  recompute the residual with the fixed forces, test convergence and
  reset the velocities; otherwise update the geometry-dependent
  quantities; finally fit a paraboloid to the converged nodes.
* Implementation: MATLAB (§5); the hardware for the timings is not
  stated.

# Tests and results

* Symmetric reflector (§5.1, Figs. 1–7): an inscribed regular hexagon
  subdivided into equilateral triangles (side printed 0.1 m) mapped onto
  parabolic surfaces; aperture 10 m; initial focal length 6 m; minimum
  net separation 0.3 m. Prescribed forces 20 N in both parabolic nets
  and 5 N in the vertical cables; $E=20$ GPa, cable area 3.14 mm²,
  $\lambda=0.0003$, $\Delta t=1$. Converged in 0.58 s; the residual norm
  falls monotonically from about 150 to about 0 within about 500
  iterations (read from Fig. 4). Fitted surfaces (mm):
  $z=\frac{x^2+y^2}{21791.2}-96.99$ (front),
  $z=-\frac{x^2+y^2}{21791.2}+203$ (back); final focal length
  5.4478 m. On the 28 cables of one twelfth of a net (Figs. 6–7) the
  forces of [32] deviate from about −1.6 N to +3.2 N, those of the
  proposed method not at all.
* Asymmetric reflector (§5.2, Figs. 8–13): same geometry; forces 20 N
  (front net), 140 N (back net), 5 N (vertical cables); $\lambda=0.00137$,
  $\Delta t=1$; converged in 1.33 s within about 500 iterations (read
  from Fig. 11). Fitted surfaces (mm):
  $z=\frac{x^2+y^2}{22256.8}-84.88$ (front),
  $z=-\frac{x^2+y^2}{162733.9}-302.4$ (back); focal lengths 5.5642 m and
  40.6835 m.

# Notation map

The paper is structural mechanics; none of its quantities has a registry
counterpart.

| Wang et al. (2018) | Registry | Note |
|---|---|---|
| $t$, $\Delta t$ | words (pseudo-time and fictitious step of dynamic relaxation, $\Delta t=1$, unitless) | **collision:** registry $t$, $\Delta t$ are physical time and time step |
| $x$, $y$, $z$ | words (Cartesian nodal coordinates) | $z$ is the reflector axis, not the registry's thruster axial coordinate |
| $\mathbf v^t$, $v_{i,x}$ | words (fictitious nodal velocity) | **collision** with the particle velocity $\mathbf v$ |
| $\mathbf M^t$, $M_{i,x}$ | words (fictitious nodal mass) | |
| $\mathbf C^t$ | words (damping matrix) | |
| $\mathbf R^t$, $R_{i,x}$ | words (residual force) | **collision** with the friction force density $\mathbf R_{sk}$ |
| $\mathbf A^t$ | words (equilibrium matrix) | |
| $\mathbf F^t$, $F_j$ | words (member axial force) | **collision** with thrust $F$ |
| $l_j$, $L_j^t$, $L_j^0$ | words (member length, current and initial) | **collision** with the domain length $L$ |
| $E_j$, $A_j$ | words (elastic modulus, cross-sectional area) | **collision** with the electric field $\mathbf E$ |
| $S_i^t$ | words (maximum nodal stiffness) | **collision** with the shape function $S(\mathbf x)$ |
| $\lambda$ | words (coefficient of mass) | **collision** with $\lambda_D$, $\lambda_w$, $\lambda_{\mathrm{mfp}}$ |
| $KE^t$ | words (kinetic energy of the structure) | |
| $\varphi$ | words (set of members at a node) | not the potential $\phi$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Form-finding_of_deployable_mesh_reflectors_using_dynamic_rel.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 9 pages
     (380–388), IAA copyright.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.017, printed on page 1
     and checked on Crossref: title, all four authors, Acta Astronaut.
     151:380–388 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 17 Nov 2017, accepted 5 Jun 2018,
     online 15 Jun 2018 (no revision date). Page 1 matches the filename
     title.
   * **How it was read.** Full text layer; Eqs. 3–13 and the Step 0 and
     Step 3 formulas, garbled in the text layer, read on rendered pages
     2, 3, 6 and 7, all legible. Iteration counts read approximately from
     Figs. 4 and 11.
   * **Recorded as printed.**
     * Eq. 4 prints the central-difference acceleration with denominator
       2 instead of $\Delta t$; Eq. 11 is consistent with $\Delta t$.
     * Eq. 6 prints $\mathbf x^{t+\Delta t}=\mathbf x^{t-\Delta t}+\Delta t\,\mathbf v^{t+\Delta t/2}$;
       the leapfrog consistent with Eqs. 4 and 11 starts from
       $\mathbf x^t$.
     * Eq. 12 has no sum over nodes, though the text calls it "the
       kinetic energy of structure".
     * Step 0 (§4) takes the initial mass and $\lambda$ "by Eq. (12)"
       (the kinetic energy); the mass formula is Eq. 13 (or 9).
     * Step 3.1 uses the integer-step velocity $v_{i,x}^{t+\Delta t}$ in
       the peak correction, while velocities live at half steps
       elsewhere.
     * §3.3 chooses realistic axial stiffness so that the program can
       "adjust the forces", yet §3.2 and §4 keep the forces constant;
       the stiffness then enters only the fictitious mass (Eq. 7). The
       force ratio of 1 is an input, and §5 compares a method that
       imposes uniformity with methods that optimise toward it, as §6
       itself concedes.
     * §5.1–5.2 give a triangle side of 0.1 m on a 10 m aperture;
       Figs. 1, 2a, 8 and 9a show about ten triangles across the
       diameter, i.e. sides of about 1 m. One of the two is wrong.
     * §5.1 back-net fit "+203" (mm) puts the back vertex 300 mm above
       the front vertex (−96.99) and makes the nets intersect at
       mid-radius; Figs. 2b and 3 show the back vertex near −200 mm. The
       sign is likely a slip (−203 matches the figures and the
       asymmetric case's −302.4).
     * §5.1 assigns the ratios 1.24 and 1.38 to "Ref. [27and32]", while
       Fig. 7 compares only with [32]; the 0.87 N standard deviation is
       not assigned to a reference.
     * Reader's check: the focal lengths agree with the fit coefficients
       divided by 4 (21791.2/4 = 5447.8 mm; 22256.8/4 = 5564.2 mm;
       162733.9/4 = 40683.5 mm).
     * Reference list: [2] printed with year 2015 for J. Spacecr.
       Rockets 26 (vol. 26 is 1989); [19] (Day, "An Introduction to
       Dynamic Relaxation") printed as a Benjamin/Cummings 1965 book,
       while Day's paper is usually cited as The Engineer 219 (1965).
   * **Reference list.** 33 printed entries ([1]–[33]), matching the
     Crossref reference count.
