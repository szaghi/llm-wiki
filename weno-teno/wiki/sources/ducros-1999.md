---
type: Source
title: "Ducros et al. (1999) — Large-eddy simulation of the shock/turbulence interaction"
description: "Originates the Ducros dilatation–vorticity sensor as a factor of Jameson's pressure sensor in the second-order JST dissipation of a second-order skew-symmetric finite-volume central scheme, so that the shock-capturing term is confined to shocks while a filtered-structure-function subgrid model acts elsewhere; tested on decaying compressible turbulence, a 2D shock–vortex interaction and 3D LES of isotropic turbulence through a normal shock, with the finding that shock dissipation damps eddies as small as the captured shock width."
resource: "doi:10.1006/jcph.1999.6238"
source_kind: paper
authors: [Ducros F., Ferrand V., Nicoud F., Weber C., Darracq D., Gacherieu C., Poinsot T.]
year: 1999
venue: "J. Comput. Phys. 152:517-549"
local_file: "/home/stefano/papers/mosaic/weno-teno/1999_Crossref_Journal_of_Computational_Physics_Ducros_Large-Eddy_Simulation_of_the_ShockTurbulence_Interaction.pdf"
tags: [central-scheme, finite-volume, artificial-viscosity, troubled-cell, turbulence, shock-capturing, kinetic-energy-preserving]
timestamp: 2026-11-17T08:43:53Z
---

# Summary

Ducros et al. (1999) build a numerical tool for large-eddy simulation (LES) of the
interaction between turbulence and shocks: enough dissipation in the shock to capture it,
less than the subgrid model away from it. The scheme is the explicit, second-order,
collocated finite-volume central scheme of the NSMB multi-block solver, advanced by a
four-stage Runge–Kutta method, with the scalar artificial dissipation of Jameson, Schmidt
and Turkel (JST; [artificial viscosity](/methods/artificial-viscosity.md)) and the
filtered-structure-function (FSF) subgrid model. Three features distinguish it.

- **A large second-order coefficient and no fourth-order term.** $k_2=1.5$ makes the
  shock region "nearly TVD-like"; $k_4=0$ in the runs with the sensor product (the classical-JST comparisons keep $k_4=0.02$), because the subgrid model damps
  the small-scale oscillations that the fourth-order term is meant to remove.
- **A flux of the means.** The central flux of the mean state, written for the model law
  $\partial_ta+\partial_x(ab)=0$, is the second-order skew-symmetric (half divergence, half
  product-rule) form, in conservation form ([split convective forms](/methods/split-convective-forms.md)).
- **The sensor.** Jameson's pressure sensor is multiplied by the dilatation–vorticity ratio
  $\Phi_{\mathrm D}=(\nabla\cdot v)^2/((\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D})$,
  which the authors call a "modified Jameson's sensor" and later sources the
  [Ducros sensor](/definitions/ducros-shock-sensor.md). It is Galilean invariant and switches
  the second-order dissipation off in vortical, weakly compressible regions.

The tests are decaying compressible isotropic turbulence on $32^3$
([compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)),
a Lamb–Oseen vortex through a stationary shock in 2D
([shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)) and 3D LES of
isotropic turbulence convected through a Mach 1.2 normal shock
([shock–turbulence interaction](/benchmarks/shock-turbulence-interaction.md)). The
classical JST dissipation is too dissipative for LES; with the sensor product the LES
without artificial dissipation is recovered off-shock. Inside the shock, the
shock-capturing dissipation still damps eddies of the size of the captured shock (about
three cells), so the shock-normal mesh must be refined, or the field pre-filtered, until
the smallest resolved energetic eddies are larger than the shock width. The paper also
argues against monotone-integrated LES (MILES), the use of numerical dissipation as the
subgrid model ([implicit LES](/definitions/implicit-large-eddy-simulation.md);
[numerical dissipation](/definitions/numerical-dissipation.md)).

# Version read

Version of record, J. Comput. Phys. 152:517–549 (Academic Press), 33 pages, all read.
Page 1 prints "Article ID jcph.1999.6238" and no DOI; the DOI 10.1006/jcph.1999.6238 is the
Academic Press article-ID form already in the bibliography. Received April 30, 1998; revised
February 4, 1999. The text layer maps Greek letters to digits ($\Psi\to9$, $\Phi\to8$,
$\Delta\to1$, $\epsilon\to2$, $\Theta\to2$, $\Xi\to4$), so the equations of pp. 520–524 and Eq. (29)
(p. 544) were read from page renders, as were Figs. 10–11 and 24. Bundle label: Ducros et al.
(1999). The authors are at CERFACS, Toulouse (Ferrand and Poinsot also IMFT; Nicoud's present
address CTR, Stanford). The earlier bibliography entry listed six authors and "others"; page 1
has a seventh, Poinsot T.

# Key claims

Registry notation (see the notation map). Page-local: JST constants $k_2$, $k_4$ and
coefficients $\varepsilon_{2,i+1/2}=k_2\,(\text{sensor})_{i+1/2}$, $\varepsilon_{4,i+1/2}=\max(0,k_4-\varepsilon_{2,i+1/2})$
with the spectral radius $a_{i+1/2}$ factored out of the dissipation term
$\mathcal D_{i+1/2}$, as on [artificial viscosity](/methods/artificial-viscosity.md) (the paper
puts it inside, $\epsilon^{(2)}=k^{(2)}\mathcal R\Psi$; the flux is the same); Jameson's pressure
sensor $\varphi_{\mathrm J}$; turbulent Mach number $M_t$; upstream Mach number $M_1$;
Reynolds stresses $\mathsf R_{ij}$; captured shock width $\lambda_{\mathrm{sh}}$; LES cut-off
length $\Delta_c\approx2\Delta$; smallest resolved energetic scale $L_{uvw}$; eddy viscosity
$\nu_{\mathrm{sgs}}$; energy spectrum $E_k(k_w,t)$.

1. JST flux of the solver (§3, Eqs. (8)–(13), as described in Jameson et al. [42]): $\hat f_{i+1/2}=f\big(\{\!\{u\}\!\}_{i+1/2}\big)-a_{i+1/2}\big[\varepsilon_{2,i+1/2}(u_{i+1}-u_i)-\varepsilon_{4,i+1/2}(u_{i+2}-3u_{i+1}+3u_i-u_{i-1})\big]$, $\varepsilon_{2,i+1/2}=k_2\varphi_{\mathrm J,i+1/2}$, $\varepsilon_{4,i+1/2}=\max(0,k_4-\varepsilon_{2,i+1/2})$, $\varphi_{\mathrm J,i}=\lvert(p_{i+1}-2p_i+p_{i-1})/(p_{i+1}+2p_i+p_{i-1})\rvert$, $\varphi_{\mathrm J,i+1/2}=\max(\varphi_{\mathrm J,i},\varphi_{\mathrm J,i+1})$, $a_{i+1/2}$ the spectral radius of the flux Jacobian at the face. **Stated** (recalled)
2. Choice of $k_2$ (§3, pp. 522–523): after Swanson & Turkel, $k_2\varphi_{\mathrm J}\approx0.5$ makes the scalar scheme close to first-order upwind; for their test case $\varphi_{\mathrm J}$ is "typically around 0.15", so the steady-flow value $k_2=0.5$ ($k_2\varphi_{\mathrm J}\approx0.075$) leaves spurious oscillations in unsteady runs, and $k_2\varphi_{\mathrm J}\approx0.25$, "half the theoretical value", suppresses them: $k_2=1.5$, "a nearly TVD-like scheme in regions of sharp pressure gradient". **Stated** (empirical check, not shown) *(Compiler check, not in the source: $1.5\times0.15=0.225\approx0.25$.)*
3. $k_4$ "can be set to zero" in LES because the oscillations it damps develop at small scales, where the subgrid model damps them (§3, §6). The artificial and subgrid dissipations are both nonlinear and both needed, "the SGS dissipation being unable to sustain density and pressure discontinuities" (§3). **Stated**
4. Flux of the means (§3, Eqs. (14)–(21)): for $\partial_ta+\partial_x(ab)=0$ on a regular mesh the mean of the fluxes $\{\!\{ab\}\!\}_{i+1/2}$ gives the centred divergence form (18), and the flux of the means $\{\!\{a\}\!\}_{i+1/2}\{\!\{b\}\!\}_{i+1/2}$ gives $\frac{da_i}{dt}+\tfrac12\frac{(ab)_{i+1}-(ab)_{i-1}}{2\Delta x}+\tfrac12a_i\frac{b_{i+1}-b_{i-1}}{2\Delta x}+\tfrac12b_i\frac{a_{i+1}-a_{i-1}}{2\Delta x}=0$, "a skew-symmetric form of second-order" (page-local $a$, $b$ for the paper's $U$, $\psi$). **Derived** *(Compiler check, not in the source: expanding $4(\hat f_{i+1/2}-\hat f_{i-1/2})$ gives exactly Eq. (21).)*
5. The skew-symmetric form reduces aliasing errors, conserves kinetic energy for incompressible flow (after [45], [26]) and is "compatible with the conservative discretization of Eq. (15), a property of crucial importance to ensure the shock capturing capability" (§3, p. 524). **Stated**
6. Compressible adaptation (§3, p. 524): for the $\rho v_kv_l$ terms both factors are set to $\rho v$ and the flux is divided by the mean density, i.e. $\{\!\{\rho v_k\}\!\}\{\!\{\rho v_l\}\!\}/\{\!\{\rho\}\!\}$. **Stated** *(Compiler check, not in the source: this is the convective part of $f(\{\!\{u\}\!\})$ in claim 1; its velocity factor is the density-weighted mean $\{\!\{\rho v_k\}\!\}/\{\!\{\rho\}\!\}$, not $\{\!\{v_k\}\!\}$, so the exact identity of claim 4 holds only for the incompressible model term; see [kinetic energy preservation](/properties/kinetic-energy-preservation.md).)*
7. Second order is defended against Ghosal's analysis: low-order methods are common in complex geometries; the centred skew-symmetric scheme is non-dissipative, so the model's dissipation is effective; the problems treated are not caused by aliasing or dispersion, so the improvements "will certainly hold for the use of an higher-order centered scheme" (§3, p. 522). **Stated**
8. The sensor (§3, Eqs. (22)–(24)): $\Phi_{\mathrm D}=(\nabla\cdot v)^2/\big((\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}\big)$, $\epsilon_{\mathrm D}=10^{-30}$ "to prevent numerical divergence in regions where both $\nabla\cdot\mathbf u$ and $\omega$ are zero"; it "varies between 0 for weakly compressible regions to about 1 in shock regions". The "modified Jameson's approach" uses $\varepsilon_{2,i+1/2}=k_2\max\big(\varphi_{\mathrm J,i}\Phi_{\mathrm D,i},\ \varphi_{\mathrm J,i+1}\Phi_{\mathrm D,i+1}\big)$: the face value is the maximum of the two cell products, and $\Phi_{\mathrm D,i}$ "is simply a local evaluation of Eq. (22)" (the discretization of $\nabla\cdot v$ and $\nabla\times v$ is not printed). **Stated** (definition)
9. Motivation (§3, pp. 524–525): earlier corrections that shrink the dissipative region (an entropy-like quantity, a monotone function of the local Mach number multiplying the scaling factor, Crumpton & Shaw's shock-region flag set before each Runge–Kutta step) add "a new source on non-Galilean invariance" when based on the Mach number; $\Phi_{\mathrm D}$ "conserves the Galilean invariant property of the sensor" and is a smooth correction "proportional to the level of local compressibility". The JST scheme itself is "no longer Galilean invariant due to the artificial viscosity", so $k_2$, $k_4$ hold in the shock frame, in which every run with a shock is made (§4.2, p. 532). **Stated** *(Compiler check, not in the source: through the spectral radius $\lvert v\rvert+c$, which is not Galilean invariant.)*
10. Why the product stays small off-shock (§4.1, Figs. 5–6, THI-4): during the decay the mean and rms of $\varphi_{\mathrm J}$ decrease while those of $\Phi_{\mathrm D}$ increase; the product is small "not only due to the low values of each component … but also due to their relatively weak correlation". **Shown**
11. Decaying turbulence (§4.1, Table I, Figs. 1–3): THI-2 ($k_2=1.5$, $k_4=0.02$, $\varphi_{\mathrm J}$) is "clearly too dissipative", the energy near the cut-off falling "by more than a decade"; THI-3 ($k_4=0$, $\varphi_{\mathrm J}$) still perturbs the subgrid model, especially early when the cut-off energy, and hence the FSF dissipation, is nearly zero; THI-4 ($k_4=0$, $\varphi_{\mathrm J}\Phi_{\mathrm D}$) "gives the same results as the standard LES" without artificial dissipation (THI-1). Kinetic energy decays as $t^{-1.4}$ after the enstrophy peak in THI-1 to THI-4. **Shown**
12. Without subgrid model and dissipation (THI-5) the skew-symmetric scheme diverges in inviscid decaying compressible turbulence ($M_t\approx0.13$ initially): "the skew-symmetric form by itself is not sufficient to sustain such a simulation of compressible turbulence"; it "would be sustained for a truly incompressible regime" (not run). With the sensor-weighted second-order dissipation and no model (THI-6) the spectrum becomes $k_w^2$, "symptomatic of an equipartition equilibrium": the second-order dissipation prevents divergence but does not act as a subgrid model (§4.1, Fig. 1). **Shown** (the incompressible remark **Stated**)
13. Numerical dissipation of second and fourth order "always brings a spurious dissipation, too large when the fourth order is employed and too weak when the second order alone is employed. In consequence, it is not able to mimic the dissipation of a true subgrid-scale model, and therefore is not well adapted to LES" (§4.1), in agreement with Garnier et al. [50]. **Stated** (from THI-2, THI-3, THI-6)
14. MILES critique (§1): with piecewise-parabolic or MILES approaches numerical dissipation can exceed the subgrid dissipation [21], possibly because shock-capturing schemes fall to first order in the shock; and "built-in numerical dissipation is unable to vanish in near-wall regions as SGS dissipation does", a "major drawback of the MILES approach" that may limit it to free shear flows. **Stated**
15. Comte-Bellot–Corrsin decay at $M_t=0.26$ (§4.1, Figs. 7–8): FSF-LES without artificial dissipation (CBC-1) has about 20% energy error at $t/t_0=4.07$; the sensor product (CBC-2) stays close to CBC-1 and classical JST with $k_4=0.02$ (CBC-3) does not; the larger CBC-1/CBC-2 gap than THI-1/THI-4 is attributed to the higher $M_t$. **Shown**
16. 2D shock–vortex interaction (§4.2, Table II, Figs. 9–11): a Lamb–Oseen vortex (maximum tangential velocity $0.16U_{\mathrm{ref}}$) crosses a stationary shock at $M_1=1.2$ ($U_1=1.42U_{\mathrm{ref}}$) on $128\times16$, $256\times32$, $512\times64$, without subgrid model. Classical JST with $k_4=0.02$ loses enstrophy before and after the shock on the two coarser grids (VS-1, VS-2); the sensor product "maintains a plateau for enstrophy in both the pre- and post-shock regions"; the growth through the shock, compared with $\omega_2/\omega_1\approx\rho_2/\rho_1=U_1/U_2$ (Eq. (25), after Mahesh et al.), improves with resolution and with the sensor product; the vortex becomes elliptic, as LIA predicts. "Expected results are qualitatively and quantitatively recovered in all cases" ($M_1=1.1$–1.7). **Shown** *(Compiler check, not in the source: the Fig. 11 plateaus read about 1.17, 1.32, 1.62, 2.05 for $M_1=1.1,1.2,1.4,1.7$, against $\rho_2/\rho_1=1.169,1.342,1.690,2.198$ for $\gamma=1.4$; within about 2% up to $M_1=1.2$ and 4–7% low at 1.4 and 1.7.)*
17. 3D shock/turbulence LES (§4.3, Table III, Figs. 12–20): box $(2,1,1)L_{\mathrm{ref}}$, periodic in $y$, $z$, stationary shock near $x=1$, $M_1=1.2$, inflow from the decaying-turbulence LES through Taylor's hypothesis ($M_t\approx0.075$, $\sqrt q/U_1\approx0.06$), $L_{uvw}=L_{\mathrm{ref}}/16$, infinite Reynolds number, FSF on; grids $64\times32\times32$ (ST-1, ST-2), $262\times32\times32$ refined to $\Delta x\approx\tfrac18L_{\mathrm{ref}}/32$ from before the shock to the outflow (ST-3, ST-4), $156\times32\times32$ refined around the shock (ST-5); ST-1, ST-3 classical JST with $k_4=0.02$, ST-2, ST-4, ST-5 the sensor product with $k_4=0$. **Stated** (setup)
18. Only the sensor product gives a pre-shock turbulent-kinetic-energy decay consistent with homogeneous decay under Taylor's hypothesis, at either resolution; the standard Jameson sensor dissipates spuriously (ST-1, ST-3) and gives a spurious pre-shock vorticity decay; pre-shock $M_t$ falls from 0.075 to 0.061 (ST-1, ST-3) or 0.068 (ST-2, ST-4) (§4.3.3–4.3.4, Figs. 16–17, 19–20). **Shown**
19. Reynolds-stress growth across the shock to $x\approx1.4$ (Table IV): $\mathsf R_{11}$ +19% (DNS of Lee et al. 1993), +34% (LIA), +25% (ST-2), +37% (ST-4), +41% (ST-5); $\mathsf R_{22}$ +4.4%, +10%, 0%, +6%, +6%. Transverse vorticity variance +85% (ST-4), +80% (ST-5) against 60–80% (DNS) and about 80% (LIA); the streamwise vorticity variance is nearly unchanged in ST-1, 3, 4, 5 but decreases in ST-2 (§4.3.3–4.3.4). **Shown** (DNS and LIA values read from figures of [7], [6])
20. Off-shock the subgrid dissipation dominates, but the standard second-order dissipation "can be non-negligible (around 10%)"; with $\Phi_{\mathrm D}$ it falls to "a negligible level"; in the shock the numerical dissipation dominates the subgrid dissipation, "leading to a weak influence of the subgrid scale modeling in such regions, at least for the numerical scheme used here" (§4.4, Fig. 24, ST-2 and ST-5); "These conclusions hold for regions where the grid is refined" (p. 543). **Shown** *(Plot reading, not in the text: off-shock the sensor-weighted term lies about $10^{-8}$–$10^{-12}$ against about $10^{-4}$ for the subgrid term, log scale.)*
21. $\Phi_{\mathrm D}$ alone at the level 0.1 "selects small scales and theoretically allows some dissipation", but its weak correlation with $\varphi_{\mathrm J}$ keeps the product low; the levels 0.5 and 0.8 select the shock region, with holes at 0.8 that even reduce the Jameson value inside the shock (§4.4, Fig. 23). **Shown**
22. Spectral argument (§5, Eq. (29)): for an equivalent incompressible flow the dissipations act like $\nu_{\mathrm{sgs}}k_w^2E_k$, $\nu_2k_w^2E_k$ and $\nu_4k_w^4E_k$ (page-local $\nu_2$, $\nu_4$ for the JST coefficients used as viscosities), "which explains why the use of the fourth-order dissipation is so crucial for small scales damping and can rapidly lead to an over-dissipative behaviour when the coefficient is a priori fixed". **Derived** (heuristic)
23. Scale separation (§5, §6): the second-order term captures the shock within about three points, $\lambda_{\mathrm{sh}}\approx\Delta_c$ on the coarse grid; when the smallest resolved energetic eddies reach the shock with $L_{uvw}\sim\lambda_{\mathrm{sh}}$ (ST-2, $\approx L_{\mathrm{ref}}/16$) the shock-capturing dissipation damps them: lower growth of kinetic energy, $\mathsf R_{ii}$ and transverse vorticity, and a spurious drop of streamwise vorticity. The refined grids separate the scales ($\lambda_{\mathrm{sh}}\approx3/(8\cdot32)L_{\mathrm{ref}}$). Remedies: local automatic mesh refinement (expected to give ST-5 quality) or pre-filtering the resolved field to a cut-off larger than the shock width. **Shown** (ST-2 against ST-4, ST-5) and **Stated** (remedies)
24. Refining well upstream of the shock lets infinite-Reynolds-number turbulence cascade into the new scales ($k_{c1}\approx32/L_{\mathrm{ref}}\to k_{c2}\approx8\cdot32/L_{\mathrm{ref}}$) and raises both vorticity components independently of the shock (ST-3, ST-4); refining only at the shock (ST-5) avoids it (§4.3.4, §5). **Shown**
25. Conclusions (§6): the sensor is "frame independent, easy to implement in a parallel code, and relatively costless" (no cost figure); the amplification is slightly higher than published DNS, "which may be due to the absence of molecular viscosity and to the reduced numerical dissipation"; the scale-separation conclusion "is taken from simulations using second order methods and may be modified when using higher order numerical schemes". **Stated**

# Printed slips

- **Flux sign convention.** Eqs. (5)–(7) write $\partial_t\bar U=+\sum_i\partial_{x_i}\bar F_i$ with $\bar F_i$ minus the physical flux (first row $-\bar\rho\tilde u_i$), while Eq. (8) $F_{j+1/2}=F(\text{mean})-d_{j+1/2}$ with $d=\epsilon^{(2)}(U_{j+1}-U_j)-\dots$ is dissipative only for the physical flux and the update $\partial_tU+(F_{j+1/2}-F_{j-1/2})/\mathcal V=0$ of Eq. (15). *(Compiler check, not in the source: with $F=-f$, Eq. (8) adds $+\epsilon^{(2)}(U_{j+1}-U_j)$ to the physical flux, the anti-dissipative sign.)*
- Eq. (7), energy row of $\bar F_i$: the conduction term is printed $\lambda(\tilde T)\,\partial\tilde T/\partial x_j$; in the flux of direction $i$ it should be $\partial\tilde T/\partial x_i$.
- §2: the subgrid heat flux is defined with $C_p$, $Q_j=-\bar\rho C_p\tilde u_j\tilde T+\overline{\rho C_pu_jT}$, and modelled with $C_v$, $Q_i=-\bar\rho C_v\kappa_t\,\partial\tilde T/\partial x_i$.
- p. 524: "$\Psi_i$ is given by Eqs. (13)" (the cell value is Eq. (12)); "adding a correction to the sensor described in Eq. (9)" (the sensor is Eqs. (12)–(13); Eq. (9) is the dissipation).
- p. 524, compressible adaptation: "setting $U_j$ (respectively $\psi_j$) to $\bar\rho\tilde u_j$ (respectively $\bar\rho\tilde u_j$)" prints both factors alike, with $j$ as grid and component index; "the local flux $F_{j-1/2}$ of Eq. (20) being divided by the mean density $(\bar\rho_j+\bar\rho_{j+1})$" has the indices of $F_{j+1/2}$ and twice the mean.
- The grid index changes from $j$ (Eqs. (8)–(21)) to $i$ (Eqs. (23)–(24)).
- §4.1: "$t\approx15U_{\mathrm{ref}}/L_{\mathrm{ref}}$" and "28 and $19U_{\mathrm{ref}}/L_{\mathrm{ref}}$": units inverted (elsewhere $L_{\mathrm{ref}}/U_{\mathrm{ref}}$). The two estimates are mutually consistent ($28/19\approx5.9/4$).
- Eq. (29) prints the fourth-order term as $2\epsilon^{(4)}k^4/k_c^2$, while the text below says it acts like $\epsilon^{(4)}k^4E(k,t)$; the transfer term is $T^{k<k_c}$ in the equation and $T^{k\langle k_c}$ in the text.
- §4.4 is titled "A Posteriori Test on the Modified Sensor", while the Abstract ("A priori testing shows"), §1 ("A priori tests … are provided in Subsection 4.4") and §5 ("as confirmed by a priori testing") call the same analysis a priori. §4.4 opens on ST-2 and ST-4 (Figs. 21–22), while Fig. 24 uses ST-2 and ST-5.
- Reference [54] (M. J. Lee, Kim & Moin, "Turbulence structure at high shear rate") is cited for the LIA values of Table IV ("LIA results are estimated from Lee et al. [54]", p. 537) and for a grid refinement that recovers DNS with shock capturing (p. 535); neither fits a homogeneous-shear paper, and the Table IV note sources the LIA values from Fig. 4 of [7].
- §3: "$\epsilon^{(4)}$ can be set to zero for two reasons … The second reason is given below", but no second reason is labelled as such.
- Eq. (22) writes $\nabla\cdot\mathbf u$ (unfiltered) beside $\boldsymbol\omega=\nabla\wedge\tilde{\mathbf u}$ (filtered), and $(\boldsymbol\omega)^2$ for $\lvert\boldsymbol\omega\rvert^2$.
- Fig. 11 against "quantitatively recovered in all cases": see claim 16.
- Typos: "meshs", "accross" (Abstract); "mentionned" (p. 523); "eqations" (§2); "doted" (Fig. 10 caption); "steamwise" (Fig. 14 caption); "approximatively" (p. 538); "stimulations" (Figs. 16, 18 captions); "Mt ≈ 0, 13" (decimal comma, §4.1); "Schock" (ref. [15]); "Standford" (refs. [23], [44], [55]).

# Notation map

| Ducros et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$ (Eqs. (8)–(21)), $i$ (Eqs. (23)–(24)) | $i$ | grid index; the paper switches letters |
| $\bar U=(\bar\rho,\bar\rho\tilde u_i,\bar\rho\tilde e)$ | $u=(\rho,\rho v,E)$ | filtered and Favre-filtered; $\tilde e$ is the specific **total** energy, $\bar\rho\tilde e=E$ (registry $e$ is internal) |
| $\tilde u_i$, $\mathbf u$ | $v_i$, $v$ | velocity |
| $\bar F_i=F_i(\bar U)$ | $-f^{(i)}(u)$ | Eqs. (5)–(7) carry a **minus sign**; Eq. (8) uses the physical flux |
| $F_{j+1/2}$ | $\hat f_{i+1/2}$ | |
| $d_{j+1/2}$ | $\mathcal D_{i+1/2}$ (page-local) | JST dissipation term |
| $k^{(2)}$, $k^{(4)}$ | $k_2$, $k_4$ (page-local) | JST constants |
| $\epsilon^{(2)}$, $\epsilon^{(4)}$ | $a_{i+1/2}\varepsilon_2$, $a_{i+1/2}\varepsilon_4$ | spectral radius factored out on this page |
| $\mathcal R_{j+1/2}$ | $a_{i+1/2}$ | spectral radius of $\partial F/\partial U$ |
| $\Psi_j$, $\Psi_{j+1/2}$ | $\varphi_{\mathrm J,i}$, $\varphi_{\mathrm J,i+1/2}$ | Jameson's pressure sensor; **collides** with the registry's $\Psi_{\mathrm D}$ (modified Ducros sensor) |
| $\Phi$, $\epsilon=10^{-30}$ | $\Phi_{\mathrm D}$, $\epsilon_{\mathrm D}$ | classical Ducros ratio (registry §10) |
| $\Phi\Psi$ | $\Phi_{\mathrm D}\varphi_{\mathrm J}$ | "modified Jameson's sensor" |
| $\boldsymbol\omega=\nabla\wedge\tilde{\mathbf u}$ | $\nabla\times v$ | |
| $U$, $\psi$ (Eq. (14)) | $a$, $b$ (page-local) | $\psi$ is the entropy potential and $a$ the wave speed in the registry |
| $\mathcal V$, $\mathbf S$ | $\lvert I_i\rvert$ ($\Delta x$ in 1D), face normal | |
| $\Delta$, $\Delta_c\approx2\Delta$, $k_c\approx\pi/\Delta$ | $\Delta$, $\Delta_c$, $k_{w,c}$ (page-local) | filter scale and cut-off |
| $\nu_t$, $\mu_t=\bar\rho\nu_t$, $\kappa_t=\nu_t/Pr_t$ | $\nu_{\mathrm{sgs}}$, $\mu_{\mathrm{sgs}}$, page-local diffusivity | $\nu$ is the CFL number, $\kappa$ the kinetic energy |
| $\tau_{ij}$, $Q_j$, $\tilde S_{ij}$, $\epsilon_{\mathrm{sgs}}=-\tau_{ij}\tilde S_{ij}$ | page-local | $\tilde S_{ij}$ is trace-free and carries no factor ½ |
| $E(k,t)$, $T^{k<k_c}$ | $E_k(k_w,t)$, $T_<$ (page-local) | registry $E$ is the total energy |
| $R_{ij}$ (Eq. (28)), $E=\tfrac12R_{ii}$ | $\mathsf R_{ij}$, page-local turbulent kinetic energy | registry $R$ is the eigenvector matrix |
| $\lambda$ (shock width) | $\lambda_{\mathrm{sh}}$ | registry $\lambda_l$ are eigenvalues |
| $\lambda(\tilde T)$ | page-local conductivity | |
| $M_1$, $M_t$, $U_1$, $U_2$, $\rho_1$, $\rho_2$ | page-local | upstream and downstream states, turbulent Mach number |
| $\Xi=\sqrt{\Theta'^2}/\sqrt{\omega'^2}$ (§2) | page-local | rms dilatation over rms vorticity; not Sciacovelli et al.'s $\Xi_i$ |

# Reference list

The paper prints 56 references, numbered [1]–[56] in order of first citation, no DOIs. The
list is merged complete into the [bibliography](/bibliography.md), with `citedby` including
`ducros-1999`. Identity notes:

- [7] (Lee, Lele & Moin, J. Fluid Mech. 251, 1993) and [23] (S. Lee, CTR Annual Research
  Briefs, printed 1992) are distinct works; [53] (Phys. Fluids 4(7), 1992) is a third.
- [19] prints "S. O. Elaine and J. P. Boris": given name and surname of Elaine S. Oran
  swapped.
- [21] (Garnier, Mossi, Sagaut, Comte & Deville, "On the use of shock-capturing schemes for
  large-eddy simulation", "J. Comput. Fluid Dyn., in press") is the in-press form of the
  paper published in J. Comput. Phys. (1999), kept as its own entry by bundle law; [50] is a
  1998 ICFD conference version with the same title.
- [24] prints "Phys. Fluids 3, 2746 (1992)" for the Phys. Fluids A 3 paper of 1991.
- [32] prints "AIAA Paper 95-0355, 33(7), 1995", a paper number with a volume and issue.
- [35] (Morkovin) prints 1961; [36] (Sarkar et al., J. Fluid Mech. 227, 1991) has no page.
- [42] prints "AIAA Paper 81-1250" for the Jameson–Schmidt–Turkel paper (AIAA Paper 81-1259
  in the bibliography).
- [54] (M. J. Lee, Kim & Moin, Turbulent Shear Flows 6, 1987) has no pages; its in-text uses
  look misnumbered (Printed slips).
- [56] prints "Phys. Fluid 12, 2900 (1992)"; "12" is presumably the issue of Phys. Fluids A 4.
- [11] prints the second author "D. Alex" and [13] "R. Hannapel", recorded as printed.

# Pages created or updated

Chunk 14 (2026-11-17). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
* [Conservative split central derivative](/operators/conservative-split-derivative.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Implicit large-eddy simulation (ILES)](/definitions/implicit-large-eddy-simulation.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Shock–turbulence interaction](/benchmarks/shock-turbulence-interaction.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
