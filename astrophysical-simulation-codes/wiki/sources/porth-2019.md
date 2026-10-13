---
type: Source
title: "Porth et al. (2019) — The Event Horizon General Relativistic Magnetohydrodynamic Code Comparison Project"
description: "Nine GRMHD codes (Athena++, BHAC, Cosmos++, ECHO, H-AMR, HARM-Noble, iharm3D, IllinoisGRMHD, KORAL) evolve one weakly magnetized Fishbone–Moncrief torus around a spinning black hole at three resolutions with their own grids, boundaries and floors; the spread in horizon fluxes falls with resolution (accretion-rate max/min 1.772 at the highest standard resolution), and the residual differences are traced to MRI resolution, polar boundaries, outer-boundary placement, floors and PPM versus PLM reconstruction."
resource: "doi:10.3847/1538-4365/ab29fd"
source_kind: paper
authors: [Porth O., Chatterjee K., Narayan R., Gammie C.F., Mizuno Y., Anninos P., Baker J.G., Bugli M., Chan C., Davelaar J., Del Zanna L., Etienne Z.B., Fragile P.C., Kelly B.J., Liska M., Markoff S., McKinney J.C., Mishra B., Noble S.C., Olivares H., Prather B., Rezzolla L., Ryan B.R., Stone J.M., Tomei N., White C.J., Younsi Z.]
year: 2019
venue: "Astrophys. J. Suppl. 243:26"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2019-ApJS-Porth-1038471538-4365ab29fd.pdf"
tags: [mhd, relativity, benchmark, verification, constrained-transport, riemann-solver, primitive-recovery, amr, gpu, performance]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Nine general-relativistic MHD (GRMHD) codes evolve one common problem: a
Fishbone–Moncrief torus around a Kerr black hole of spin 0.9375, threaded
by a weak single poloidal loop, which develops MRI turbulence and reaches a
SANE (standard and normal evolution) accretion state. The codes are
Athena++, BHAC, Cosmos++, ECHO, H-AMR, HARM-Noble, iharm3D, IllinoisGRMHD
and KORAL. Each runs at three nominal resolutions ($96^3$, $128^3$,
$192^3$ in the domain of interest), with two Cartesian AMR runs and two
very-high-resolution runs added (§4, Table 2). Grids, boundaries and floors
are left to each group, so the comparison measures each code "as
typically used" (§4). One set of diagnostics is applied to all runs:
horizon fluxes, disk-averaged profiles, time- and azimuth-averaged maps, an
optically thin emission proxy and its power spectrum, MRI quality factors
and the Maxwell-stress parameter (§5.1). The spread between codes falls
with resolution. The differences are traced to MRI resolution, polar-axis
boundaries, outer-boundary placement, floors and reconstruction (§5–§6,
App. A). The paper concludes that "the community of GRMHD codes is mature,
capable, and consistent on these test problems" (abstract). Merged into
[EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md),
[Magnetized Fishbone–Moncrief torus](/benchmarks/magnetized-torus-accretion.md)
and [H-AMR](/software/h-amr.md).

# Key claims

1. **Common ground** (§6). "All apply overall 2nd order conservative
   schemes and preserve the divergence of the magnetic field to machine
   precision. All except iharm3D applied the piecewise-parabolic-method
   (PPM)". The codes differ in the order of time integration, the Riemann
   solver (HLL or LLF) and the discretization of the induction equation.
2. **Per-code configuration** (Table 1, §4.1): integrators from
   predictor–corrector to RK4, HLL or LLF, PPM or PLM, and five
   constrained-transport variants; tabulated on the
   [comparison page](/results/eht-grmhd-code-comparison.md).
3. **Code lineages** (§3): short descriptions of the nine codes, among them
   H-AMR as a GPU rewrite of HARM with "locally adaptive timestepping" and
   IllinoisGRMHD as a vector-potential Cartesian AMR code in the Einstein
   Toolkit.
4. **Spreads** (Table 2, max/min across codes): time-averaged accretion rate
   3.903 / 8.604 / 1.772, normalized horizon magnetic flux 17.408 / 12.24 /
   2.777, specific angular-momentum flux 1.823 / 1.201 / 1.121, normalized
   energy flux 7.096 / 4.631 / 1.405 at nominal resolutions 96 / 128 / 192.
   All runs are SANE (§5.2).
5. **Resolution, not cell count, organizes the data** (§5.2, Fig. 5,
   §6.1): ordering runs by the proper meridional cell spacing makes the
   spread in accretion rate and horizon flux collapse below a critical
   resolution (printed range recorded below).
6. **Turbulence convergence** (§5.6–§5.7, §6.1). Disk-averaged MRI quality
   factors rise with resolution; only the highest standard resolution keeps
   the turbulence alive to $t = 10^4$ in units of $r_{\mathrm g}/c$; disk
   radius converges above 192 meridional cells; the disk Maxwell-stress
   parameter and magnetization keep rising weakly up to about $1024^3$. "Convergence in
   the strict sense cannot be achieved for ideal MHD simulations of
   turbulence".
7. **Polar boundaries** (§4.1, §5.2, §5.4, §6.2). Polar cut-outs with
   "soft" boundaries let a truncation-error radial magnetic flux leave the
   domain and deplete the funnel field; Cosmos++'s horizon flux is
   "consistently off by a factor of ∼ 4".
8. **Floors** (§4, §4.1, §6.3) differ widely and set the funnel plasma
   state, which "should not be taken at face value", with minor effect on
   the jet opening angle. See [density and pressure floors](/methods/numerical-floors.md).
9. **Primitive recovery** (§4.1): seven different fallback chains inside the
   codes; see [primitive-variable recovery](/methods/primitive-variable-recovery.md).
10. **PPM versus PLM** (App. A, Table 3, Fig. 23): at fixed second order,
    PLM runs of H-AMR and Athena++ give accretion rates "a factor of two to
    almost six" below their PPM runs even at $192^3$; KORAL's are closer.
11. **CT variants** (App. A): the upwind CT of Gardiner & Stone
    "reproduces the correct solution for plane-parallel grid-aligned fields,
    however the amount of dissipation of the scheme is effectively doubled"
    relative to arithmetic EMF averaging.
12. **Run-to-run variation** (App. B, Table 4): KORAL repeated on two
    machines with different random perturbations differs "typically in the
    low percent regime", less than between codes.
13. **H-AMR throughput** (§4.1.5): "3 − 5 × 10⁸ zone-cycles/s/GPU" with
    3–4 levels of local adaptive time stepping, quoted from Chatterjee et
    al. (2019).
14. **Seeding bug** (footnote 3): HARM-Noble used the same random seed on all
    MPI ranks, so its initial perturbation was azimuthally periodic and its
    runs lack the low azimuthal modes.

**Tests.** One benchmark, the [magnetized Fishbone–Moncrief torus](/benchmarks/magnetized-torus-accretion.md)
(§4), with ancillary runs: PLM variants of H-AMR, KORAL and Athena++
(App. A); KORAL run-to-run (App. B); half-azimuthal-resolution runs of
BHAC and KORAL with horizon fluxes consistent with full resolution
(§5.6.3); fluid-frame versus coordinate-frame Maxwell stress, a
few-percent difference (App. D); and a validation of the emission proxy
against a general-relativistic ray-traced light curve (§5.5, Fig. 16).

# Notation map

Paper units: $G = c = 1$, lengths and times in units of the black-hole mass
$M$, the factor $1/\sqrt{4\pi}$ absorbed in the field.

| Porth et al. (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $p$ | $\rho$, $p$ | rest-mass density, gas pressure |
| $u$ (internal energy density) | $\rho e$ | **collision:** registry $u$ is the conserved state |
| $u^\mu$, $b^\mu$, $b^2$ | words ("four-velocity", "fluid-frame field") | not in the registry; $u^\mu$ collides with $u$ |
| $\hat\gamma$ | $\gamma$ | adiabatic index, 4/3 here |
| $\Gamma$ (Lorentz factor) | $W$ | |
| $g_{\mu\nu}$, $g$, $T^{\mu\nu}$, $\Gamma^\lambda{}_{\nu\kappa}$ | words | not in the registry; $\Gamma$ collides with $\Gamma_1$ in name only |
| $\gamma_{rr}$, $\gamma_{\phi\phi}$ | $\gamma_{ij}$ | spatial metric components |
| $B^i$ | $\mathbf B$ | Eulerian field, Heaviside–Lorentz-like units |
| $B = \sqrt{b^\alpha b_\alpha}$ | words ("fluid-frame field strength") | **collision** with $\mathbf B$ |
| $\sigma$, $\beta$ (plasma) | words ("magnetization", "plasma beta") | $\beta$ **collides** with the shift $\beta^i$ and with the PSD slope $\beta$ of §5.5 |
| $M$ | $M_{\mathrm{BH}}$; as a length, $r_{\mathrm g}$ | |
| $a$ (spin) | words | **collision:** registry $a$ is the cosmological scale factor |
| $r_h$ | words ("horizon radius") | |
| $\dot M$ | $\dot M$ | |
| $\Phi_{BH}$, $\phi = \Phi_{BH}/\sqrt{\dot M}$ | words | **collisions** with the potential $\Phi$ and the azimuth |
| $\dot L$, $\dot E$ | words | horizon angular-momentum and energy fluxes |
| $\Delta r_p$, $\Delta\theta_p$, $\Delta\phi_p$ | words ("proper cell spacing") | measured at $12M$ in the midplane (eq. 10) |
| $N_r$, $N_\theta$, $N_\phi$ | $N$ (nominal), words per direction | |
| $h$ (MKS parameter, eqs. 11–12) | words | **collision** with the cell size $h$ |
| $h$ (specific enthalpy, eq. 25) | $h_{\mathrm{rel}}$ | |
| $\lambda^{(\theta)}$, $Q^{(i)}$ | words ("MRI wavelength", "MRI quality factor") | $\lambda$ **collides** with the eigenvalues $\lambda^{(p)}$ |
| $\alpha(r,t)$ | words ("Maxwell-stress $\alpha$") | **collides** with $\alpha_{\mathrm c}$, $\alpha_{\mathrm L}$ and the FMKS exponent of eq. 12 |
| $P_{\rm tot}$ | $P^*$ (with the fluid-frame field) | |
| $\kappa$ (eq. 20), $L(t)$, $j$, $k$ | words | **collisions** with opacity $\kappa$ and $\mathcal L$ |
| $\rho_{fl}$, $p_{fl}$, $u_{fl}$ | words ("floor values") | |

# Pages created or updated

* Created [EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md),
  [H-AMR](/software/h-amr.md),
  [Magnetized Fishbone–Moncrief torus](/benchmarks/magnetized-torus-accretion.md),
  [Density and pressure floors](/methods/numerical-floors.md).
* Updated [Constrained transport](/methods/constrained-transport.md),
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Primitive-variable recovery in relativistic MHD](/methods/primitive-variable-recovery.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md).
* Also cited on [Athena++](/software/athena-plus-plus.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2019-ApJS-Porth-1038471538-4365ab29fd.pdf`.
   * **Version.** arXiv:1904.04923v2 [astro-ph.HE], 5 Aug 2019, AASTeX62
     "Draft version August 7, 2019", 51 pages, the accepted manuscript
     (received 5 April, revised 17 May, accepted 28 May 2019), not the
     typeset article. Page, section, table and figure numbers refer to it.
   * **Identity.** doi:10.3847/1538-4365/ab29fd, checked on Crossref: title
     matches page 1; Astrophys. J. Suppl. Ser. 243(2):26, published
     2019-08-01; 219 authors (the 27 code authors listed in the
     frontmatter, then the Event Horizon Telescope Collaboration).
   * **How it was read.** Text extraction of all sections and appendices;
     eq. 12 and the Fig. 5 abscissa checked on the rendered pages. Figure
     values beyond those in the text and tables were not transcribed. The
     Table 2 header row is garbled in the text layer; its column identities
     were inferred from layout and caption. Eq. D2 is garbled in the text
     layer and is not reproduced.
   * **Recorded as printed.** The critical resolution is printed as
     "∆θp = 0.0125 − 0.25" (Fig. 5 caption) and "∆θp ≃ 0.25 − 0.0125M"
     (§6.1), while Fig. 5's abscissa spans $2^{-5}$–$2^{-1}$ and Table 1's
     low-resolution meridional spacings are 0.118–0.393, so 0.125–0.25 is
     the likely intent; not corrected. KORAL's time-averaged accretion
     rates in Table 4 (0.408/0.418, 0.318/0.361, 0.29/0.327 at
     96/128/192) are 1.6–2.7 times those of Table 2 (0.157, 0.199, 0.183)
     for the same nominal resolutions and window, unexplained. HARM-Noble's
     solver is "LLF" in Table 1 and "LF" in §4.1.6. The H-AMR throughput is
     quoted from Chatterjee et al. (2019) without hardware, precision or
     problem size.
   * **Reference list:** 210 printed entries, 209 works: Fragile et al.
     (2012), ApJS 201:9, is printed twice and merged once. Olivares et al.
     (arXiv:1906.10795) is merged into its A&A 629:A61 publication.
     Giacomazzo & Rezzolla is printed "24, 235" and recorded as Class.
     Quantum Grav. 24:S235. Löffler et al. (2012) is printed with a doubled
     "doi:" prefix. No article titles are printed (ApJS style).
