---
type: Method
title: "Active model split hybrid RANS/LES"
description: "Haering, Oliver and Moser's hybrid RANS/LES method that splits the modelled stress into a mean part scaled from RANS and an energy-transfer part acting on resolved fluctuations, and adds active forcing where an anisotropic resolution indicator allows; it needs no blending function and removes log-layer mismatch."
status: established
aliases: [AMS, active model split, model splitting, model-split hybrid RANS/LES]
tags: [hybrid-rans-les, eddy-viscosity, sgs-model, boundary-layer, separated-flow]
timestamp: 2026-10-25T13:49:00Z
---

# Active model split hybrid RANS/LES

Active model split (AMS) is a [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
method built to remove modelled-stress depletion and the ad hoc blending of
RANS and LES models ([Haering et al. (2022)](/sources/haering-2022.md)). It
has three parts, all active everywhere: a *mean-stress* model that supplies
the unresolved part of the Reynolds stress, scaled down from a RANS model by
the unresolved fraction of the kinetic energy; an *energy-transfer* model
that drains energy from the resolved fluctuations only; and an *active
forcing* that creates resolved fluctuations at the smallest locally
resolvable scale wherever an anisotropic resolution indicator says the grid
can carry them. No blending function is used, and in the DNS limit every
model term vanishes, so AMS "is essentially an LES that by construction
respects both RANS and DNS limits" (§IV E).

Notation (page-local unless in the registry): $k_{\mathrm{tot}}$,
$k_{\mathrm{sgs}}$, $k_{\mathrm{res}}$ are the registry's total, subgrid and
resolved kinetic energies; $\alpha_k=k_{\mathrm{sgs}}/k_{\mathrm{tot}}$ is the
modelled-energy fraction and $\beta_k=1-k_{\mathrm{res}}/k_{\mathrm{tot}}$ the
computable unresolved fraction; $\nu_s$, $\nu_e$, $\nu_{\mathrm{tot}}$ are the
mean-stress, energy-transfer and total eddy viscosities; $\bar u_i'=\bar u_i-\langle\bar u_i\rangle$
and $\bar S'_{ij}$ are the resolved velocity and strain fluctuations;
$\{\phi\}$ is the pseudo-mean defined below. Stresses are written in the
registry's positive-trace convention; Haering et al. define their subgrid
stress with the opposite sign.

## Model splitting

Haering et al. require two statistical properties of a subgrid model for an
accurate mean flow: the right mean subgrid stress, and the right mean energy
transfer from resolved to subgrid scales. RANS models are built only for the
first, LES models are calibrated only for the second (§III, Eqs. 4–5). The
split model

$$\tau^d_{ij}\approx-2\nu_s\langle\bar S_{ij}\rangle-2\nu_e\bar S'_{ij}$$

can meet both at once in flows with a one-dimensional mean, provided both
viscosities are non-fluctuating; otherwise cross terms such as
$\langle\nu_e\bar S'_{ij}\rangle$ contribute to the mean stress (§III A, Eqs.
6–8). With a triple decomposition of the velocity into mean, resolved
fluctuation and subgrid fluctuation, and gradient-diffusion scaling of each
mixed term with time scales $k_{\mathrm{tot}}/\varepsilon$ and
$k_{\mathrm{sgs}}/\varepsilon$, they derive (§III B, Eqs. 15–24)

$$\nu_s=\alpha_k(2-\alpha_k)\,\nu_{\mathrm{tot}},\qquad\nu_e=\alpha_k(1-\alpha_k)\,\nu_{\mathrm{tot}},$$

so that $\langle\tau^d_{ij}\rangle=-2\nu_s\langle\bar S_{ij}\rangle$ and the energy
transfer comes entirely from $2\nu_e\langle\bar S'_{ij}\bar S'_{ij}\rangle$.
$\nu_e$ vanishes in both the RANS ($\alpha_k=1$) and DNS ($\alpha_k=0$) limits.
*(Compiler check, not in the sources: summing the authors' symmetrized
mixed-term estimates, $-2\alpha_k\nu_{\mathrm{tot}}(2\langle S\rangle+\bar S')$
for the cross terms and $+2\alpha_k^2\nu_{\mathrm{tot}}(\langle S\rangle+\bar S')$
for the subgrid–subgrid term, gives exactly these coefficients.)* The
authors conclude that the single-viscosity form "is not generally valid",
because the mean and fluctuating gradients scale differently, and that
"model splitting like that described here is how LES should generally be
performed" (§III B, §VI); see the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md).

$\alpha_k$ is not computable in a simulation; $\beta_k$ is. For filters that
minimize the $L^2$ error the two coincide, but second-order finite volume
"most closely approximates box filtering", and box-filtered channel DNS at
$Re_\tau=1000$ (six filter sizes, $y^+<300$ excluded) gives
$\alpha_k=\beta_k^{1.7}$; Kolmogorov scaling in isotropic turbulence at
infinite $Re$ would give $\alpha_k\propto\beta_k$. The same data support the
$\alpha_k(2-\alpha_k)$ scaling of the subgrid shear stress, with
$\alpha_k^{9/8}(2-\alpha_k)$ fitting "slightly better" (§III B, Fig. 1).

## Components of AMS

**Pseudo-mean.** Using the true mean in the model "yields poor simulation
results", empirically. AMS uses a causal exponential time filter,
$d_t\{\phi\}=(\bar\phi-\{\phi\})/T_{\mathrm{ave}}$ with
$T_{\mathrm{ave}}=C_\phi k_{\mathrm{tot}}/\varepsilon$, $C_\phi=1$ (4 for the
production); fluctuations are taken about it, so the slow large scales act
as an unsteady mean for the subgrid (§IV A, Eq. 25). The model "appears
somewhat insensitive" to $C_\phi$, whose value was not optimized.

**Mean stress.** The mean part is the RANS deviatoric Reynolds stress
evaluated from pseudo-mean quantities and multiplied by
$\alpha_k(2-\alpha_k)$, with $\alpha_k=\beta_k^{1.7}$. $k_{\mathrm{tot}}$ comes
from a RANS $k$-equation whose $k$ is the kinetic energy; its production
uses the total (modelled plus resolved) stress against the pseudo-mean
strain, $P_k=-\big[(\tau^s_{ij}+\bar u_i'\bar u_j')\{S_{ij}\}\big]$, in which
$\tau^s_{ij}$ denotes the modelled mean stress (§IV B, Eqs. 26–27). The
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) is excluded because its
$k$ is, in attached boundary layers, "more akin to $\tfrac32v^2$";
the base models are the Chien low-Reynolds $k$-$\varepsilon$ and a
$v^2$-$f$ model ($v^2$ its wall-normal velocity variance variable, page-local) with a new time-scale limit (App. A, Eq. A3).

**Energy transfer.** The fluctuating part uses the anisotropic M43 tensor
eddy viscosity of the same group, $\nu^E_{ij}=f(r_{\mathcal M})\,C(\mathcal M)\,
\varepsilon^{1/3}\mathcal M^{4/3}_{ij}$, with $\mathcal M_{ij}$ the resolution
tensor (whose eigenvalues are the grid scales in the principal directions)
and $\varepsilon$ from the RANS model, acting on the resolved fluctuating
velocity gradient:
$\tau^e_{ij}=-\big(\nu^E_{ik}\partial_k\bar u_j'+\nu^E_{jk}\partial_k\bar u_i'-\tfrac23\nu^E_{mn}\bar S'_{mn}\delta_{ij}\big)$
(§IV C; App. B, Eqs. B1–B4, coefficients for second-order finite volume in
Table VI; $f(r_{\mathcal M})=\max(\min(\langle r_{\mathcal M}\rangle^2,30),1)$).
Because $\nu^E$ does not fluctuate, $\langle\tau^e_{ij}\rangle=0$ and the two
parts are exactly the mean and fluctuating model stress (§IV C).

**Resolution adequacy.** An anisotropic indicator $r_{\mathcal M}$ compares
the grid, through $\mathcal M_{ij}$, with the smallest locally resolvable
scale estimated from a tensorial subgrid production and the unresolved
energy $\beta_kk_{\mathrm{tot}}$ (§IV D 1, Eqs. 28–34). It is a conservative
bound and reduces, for an isotropic grid and isotropic equilibrium
turbulence, to a DES-like length-scale comparison: "an anisotropic
generalization of the DES resolution metric". A coefficient $C_r$, "how many
grid spacings are required", is 1 by default. $\langle r_{\mathcal M}\rangle<1$
means the grid can resolve smaller scales.

**Active forcing.** Where $\langle r_{\mathcal M}\rangle<1$ a body force $f_i$
with a Taylor–Green-vortex structure, advected with the pseudo-mean, injects
fluctuations of size $\min(8L_{\mathrm{sgs}},d)$ with
$L_{\mathrm{sgs}}=(\beta_kk_{\mathrm{tot}})^{3/2}/\varepsilon$ and target
magnitude $8\sqrt{a_vk_{\mathrm{tot}}}/(\sqrt{\beta_k}\,T)$, where
$a_v=\tfrac32v^2/k$ is an anisotropy surrogate from the
$v^2$-$f$ relation and $T=k/\varepsilon$ (page-local names); the
force is switched off where it would remove energy, $f_i\bar u_i'<0$, and is
limited towards the RANS and DNS limits (§IV D 2–3, Eqs. 35–45). The authors
call the structure ad hoc, a "place holder". It is not divergence-free; the
incompressible solver projects out its dilatational part, and in
compressible solvers it "may result in spurious acoustic sources" (§IV E).

## Results

All runs use the second-order incompressible finite-volume code CDP (§V).

- **Channel, $Re_\tau\approx5200$**, Chien $k$-$\varepsilon$ with $u_\tau$
  prescribed from DNS, four grids with $\Delta x^+\approx700$ to $1550$ (a
  horizontal-resolution range of at least 2.2): all grids predict the mean
  adequately with no [log-layer mismatch](/definitions/log-layer-mismatch.md);
  $\beta_k$ falls to 0.4 at the centre of the fine grid, beyond the
  $\beta_k\lesssim0.1$ that typical LES requires, "enabling true 'coarse' LES";
  the RANS $k$ stays "virtually unchanged" from pure RANS and agrees with the
  resolved-plus-modelled energy; resolution anisotropy reaches 20:1 without
  harm (§V A 1, Table I, Figs. 2–3).
- **Transition from RANS.** Started from RANS in time, $\beta_k$ overshoots to
  0.4 at 1.6 flow-throughs and the mean is temporarily blunted before
  healing by about 8; in a $16\pi$-long channel with a RANS inlet, $\beta_k$
  falls without overshoot but only to "just under 0.7" after $12\pi$; the
  authors conclude that the forcing relies on streamwise periodicity to be
  most effective (§V A 2–3, Figs. 4–7).
- **Channel, $Re_\tau=20{,}000$**, $v^2$-$f$ base model: AMS produces
  an outer peak of $k$, but the mean departs from the log law for
  $y^+=200$–$2000$, which the authors attribute to the RANS model (§V A 4,
  Fig. 8).
- **[Periodic hill](/benchmarks/periodic-hill.md), $Re_h=10{,}600$**, grids of
  0.2 to 0.9 million cells (14 to 62 times fewer than the 13-million-cell
  wall-resolved LES): RANS reattaches at about $x=7$, AMS near the reference
  $x\approx4$, with mean velocity close to experiment and wall-resolved LES at
  all resolutions; the vertical velocity just after separation stays close to
  RANS because $\beta_k\approx1$ in the separating shear layer. The authors
  state "nearly identical results to the wall-resolved LES ... at a
  resolution reduction of over an order-of-magnitude and computational costs
  reduced by a factor of 30 or more" (no timings given) and estimate a
  [wall-modelled LES](/methods/wall-modelled-les.md) of the hill at about 12
  million cells, or 1.6 million with streamwise grid variation (§V B,
  Table II, Figs. 9–12).
- **$C_r$.** Halving $C_r$ to 0.5 on the coarse channel lowers the centre
  $\beta_k$ from just above 0.5 to 0.2 with only slight changes to the mean;
  $C_r<0.5$ distorts the mean and $k$; $C_r=0.5$ "may be more appropriate for
  the numerical schemes used here" (§V C, Figs. 13–15).
- **Energy-transfer variants.** Anisotropic M43 performs best; an
  $\alpha_k$-based eddy viscosity and an upwinding (implicit) transfer model
  also work; isotropic M43 overpredicts the wall stress, so M43 "does require
  the anisotropic form" (§V D, Fig. 16). Fluctuating-viscosity models
  (Smagorinsky, Vreman, WALE) would require their contribution to the mean
  stress to be subtracted from the mean-stress model.

## Qualifications

- $\alpha_k=\beta_k^{1.7}$ is fitted to box-filtered channel DNS; the
  authors state that the relation must be found "for the particular
  numerics of the code in use" and "depends on characteristics of the
  turbulence" (§III B).
- The authors print the reconstruction of the total kinetic energy two ways:
  resolved plus $\alpha_k$ times the RANS $k$ (captions of Figs. 3 and 8) and
  resolved plus $\beta_k$ times the RANS $k$ (captions of Figs. 13 and 16, text
  p. 23); with $k_{\mathrm{sgs}}=\alpha_kk_{\mathrm{tot}}$ by their definition the
  two differ.
- The steady coarse-grid centre value of $\beta_k$ is "about 0.6" in §V A 2
  and "just above 0.5" in §V C, for the same grid and $C_r=1$.
- Their Eq. 1, the $\varepsilon$-destruction model
  $2\langle\partial_j\partial_ku_i\,\partial_j\partial_ku_i\rangle\approx C_{\varepsilon2}\varepsilon^2/k$,
  lacks a factor $\nu^2$ on the left as printed *(compiler check, not in the
  sources: the left side has units $\mathrm{L^{-2}T^{-2}}$, the right
  $\mathrm{L^2T^{-4}}$)*.

# Citations

- [Haering et al. (2022)](/sources/haering-2022.md) — §II–§VI; Eqs. 3–45; App. A–C; Tables I–II, VI; Figs. 1–16.
