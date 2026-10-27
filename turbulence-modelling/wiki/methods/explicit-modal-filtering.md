---
type: Method
title: "Explicit modal filtering as an LES closure"
description: "Explicit filtering of the solution itself, in the modal space of a high-order element or by compact physical-space filters, damps the highest resolved modes in place of a subgrid stress. The sources gate it by a resolution or smoothness sensor, tie its cutoff to local flow characteristics, and compare it with Smagorinsky, entropy filtering, split forms and implicit LES."
status: established
aliases: [explicit modal filter, modal filtering, solution filtering, dynamic explicit modal filter, DEMF, self-tuning dynamic explicit modal filter, STDEMF, local modal filter, LMF, explicit filtering regularization, relaxation filtering]
tags: [les, filtering, implicit-les, dg, numerical-dissipation, sgs-model]
timestamp: 2026-10-27T06:03:00Z
---

# Explicit modal filtering as an LES closure

**Explicit filtering of the solution** replaces or supplements a subgrid
stress by a filter applied to the conserved variables during the time
integration. In a high-order element method the solution of each element is
transformed to a modal (orthogonal-polynomial) basis, the high-index modes
are attenuated by a low-pass kernel, and the result is transformed back,
possibly blended with the unfiltered solution. The filter removes the energy
that piles up at the resolution limit when the subgrid scales are missing,
so it acts as the closure of a
[large-eddy simulation](/definitions/large-eddy-simulation.md) with no
modelled stress, between explicit modelling and
[implicit LES](/definitions/implicit-les.md). It differs from
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
which weights an added viscous flux mode by mode rather than the solution.
The sources use three forms: a dynamic modal filter with a flow-dependent
cutoff ([Ranjbar et al. 2026](/sources/ranjbar-2026.md)), an exponential
modal filter switched on by a smoothness sensor
([Wang 2024](/sources/wang-2024-b.md)), and compact physical-space filters
used as a regularization of finite-difference LES
([Caban et al. 2026](/sources/caban-2026.md)), including the relaxation
(selective) filter of central schemes ([Volpiani 2024](/sources/volpiani-2024.md)).

## Modal transform and kernel

In one reference direction, with $N$ the polynomial degree, the nodal
solution $\sum_{i=0}^{N}u_i\,l_i(\xi)$ on Lagrange interpolants $l_i$ equals
a modal expansion $\sum_{k=0}^{N}\hat u_k\,P_k(\xi)$ in orthogonal
polynomials $P_k$ (all page-local). Ranjbar et al. (2026, §II.B,
Eqs. 17–27) obtain the forward and backward matrices from orthogonality,

$$\hat u_k=\sum_{i=0}^{N}\mathcal M_{ki}u_i,\quad \mathcal M_{ki}=\frac{\int_{-1}^{1}l_iP_kw\,d\xi}{\int_{-1}^{1}P_k^2w\,d\xi},\qquad u_k=\sum_{i=0}^{N}\mathcal N_{ki}\hat u_i,\quad \mathcal N_{ki}=\frac{\int_{-1}^{1}P_il_k\,d\xi}{\int_{-1}^{1}l_k^2\,d\xi},$$

with $w$ the weight of the polynomial family and $\mathcal M$, $\mathcal N$
page-local. The backward formula uses the discrete orthogonality of the
Lagrange interpolants under the nodal quadrature (Gauss–Lobatto or
Gauss–Legendre, citing Mateo-Gabín et al.). In three dimensions the
transform is three successive one-dimensional products (Eqs. 26–27). The
matrices are computed once; the authors use Legendre polynomials on
Gauss–Lobatto points ($w=1$). Their earlier version (DEMF, Ranjbar et al.
2024, cited) was tied to Chebyshev polynomials on a staggered Chebyshev grid,
where the transform is a discrete cosine transform.

Wang (2024, §2.3, Eqs. 17–18) uses the matrix form
$\mathcal F=\mathcal V\Lambda\mathcal V^{-1}$ of Hesthaven & Warburton
(cited), with $\mathcal V$ the Vandermonde matrix and the exponential
kernel on the diagonal $\Lambda$: modal weights $1$ below a cutoff
$\vartheta_c$ of the normalized mode index $\vartheta_m$ and
$\exp\{-\alpha_f[(\vartheta_m-\vartheta_c)/(1-\vartheta_c)]^{s_f}\}$ above
it, with $\alpha_f=36$ (printed as $-\log_{10}$ of machine precision; see Qualifications) and
$s_f=6$ (registry symbols; the source's $\eta$, $\alpha$, $s$;
$\vartheta_c$ not printed).

**Grouped modes.** Ranjbar et al. (§II.B, Eqs. 28–31) do not use a tensor
product of one-dimensional kernels. They group the three-dimensional modes
$(i,j,k)$ by the radius $\sqrt{i^2+j^2+k^2}\in[n-\tfrac12,n+\tfrac12)$ into
"energy levels" $\Gamma_n$, the $\ell^2$ norm of the modes of group $n$,
$2\le n\le n_g$ with $n_g=\mathrm{round}\big(\sqrt{3(N+1)^2}\big)$ the
number of groups (all page-local; the source's $N$). High-index $\Gamma_n$
measure small scales, and energy accumulation in under-resolved flow shows
as large high-index $\Gamma_n$. The kernel acts on the group index:

$$\varphi_n=\begin{cases}1,& n\le M_c,\\ -\tanh\!\Big[-3\,\dfrac{(n-n_g)^2}{(M_c-n_g)^2}\Big],& n>M_c,\end{cases}$$

($\varphi_n$, $M_c$ page-local; the source's $\mathscr F_n$ and $M$). It
keeps the groups up to the real-valued cutoff $M_c$, attenuates those above,
and vanishes at the highest group $n=n_g$. The earlier DEMF used a sharp
cutoff that removed a user-chosen integer number of the highest groups.
For $N=4$ there are 8 energy levels, $n=2,\dots,9$ (§II.B).

**Blending and frequency.** After the back-transform the filtered nodal
values are blended with the unfiltered ones, $u^{\mathrm r}=\alpha_bu^{\mathrm f}+(1-\alpha_b)u$
(Eq. 44; $\alpha_b$, $u^{\mathrm f}$, $u^{\mathrm r}$ page-local), and the
filter may act every few steps. Citing Ghiasi et al. (2019), Ranjbar et al.
state that settings with the same product of blending factor and filtering
frequency give identical results; they use $\alpha_b=0.01$ every step.

## Where and how strongly to filter

**Resolution sensor.** Ranjbar et al. (§II.B, Eqs. 40–42, from their DEMF)
filter only elements with $\eta<\Delta$, where $\eta$ is a local Kolmogorov
length from the element-averaged dissipation of the velocity fluctuations
and $\Delta=\mathcal J^{1/3}/\prod_i(N_i+1)^{1/3}$ the average grid spacing
of the element ($\mathcal J$ the Jacobian determinant; after Komperda et
al., cited). The paper does not say how the mean of the fluctuations is
taken.

**Self-tuned cutoff.** Their contribution (§II.B, Eqs. 34–39) makes the
cutoff element-wise and time-dependent:

$$M_c=n_g\Big(\frac{\Delta}{\eta}\Big)^{-c_{\mathrm{st}}}(1-X)^{c_{\mathrm{st}}},\qquad X=X_SX_\Omega,$$

$$X_S=1-\exp\Big(\frac{-\lvert\bar Q_S\rvert}{\langle\lvert\bar Q_S\rvert\rangle+\kappa_{\mathrm r}}\Big),\qquad X_\Omega=1-\exp\Big(\frac{-\bar Q_\Omega}{\langle\bar Q_\Omega\rangle+\kappa_{\mathrm r}}\Big),$$

with $Q_S=\tfrac12[(\mathrm{tr}\,S)^2-\mathrm{tr}(S^2)]$ and
$Q_\Omega=-\tfrac12\mathrm{tr}(\Omega^2)$ the second invariants of the
strain- and rotation-rate tensors (after Tlales et al., cited), $\bar Q$
their nodal average over the element, $\langle\cdot\rangle$ an average over
the unresolved elements (over all of them in a periodic box, over
homogeneous planes or time in a channel), $\kappa_{\mathrm r}$ a small
regularizing constant (value not printed) and $c_{\mathrm{st}}>0$ the one
tunable constant ($M_c$, $X$, $X_S$, $X_\Omega$, $Q_S$, $Q_\Omega$,
$\kappa_{\mathrm r}$, $c_{\mathrm{st}}$ page-local; the source's $M$, $X$,
$Q$, $\kappa$, $c$). The filter strengthens (lower $M_c$) as $\Delta/\eta$
grows and where strain and rotation are strong. The authors choose
normalization by averages over thresholds because thresholds are
problem-dependent (Pang et al.; Tlales et al., cited). The motivation is a
priori: joint PDFs on coarse Taylor–Green runs associate large $\lvert Q_S\rvert$,
$Q_\Omega$ and $X$ with large high-index energy levels, so the cutoff should
depend on strain and rotation and not only on $\eta$ (§III.B, Figs. 8–10).
In their worked example, $N=10$ gives $n_g=19$, and with $X=0.6$,
$c_{\mathrm{st}}=0.4$ the cutoff is $M_c=11.2$ at $\Delta/\eta=1.5$ and
$9.12$ at $\Delta/\eta=2.5$ (Fig. 1). The fixed cutoff
$M=5\sqrt N$ of Karamanos & Karniadakis for SVV, and the fixed cutoffs of
later SVV work and of DEMF, are the contrast (§II.B).

**Smoothness sensor.** Wang (2024, §2.3, Algorithm 1) calls the scheme a
local modal filter: after every Runge–Kutta stage the Persson–Peraire
indicator $s_e$ of the density (the $\log_{10}$ of the relative energy in
the highest mode) is computed in each element, and the filter acts where
$s_e\ge s_0$. The thresholds of the Li–Wang classification cannot be used
directly: the lower one filters too many elements, the upper one does not
stabilize. A range just below the Li–Wang centre works, summarized as
$s_0\in[-(N+2),-(N+1)]$ for $N=2$, 3 (Table 2b, §5; see
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
for the indicator).

## Explicit filters as a regularization in finite differences

[Caban et al. (2026)](/sources/caban-2026.md) (§3.1, Eqs. 13–17, Table 1)
regularize compact-difference LES by explicit physical-space filters of the
compact form

$$\bar f_j+\sum_{k=1}^{M_s}a_k(\bar f_{j+k}+\bar f_{j-k})=\tfrac12\sum_{l=0}^{N_s}b_l(f_{j+l}+f_{j-l}),\qquad \hat G_E(kh)=\frac{\sum_{l=0}^{N_s}b_l\cos(l\,kh)}{1+2\sum_{k'=1}^{M_s}a_{k'}\cos(k'kh)},$$

($M_s$, $N_s$, $a_k$, $b_l$, $\hat G_E$ page-local; $M_s=0$ gives a
finite-difference filter), of order $2N_s$, with $\hat G_E(0)=1$ and
$\hat G_E(\pi)=0$, and the free parameter $a_1$ widening the pass band. Their
regularization filter (N-DI-R) is the approximate-deconvolution form

$$\hat G_{QG}=1-(1-\hat G_E)^{N_{\mathrm{AD}}+1}$$

($\hat G_{QG}$, $N_{\mathrm{AD}}$ page-local), built from the eighth-order
compact filter with $N_{\mathrm{AD}}=2$ and applied in three dimensions to
the velocity at the end of each time step. It is close to one over a much
wider range than $\hat G_E$ and acts only on small scales; explicit
filtering with it is "equivalent to" the dissipative relaxation term of
Stolz et al. (cited) of the
[approximate deconvolution model](/methods/scale-similarity-model.md). In
the transitional Taylor–Green vortex at $Re=1600$ on $64^3$, this filter
with no subgrid model, an implicit LES, gives an energy-history error of
$2.23\times10^{-2}$ with sixth- and tenth-order compact derivatives, about
half that of the best eddy-viscosity run and better than the adaptive local
deconvolution of Hickel et al. (cited); with second-order differences the
same combination is unstable (§5.3.1, Table 4, Fig. 19). In the laminar
Taylor–Green test the filter lowers the effective Reynolds number from the
energy decay, as dissipative interpolation does (§5.1, Figs. 10–11; see
[numerical dissipation](/properties/numerical-dissipation.md)).

**Relaxation (selective) filtering.** [Volpiani (2024)](/sources/volpiani-2024.md)
(§2.2.2, Eqs. 7–8, Table 3) stabilizes the central finite differences of
the Python solver BASIC by a relaxation filter applied to the conservative
variables in all three directions at every time step,

$$u^{\mathrm f}_j=u_j-\chi_f\sum_{l=-N_p}^{N_p}d_l\,u_{j+l},\qquad D_k(kh)=d_0+2\sum_{l=1}^{N_p}d_l\cos(l\,kh),$$

with $d_{-l}=d_l$ (no dispersion), $0\le\chi_f\le1$ the strength, $2N_p+1$
the stencil and $D_k$ the damping function ($u^{\mathrm f}$, $\chi_f$,
$d_l$, $N_p$, $D_k$ page-local; the source writes $\Delta x$ for $h$).
The constraints $d_0+2\sum d_l=0$ and $d_0+2\sum(-1)^ld_l=1$ give
$D_k(0)=0$ and $D_k(\pi)=1$, so the mean is left untouched and the
grid-to-grid mode is the most damped *(compiler check, not in the
sources)*; two further moment constraints give formal sixth order. The new 11-point filter
RFo11p minimizes $\int D_k^2\,d(kh)$ over $0.2\le kh\le1.3$ under
$D_k>0$ (purely dissipative), with a penalty on the slope of $D_k$
($d_0=0.22107796514583924$, $d_1=-0.19150151148699646$,
$d_2=0.12311347506118175$, $d_3=-0.05624682921948344$,
$d_4=0.0163475525925704$, $d_5=-0.002251669520191884$). By Fourier
analysis it is more accurate than the optimized filter of Bogey & Bailly
(2004, as recalled) at low wavenumbers and than that of Bogey et al.
(2009, as recalled) at high wavenumbers; the 2004 filter, of lower formal
order, is "more dissipative for long waves", which shows as early
kinetic-energy loss (App. 1, Fig. 20; §4). The strength is fixed at
$\chi_f=0.1$; the author notes that the damping depends on the filtering
frequency, hence on the time step (citing Edoh et al.; Lamballais et al.),
and recalls from Aubard et al. (2013) that the solution becomes
independent of the finite-difference stencil beyond seven points while
the filter shape strongly affects the LES (§2.2.2, §5).

## Results

**Relaxation filtering against split forms and subgrid models.** Volpiani
(2024, §4–5) runs the compressible
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($M=0.085$):

- **Inviscid, $64^3$, $t=5$** (Table 1). The normalized kinetic energy
  retained grows with the filter order: 0.176, 0.903, 0.963, 0.978, 0.983
  for $N_p=1,\dots,5$; 0.978, 0.985 and 0.986 for the 2004, 2009 and new
  optimized 11-point schemes; 0.998–0.999 for the
  [kinetic-energy-preserving split forms](/properties/kinetic-energy-preservation.md)
  without filter. Relaxation filtering is the cheapest per iteration
  (78.9 s per 100 iterations per processor for RF-5, against 115.9–298.9 s
  for the split forms).
- **Viscous, $Re=1600$, $64^3$–$512^3$.** Filtering with no subgrid model
  (an [implicit LES](/definitions/implicit-les.md) in the author's
  vocabulary) predicts the kinetic-energy dissipation rate $-d\mathcal K/dt$ ($\mathcal K$ the volume-averaged kinetic energy, page-local) well
  on all grids while under-predicting the enstrophy-based rate on coarse
  grids, which the author reads as under-resolved structures whose energy
  drain is carried by the filter (§5, Figs. 6–8); the new filter is the
  least dissipative and best predicts the dissipation peak on $64^3$
  (Fig. 9), and on $128^3$ it agrees with DNS of Dairay et al. (as
  recalled) at $Re=2500$, 5000 and 10000 (Fig. 10).
- **Against explicit LES.** Split forms with the
  [Smagorinsky](/methods/smagorinsky-model.md), multiscale Smagorinsky or
  [dynamic](/methods/dynamic-procedure.md) models stay noisy; adding the
  filter to them improves the results, and "regardless of the model, the
  best result is achieved for the implicit LES with RF with the optimized
  filter and no SGS model" (§5, Figs. 15–17).
- **Split form plus filter.** Combining a split form with the filter lets
  $\chi_f$ drop from 0.1 to 0.01 (the divergence form is unstable at 0.01)
  and removes the energy pile-up on $64^3$ for wavenumbers below about
  two thirds of the maximum; the best $\chi_f$ "might be case dependent"
  (§5, Fig. 18).

**Self-tuning modal filter in DGSEM.** Ranjbar et al. (2026, §III) run
[HORSES3D](/software/horses3d.md) on under-resolved meshes and compare the
unmodelled run, the earlier DEMF with user-chosen numbers of removed groups,
the [Smagorinsky model](/methods/smagorinsky-model.md) and the self-tuning
filter:

- **decaying [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)**
  (initial field of Blaisdell et al., $Re_c=450$ in the source's reference
  units; DNS $12^3$ elements with $N=8$; coarse $6^3$ elements with $N=7$):
  the unmodelled run over-predicts the kinetic energy, Smagorinsky with
  $C_s=0.12$ over-dissipates for $t>2.4$, the two DEMF settings bracket the
  DNS, and the self-tuning filter with $c_{\mathrm{st}}=0.65$ agrees best;
  the element-averaged strain and rotation invariants of the filtered run
  come "very close" to DNS (§III.A, Figs. 3, 6);
- **[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)** at $Re=200$
  ($11^3$ elements, $N=4$) and $Re=800$ ($7^3$, $N=10$), DNS resolutions
  after Fehn et al.: with $c_{\mathrm{st}}=0.25$ at both orders the
  self-tuning filter is closest to the DNS dissipation rate, slightly low
  in $t\in[8,12]$; Smagorinsky adds viscosity in the laminar phase and is
  called "not a suitable option"; the same $c_{\mathrm{st}}$ serves both
  polynomial degrees, whereas DEMF needs more removed groups at the higher
  degree (§III.B, Figs. 13–14);
- **compressible [channel flow](/benchmarks/turbulent-channel-flow.md)** at
  $Re_\tau=395$, Mach 0.3 ($14\times12\times16$ elements, $N=6$): the
  unmodelled run over-predicts all rms velocities and has non-zero wall
  fluctuations from the weak wall condition; filtering drives the wall
  values to zero, and $c_{\mathrm{st}}=0.5$ gives the closest agreement
  with Moser et al.'s DNS; Smagorinsky crashes for $C_s<0.15$ and is
  inaccurate at $C_s=0.2$, results not shown (§III.C, Fig. 15).

The optimal $c_{\mathrm{st}}$ lies in $[0.2,0.7]$; a 10–20% change of it
changes the kinetic-energy history by a relative rms measure of 0.042–0.105
in isotropic turbulence and the channel rms velocities by 0.114–0.151
(§III.D.2, Eq. 51, Fig. 17). The cost overhead is 1–2.5% of the wall time
(§III.D.3). As the flow becomes laminar the energy fraction above the
cutoff becomes negligible, so the filter switches itself off, unlike
Smagorinsky (§III.D.4, Fig. 18). The mean cutoff rises as isotropic
turbulence decays (3.82, 4.90 and 5.92 at $t=2$, 4 and 6) and spreads
widely in the inhomogeneous Taylor–Green flow (§III.A–B, Figs. 5, 12). The
authors attribute the lower optimal cutoffs of the self-tuning filter,
compared with DEMF, to its kernel attenuating rather than removing the
modes above the cutoff (§III.A).

**Local modal filter in flux reconstruction.** In Wang's
[flux-reconstruction](/methods/flux-reconstruction.md) implicit LES (2024,
§4) the filter adds no visible dissipation to the Taylor–Green vortex at
$Re=1600$ and 5000 ($64^3$ elements, $N=3$) at a 5.5% overhead, and leaves
the isentropic Mach number of the T106C cascade unchanged. On the LS89 vane
the heat-transfer coefficient depends more on the threshold than on the
Riemann solver. The positivity-preserving entropy filter of Dzanic &
Witherden (cited) stabilizes the same case without tuning but damps the
high-frequency pressure spectrum more and costs about 15% more per
iteration (§4.3.2, §4.4.3, Figs. 15–17).

## Relation to implicit LES and to SVV

Ranjbar et al. (§I) present solution filtering as simpler than SVV, whose
extra flux "alters the structure of the governing equations" and needs its
own stability and dispersion–dissipation analysis (citing Manzanero et al.;
Moura et al.). Wang (2024, §2.3, §5) notes that solution filtering adds
local dissipation to the [numerical dissipation](/properties/numerical-dissipation.md)
on which implicit LES relies, may cause time inconsistency (citing Edoh et
al.), and recalls Lamballais et al.'s link between solution filtering and
SVV in finite differences. Caban et al. (2026) classify their regularized
runs without a subgrid model as implicit LES (§5). The relaxation filter of
[Nek5000](/software/nek5000.md), used as an implicit subgrid model by Mukha
et al. (2025), is on the
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
page. In each source the filter is tuned against DNS of the same flow
(the constant $c_{\mathrm{st}}$, the threshold $s_0$, the filter order).

## Qualifications

- Ranjbar et al. (2026) re-tune $c_{\mathrm{st}}$ per flow (0.65, 0.25,
  0.5), so the self-tuning removes the integer choice of DEMF but not the
  dependence on the case; the Smagorinsky comparisons use one fixed $C_s$
  per case, with no dynamic procedure or wall damping in the channel.
- Ranjbar et al. call the kernel decay above the cutoff "exponentially
  reducing" (§II.B), while Eq. (31) is a hyperbolic tangent of a quadratic;
  they once describe modal filtering as removing energy "from the large
  resolved scales" (§I), where the rest of the paper means the smallest
  resolved scales; and §III.D.1 associates "more positive $Q_S$" with
  high-index levels, where p. 13 and the preceding sentence associate large
  negative $Q_S$ with them.
- Wang (2024, §2.3) defines the filter strength as $-\log_{10}$ of machine
  precision, $\approx36$ in double precision; $-\ln(2.2\times10^{-16})\approx36.0$,
  whereas $-\log_{10}(2.2\times10^{-16})\approx15.7$, so the value 36 is the
  natural logarithm *(compiler check, not in the sources)*.
- Volpiani (2024) labels the relaxation-filtered runs both implicit LES
  (no subgrid model) and LES "explicitly filtered with a well-defined
  filter function" (§1, §5): the filter is a grid stencil applied to the
  solution every step, whereas the explicitly filtered LES of Valencia et
  al. (2026) on [large-eddy simulation](/definitions/large-eddy-simulation.md)
  sets a filter width $\Delta$ by the filter-to-grid ratio. The value of
  $C_s$ in Volpiani's Smagorinsky runs and the balancing constants of the
  time-integrator optimization are not printed; the Fig. 18 caption
  writes "RT" for RF.
- Caban et al. (2026) print the middle rows of the filter-coefficient
  system (Eq. 16) with an index $j$ where the summation index is $l$.

# Citations

- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §I; §II.B, Eqs. (17)–(44), Figs. 1–2; §III.A, Figs. 3, 5–6; §III.B, Figs. 8–10, 12–14; §III.C, Figs. 15–16; §III.D.1–4, Eq. (51), Figs. 17–18.
- [Wang (2024)](/sources/wang-2024-b.md) — §2.3, Eqs. (17)–(19), Algorithm 1, Table 2; §4.1–4.4, Figs. 2–3, 15–21; §5.
- [Caban et al. (2026)](/sources/caban-2026.md) — §3.1, Eqs. (13)–(17), Table 1, Fig. 2; §5.1, Figs. 10–11; §5.3.1, Table 4, Fig. 19; §5.
- [Volpiani (2024)](/sources/volpiani-2024.md) — §1; §2.2.2, Eqs. (7)–(8), Table 3; §4, Table 1; §5, Figs. 6–10, 15–18; §6; App. 1, Fig. 20.
