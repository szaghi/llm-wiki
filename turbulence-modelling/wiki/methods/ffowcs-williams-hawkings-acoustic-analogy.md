---
type: Method
title: "Ffowcs Williams–Hawkings acoustic analogy"
description: "The Ffowcs Williams–Hawkings analogy turns a flow solution into far-field sound through surface (thickness, loading) and volume (quadrupole) integrals; this page gives its convective and 2D frequency-domain forms, surface and quadrupole choices, retarded-time handling, its continuous adjoint for shape optimization, and the accuracy reported for jets, fans, a wind turbine and a rod–airfoil."
status: established
aliases: [FW-H, FWH, Ffowcs Williams-Hawkings equation, acoustic analogy, hybrid aeroacoustic prediction]
tags: [aeroacoustics, les, hybrid-rans-les, rans, turbomachinery]
timestamp: 2026-10-29T05:13:00Z
---

# Ffowcs Williams–Hawkings acoustic analogy

The **Ffowcs Williams–Hawkings (FW-H) analogy** computes the sound radiated
by a flow from a fluid-dynamic solution, without resolving the acoustic
field in the flow solver.
[Rismondo et al. (2025)](/sources/rismondo-2025.md), §1.2, cite Lighthill
(1952), who rearranged the compressible Navier–Stokes equations into an
inhomogeneous wave equation for the acoustic field, and Ffowcs Williams &
Hawkings (1969), who extended it to bodies in relative motion and solved it
with the free-space Green function. The radiated pressure then splits into a **linear**
surface part and a **nonlinear** volume part. The surface part holds the
*thickness* term (fluid displaced by the body) and the *loading* term
(pressure and viscous stress on it). The volume part is the *quadrupole*
term of the fluctuating velocity field around the body. The analogy assumes that the
sound does not act back on the flow. The computation is therefore a
two-step **hybrid** method: an LES, a
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) or a direct noise
computation supplies the sources, and an integral gives the sound at the
observers. Rismondo et al. call this "particularly advantageous" in
low-speed flows ($M<0.3$), where the flow can be computed as incompressible.

In this bundle the analogy is the downstream user of turbulence
simulations. The sources use it on a round jet, twin square jets, a fan
stage, a wind turbine, a rod–airfoil configuration and code verification.
Its accuracy depends on the simulation that feeds it, which in one source
is a 2D URANS.

## Convective form

Page-local symbols: $c_0$, $\rho_0$, $p_0$ the ambient sound speed, density
and pressure; $\rho'=\rho-\rho_0$ and $p'$ the acoustic density and
pressure ($p'=c_0^2\rho'$ in the far field); $U_{0,i}$ a uniform stream,
$M_0=\lvert\boldsymbol U_0\rvert/c_0$, $\beta_M=\sqrt{1-M_0^2}$; $g(\boldsymbol x,t)=0$ the
integration surface $S$ with outward unit normal $n_i$, $H$ the Heaviside
function and $\delta(g)$ the surface delta; $Q_i$ the thickness (mass-flux)
source; $\ell_{ij}$ the loading tensor; $T^{\mathrm L}_{ij}$ the Lighthill
tensor; $\boldsymbol x$ the observer, $\boldsymbol s$ the source point and
$t_e$ the emission (retarded) time. $\sigma_{ij}$ is the registry's viscous
stress.

[Ferrer et al. (2023)](/sources/ferrer-2023.md), §4.6, Eq. (23), write the
convective FW-H equation for a medium in uniform motion:

$$\Big(\partial_t^2+U_{0,i}U_{0,j}\partial_i\partial_j+2U_{0,i}\partial_i\partial_t-c_0^2\partial_i\partial_i\Big)\big(H\rho'\big)=\big(\partial_t+U_{0,i}\partial_i\big)\big(Q_in_i\,\delta(g)\big)-\partial_i\big(\ell_{ij}n_j\,\delta(g)\big)+\partial_i\partial_j\big(T^{\mathrm L}_{ij}H\big).$$

Rismondo et al. (2025), §2.2, Eqs. (2.3)–(2.7), give its integral solution
with the stream along $x_1$. They use the linear terms of Najafi-Yazdi,
Brès & Mongeau (2011) and the volume terms of Cianferra et al. (2019):

$$\begin{aligned}
4\pi p'(\boldsymbol x,t)=&\;\frac{\partial}{\partial t}\int_S\Big[(1-M_0)\frac{Q_in_i}{R^*}\Big]_{t_e}dS-\int_S\Big[U_{0}\frac{r^*_1Q_in_i}{R^{*2}}\Big]_{t_e}dS\\
&+\frac1{c_0}\frac{\partial}{\partial t}\int_S\Big[\frac{\ell_{ij}n_jr_i}{R^*}\Big]_{t_e}dS+\int_S\Big[\frac{\ell_{ij}n_jr^*_i}{R^{*2}}\Big]_{t_e}dS\\
&+\frac1{c_0^2}\frac{\partial^2}{\partial t^2}\int_V\Big[T^{\mathrm L}_{ij}\frac{r_ir_j}{R^*}\Big]_{t_e}dV
+\frac1{c_0}\frac{\partial}{\partial t}\int_V\Big[T^{\mathrm L}_{ij}\Big(\frac{2r_ir^*_j}{R^{*2}}+\frac{r^*_ir^*_j-\Lambda_{ij}}{R^{*2}}\Big)\Big]_{t_e}dV\\
&+\int_V\Big[T^{\mathrm L}_{ij}\frac{3r^*_ir^*_j-\Lambda_{ij}}{R^{*3}}\Big]_{t_e}dV,
\end{aligned}$$

with $U_0=\lvert\boldsymbol U_0\rvert$, the advective distance
$R^*=\sqrt{(x_1-s_1)^2+\beta_M^2[(x_2-s_2)^2+(x_3-s_3)^2]}$, the radiation
vectors $r^*_1=(x_1-s_1)/R^*$, $r^*_{2,3}=\beta_M^2(x_{2,3}-s_{2,3})/R^*$,
$r_1=(r^*_1-M_0)/\beta_M^2$, $r_{2,3}=(x_{2,3}-s_{2,3})/R^*$, and
$\Lambda_{ij}=\mathrm{diag}(1,\beta_M^2,\beta_M^2)$ (all page-local). The
first two terms are thickness, the next two loading, and the last three
quadrupole. For an impermeable surface moving with velocity $v_i$,
$Q_i=\rho v_i$. As printed, $\ell_{ij}=(p-p_0)\delta_{ij}+\sigma_{ij}$ and
$T^{\mathrm L}_{ij}=\rho u_iu_j+[(p-p_0)-c_0^2(\rho-\rho_0)]\delta_{ij}-\sigma_{ij}$.
At low Mach number, with negligible viscous stress and a barotropic
incompressible flow, they reduce it to $T^{\mathrm L}_{ij}\approx\rho u_iu_j$.
Ferrer et al. (Eqs. 24–26) write the thickness and loading integrals of
the same convective formulation (Najafi-Yazdi and Ghorbaniasl) with the time
derivatives of the sources inside the integrals.

The three implementations in the sources build on the same convective
formulation of Najafi-Yazdi et al. These are HORSES3D (Ferrer et al.), the
SherFWH code of [Lewis et al. (2023)](/sources/lewis-2023.md) (§5.3, after
Casalino and Najafi-Yazdi et al.) and the solver of Rismondo et al.

## Two-dimensional frequency-domain form

[Monfaredi et al. (2021)](/sources/monfaredi-2021.md), §2.2, need the
analogy for 2D unsteady flows. They state that the time-domain integral
solution of the 2D equation suffers a **tail effect** that requires an
infinitely long integration time, and therefore solve the convective
equation, with the quadrupole term removed, in the frequency domain
(Eqs. 3–8). Page-local symbols in addition to those above: $\omega_a$ the
angular frequency (not the registry's $\omega$), $k_a=\omega_a/c_0$,
$\breve\phi(\omega_a)$ the Fourier transform of $\phi(t)$, $M_{0,i}=U_{0,i}/c_0$,
$\breve G$ the 2D Green function, $\boldsymbol x_r$ the receiver,
$\boldsymbol s$ a point of the surface $g=0$, $\sigma^t_{ij}$ the
eddy-viscosity stress of the URANS (their stress carries $\mu+\mu_t$).
Their sources are
$$\begin{aligned}
Q&=(\rho u_i-\rho_0U_{0,i})\,n_i,\\
F_i&=\big(\rho(u_i-2U_{0,i})u_j+\rho_0U_{0,i}U_{0,j}+p\,\delta_{ij}-\sigma_{ij}-\sigma^t_{ij}\big)\,n_j,
\end{aligned}$$
with $n_i$ pointing towards the acoustic domain, and the frequency-domain
equation and its solution are
$$\begin{aligned}
&\big(\partial_i\partial_i+k_a^2-2iM_{0,i}k_a\partial_i-M_{0,i}M_{0,j}\partial_i\partial_j\big)\big(H\breve p'\big)=-i\omega_a\breve Q\,\delta(g)+\partial_i\big(\breve F_i\,\delta(g)\big),\\
&H\breve p'(\boldsymbol x_r,\omega_a)=-\int_{g=0}\breve F_i\,\frac{\partial\breve G}{\partial s_i}\,dS-\int_{g=0}i\omega_a\breve Q\,\breve G\,dS,
\end{aligned}$$
with the subsonic 2D Green function
$$\breve G=\frac{i}{4\beta_M}\exp\!\Big(\frac{iM_0k_ad_1}{\beta_M^2}\Big)H^{(2)}_0\!\Big(\frac{k_a}{\beta_M^2}\sqrt{d_1^2+\beta_M^2d_2^2}\Big),$$
$H^{(2)}_0$ the Hankel function of the second kind and order zero, and
$(d_1,d_2)$ (page-local) the receiver–source separation rotated into the
stream direction (Eqs. 7–8). The sources $Q$, $F_i$ are stored at the
surface nodes at every time step; after the run their time means are
subtracted, a Hanning-type window is applied and the Fourier transform is
taken before the integrals are evaluated. Their time-domain wave operator
(Eq. 3), written for a body at rest in a uniform stream, has the form of
the convective operator of Ferrer et al. (2023) above, applied to
$Hp'/c_0^2$ instead of $H\rho'$ *(compiler check, not in the sources)*.
The viscous and eddy-viscosity stresses enter their loading term with a
minus sign (Eq. 4; see Qualifications for the sign printed by Rismondo et
al.).

**Verification.** A stationary monopole in a stream at $M_0=0.6$, enclosed
by a circular surface of radius 4 m with 150 nodes, gives an r.m.s.
directivity at 500 m that matches the analytical solution "exactly"
(§2.2.1, Fig. 2). At receivers close to the surface the hybrid pressure
histories match those of the URANS itself; the authors attribute the
differences at the start and end of the record to the window (Figs. 4, 9).

## Continuous adjoint of the analogy

Monfaredi et al. (2021), §3, differentiate the whole hybrid chain for
gradient-based aeroacoustic shape optimization. The objective is the
integrated spectral magnitude at one receiver,
$$J=\int|\breve p'(\boldsymbol x_r,\omega_a)|\,d\omega_a,$$
which they describe as "the total energy contained in the spectrum of the
sound pressure" (Eq. 9). The flow solver is an in-house GPU-enabled 2D
compressible URANS with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
(vertex-centred finite volumes on unstructured grids, Roe flux with the
Van Leer limiter, dual time stepping, second order in time; §2.1). The
unsteady continuous adjoint includes the adjoint Spalart–Allmaras and
the adjoint wall-distance (Eikonal) equations; the adjoint turbulence
model is not printed but referred to a thesis (§1, §3). This extends the
authors' earlier inviscid FW-H adjoint to viscous and turbulent flow.
Because the surface is placed on a grid line far enough from the body to
be unaffected by shape changes, the Green function, its gradient and the
surface element have zero design derivatives (§3). The structure of the
result (§3, Eqs. 21–33):

- the derivative of $J$ in the frequency domain is mapped back to the time
  domain through the windowed, mean-subtracted Fourier transform, which
  gives time-domain kernels multiplying the design derivatives of $F_i$
  and $Q$ on the surface (Eqs. 23–26);
- the objective enters the adjoint mean-flow equations **only as source
  terms** on the finite volumes of the surface nodes and of their
  neighbours, the latter from the gradient terms of the viscous stress in
  $F_i$ (Eqs. 31–33). The adjoint boundary conditions and the sensitivity
  expression are those of any other objective;
- outside the optimization window the adjoint has no source and decays
  while it is convected towards the inlet backward in time. The
  sensitivities converge within 460 steps after the window, so the
  backward integration stops at 2490 steps instead of covering all 7490
  primal steps, which saves cost and the storage of the primal transient
  (§4.2, Figs. 12–13).

Adjoint sensitivities agree with central finite differences (step
$10^{-7}$ of the body length) for the mean lift, the mean drag and the
noise objective of a laminar cylinder at $Re=1000$, and for the noise of
the rod–airfoil case (Figs. 5, 14; see
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)). The
authors attribute the small noise-objective differences partly to
finite-difference round-off, which grows with the integration time.

**Rod–airfoil optimization.** A rod of diameter $C/10$ one chord upstream
of a [NACA 0012](/benchmarks/naca-0012-airfoil.md) of chord $C=0.1$ m, at
$M_\infty=0.2$ and $Re_C=4.8\times10^5$, on a 161,906-node grid with
first-node $y^+<1$ (§4.2). The 2D URANS gives a shedding Strouhal number
of 0.24, against about 0.19 measured, and a tonal peak at 1728 Hz above the
measured one; overprediction of the shedding frequency, the spectral
peaks and the OASPL is, by their account and the works they cite, a known
shortcoming of URANS (§1, §4.2). A grid study of the OASPL directivity at
1.85 m (124,000, 161,906 and 240,000 nodes) settles on the medium grid.
Steepest descent on 50 free-form-deformation variables lowers $J$ by 30%
in 12 cycles. The main peak of the power spectral density falls by about
3.7 dB to 90.7 dB, the five tonal frequencies are unchanged, the
directivity rises between $135^\circ$ and $195^\circ$, and the mean drag
coefficient rises by 0.011 while the lift coefficient falls by 0.018
(§4.2, Figs. 15–17). They name comparison with DES and LES and their
adjoints as the next step (§5).

## Choices of the integration surface

- **Solid (impermeable) body surface.** The surface carries thickness and
  loading terms from the wall pressure of the flow solution. Lewis et al.
  (2023, §5.3) use the rotor and stator wall pressure of a fan stage, with
  the loading (dipole) term only. Rismondo et al. (2025) integrate over the
  turbine surface.
- **Permeable surface.** A closed surface in the fluid encloses the source
  region, so that its integrals carry the quadrupoles inside it.
  [Basile et al. (2023)](/sources/basile-2023.md), §4.3, wrap a jet in four
  cylindrical–conical surfaces (radii $0.68D$–$1.7D$ at the nozzle) closed
  by downstream discs at $x/D=20$, 25, 30. They add the extra flux terms of
  Rahier et al. that stabilize the low-frequency result of a closed
  downstream surface, and report results "globally independent" of the
  surface choice, showing one combination only.
  [Monfaredi et al. (2021)](/sources/monfaredi-2021.md), §2.2, §4, place
  a permeable 2D surface on a grid line: a circle of radius $3.5D$ around
  the cylinder, and a surface of 1016 nodes around the rod–airfoil.
  [Ahn et al. (2023)](/sources/ahn-2023.md), §IV D, use a permeable
  open-disk (classical, not closed downstream) surface around
  over-expanded twin square jets, sized after an earlier
  single-rectangular-jet LES. Its finest spacing of about $0.024h_n$ ($h_n$
  the nozzle exit height, registry §11) resolves up to $St\approx3.5$ at
  about 11 cells per wavelength. They name averaging over multiple closed
  end discs (Mendez et al.) and quadrupole corrections as improvements
  they did not use. HORSES3D supports both
  solid and permeable surfaces (Ferrer et al. 2023, §4.6). Rismondo et al.
  (§1.2) cite marine-propeller studies that use the porous
  formulation of Di Francescantonio (1997) and its modifications.

## Quadrupole terms: neglect or integrate

Three of the six sources that evaluate FW-H integrals drop the volume
integral. Monfaredi et al. (2021, §2.2) call the quadrupole term negligible
for the low-speed flows they treat ($M_\infty=0.2$) and add that dropping
it avoids computing and storing a volume term. Ferrer et al. (2023, §4.6) neglect
quadrupoles in HORSES3D. Lewis et al. (2023, §5.3) neglect quadrupole and
monopole sources because the fan's relative tip Mach number is 0.57.
Rismondo et al. (2025, §1.2) note that the wake contribution has
"historically" been omitted because the loading term dominates in many
situations, especially in the far field. They keep it, over a cylinder of
radius $0.9D$ that holds the wake of a model wind turbine to $x/D=7$
($D=0.18$ m, $Re_D=9.6\times10^4$, tip Mach number about 0.11). Their
results bound where the neglect is safe (§4.2–4.3, Figs. 18–25):

- the nonlinear (quadrupole) part is significant only below about four
  times the rotation frequency $f_T$ (page-local). At $r/D=1$ it dominates
  the lowest frequencies, and the linear part dominates from the blade
  passing frequency $3f_T$ upward;
- in the near field ($K_\lambda<1$, with $K_\lambda$ the distance over the
  blade-passing wavelength, page-local) the linear part decays as $r^{-4}$
  in the rotor plane, steeper than $r^{-1}$. The authors explain this by
  Ianniello's rotpole model ($r^{-(n+1)}$ for $n=3$ blades). The quadrupole
  part therefore matters at intermediate distances, and both decay as
  $r^{-1}$ beyond about $4D$;
- the nonlinear noise at a near-field microphone comes mostly from the wake
  directly beneath it, so the whole wake must be inside $V$.

Lewis et al. neglect quadrupoles on a Mach-number argument (relative tip
Mach number 0.57), and Rismondo et al. find them significant at a tip Mach
number of about 0.11. The two
claims concern different quantities and distances: Lewis et al. predict
in-duct and far-field fan broadband noise, and Rismondo et al. find the
quadrupole important in the near field and at low frequency.

## Retarded time and source compactness

Every term is evaluated at the emission time $t_e$ that solves
$t-t_e-\lvert\boldsymbol x(t)-\boldsymbol s(t_e)\rvert/c_0=0$. HORSES3D evaluates the
integrals with a source-time-dominant algorithm on the Gauss nodes of each
face of the FW-H surface (Ferrer et al. 2023, §4.6). Ferrer et al. write the
emission time as $t_e=t-R/c_0$. Rismondo et al. (2025,
§4.2, Eqs. 4.3–4.5) neglect the retarded-time differences across the
source region, which they call compressibility delays. They justify this
by the criterion of Cianferra et al. (2019), page-local:
$$\mathrm{MFP}=\frac{1}{\Delta_{\mathrm{del}}f_{\max}},\qquad \Delta_{\mathrm{del}}=\frac{\max_{\boldsymbol s\in S,V}\lvert\boldsymbol s(t_e)-\boldsymbol x(t)\rvert-\min_{\boldsymbol s\in S,V}\lvert\boldsymbol s(t_e)-\boldsymbol x(t)\rvert}{c_0}.$$
The source prints the differences $\boldsymbol s(t_e)-\boldsymbol x(t)$
without the modulus and writes the definition as "$\mathrm{MFP}=\dots=1$".
Delays may be ignored below $f_{\max}$, where $\mathrm{MFP}>1$. At the
nearest microphone they find $f_{\max}=30f_T$ for the surface terms and
$3.85f_T$ for the volume terms (Tables 3–4). By that criterion the delays
of the volume terms are not negligible above $3.85f_T$ at that microphone,
a range that contains the rise of the nonlinear spectrum above $20f_T$
that they report.

## Accuracy reported

| Source | Flow solver feeding FW-H | Case | Surface, terms | Result |
|---|---|---|---|---|
| Ferrer et al. (2023), §4.6 | HORSES3D DGSEM | stationary monopole in a $M_0=0.5$ stream, observer at 500 source lengths; NACA 0012 at $Re=10^5$, $M=0.4$ | solid or permeable, no quadrupoles | frequency "good", amplitude error "around 7%"; dipole directivity at $r=2c$ (qualitative) |
| Basile et al. (2023), §4.4 | hp-adaptive modal DG, ZDES mode 0+1 ([detached-eddy simulation](/methods/detached-eddy-simulation.md)) | PPRIME jet, $M_j=0.9$, $Re_D\simeq10^6$ | permeable closed surfaces, Rahier terms | finest mesh OASPL ($0.05<St<3$) about 1 dB (polar) and 2 dB (cylindrical array) high at high angles, 1–2 dB low below $40^\circ$; coarser meshes overpredict at all angles |
| Ahn et al. (2023), §IV D | unstructured finite-volume [implicit LES](/definitions/implicit-les.md) (EDGE; second-order central fluxes with Jameson-type [artificial dissipation](/methods/artificial-viscosity-shock-capturing.md)), nozzle boundary layer tripped by a wall step | twin square jets, NPR 3.0, $M_j=1.36$, $Re=8.85\times10^5$ (equivalent diameter) | permeable open disk; samples every $5\times10^{-6}$ s, 8000 samples | far-field OASPL at $67.2h_n$ agrees with the microphones, maximum near $140^\circ$ and a hump near $90^\circ$ in both; screech 7928 Hz against 8172 Hz measured |
| Lewis et al. (2023), §5.3.1 | AVBP [wall-modelled LES](/methods/wall-modelled-les.md), WALE | [ACAT1 fan stage](/benchmarks/acat1-fan-stage.md) at approach | solid blades and vanes, loading only | free-field FW-H overpredicts stator noise by 5–7 dB upstream (1–5 kHz) and about 4 dB (upstream), 2 dB (downstream) above 5 kHz |
| Monfaredi et al. (2021), §2.2.1, §4.2 | in-house 2D URANS, Spalart–Allmaras | monopole in a $M_0=0.6$ stream; rod–airfoil, $M_\infty=0.2$, $Re_C=4.8\times10^5$ | permeable, frequency domain, no quadrupoles | monopole directivity at 500 m matches the analytical solution; rod–airfoil OASPL directivity agrees with an earlier 2D URANS and the measured trend, overprediction expected of URANS |
| Rismondo et al. (2025), §4 | OpenFOAM wall-resolved LES, WALE ([OpenFOAM](/software/openfoam.md)) | model wind turbine, $Re_D=9.6\times10^4$ | solid turbine surface plus wake volume | tonal noise at $3f_T$ plus trailing-edge broadband (linear); low-frequency wake broadband (nonlinear); near-field asymmetric, far-field symmetric dipole directivity (no acoustic measurement compared) |

Two lessons recur:

- **The source simulation decides the result.** Lewis et al. find a
  mesh as fine as their refined WMLES ("LES2") "mandatory" for reliable
  noise. Their coarser mesh LES1, which also meets the published WMLES
  wall-mesh criteria, is almost 5 dB worse at low and mid frequency
  (§5.3.1, §6). Basile et al.
  find that refining the jet mesh lowers the predicted noise, most at low
  frequency, and attribute the remaining excess at high angles to the
  untripped nozzle (§4.4). Ahn et al. (2023, §III, §IV A–B) trip the
  nozzle boundary layer of their jets with a step of height $0.02h_n$ in
  the convergent section, which brings the near-nozzle shear-layer
  turbulent kinetic energy and the length of the supersonic region closer
  to PIV than the untripped run; their FW-H prediction is made on the
  tripped run only (see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
- **Free-field propagation is a model error in ducts.** For the ducted
  fan, Goldstein's in-duct analogy, which accounts for duct cut-off,
  predicts at least 2 dB less than FW-H, about 5 dB less between 3 and
  6 kHz. With an indicative $\pm3$ dB rotor-shielding correction it agrees
  "very well" with the measurements (Lewis et al. 2023, §5.3.1).

## Alternatives in the sources

- **Goldstein's in-duct analogy** (Lewis et al. 2023), above.
- **Acoustic perturbation equations.**
  [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md), §2,
  propagate installed-jet noise by solving APE-4 with a high-order DG
  method in [Nektar++](/software/nektar-plus-plus.md). The source is the
  Lamb vector from a finite-volume LES, coupled one-way in memory. This
  hybrid method solves a propagation PDE on a grid instead of evaluating an
  FW-H integral. It lets a plate scatter and reflect the sound, and carries
  high-frequency waves that the LES itself dissipates (§4.3–4.4). The
  authors cite the LES/FW-H study of Wang et al. (2020) at $M=0.6$ as
  underpredicting isolated-jet noise. A different result of Ffowcs Williams,
  the $\sin^2(\theta/2)$ edge-scattering directivity of Ffowcs Williams &
  Hall (1970), is the law their installed-jet noise increments follow on
  the unshielded side up to $110^\circ$ (§4.3).
- **Direct noise computation**, in which the compressible solver resolves
  the acoustic field itself, is shown with HORSES3D (Ferrer et al. 2023,
  §4.6, dilatation field of the NACA 0012).
  [Gao et al. (2025)](/sources/gao-2025.md), §IV, state the argument for
  it on wall-bounded sources: far-field prediction "often rel[ies]" on the
  FW-H integral, but for sound generated by geometry under turbulent
  boundary layers "the near-wall turbulence poses significant challenges
  in the selection and formulation of integration surfaces", whereas
  their high-order finite-difference aeroacoustic solver (with a slip-wall
  WMLES; see [slip-wall models](/methods/slip-wall-model.md)) computes far-field
  noise "without relying on integral formulations"; that far-field
  computation is announced as future work, the paper reporting only
  wall-pressure spectra.
- Rismondo et al. (§1.2) cite Nelson et al. (2012), who combined
  delayed DES with Farassat's linear formulation for a full wind turbine.

## Qualifications

- Rismondo et al. print $\ell_{ij}=(p-p_0)\delta_{ij}+\sigma_{ij}$ and
  $T^{\mathrm L}_{ij}=\dots-\sigma_{ij}$ with opposite signs on the same
  viscous stress. Both tensors come from the momentum flux
  $\rho u_iu_j+(p-p_0)\delta_{ij}-\sigma_{ij}$ of the Navier–Stokes momentum
  equation (registry $\sigma_{ij}$), the loading as its surface part and
  $T^{\mathrm L}_{ij}$ as its volume part, so the two printed signs cannot
  both hold; the printed $T^{\mathrm L}_{ij}$ matches the momentum
  equation *(compiler check, not in the sources)*. Rismondo et al. drop
  the viscous stress from $T^{\mathrm L}_{ij}$ at low Mach number. They also say Eq. (2.3) "contains seven terms" but plot
  "six terms" (the first two merged in their Fig. 19). Their nonlinear
  frequency range is printed "$f<4.0f/f_T$" in §4.2 and $f<4f_T$ in §5.
- Ferrer et al. (2023, §4.6) call $Q_i$, $\ell_{ij}$, $T^{\mathrm L}_{ij}$ the
  "loading, thickness, and quadrupole" terms, swapping the first two
  relative to their own Eqs. (25)–(26).
- Ahn et al. (2023, §IV D) compute their spectra from "sub-set data of
  250 000 time steps" while using 8000 FW-H samples saved every 100 solver
  steps; the paper does not say whether the subset counts solver steps
  (250 000 solver steps are 2500 saved samples) or saved samples. With
  their time step $0.0012h_n/u_j$ ($u_j=399$ m/s, $h_n=16.61$ mm), 100
  steps are $5.0\times10^{-6}$ s, matching the printed sampling interval
  *(compiler check, not in the sources)*.
- Monfaredi et al. (2021) give the optimized main-peak reduction as
  "about 3.7 dB" in §4.2 and as 3.6 dB in §5, and print the receiver
  $\boldsymbol x_{r1}$ as $(0.31, 0.101)$ m in §4.2 and $(0.31, 0.104)$ m in the
  Fig. 9 caption. They call 3456 Hz "the third harmonic" of a tonal peak
  at 1728 Hz, which they count as the first harmonic; $3456=2\times1728$,
  so on their own count it is the second *(compiler check, not in the
  sources)*. Their $\omega$ is an angular frequency in Eqs. (5) and (7)
  (and in rad/s in §2.2.1) but an ordinary frequency in the kernel
  $e^{-2i\pi\omega t}$ of Eq. (23). The optimization targets the main
  tonal peak, which they call "of the utmost importance as the current
  simulation is performed using the URANS model" (§4.2); they attribute
  the broadband component of the rod–airfoil noise to the impingement of
  vortices on the airfoil and note that most earlier studies of it are 3D
  LES or DES (§1, §4.2).
- Basile et al. assert the surface independence without showing the other
  surfaces. Rismondo et al. assert independence from the volume radius
  ($0.7D$–$0.9D$) without showing it, and compare no acoustic measurement.

# Citations

- [Rismondo et al. (2025)](/sources/rismondo-2025.md) — §1.2 (history, quadrupole omission, porous formulation, cited studies); §2.2, Eqs. (2.3)–(2.7) (advective FW-H); §4.1–4.3, Eqs. (4.3)–(4.6), Tables 3–4, Figs. 18–27 (spectra, MFP criterion, source regions, directivity, decay); §5.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — arXiv v1: §4.6, Eqs. (23)–(26), Figs. 12–13 (convective FW-H in HORSES3D, monopole test, NACA 0012).
- [Basile et al. (2023)](/sources/basile-2023.md) — HAL accepted manuscript: §4.3 (permeable surfaces, Rahier terms); §4.4, Figs. 14–15 (jet PSD and OASPL).
- [Lewis et al. (2023)](/sources/lewis-2023.md) — HAL accepted manuscript: §5.3 (SherFWH, SherGoldstein, neglected sources); §5.3.1, Figs. 36–42 (FW-H and Goldstein predictions, shielding correction); §6.
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §III (EDGE implicit LES, tripping step); §IV A–B (effect of tripping); §IV D, Table II, Figs. 22–25 (permeable FW-H surface, sampling, OASPL, spectra, screech frequency).
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) — §1; §2.1–2.2, Eqs. (1)–(8) (URANS, 2D frequency-domain FW-H); §2.2.1, Fig. 2 (monopole); §3, Eqs. (9)–(36) (objective, continuous adjoint, FW-H source terms); §4.1–4.2, Figs. 4–17 (verification, truncated adjoint, rod–airfoil optimization); §5.
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §2.2–2.3 (LES/APE alternative); §4.3–4.4 (Ffowcs Williams & Hall directivity, cited LES/FW-H of Wang et al.).
- [Gao et al. (2025)](/sources/gao-2025.md) — §IV (direct aeroacoustic computation preferred to FW-H integration surfaces under turbulent boundary layers; passing mention).
