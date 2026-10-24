---
type: Source
title: "Komissarov & Phillips (2024) — A splitting method for numerical relativistic magnetohydrodynamics"
description: "Splits the relativistic MHD field into a force-free component and a plasma-inertia perturbation integrated together and recombined each step, with conditional energy transfer, so that a third-order finite-difference scheme with a new mapped-TVD WENO3, HLL and GLM cleaning survives magnetisations up to about 10^9; numerical resistivity is calibrated and plasmoid reconnection studied."
resource: "doi:10.1093/mnras/stae2620"
source_kind: paper
authors: [Komissarov S.S., Phillips D.]
year: 2024
venue: "Mon. Not. R. Astron. Soc. 536:1268-1302"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Monthly_Notices_of_the_Royal_Astronomical_Society_Komissarov_A_splitting_method_for_numerical_relativistic_magnetohydrody.pdf"
tags: [relativistic, mhd, finite-difference, weno, critical-points, numerical-dissipation]
timestamp: 2026-10-23T15:16:00Z
---

# Summary

Conservative schemes for ideal [relativistic MHD](/definitions/relativistic-hydrodynamics.md)
fail at high magnetisation $\sigma_{\mathrm m}=b^2/w_{\mathrm h}$: the conserved
variables can no longer be converted to physical primitives. Komissarov & Phillips
trace the failure to the Faraday equation. When the field dominates the
energy-momentum, small field errors push the plasma energy-momentum 4-vector into
the space-like domain. A simple analysis bounds the tolerable relative field error
by about $W^2/\sigma_{\mathrm m}$.

The remedy is the [force-free splitting](/methods/force-free-splitting-rmhd.md), a
dynamic generalisation of Tanaka's (1994) background-field splitting. The field is
written as a force-free (FFDE) component plus a perturbation due to plasma inertia.
The perturbation system is relativistic MHD without the terms quadratic in the
force-free field. Both systems are conservation laws and are integrated together.
At the end of every step they are recombined into a fresh force-free field and the
perturbation is zeroed. The force-free electric field is recovered from the
momentum only, so a conditional energy transfer moves a positive force-free energy
deficit above a threshold into the plasma. Exact total-energy conservation is given
up by design.

The code is a third-order point-value
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
close to ECHO. It interpolates primitives with a new third-order WENO, a
[mapping](/methods/mapped-weno.md) of Falle's second-order TVD weights whose
[smoothness indicators](/definitions/smoothness-indicator.md) carry a scale floor
meant to keep [accuracy at critical points](/properties/critical-point-accuracy.md).
It uses HLL fluxes, the DER step of Del Zanna et al. (their "3rd-order approximation for $\nabla\cdot f$", §3 (iv)) switched off near
strong shocks, and [GLM cleaning](/methods/glm-divergence-cleaning.md) of
[$\nabla\cdot B$](/properties/divergence-free-magnetic-field.md).

The tests include a [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
at $\sigma_{\mathrm m}=545$, which converges at third order. Degenerate Alfvén-wave
decay calibrates a [numerical-resistivity](/definitions/numerical-dissipation.md)
ansatz. There are shock and rarefaction tests, a moving Lundquist rope and a
[cylindrical explosion](/benchmarks/mhd-blast-wave.md) up to
$\sigma_{\mathrm m}\approx4.5\times10^9$. In the
[tearing of a Harris sheet](/benchmarks/tearing-mode-instability.md), the linear
growth agrees with Furth et al. (1963) and the late phase is plasmoid-dominated. An
ABC grid of ropes is compared with particle-in-cell (PIC) results.

# Version read

The archive file is arXiv:2409.03637v3 [astro-ph.HE], 15 November 2024, an MNRAS
LaTeX preprint ("Preprint 18 November 2024", blank received and accepted dates) that
acknowledges the referee. It is therefore the post-review text, not the typeset
version of record. Its 36 pages are all read (main text pp. 1–31, references
pp. 32–33, Appendices A–B pp. 33–36); pp. 8 and 18 were checked on the page images.
Title and authors match the Crossref record. The equation, section and table
numbers on this page are those of arXiv v3.

# Key claims

Registry notation. Page-local: $\sigma_{\mathrm m}=b^2/w_{\mathrm h}$ the
magnetisation, $b^2=B^2-\mathcal E^2$, $w_{\mathrm h}=\rho+\kappa_\gamma p$ the
enthalpy density with $\kappa_\gamma=\gamma/(\gamma-1)$; $B_{(0)}$, $\mathcal E_{(0)}$
the force-free and $B_{(1)}$, $\mathcal E_{(1)}$ the perturbation fields;
$E_{(0)}$ the force-free energy density and $\delta E_{(0)}$ its deficit after the
conversion; $\alpha_{\mathrm e}$ the transfer threshold; $\eta_{\mathrm{num}}$ the
numerical resistivity, $A_\eta$ its constant, $L$ the field length scale,
$r_{\mathrm o}$ the order of accuracy; $S_{\mathrm L}$, $S^*_{\mathrm L}$ the
Lundquist numbers on the sheet half-length and half-thickness (see the Notation
map).

1. The integration errors of the Faraday equation, not those of the energy-momentum equations, cause the high-$\sigma_{\mathrm m}$ failures specific to relativistic MHD; the latter's truncation errors are "the same as in numerical relativistic hydrodynamics" (§2.1). **Stated**
2. For $v_0\parallel B_0$ and $\delta B\parallel B_0$ the perturbed state stays physical only if $\delta B/B_0\lesssim2W_0^2/\sigma_{\mathrm m,0}$ (Eq. 17); for $v_0\perp B_0$ the bound is $\delta B/B_0\lesssim W_0^2/\sigma_{\mathrm m,0}$ (Eq. 20), and the bounds "differ only by the factor of two" (§2.1). **Derived** (approximate, special cases)
3. The perturbation equations (27)–(33) contain no terms quadratic in $B_{(0)}$, $\mathcal E_{(0)}$, which dominate at high $\sigma_{\mathrm m}$; this reduces the effect of force-free truncation errors on the plasma parameters (§2.2). **Derived**
4. The split scheme contains a force-free code (integrate only system 0, keep $B_{(1)}=\mathcal E_{(1)}=0$) and the standard unsplit code (skip step (i), keep $B_{(0)}=\mathcal E_{(0)}=0$), chosen by switches (§2.3). **Stated**
5. Transferring a positive deficit $\delta E_{(0)}>0$ to the plasma only heats it: with $\delta p=A\,\delta E_{\mathrm{pl}}$ and $A>0$ for $1<\gamma<2$, it "should not result in conversion failure"; a negative transfer could make the plasma 4-vector space-like, so it is switched off (§2.4). **Derived**
6. With the conditional transfer, conversion failures are "almost completely" eliminated even at extremely high $\sigma_{\mathrm m}$ (§2.4). **Shown** (qualitative)
7. The conversion algorithm (Eq. 66 with the cubic 72) converges by the secant method in at most 10 iterations "when $\sigma$ is not extremely large"; the Brent–Dekker fallback "always converges" once a bracket is found, in up to 60 iterations in extreme cases; a Monte-Carlo test showed "not a single incident of convergence failure" (§3.6, Fig. 1). **Shown**
8. The Alfvén-wave test ($B_0=50$, $\sigma_{\mathrm m}=545$) converges at third order from $N_x=20$ on, with $L^1(B_2)$ orders 3.5, 3.1, 3.0, 3.1 (Table 1); for $\sigma_{\mathrm m}\gg1$, $L^1(B_2)\propto\sqrt{\sigma_{\mathrm m}}$ and $L^1(\rho),L^1(p)\propto\sigma_{\mathrm m}$ (§4.1). **Shown**
9. In the 1D Harris sheet the total energy changes by about 1% with $\alpha_{\mathrm e}=1$ and about 0.09% with $\alpha_{\mathrm e}=0$; the transfer accounts for about 47% of the plasma heating, the rest coming from an uncontrollable channel, the interaction and perturbation field energies zeroed at each recombination (Eq. 85, Table 2). **Shown**
10. The threshold $\alpha_{\mathrm e}=10^{-3}$ suppresses parasitic heating at rarefactions while keeping current-sheet heating, and is the default (§4.2, Fig. 5). **Shown**
11. Numerical-resistivity ansatz (Eq. 91): $\eta_{\mathrm{num}}=A_\eta(L^2/\Delta t)(\Delta x/L)^{r_{\mathrm o}+1}=A_\eta L(\Delta x/\Delta t)(\Delta x/L)^{r_{\mathrm o}}$, $r_{\mathrm o}=3$, from accumulating the local truncation error over the resistive time (§4.3). **Derived** (heuristic; "a proper analytical study ... is beyond the scope")
12. The decay of a degenerate Alfvén wave confirms the ansatz: $\eta_{\mathrm{num}}\propto N_x^{-3}$, $A_\eta\approx0.031$ for $N_x\gtrsim20$, and the decay rate grows as $k_w^4$ (Table 3, Fig. 6). **Shown**
13. The ansatz is "almost identical to the special case" of Rembiasz et al. (2017), who "reported negative resistivity for their scheme" (§4.3). **Stated**
14. The split scheme captures low-$\sigma_{\mathrm m}$ fast shocks (FS7, $\sigma_{\mathrm m}=10^{-3}$; FS9, sub-relativistic) and high-$\sigma_{\mathrm m}$ fast and slow shocks (FS5, SS1, $\sigma_{\mathrm m}=10^3$) well; with the transfer off, the gas pressure of FS5 is about 20% low (§4.5). **Shown**
15. FS5A (FS5 in the upstream rest frame) fails in the plasma variables: the gas pressure overshoots the exact value more than tenfold. The authors attribute this to the near-light shock speed and a jump $\Delta B_2\approx2\times10^2$ (about 3 in FS5), giving "about one hundred times stronger numerical magnetic dissipation" (§4.5.5, Fig. 11). **Shown** (failure) / cause **Stated**
16. In the moving Lundquist rope ($v=0.8$, $\sigma_{\mathrm m}\approx2000$, $200^2$, $t=5$) pressure errors reach 8% and field errors are "hardly visible"; the standard mode crashes at the start even with Courant number 0.01 (§5.1, §5.6). **Shown**
17. The numerical resistivity is anisotropic: it is halved for a field at 45° to the grid (Tables 3, 5) and is modelled as $\eta_{\mathrm{num}}=\tfrac{\eta_0}4(3+\cos4\theta_B)$, $\theta_B$ the field angle (Eq. 98) (§5.2). **Shown** (factor) / Eq. 98 **Stated**
18. Cylindrical explosion: at $B_0=0.01$ and $0.1$ the split and standard modes are visually indistinguishable; at $B_0=1$ the standard mode crashes, and the earlier result of Komissarov (1999) could not be reproduced "on request, indicating some unusual undocumented tweaking of the code"; at $B_0=10^3$ ($\sigma_{\mathrm m}=4.5\times10^9$ outside) the split scheme runs, with Courant number 0.1 for the first steps (§5.3). **Shown**
19. The $B_0=0.1$ explosion on $200^2$ to $t=4$ takes 24 CPU seconds (134 steps), gfortran -O on one core of an Apple M2 at 3.49 GHz; the standard mode is only about 20% faster; variable conversion takes about 36% of the run time (§5.3). **Shown**
20. Harris-sheet tearing ($\sigma_{\mathrm m,0}=5\times10^4$, $400^2$): growth rates of about 2.7, 2.0 and 1.7 in successive unit intervals give $320<S^*_{\mathrm L}<480$ via Furth et al.'s $\omega_m\tau^*_A\approx0.63S^{*-1/2}_{\mathrm L}$; the resulting fastest wavelength range $0.25<\lambda_m<0.36$ matches the observed 0.33 (six plasmoids) (§5.4.1). **Shown**
21. In the nonlinear plasmoid-dominated phase the global reconnection rate from the energy growth is about 0.04; the inflow speed near an x-point is about 0.05, "only slightly below" the universal rate of about 0.1 (§5.4.2). **Shown**
22. Current sheets in the ABC grid fragment (one plasmoid each) at aspect ratio about 0.045, far above the Sweet–Parker value about 0.003 and close to the Pucci–Velli value 0.057, which supports Pucci & Velli (2014) (§5.5). **Shown**
23. Against PIC (Lyutikov et al. 2017), the electromagnetic energy at $t=10$ drops by about 40% in PIC and 18% here, so PIC reconnects about twice as fast; plasmoids form on a similar time scale (§5.5). **Shown**
24. The error parameter $E_r=(\delta B/B)\,\sigma_{\mathrm m}/W^2$, with $\delta B$ estimated from $\nabla\cdot B$, predicts the standard-mode failures: $E_r\gg1$ for the rope at start-up, $E_r\approx4$ for the $B_0=1$ explosion, $E_r\approx20$ near the tearing sheets, and $E_r\lesssim0.3$ for $B_0=0.1$, where the standard mode succeeds (§5.6, Fig. 22). **Shown**
25. The study "seems to be the first" more-or-less systematic study of plasmoid-dominated reconnection with ideal relativistic MHD codes in agreement with resistive theory (§6). **Stated**
26. The modified TVD/WENO weights restore accuracy at critical points; weights based only on ratios of Jiang–Shu-type indicators "do not differentiate between shocks and critical points" (App. A1). **Derived** (asymptotic argument; no isolated critical-point convergence test)

The third-order interpolation of Appendix A, in registry notation: candidates
$P_\mp$ the linear interpolants on $\{x_{i-1},x_i\}$ and $\{x_i,x_{i+1}\}$, indicators
$\beta_\mp=(u_i-u_{i\mp1})^2+U^2/n_{\mathrm{sm}}^2+\epsilon$ with
$U=\max(\lvert u_{i-1}\rvert,\lvert u_i\rvert,\lvert u_{i+1}\rvert)$,
$n_{\mathrm{sm}}=10$, $\epsilon=10^{-25}$; Falle's TVD weights
$\omega_-=\beta_+/(\beta_-+\beta_+)$, $\omega_+=\beta_-/(\beta_-+\beta_+)$; linear
weights $d_a=1/4$, $d_b=3/4$; and the mapping $g_n(\omega)=1-(1-2\omega)^n$, with
$\omega^r_+=d_bg_n(\omega_+)$ for $\omega_+\le\tfrac12$ and
$1-d_ag_n(1-\omega_+)$ otherwise ($a$ and $b$ swapped for the left face; $n=4$ in
Fig. A1). The authors liken it to the mapped WENO5 of Henrick et al. (2005).

# Printed slips

- **FS9 magnetisation:** §4.5.2 prints "$\sigma=10^{-3}$", Table 4 prints $\sigma=10^{-4}$, and §6 repeats "$\sigma=10^{-3}$" for FS7 and FS9. *(Compiler check, not in the sources:)* from the Table-4 state, $B^2=2(0.0070724819)^2=1.0004\times10^{-4}$ and $w_{\mathrm h}=1+4\times10^{-4}$ at rest, so $\sigma_{\mathrm m}\approx1.0\times10^{-4}$, as is the printed $\beta=2$.
- **1D Harris sheet:** §4.2 prints "asymptotic magnetisation $\sigma=54500$" for $B_0=500$, $p_0=\rho_0=1$, $\gamma=4/3$. *(Compiler check, not in the sources:)* $w_{\mathrm h}=1+4\cdot1=5$, so $\sigma_{\mathrm m}=500^2/5=5\times10^4$, the value §5.4 prints for the same parameters.
- **FS5A shock speed:** §4.5.3 and §4.5.5 print $v_s=-0.99968$; Table 4 gives $v_{sh}=-0.99989427$. *(Compiler check, not in the sources:)* the shock speed $-0.5$ seen from the upstream frame moving at $0.99968283$ is $(-0.5-0.99968283)/(1+0.5\cdot0.99968283)=-0.9998943$, the Table value; the text value is the upstream speed itself.
- **SS test (§4.5.4):** "slow magnetosonic Mach number $M_f=2.1$" (Table 4: $M_s=2.101839785$); the text shows "the solution at $t=10$, when the shock is expected to reach $x=-5.0$", outside the domain $(-1.5,0.5)$, while the Fig. 10 caption says $t=2$. The test is "SS" in the text and SS1 in Table 4.
- **Fig. 5:** the caption gives the middle panel as $\alpha_e=0.01$ at $t=4$; the text says $\alpha_e=0.001$ and $t=4.5$.
- **ABC grid (§5.5):** "$k=2/\pi$" on the periodic domain $(-1,1)^2$. *(Compiler check, not in the sources:)* the field period $2\pi/k=\pi^2\approx9.9$ is not compatible with a periodic domain of width 2; $k=2\pi$ would be.
- **Table 5:** the row "$2\eta k^2$" with $k=2\sqrt2\pi$. *(Compiler check, not in the sources:)* the printed $0.39$ at $N_x=10$ gives $\eta=0.39/(2\cdot8\pi^2)=2.5\times10^{-3}$, whereas the printed $\eta_{num}=0.50\times10^{-2}$ equals $0.39/(2\cdot4\pi^2)$, i.e. uses $k=2\pi$. The text calls the resistivities "exactly the same" as in Table 3, which prints $0.49\times10^{-2}$ and $A_\eta=0.063$ against $0.50\times10^{-2}$ and $0.064$.
- **Tearing length scale (§5.4):** $L=\frac a{\sqrt2}\cosh\frac xa$, although the sheet varies in $y$; "At $x=a$, $L\approx0.009$". *(Compiler check, not in the sources:)* with $a=0.01$, $a\cosh(1)/\sqrt2=0.0109$.
- Unresolved references: a citation "?" in §6 and "figure reffig:fs5a" in §4.5.5. App. B solves "the cubic equation (12)", which is the cubic (B19); it cites "Del Zanna (2007)" for Del Zanna et al. (2007).
- Symbols: $n_{sm}$ printed $n_s$ in "we set $n_s=10$"; one constant named $\hat E_1$ (Eq. 70) and $\tilde E_1$ (B23); $\kappa$ both $\Gamma/(\Gamma-1)$ and the GLM damping rate; "rounding error" for truncation error (§2.4, §4.3, §6). Fig. 2 caption "Alfwen".

# Notation map

| Komissarov & Phillips (arXiv v3) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B$, $E$ | $B$, $\mathcal E$ | magnetic and electric field ($c=1$, no $4\pi$); **collision**: registry $E$ is the total energy |
| $B_{(0)},E_{(0)}$; $B_{(1)},E_{(1)}$ | $B_{(0)},\mathcal E_{(0)}$; $B_{(1)},\mathcal E_{(1)}$ (local) | force-free and perturbation parts; the subscript is not a time level |
| $\mathcal E$, $S$ ($\Pi^\nu=(\mathcal E,S)$) | $E$, $S_{\mathrm m}$ (local) | energy and momentum densities; **collision** of $S$ with the source $S(u)$ and of $\mathcal E$ with the electric field |
| $v$, $\gamma$, $u=\gamma v$ | $v$, $W$, $Wv$ | **collision**: $\gamma$ is the Lorentz factor, $u$ the 4-velocity |
| $\Gamma$, $\kappa=\Gamma/(\Gamma-1)$ | $\gamma$, $\kappa_\gamma$ (local) | $\Gamma=4/3$; **collision** of $\kappa$ with the kinetic energy |
| $w=\rho+\kappa p$ | $w_{\mathrm h}$ (local) | enthalpy density; **collision** with the entropy variables $w$ and with the TVD weights $w_\pm$ |
| $\sigma=b^2/w$ | $\sigma_{\mathrm m}$ (local) | **collision** with the affine scaling $\sigma$ |
| $\beta=p/p_m$ | $\beta_{\mathrm p}$ | plasma beta; agrees, since $p_m=B^2/2$ |
| $q$, $f$, $Q$, $\mathcal F$ | $u$, $f$, grid array, $\mathcal L$ | point values (finite difference) |
| $u^l$, $u^r$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | interface states |
| $a^\pm\ge0$ | $s^+$, $-s^-$ | HLL speed bounds, both written nonnegative in the source |
| $\Phi_{(s)}$ | $\psi_{\mathrm{GLM}}$ per system | damping rate $0.2/\Delta t$ |
| $S_\pm$, $P_\pm$ | $S_k$, $P_\mp$ | two-point sub-stencils and linear interpolants; **collision** of $S$ with the momentum |
| $\beta_\pm$ | $\beta_k$ | indicators with the floor $U^2/n_{\mathrm{sm}}^2+\epsilon$ |
| $w_\pm$; $w^l_\pm$, $w^r_\pm$ | $\omega_\pm$; $\omega^l_\pm$, $\omega^r_\pm$ | TVD and WENO weights |
| $\gamma_a=1/4$, $\gamma_b=3/4$ | $d_a$, $d_b$ | linear weights; **collision** with the Lorentz factor and $\gamma_k$ |
| $p_n(x)=1-(1-2x)^n$ | $g_n(\omega)$ | mapping; **collision** of $p$ with the pressure |
| $C$, $h$ | $\nu$, $\Delta x$ | Courant number, $\Delta t=C\Delta x$; **collision** of $h$ with the numerical flux |
| $r$ | $r_{\mathrm o}$ (local) | order of accuracy, 3; **collision** with the registry's stencil size $r$ |
| $\eta$, $\eta_{num}$, $A_\eta$, $L$, $n_L$ | $\eta_{\mathrm m}$, $\eta_{\mathrm{num}}$, $A_\eta$, $L$, $n_L$ (local) | **collision** of $\eta$ with the entropy |
| $k$ (wave) | $k_w$ | wavenumber |
| $S$, $S^*$, $\tau_A$, $\tau^*_A$ | $S_{\mathrm L}$, $S^*_{\mathrm L}$, $\tau_A$, $\tau^*_A$ (local) | Lundquist numbers and Alfvén times |
| $X=u^2-u_{(0)}^2$, $W=w\gamma^2$, $D=\rho\gamma$ | local | conversion variables; **collision** of $W$ with the registry Lorentz factor |
| $\alpha_e$, $\alpha_u$, $\alpha_p$ | $\alpha_{\mathrm e}$, $\alpha_u$, $\alpha_p$ (local) | transfer and shock-detector thresholds |

# Reference list

The paper prints 79 references in MNRAS author-year style, mostly without titles and
with first pages only. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `komissarov-2024`. The
same-author-year works of Komissarov take suffixes in printed order, so the printed
2007a and 2007b (with Barkov et al.) are `komissarov-2007-b` and `komissarov-2007-c`
after the single-author 2007 paper. Harten, Lax & van Leer (1983) and Martí (2015,
Comput. Phys. Commun.) are matched by venue to their existing keys. Three arXiv
preprints are kept as their own entries, and the Event Horizon Telescope
Collaboration (2021) is a corporate author. The unresolved "?" of §6 has no entry.
No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunk 10 (2026-10-23). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Constrained transport for the induction equation](/methods/constrained-transport.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Force-free splitting for relativistic MHD](/methods/force-free-splitting-rmhd.md)
* [GLM divergence cleaning](/methods/glm-divergence-cleaning.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
* [Tearing-mode instability](/benchmarks/tearing-mode-instability.md)
