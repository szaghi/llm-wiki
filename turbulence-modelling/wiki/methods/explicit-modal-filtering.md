---
type: Method
title: "Explicit modal filtering as an LES closure"
description: "Explicit filtering, in the modal space of a high-order element or by compact and differential physical-space filters, damps the highest resolved modes in place of a subgrid stress. The sources gate it by sensors or an entropy bound, tie its cutoff to local flow characteristics, normalize it by the time step, and compare it with Smagorinsky and implicit LES."
status: established
aliases: [explicit modal filter, modal filtering, solution filtering, dynamic explicit modal filter, DEMF, self-tuning dynamic explicit modal filter, STDEMF, local modal filter, LMF, explicit filtering regularization, relaxation filtering, explicit differential filter, Najafi-Yazdi filter, entropy-adaptive filter, improved adaptive filter]
tags: [les, filtering, implicit-les, dg, numerical-dissipation, sgs-model]
timestamp: 2026-10-29T07:40:00Z
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
it, with $\alpha_f=36$ (printed as $-\log_{10}$ of the machine zero; see Qualifications) and
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

$$X_S=1-\exp\Big(\frac{-\lvert\{Q_S\}_e\rvert}{\langle\lvert\{Q_S\}_e\rvert\rangle_u+\kappa_{\mathrm r}}\Big),\qquad X_\Omega=1-\exp\Big(\frac{-\{Q_\Omega\}_e}{\langle\{Q_\Omega\}_e\rangle_u+\kappa_{\mathrm r}}\Big),$$

with $Q_S=\tfrac12[(\mathrm{tr}\,S)^2-\mathrm{tr}(S^2)]$ and
$Q_\Omega=-\tfrac12\mathrm{tr}(\Omega^2)$ the second invariants of the
strain- and rotation-rate tensors (after Tlales et al., cited),
$\{\cdot\}_e$ their nodal average over the element, $\langle\cdot\rangle_u$
an average over the unresolved elements (over all of them in a periodic
box, over homogeneous planes or time in a channel; not the registry's
Reynolds average), $\kappa_{\mathrm r}$ a small
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

**Wall cells of wall-modelled LES only.** [Okano & Haga (2026)](/sources/okano-2026.md)
(§1, §3, §5.1–5.2) describe the stabilization of
[wall-modelled LES](/methods/wall-modelled-les.md) in
[flux reconstruction](/methods/flux-reconstruction.md) proposed by
Fukushima & Haga (as cited): an auxiliary boundary condition for the
gradients plus a modal filter (of Hamedi & Vermeire, as cited) applied
only to the wall-adjacent cells and only in the wall-normal direction,
where the coarse cells below the matching height make the polynomials
oscillate. In a compressible channel at bulk Mach 0.8 this filter and
their near-wall artificial viscosity give the same $Re_\tau$ (1676 against
1677) and skin friction at a wall-to-recovery temperature ratio of 0.81,
but the filtered runs blow up at 0.2 and 0.1, and with their numerics for
any wall colder than 0.4 (at 0.1 within 500 steps at $N=3$). The
replacement is an
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
confined to the same cells (Table 3, Figs. 2–4, 10).

## A filter strength independent of the time step

[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) use the same
Vandermonde form, $\mathcal F=\mathcal V\Lambda\mathcal V^{-1}$, in a
[flux-reconstruction](/methods/flux-reconstruction.md) scheme that recovers
collocated nodal DG (Radau correction functions, Rusanov interface flux,
BR2 viscous fluxes), with the exponential kernel

$$\Lambda_{mm}=\begin{cases}1,&\vartheta^{\mathrm t}_m\le\vartheta^{\mathrm t}_c,\\ \exp\!\Big[-\alpha_f\Big(\dfrac{\vartheta^{\mathrm t}_m-\vartheta^{\mathrm t}_c}{\vartheta^{\mathrm t}_{\max}-\vartheta^{\mathrm t}_c}\Big)^{s_f}\Big],&\vartheta^{\mathrm t}_c<\vartheta^{\mathrm t}_m\le\vartheta^{\mathrm t}_{\max},\end{cases}$$

where $\vartheta^{\mathrm t}_m$ is the total degree of the orthonormal mode
$m$ (the sum of the exponents of its highest monomial, from Pascal's
triangle in several layers), $\vartheta^{\mathrm t}_c$ the cut-off degree and
$\vartheta^{\mathrm t}_{\max}$ the largest total degree (§3.3, Eqs. 31–32;
the source's $\eta$, $\eta_c$, $\eta_{\max}$, $\alpha$, $s$). These degrees
are integers, not normalized: $\vartheta^{\mathrm t}_m$ (page-local) is
distinct from the normalized index $\vartheta_m\in[0,1]$ of Wang (2024)
above. The paper does not print $\vartheta^{\mathrm t}_{\max}$ as a function
of $N$.

**Normalization by the time step.** Applying a fixed filter after every
step makes its cumulative effect over a fixed time depend on $\Delta t$.
The authors' first contribution (§3.2, Eqs. 28–30) applies after each step
$\Lambda^*=\Lambda^{1/n_T}$ with $n_T=T_{\mathrm{char}}/\Delta t$ (page-local),
so that $n_T$ applications are "analogous to applying $F$ after each
characteristic time … only once" and the observed strength does not depend
on $\Delta t$; the authors restrict this to time integrators of
sufficiently high order run away from their stability limit, where the
spatial operator governs the behaviour (§3.2). With the kernel above,
$\Lambda^{1/n_T}$ has the damping exponent $\alpha_f/n_T$ per step
*(compiler check, not in the sources)*; the $\alpha_f$ of the tables below
are of order $10^5$–$10^{14}$, against $\alpha_f=36$ applied per stage,
without such a normalization, by Wang (2024).

**Optimized parameters.** Their second contribution (§3.4, Algorithms 1–4)
searches, over more than 14 000 runs of the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on a deliberately
coarse $16^3$-degree-of-freedom mesh at $N=3$, 4, 5, $s_f\in\{2,4,8,16\}$
and $M=0.1$–0.5, for the weakest filter that keeps pressure and density
physical up to $20\,T_{\mathrm{char}}$ (bisection on $\alpha_f$ for the
highest stable $\vartheta^{\mathrm t}_c$), and among stable filters picks the one that
damps the high modes most while leaving the low ones untouched. The
optimum always has $s_f=16$ (Tables 4–6):

| $N$ | $\vartheta^{\mathrm t}_c$ | $\alpha_f$ range over the five "strengths" |
|---|---|---|
| 3 | 5 | $2.2\times10^{5}$ to $1.5\times10^{9}$ |
| 4 | 7 ($M=0.1$–0.4), 6 ($M=0.5$) | $2.9\times10^{11}$ to $1.6\times10^{13}$ |
| 5 | 8 ($M=0.1$, 0.2), 6 ($M=0.3$–0.5) | $1.9\times10^{10}$ to $1.9\times10^{14}$ |

A filter optimized at Mach number $M$ is labelled a "strength"; the
$M=0.5$ one is the strongest and is used for the wall-bounded cases. The
authors say the optimum splits the spectrum "in general" at about 2/3,
tending to 1/2 as $N$ grows, "similar to the 2/3 rule of dealiasing"
(§3.4). The filters are
optimized for the DG-recovering correction function and the Rusanov flux,
and the authors say they "would not be generally suitable for other
correction functions" (§2.1, §3.4).

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

($\hat G_{QG}$ page-local, $N_{\mathrm{AD}}$ registry §11), built from the eighth-order
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
the stencil and $D_k$ the damping function ($\chi_f$ registry §11;
$u^{\mathrm f}$, $d_l$, $N_p$, $D_k$ page-local; the source writes $\Delta x$ for $h$).
The constraints $d_0+2\sum d_l=0$ and $d_0+2\sum(-1)^ld_l=1$ give
$D_k(0)=0$ and $D_k(\pi)=1$, so the mean is left untouched and the
grid-to-grid mode is the most damped *(compiler check, not in the
sources)*; two further moment constraints give formal sixth order. The new 11-point filter
RFo11p minimizes $\int D_k^2\,d(kh)$ over $0.2\le kh\le1.3$ under
$D_k>0$ (purely dissipative), with a penalty on the slope of $D_k$
($d_0=0.22107796514583924$, $d_1=-0.19150151148699646$,
$d_2=0.12311347506118175$, $d_3=-0.05624682921948344$,
$d_4=0.0163475525925704$, $d_5=-0.002251669520191884$). By Fourier
analysis it is more accurate than the optimized filters that Volpiani
cites from Bogey & Bailly (2004) at low wavenumbers and from Bogey et al.
(2009) at high wavenumbers; the 2004 filter, of lower formal
order, is "more dissipative for long waves", which shows as early
kinetic-energy loss (App. 1, Fig. 20; §4). The strength is fixed at
$\chi_f=0.1$; the author notes that the damping depends on the filtering
frequency, hence on the time step (citing Edoh et al.; Lamballais et al.),
and cites Aubard et al. (2013) for the finding that the solution becomes
independent of the finite-difference stencil beyond seven points while
the filter shape strongly affects the LES (§2.2.2, §5).

**Compact filter with an adaptive shock reduction in DNS.**
[Kang & Lee (2024)](/sources/kang-2024.md) (§II.B, Eq. 9) stabilize the
sixth-order compact-difference DNS of a Mach 2.9, $24^\circ$
compression-ramp interaction with the Gaitonde–Visbal compact low-pass
filter (cited), applied to the solution vector at every final Runge–Kutta
stage. In the notation of the Caban et al. form above it has $M_s=1$,
$a_1$ the free parameter (the source's $\alpha_f$) and $N_s$ the half
stencil, with the eighth-order ($N_s=4$) coefficients

$$b_0=\tfrac{93+70a_1}{128},\quad b_1=\tfrac{7+18a_1}{16},\quad b_2=\tfrac{-7+14a_1}{32},\quad b_3=\tfrac{1-2a_1}{16},\quad b_4=\tfrac{-1+2a_1}{128},$$

$-0.5<a_1\le0.5$, with less damping as $a_1\to0.5$; the DNS uses
$a_1=0.47$. These coefficients give $\sum_lb_l=1+2a_1$ and
$\sum_l(-1)^lb_l=0$, i.e. $\hat G_E(0)=1$ and $\hat G_E(\pi)=0$
*(compiler check, not in the sources)*. Where a modified Ducros-type
sensor detects a shock (formula and threshold not printed; see
[shock sensors](/definitions/shock-sensor.md)), the filter drops to second
order ($N_s=1$) with $a_1=0.49$, after Visbal & Gaitonde (cited); a
localized artificial diffusivity of viscosity and conductivity handles the
remaining large gradients (see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).
The filter here stabilizes a DNS on $2865\times298\times420$ points
($\Delta x^+=4.6$).

## Differential filters on unstructured grids

[Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) filter in
physical space by solving an elliptic equation, so that the filter is
implicit in space and works on any element shape. They cite Germano's
differential filter (§3, Eq. 7),
$\bar\phi-\delta_{\mathrm G}^2\,\partial_i\partial_i\bar\phi=\phi$, with
transfer function $\hat G(k)=1/(1+\delta_{\mathrm G}^2k^2)$ (Eq. 11;
$\delta_{\mathrm G}$ the filter radius, page-local): it attenuates every
wavenumber but never removes one completely, and the single parameter
$\delta_{\mathrm G}$ fixes roll-off, cut-off and attenuation at the grid
cut-off together. Their filter, an extension of the one-dimensional
Najafi-Yazdi filter (cited) to two- and three-dimensional unstructured
grids, adds a second-derivative term on the right-hand side, written in
each element's reference coordinates $\xi_i$ (§3.1, Eqs. 9–10),

$$\bar\phi+\frac{\partial}{\partial\xi_i}\Big(a_{\mathrm D}\frac{\partial\bar\phi}{\partial\xi_i}\Big)=\phi+\frac{\partial}{\partial\xi_i}\Big(b_{\mathrm D}\frac{\partial\phi}{\partial\xi_i}\Big),\qquad \hat G(k)=\frac{1-b_{\mathrm D}k^2}{1-a_{\mathrm D}k^2}\ \text{(continuous, constant coefficients)},$$

with $a_{\mathrm D}$, $b_{\mathrm D}$ (page-local; the source's $\alpha$,
$\beta$) interpolated from nodal values $a_{\mathrm D,k}$,
$b_{\mathrm D,k}$. The right-hand coefficient is chosen for complete
attenuation at the grid cut-off ("unconditional numerical stability as
well as strong anti-aliasing"), the left-hand one sets the shape and the
cut-off wavenumber. The value of $b_{\mathrm D}$ that gives
$\hat G(\pi/h)=0$ depends on the discretization: $1/\pi^2$ for the
continuous filter, $1/4$ for a second-order central difference, whose
transfer function is
$[1-2b_{\mathrm D}(1-\cos kh)]/[1-2a_{\mathrm D}(1-\cos kh)]$, and $1/12$
for a finite-element form (§3.1, Eq. 13). The parameters must therefore
be fixed after discretization.

**Design on an unstructured stencil.** A Galerkin discretization gives the
sparse system $\mathbf M\bar\Phi=\mathbf N\Phi$ for the nodal values
(§3.2, Eqs. 27–29; $\mathbf M$, $\mathbf N$ page-local). For design the
authors define a "generalized" Z-transform on the local stencil of a node,
with exponents equal to coordinate differences normalized by the minimum
spacing in each direction (App. A, Eq. A.8), and impose element by element
(§4.1–4.6):

- conservation of constants, transfer function equal to one at zero
  wavenumber (Eqs. 32–34);
- complete attenuation of the grid-to-grid wave along every element edge,
  which fixes the nodal $b_{\mathrm D,k}$: $(1,-\tfrac23,2,-\tfrac23)$ on
  the bilinear quadrilateral, "exactly the same values as were obtained for
  structured grids" (App. B.1, Eq. B.18); $(1,-\tfrac79,\tfrac43,-\tfrac79,-\tfrac79,\tfrac43,\tfrac{14}9,\tfrac43)$
  on the bilinear hexahedron (Eqs. B.45–B.46); $1/12$ on the linear
  triangle and $3/40$ on the linear tetrahedron (Eqs. B.26–B.27, B.55–B.56).
  On linear triangles and tetrahedra complete attenuation holds along the
  reference axes or along their diagonal, not both, while bilinear and
  higher elements attenuate completely in all directions (App. B.2);
- a sufficient element-wise stability condition $|\hat G|\le1$, written
  as a non-negative stability index (Eqs. 41–42), which bounds the ratios
  $a_{\mathrm D,k}/b_{\mathrm D,k}$ (Table 1): for the quadrilateral
  $a_{\mathrm D,2}/b_{\mathrm D,2}>1$ and
  $a_{\mathrm D,3}/b_{\mathrm D,3}<a_{\mathrm D,2}/b_{\mathrm D,2}$
  (Eq. 46), for triangles and tetrahedra $a_{\mathrm D,1}/b_{\mathrm D,1}=1$
  and the other ratios below one. Being only
  sufficient, it can be more dissipative than necessary (§4.5);
- a cut-off wavenumber, where $|\hat G|=1/2$ on the assembled (not the
  element-wise) transfer function; it varies from node to node and is set
  in practice by choosing the ratios (§4.6, Eqs. 47–48). On a Cartesian
  quadrilateral grid, ratios 1.2 and 1.05 give a cut-off of at least
  $3\pi/4$ and $|\hat G|\ge0.9$ for $kh\le\pi/2$; for aeroacoustics a
  cut-off of at least $\pi/2$ is called customary and $3\pi/4$ ideal.

Positivity is reduced to a phase condition that the authors leave open
("further investigations are needed", §4.2); Galilean invariance and
orientation independence are argued, "No mathematical proof will be
attempted here" (§4.3, §4.7). Any differential filter discretized on a
non-uniform or unstructured grid loses commutation with differentiation,
because its width varies in space (§3.1, Eq. 18). Repeated application
equals one application with a larger radius, though not necessarily
within the same filter family (§4.8). The filter is the basis of a van
Cittert [approximate deconvolution model](/methods/scale-similarity-model.md)
with no eddy viscosity on a continuous-Galerkin finite-element solver; the
LES results are on that page. In decaying isotropic turbulence the
hexahedral filter (ratios 1, 1.2, 1.1, 1.05) gives a cut-off of about
$3\pi/4$ relative to the local spacing, and on tetrahedra the filter
follows the smaller local element size (§6.1, Fig. 6); for the
Taylor–Green LES the ratios (1.1, 1.05, 1.025) are said to give about
$\pi/2$ on hexahedra, and a tetrahedral ratio of 0.95 about $3\pi/5$ (§6.2; see
Qualifications).

## Entropy-bounded adaptive filter confined to shocks

[Gao et al. (2023)](/sources/gao-2023.md) (§3.1.3, Eqs. 40–48) use the
Vandermonde form $\mathcal F=\mathcal V\Lambda\mathcal V^{-1}$ with the
exponential kernel $\exp(-\alpha_f\vartheta_m^{s_f})$, $\vartheta_m=i/N$
for mode $i$, with $s_f=2$ and only the strength $\alpha_f$ varied, as in
the adaptive filter of Dzanic & Witherden (cited). That filter chooses
$\alpha_f$ in each element so that density and pressure stay above
minima and a minimum-entropy condition holds,
$s_{\mathrm{ent}}(\boldsymbol U^{n+1})\ge\min_{\Omega_e}s_{\mathrm{ent}}(\boldsymbol U^n)-\epsilon_{\mathrm{ent}}$,
with $s_{\mathrm{ent}}=\rho\ln(p\rho^{-\gamma})$, $\Omega_e$ the element
and its direct neighbours and $\epsilon_{\mathrm{ent}}$ a tolerance (all
page-local; the source's $s$, $\epsilon_s$); Gao et al. state that
Dzanic & Witherden split the hyperbolic and parabolic operators and
suggest one tolerance, $10^{-4}$, for the whole field. Gao et al.'s
change, used in the split-form DGSEM of [FLEXI](/software/flexi.md), is
to apply the filter only in elements flagged by a
[shock sensor](/definitions/shock-sensor.md) (Jameson, Persson–Peraire
or a modified Ducros indicator, per case). The authors' arguments
(§3.1.3): one tolerance can over-dissipate complex flows, especially at
high $N$ or on coarse meshes; the confinement leaves the smooth and
under-resolved turbulent regions to the
[implicit LES](/definitions/implicit-les.md) of the split form, makes
$\epsilon_{\mathrm{ent}}$ a single knob between shock sharpness (larger)
and post-shock oscillation (smaller), and removes the operator splitting.
They also report that the unconfined filter on a standard DG scheme was
"found to be unreliable" against aliasing in under-resolved turbulence,
because it aims at minimal dissipation where the cut-off eddies need
some (results not shown). With the same tolerance, the confined filter
adds "much less dissipation in smooth flow areas" than the original on a
shock–panel test (§4.2, Schlieren of Figs. 14 and 16), and it captures
the shock of the elastic-panel
[shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
at $N=6$ (§5). Compare the unconfined use of the same Dzanic–Witherden
filter by Wang (2024) in the results below, and the subcell alternative
on the [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
page.

**The filter options of a flux-reconstruction code.** The software paper
of [PyFR](/software/pyfr.md), [Witherden et al. (2025)](/sources/witherden-2025.md),
§3.2, lists four stabilizations for the under-resolved runs that the
authors identify with implicit LES ("uDNS, also referred to as ILES"),
where flux reconstruction suffers aliasing-driven instabilities (as
cited): periodic modal filtering, described as conservative and
inexpensive but indiscriminate, with free parameters (strength,
frequency, cut-off modes); anti-aliasing by a quadrature-based
least-squares projection of the flux, stated (citing an earlier
comparison) to give results "markedly superior" to modal filtering at
about twice the run time in three dimensions with a projection degree one
above the solution; Persson–Peraire-type
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md);
and the positivity-preserving entropy filter of Dzanic & Witherden. In
PyFR the entropy filter is applied only to elements that violate positive
density, positive pressure or a minimum-entropy bound, the bound being the
minimum discrete entropy of the element and its Voronoi neighbours at the
previous step; it "does not explicitly require any problem-dependent
parameterisation", apart from a fixed small tolerance that is not varied
between problems. On the supersonic Taylor–Green vortex (Mach 1.25,
$Re=1600$, $16^3$–$128^3$ hexahedra, $N=3$) its enstrophy is "in
excellent agreement" with the $2048^3$ TENO reference, and its
dilatational dissipation is closer to that reference than the
artificial-viscosity and subcell solvers at equal resolution (§5.1,
Figs. 11–12; see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
and the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)).

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
  (Fig. 9), and on $128^3$ it agrees with the DNS of Dairay et al. (2017,
  cited) at $Re=2500$, 5000 and 10000 (Fig. 10).
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

**Optimized filter in flux reconstruction.** Hamedi & Vermeire (2022,
§4–5) report that the filters leave accuracy largely intact:

- **Isentropic vortex.** Filtered and unfiltered runs are both
  super-accurate with almost the same observed order: 7.6266 against
  7.6266 at $N=3$, 9.1088 against 9.1043 at $N=4$, 10.633 against 10.427
  at $N=5$ (§4.1, Table 1).
- **Taylor–Green vortex, $Re=1600$, $64^3$ degrees of freedom.** The
  filtered runs dissipate kinetic energy slightly faster, more so for
  stronger filters, under-predict the enstrophy-based dissipation and the
  high-wavenumber energy, and show larger vortical structures; "the overall
  accuracy … is not impacted significantly" (§4.2, Figs. 9–13). The same
  holds on a sinusoidally curved mesh (§4.3).
- **Channel, $Re_\tau=395$**, 3/8 of the DNS degrees of freedom
  ($\Delta x^+\approx25$, $\Delta y^+_{\min}\approx0.9$,
  $\Delta z^+\approx17$): the unfiltered $N=5$ run is unstable and the
  filtered one stable; filtering damps only the highest modes of the
  velocity spectra, and at $N=3$ it improves the r.m.s. fluctuations for
  $10<y^+<40$ (§5.1, Table 2, Figs. 19–25); see
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md).
- **Stalled NACA0020, $Re_c=20\,000$, $20^\circ$.** $C_L=0.651$ and
  $C_D=0.357$ filtered against 0.639 and 0.353 unfiltered and 0.64 and 0.35
  in DNS; nearly identical $C_p$ (§5.2, Table 3).

They (§1) cite Park et al. as having concluded that
filtering degrades the accuracy of high-order implicit LES of a NACA0021,
and present their filters as designed to "stabilize the solution, while
maintaining accuracy" (§1, §6).

## Filters as shock capturing in discontinuous schemes (review)

[Lv & Ekaterinaris (2023)](/sources/lv-2023.md) (§4.2) review
stabilization of high-order discontinuous schemes for multiphase and
reacting flows. They state that the subcell-resolution approach of
Panourgias & Ekaterinaris (cited) is equivalent to a high-order
dissipative (nonlinear) filter, developed for centred finite differences
and "superior" for shock capturing, and use such a nonlinear filter instead
of limiters for the bow shock of a Mach 8 reacting capsule flow in modal
DG (§6.2, no reference data). Because limiting remains "too intrusive for
high-order solutions" even with a good sensor, artificial-viscosity
formulations or filtered forms such as the entropy-stable
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) of
Mateo-Gabín et al. (cited) "have therefore become more popular" for LES
with discontinuous schemes (§4.2). See also
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).

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
page. [Kumar et al. (2025)](/sources/kumar-2025.md), App. A.3–A.4,
Eqs. (A5)–(A12), print that high-pass-filter (HPF) relaxation model of
Nek5000 (Stolz et al., Schlatter et al., Fischer & Mullen, cited): a
Legendre low-pass filter $\mathcal F_N u=\sum_{k=0}^N\hat G_k\tilde u_kP_k$
($\tilde u_k$ the Legendre coefficients, $P_k$ the Legendre polynomials,
$\hat G_k$ the filter weights, page-local; the source's $\sigma_k$) with $\hat G_k=1$ for $k\le N-m$ and
$\hat G_k=\big((m-i)/m\big)^2$ for $k=N-m+i$, $i=1,\dots,m$, applied as a
tensor product in three dimensions; the high-pass part
$\mathcal H_N*u=u-\mathcal F_Nu$ enters the momentum equation as the
relaxation term $-\chi_f\,\mathcal H_N*u_i$, element by element, with
$\chi_f=5$ ($\chi_f=10$ does not change the results significantly). For
$N=8$, $m=3$ the printed weights give $\hat G_6=(2/3)^2$, $\hat G_7=(1/3)^2$,
$\hat G_8=0$ *(compiler check, not in the sources)*. The paper does not state that the term is active in its
own RANS and detached-eddy runs (see Qualifications).

## Modal filters as sensors, not as closures

In the ADDA algorithm of [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md),
§4.1, Eqs. (29)–(36), Table 1, modal filters are not applied to the
solution: the unlimited central-stencil polynomial of a CWENOZ
finite-volume reconstruction, written in a zero-mean Taylor basis, is
filtered weakly and strongly, and the energy ratio
$$E_{\mathrm R}=\frac{\int_{V_i}\big((\rho\boldsymbol u)_{\mathrm R}-(\rho\boldsymbol u)_{\mathrm W}\big)^2dV}{\int_{V_i}\big((\rho\boldsymbol u)_{\mathrm R}-(\rho\boldsymbol u)_{\mathrm S}\big)^2dV}$$
of the unfiltered (R), weakly (W) and strongly (S) filtered momentum
decides whether the cell needs more ($E_{\mathrm R}>1.2$) or less ($E_{\mathrm R}<0.95$)
dissipation ($E_{\mathrm R}$ page-local; after Domaradzki and co-workers and
Fernandez-Fidalgo et al., cited). Of seven candidate kernels, six
exponential ones $\hat G(\vartheta^{\mathrm t}_m)=\exp\{-\alpha_f[(\vartheta^{\mathrm t}_m-\vartheta^{\mathrm t}_c)/(\vartheta^{\mathrm t}_{\max}-\vartheta^{\mathrm t}_c)]^{s_f}\}$
on the total Taylor degree $\vartheta^{\mathrm t}_m$ of a mode (strength
$\alpha_f$, order $s_f$, cut-off $\vartheta^{\mathrm t}_c$ and maximum
$\vartheta^{\mathrm t}_{\max}$, registry §11) and a sharp cut-off that
drops the top-degree terms (order $r$ for the weak and also $r-1$ for the
strong filter, $r$ the reconstruction degree), only the sharp filter and
the exponential filter 7 ($\alpha_f=32/8$, $s_f=8/8$, strong/weak)
give a useful signal on the inviscid Taylor–Green vortex with CWENOZ4 on
$64^3$; filter 4 varies "very close to machine precision" and the others
stay flat (Fig. 5). The sharp filter is retained. The dissipation it
controls is on [numerical dissipation](/properties/numerical-dissipation.md).

## Qualifications

- **Printed forms in Kumar et al. (2025), App. A.4.** Eq. (A10) is printed
  without the relaxation term the text says is added to it, and the
  symbols $\mathcal H_N$ and $\chi$ (here $\chi_f$) of the text are absent
  from it; the
  text takes "$m=0$" while saying the filter "only affects the last
  mode", whereas with the printed $\hat G_k$ the value $m=0$ leaves every
  mode unfiltered *(compiler check, not in the sources)*.
- **Printed forms in Tsoutsanis & Nogueira (2025).** Table 1 gives the
  sharp filter as $\vartheta^{\mathrm t}_{\max}=r-2/r-1$ (strong/weak); with Eq. (31),
  which zeroes only the degree $\vartheta^{\mathrm t}_{\max}$, the weak value $r-1$
  would zero degree $r-1$, not the order-$r$ terms the text describes.

- Ranjbar et al. (2026) use a different $c_{\mathrm{st}}$ per flow (0.65,
  0.25, 0.5); the Smagorinsky comparisons use one fixed $C_s$ per case,
  with no dynamic procedure and no wall damping mentioned for the channel.
- Ranjbar et al. call the kernel decay above the cutoff "exponentially
  reducing" (§II.B), while Eq. (31) is a hyperbolic tangent of a quadratic;
  they once describe modal filtering as removing energy "from the large
  resolved scales" (§I), where the rest of the paper means the smallest
  resolved scales; and §III.D.1 associates "more positive $Q_S$" with
  high-index levels, where p. 13 and the preceding sentence associate large
  negative $Q_S$ with them.
- Wang (2024, §2.3) defines the filter strength as $-\log_{10}$ of the
  machine zero and gives $\approx36$ for double precision; the value of the
  machine zero is not printed.
- Volpiani (2024) labels the relaxation-filtered runs both implicit LES
  (no subgrid model) and LES "explicitly filtered with a well-defined
  filter function" (§1, §5). The value of
  $C_s$ in Volpiani's Smagorinsky runs and the balancing constants of the
  time-integrator optimization are not printed; the Fig. 18 caption
  writes "RT" for RF.
- Caban et al. (2026) print the middle rows of the filter-coefficient
  system (Eq. 16) with an index $j$ where the summation index is $l$.
- Hamedi & Vermeire (2022) call their unfiltered runs "ILES" and the
  filtered ones "LES" although the filter is the only model. Algorithm 1
  prints the update of the unstable branch as "$\eta_c=\eta_{max}-1$",
  which as printed sets the same value at every iteration and cannot carry
  out the downward search the text describes; the search starts at
  $\vartheta^{\mathrm t}_c=\vartheta^{\mathrm t}_{\max}$, where the middle branch of Eq. (32) has a
  zero denominator. Their Rusanov flux (Eq. 44) is printed with the sum of
  the two states, $+\tfrac s2(u_L+u_R)$, in the dissipative term. The
  airfoil run is said to last 100 convective times (§5.2) while the Fig. 28
  caption reads "after $200T_{char}$". The $\alpha_f$ of the "strength"
  labels is not monotone: at $N=3$ the $M=0.3$ filter has a smaller
  $\alpha_f$ than the $M=0.2$ one at the same $\vartheta^{\mathrm t}_c$ (Table 4).
- Najafiyazdi et al. (2023) print the Taylor–Green filter cut-off as
  about $\pi/2$ (hexahedra) and $3\pi/5$ (tetrahedra) in §6.2, and as
  "$\kappa_f\approx0.8\pi$" for all runs in the Fig. 13 caption. Of their
  three printed conditions for the quadrilateral coefficients (App. B.1),
  the stated solution $b_{\mathrm D}=(1,-\tfrac23,2,-\tfrac23)$ satisfies
  Eq. (B.16) but gives 10, not 8, in Eq. (B.17) as printed, and the
  difference of the two printed equations would force
  $b_{\mathrm D,2}=0$; Eq. (B.42) is printed without the factor $1/432$
  that its sibling coefficients carry, and with it the stated hexahedron
  values give the $1/8$ of Eq. (B.46) (bracket 54) *(compiler check, not
  in the sources)*. The positivity condition of §4.2 is printed as
  "$|\theta_n|\le-\pi/2$".
- Gao et al. (2023) print the entropy tolerance once as
  "$\epsilon_\sigma=10^{-4}$" (§5) and otherwise as $\epsilon_s$. The
  comparison of the confined and unconfined filters is a qualitative
  Schlieren comparison on one case.

# Citations

- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §I; §II.B, Eqs. (17)–(44), Figs. 1–2; §III.A, Figs. 3, 5–6; §III.B, Figs. 8–10, 12–14; §III.C, Figs. 15–16; §III.D.1–4, Eq. (51), Figs. 17–18.
- [Wang (2024)](/sources/wang-2024-b.md) — §2.3, Eqs. (17)–(19), Algorithm 1, Table 2; §4.1–4.4, Figs. 2–3, 15–21; §5.
- [Caban et al. (2026)](/sources/caban-2026.md) — §3.1, Eqs. (13)–(17), Table 1, Fig. 2; §5.1, Figs. 10–11; §5.3.1, Table 4, Fig. 19; §5.
- [Volpiani (2024)](/sources/volpiani-2024.md) — §1; §2.2.2, Eqs. (7)–(8), Table 3; §4, Table 1; §5, Figs. 6–10, 15–18; §6; App. 1, Fig. 20.
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §1; §2.1; §3.1–3.4, Eqs. (27)–(32), Algorithms 1–4, Tables 4–6; §4.1–4.3, Table 1, Figs. 9–18; §5.1–5.2, Tables 2–3, Figs. 19–30; §6.
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) — §3, Eqs. (7)–(18); §3.2, Eqs. (27)–(29); §4.1–4.8, Eqs. (31)–(48), Table 1; §6.1, Fig. 6; §6.2, Fig. 13; App. A, Eq. (A.8); App. B, Eqs. (B.15)–(B.56).
- [Gao et al. (2023)](/sources/gao-2023.md) — §3.1.3, Eqs. (40)–(48); §4.1–4.2, Figs. 14, 16; §5.
- [Kang & Lee (2024)](/sources/kang-2024.md) — §II.B, Eq. (9).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.2; §6.2.
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §3.2 (modal filtering, anti-aliasing, artificial viscosity and entropy filtering in PyFR); §5.1, Figs. 11–12 (entropy filter on the supersonic Taylor–Green vortex).
- [Kumar et al. (2025)](/sources/kumar-2025.md) — App. A.3–A.4, Eqs. (A5)–(A12) (HPF relaxation model of Nek5000, Legendre filter weights, $\chi_f=5$).
- [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md) — §4.1, Eqs. (29)–(36), Table 1, Fig. 5 (modal filters on a Taylor basis as an energy-ratio sensor).
- [Okano & Haga (2026)](/sources/okano-2026.md) — §1; §3, Figs. 2–4; §5.1–5.2, Table 3, Fig. 10 (wall-normal modal filter on wall-adjacent cells of flux-reconstruction WMLES, failing on cold walls).
