---
type: Method
title: "Spectral eddy viscosity"
description: "Kraichnan's spectral eddy viscosity expresses the energy transfer across a cutoff as a wavenumber-dependent viscosity with a low-wavenumber plateau and a cusp near the cutoff; the sources use it to diagnose explicit and implicit LES, build modal and adaptively regulated models, compute it from the LES or DNS field, close a subgrid-velocity model, and dispute the plateau."
status: established
aliases: [adaptive spectral eddy viscosity, adaptively reconstructed eddy viscosity, Kraichnan spectral eddy viscosity, Chollet–Lesieur model, plateau–cusp eddy viscosity, EDQNM eddy viscosity, RNG spectral viscosity]
tags: [les, sgs-model, eddy-viscosity, implicit-les, dg]
timestamp: 2026-10-29T07:36:00Z
---

# Spectral eddy viscosity

The **spectral eddy viscosity** $\nu_t(k\mid k_c)$ is the viscosity that,
acting on the resolved spectrum at wavenumber $k<k_c$, removes the energy
that nonlinear triads transfer to the scales beyond the cutoff $k_c$. On
this page $k$ is the wavenumber magnitude, as the registry prescribes for
spectral pages. [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§2.2) cite Kraichnan's definition from the resolved (supergrid) Lin
equation. Let
$\bar E(k)$ be the resolved spectrum, and $T_<(k)$, $T_>(k)$ the transfer
into $k$ from resolved and from subgrid interactions (page-local symbols).
With exact differentiation the resolved dissipation spectrum is
$2\nu k^2\bar E(k)$, and

$$\partial_t\bar E=T_<+T_>-2\nu k^2\bar E,\qquad
\nu_t(k\mid k_c)=-\frac{T_>(k)}{2k^2\bar E(k)},$$

so that $\partial_t\bar E=T_<-2(\nu+\nu_t)k^2\bar E$ (Vicente Cruz &
Lamballais 2023, Eqs. 16–22, with $\bar\varepsilon=2\nu k^2\bar E$
substituted in their Eq. 21). A positive $\nu_t$ means net forward transfer
at that wavenumber. Being a shell average, $\nu_t(k\mid k_c)$ measures only
the net transfer across the cutoff, not its local sign in space *(compiler
check, not in the sources)*; see [energy backscatter](/definitions/energy-backscatter.md).

## Plateau and cusp

For a cutoff inside an infinite inertial range the spectral eddy viscosity
is a constant **plateau** at low $k$ that rises to a **cusp** as
$k\to k_c$ (Kraichnan, cited by [Flad & Gassner (2017)](/sources/flad-2017.md),
§3.1, and by Vicente Cruz & Lamballais (2023), §6.4). Vicente Cruz &
Lamballais also cite Lesieur's interpretation, which assigns the plateau to
non-local triads and the cusp to local triads. The **Chollet–Lesieur model** (from
EDQNM; Flad & Gassner 2017, App. C, Eq. C.1–C.2; Vicente Cruz & Lamballais
2023, Eq. 55) fits both:

$$\nu_t(k\mid k_c)=0.267\Big[1+34.5\,e^{-3.03\,k_c/k}\Big]\sqrt{\frac{E(k_c)}{k_c}},$$

where 0.267 is the plateau value for an infinite Kolmogorov spectrum and the
exponential is an empirical fit of the cusp. Vicente Cruz & Lamballais
(§6.4) cite Métais & Lesieur, who made the plateau depend on the spectral
slope (spectral-dynamic model).
[Domaradzki (2024)](/sources/domaradzki-2024.md) (Eq. 2.25) recalls the
same Chollet fit (TFM/EDQNM, infinite $k^{-5/3}$ range) with the Kolmogorov
constant $C_K$ kept explicit,

$$\nu_t(k\mid k_c)=\Big(\frac{E(k_c)}{k_c}\Big)^{1/2}C_K^{-3/2}\Big(0.441+15.2\,e^{-3.03\,k_c/k}\Big),$$

with $C_K$ "taken usually as 1.4"; with that value the two printed forms
coincide ($0.441\cdot1.4^{-3/2}=0.266$, $15.2/0.441=34.5$, *compiler check,
not in the sources*). Domaradzki places the plateau at $k\lesssim0.4k_c$ (§1).
[Rajek & Pozorski (2026)](/sources/rajek-2026.md) (§II B, Eqs. 12–14) take
the same fit from Domaradzki, with $C_K=1.4$ chosen "to approximately match"
Métais & Lesieur, and print it as
$\nu_t(k\mid k_c)=(0.267+9.21\,e^{-3.03k_c/k})[E(k_c)/k_c]^{1/2}$, which they
call the **standard model**; they write it as a normalized viscosity
$\nu_t^+(k\mid k_c)$ (page-local) times the dimensional factor
$[E(k_c,t)/k_c]^{1/2}$, with the plateau $\nu_t^+(0\mid k_c)=0.267$ for
$k<0.4k_c$ (Eq. 12).

## A priori estimates against the model

Vicente Cruz & Lamballais (2023, §6.4, Figs. 16–19) estimate
$\nu_t(k\mid k_c)$ a priori from filtered DNS of the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=40\,000$
($5400^3$ DNS, LES cutoffs $k_c=108$, 270, 540):

- the plateau is nonzero, about 12, 2 and 0.2 times $\nu$ at the three
  cutoffs ($t=10$), and is insensitive to the filter shape;
- the subgrid dissipation carried by $k<k_c/4$ reaches 24%, 16% and 6% of
  the total dissipation;
- with a sharp cutoff the a priori curve matches Eq. (55) in plateau and
  cutoff value at $t=10$; with the super-Gaussian filter, the plateau agrees
  if the comparison uses an equivalent sharp cutoff $k_c=68$ (same captured
  energy as the super-Gaussian at 108); at $t=15$ the a priori plateau is
  more than twice lower than Eq. (55), attributed to the drop of
  $Re_\lambda$ from about 493 to 389;
- the cusp of a non-idempotent filter is more than an order of magnitude
  higher than the sharp-cutoff cusp, so "there is no reason to design SGS
  modelling to match quantitatively this specific cusp when a different
  filtering is expected".

The a posteriori spectral viscosity of an LES model is measured from the
model's own dissipation spectrum (Eqs. 27–29). For constant-coefficient
[Smagorinsky](/methods/smagorinsky-model.md) at numerical convergence it is
of the right order at low $k$ but nearly constant, and vanishes near $k_c$
where the a priori curve rises (§6.3, Fig. 11). For the implicit
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) it
reproduces the cusp but vanishes at low $k$, missing the plateau (§6.4).
From this missing plateau the authors conclude that the plateau "cannot
be ignored, making somewhat inconsistent the concept of
[implicit LES](/definitions/implicit-les.md) except when the mesh is close
to DNS" (§6.4).

## Eddy viscosity derived from the LES field

Domaradzki (2024, §2.2) recalls the author's spectral "autonomous" LES, in
which $\nu_t(k\mid k_c)$ is not modelled but computed at every step from
the LES field: the subgrid transfer across a sharp test cutoff $k_c/2$
gives, by Kraichnan's definition, a resolved eddy viscosity that is
rescaled to $k_c$ in the similarity variable $k/k_c$, its plateau taken
from the limit $k\to0$, and its total level set by the ultraviolet-flux
relation: the transfer across $k_c$ is the resolved transfer across $ak_c$
divided by $1-a^{4/3}$, a factor 1.66 for $a=1/2$ (Eqs. 2.26–2.27). The
physical-space version is the
[autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md).
Domaradzki compares three spectral viscosities (§3.3, Fig. 10): the
Chollet–Lesieur fit, an LES-derived cusp with a plateau at $p_{\mathrm{pl}}=0.37$ of the
cusp value at $k_c$ ($p_{\mathrm{pl}}$ page-local), and a $k$-independent viscosity
matched to the total transfer. The plateau–cusp LES-derived viscosity
agrees best with the inertial range up to $k_c$; the physical-space model
with constant $C_{\mathrm A}=0.8$ (registry §11, the non-dimensional
constant of its constant variant) practically overlaps the $k$-independent one.
Domaradzki (§3.3) also cites
Thiry, Winckelmans & Duponcheel (2019), who found the spectral viscosity
of the dynamic Smagorinsky model "essentially uniform over all
wavenumbers", and Siegel & Domaradzki (1994) found Smagorinsky spectra
approximately uniform in $k$ (§3.3); Vicente Cruz & Lamballais (§6.3,
Fig. 11) also find the a posteriori Smagorinsky viscosity nearly constant
(above).

## Plateau–cusp model in modal DG space

Flad & Gassner (2017, §3.1) explain the failure of DG implicit LES at coarse
resolution by the shape of interface dissipation: concentrated at the
highest wavenumbers, without the low-wavenumber plateau. Their third "cusp"
strategy (§5, App. C, Eqs. C.3–C.5) transfers the cusp to modal polynomial
space,

$$\nu_t^+(N+1\mid N_c+1)=9.21\,e^{-3.03\,(N_c+1)/(N+1)},$$

with $N_c$ a modal cutoff (page-local), and uses it as the weighting of a
polynomial high-pass filter applied to the lifted gradients. The cusp
stress $-2C_{\mathrm{cusp}}\Delta^2\lvert S\rvert S^d_{ij}$ of the
filtered gradients, with $C_{\mathrm{cusp}}=0.33^2$, is added to a
Smagorinsky stress with $C_s=0.13$, on a dissipation-free kinetic-energy-preserving
split-form DG baseline. On decaying HIT at $48^3$ degrees of freedom it
gives the best fit to the DNS spectrum of the three strategies tested, but
leaves the pressure–dilatation oscillations unchanged (§5, §5.1, Figs. 8,
10).

## RNG spectral viscosity inside a subgrid-velocity model

[Hausmann et al. (2022)](/sources/hausmann-2022.md) (§II A–B) use a
wavenumber-dependent viscosity for a different purpose: not to close the
resolved equations but to replace the non-linear self-interaction
("non-linear relaxation") of the *subgrid* velocity in their
[subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md)
model, which keeps only the linear sweeping and straining by the LES field.
They cite Laval et al. for the observation that dropping the non-linear
relaxation overestimates the energy spectrum and the intermittency of the
subgrid field, and that a turbulent viscosity "compensates these two
effects essentially". The viscosity is the renormalization-group (RNG)
form they cite from Canuto & Dubovikov, printed as (Eq. 11)

$$\nu^{\mathrm{RNG}}_t(k)=\Big(\nu^2-C_\nu\int_k^\infty q^{-2}E(q)\,dq\Big)^{1/2}-\nu,$$

with $\nu^{\mathrm{RNG}}_t$ and $C_\nu$ page-local, $C_\nu=2/5$ the
analytical value (0.4 in what they call their "standard setup") and $q$ a dummy
wavenumber. It is spatially uniform and acts on each Fourier mode of the
subgrid velocity like the molecular viscosity, through a damping
$-(\nu+\nu^{\mathrm{RNG}}_t)\lvert\boldsymbol k_m\rvert^2$ on the mode
coefficients (Eqs. 15–16). The authors describe it as larger at small
wavenumbers and tending to zero at large ones, mimicking the removal of
energy towards smaller scales. In forced isotropic turbulence the
velocity-gradient statistics of the enriched field change very little when
$C_\nu$ is varied from 0.1 to 1.6 (§IV A, Fig. 10d). Hausmann et al. (§II A,
§IV A) also note that a viscosity cannot reproduce the contribution of the
non-linear term to the strain–rotation relation (the skewness of the PDF of
the second invariant), which their enriched field under-predicts.

## The standard model at high Reynolds number

[Rajek & Pozorski (2026)](/sources/rajek-2026.md) run Fourier
pseudo-spectral LES of forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
with the standard (Chollet–Lesieur) model inside the resolved equations,
$\{\partial_t+[\nu+\nu_t(k\mid k_c)]k^2\}\bar u_{\boldsymbol k}=$ projected
nonlinear and forcing terms (Eq. 11), on a fixed $256^3$ grid while the
viscosity is lowered to that of a hypothetical DNS $2$ to $1024$ times finer
per direction ($Re_\lambda$ from 152 to 10 067 measured, Table III).

- At $Re_\lambda\sim100$ ($64^3$, $k_c=30$, against a $256^3$ DNS) the
  model transfers energy among the resolved scales at about the right rate:
  the LES holds more than 95% of the DNS kinetic energy, shell energies are
  overestimated by up to 15% in the first shells and underestimated by up to
  50% further on, and the PDF of the second invariant $Q$ keeps its
  non-Gaussian form with shortened tails (§III A, Figs. 1–3). With
  $\nu_t=0$ the spectrum is unphysical (§III A).
- At high $Re_\lambda$ the spectrum shows a $k^{-5/3}$ range, but the
  compensated spectrum rises for $k/k_c>0.1$ once $Re_\lambda\gtrsim1000$,
  and the energy flux equals $\varepsilon$ only in the first few shells even
  at $Re_\lambda\sim10\,000$; the authors attribute this suppression of the
  inertial subrange to excessive dissipation at intermediate and low
  wavenumbers by the positive plateau (§III C, Figs. 8–9; §IV). $E(k_c)$,
  the skewness and the flatness of the velocity derivative saturate at
  $Re_\lambda\approx1000$, so that on $256^3$ the standard model resolves
  inertial-range dynamics accurately up to $Re_\lambda\approx1000$ at most
  (§III C, Table III, Fig. 7).

**The a priori ("theoretical") viscosity used as a closure.** Following
Domaradzki et al. (1987), as cited by Rajek & Pozorski (§II D, Eq. 16),
$\nu_t(k\mid k_c)$ is computed from a DNS filtered with a sharp cutoff as
$-[T(k)-T_<(k)]/(2k^2E(k))$, with $T$ the full transfer and $T_<$ the
transfer among modes below $k_c$. At $Re_\lambda\sim100$ ($k_c=30$) it is
negative for $k<0.4k_c$, with magnitudes close to the molecular viscosity,
and grows by about an order of magnitude between $0.7k_c$ and $k_c$, in
agreement with Domaradzki et al.; its value at the cutoff grows almost
exponentially up to $k_c\eta=1$ (§III B, Figs. 4–5). Used as the closure of
an LES, which the authors state had not been done before (§V), it recovers
the DNS spectrum over almost the whole resolved range, but leaves the PDF of
$Q$ nearly as for the standard model; it needs DNS data and so has no
predictive value beyond DNS-attainable Reynolds numbers (§III B, Figs. 5–6).

## Adaptively determined spectral eddy viscosity

Rajek & Pozorski (2026, §IV, Fig. 12) propose a spectral viscosity that is
not postulated but driven, wavenumber by wavenumber, towards a prescribed
model spectrum $E_m(k)$ (page-local; from experiment, DNS or a model
spectrum fixed at high $Re$ by the Kolmogorov constant and the injection
rate). Page-local symbols: $\nu_{t,a}^+(k,t)$ the adaptive normalized
viscosity, $k_t$ a transition wavenumber,
$B(k;k_t)=\tfrac12+\tfrac12\tanh[\alpha_B(k-k_t)]$ a smooth step
($\alpha_B=0.75$), $\tau_{\mathrm{reg}}(k)=c_1[k^3E_m(k)]^{-1/2}$ the
regulator time scale ($c_1=1$). The regulator, after the deterministic
forcing of Overholt & Pope that the authors cite, reads (Eqs. 20–27, with
the damping constants $c_3=c_4=0$ that the authors state "can be safely
imposed")

$$\frac{d\nu_{t,a}^+}{dt}=\frac{\mathcal C[F_c]}{\tau_{\mathrm{reg}}(k)},\qquad
F_c=c_2\ln\frac{E(k,t)}{E_m(k)},\quad c_2=0.25,$$

where the control operator $\mathcal C$ (page-local) returns $B\,F_c$ when
$\nu_{t,a}^+>0$ or when $\nu_{t,a}^+=0$ and $F_c>0$, and zero when
$\nu_{t,a}^+=0$ and $F_c<0$: the viscosity drains energy but never adds it,
and it vanishes in the forcing band and below $k_t$ (Eq. 26). The four
regions of the model are forcing range ($\nu_t^+=0$), transition, adaptive
part up to $k_c$, and a dealiasing correction at $k_c$ for the shell
partly emptied by spherical truncation (Eq. 32). A least-squares fit of the
time-averaged adaptive viscosity to the four-parameter form

$$\nu^+_{t,m}(k)=a_0+a_1\Big\{1-\tanh\Big[\Big(\frac{k_c-k}{a_2k_c}\Big)^{a_3}\Big]\Big\}$$

(Eqs. 28–34; $a_0,\dots,a_3$ page-local) gives the **adaptively
reconstructed** viscosity, a fixed form with no run-time cost; the
regulator itself costs much less than one 3-D FFT (§IV, §V). The authors
also replace the dimensional factor $[E(k_c,t)/k_c]^{1/2}$ by the
scale-dependent $[E(k,t)/k]^{1/2}$ (Eq. 35), stating from tests not shown
that the regulator then responds better and the fit improves. They call the
model "semi-adaptive": its parameters govern only the convergence rate,
not the stationary solution (§V).

Results (§IV):

- at $Re_\lambda\sim100$ the adaptive viscosity recovers the DNS spectrum
  over $k_c/2\le k<k_c$ with a coefficient of determination of 0.993
  (0.994 for the reconstructed form) against 0.271 for the standard model,
  with only a slight enhancement of the PDF of $Q$ (Figs. 14–16);
- at $Re_\lambda\sim10\,000$ with $k_t=0.4k_c$ the reconstructed viscosity
  drains energy at about the right rate for $k\ge k_c/2$ but the flux is
  not $\varepsilon$; raising $k_c$ widens the range where it is, and
  lowering $k_t$ to $0.1k_c$ brings the spectrum close to the reference,
  yet at most 15% of the resolved shells carry $\Pi(k)=\varepsilon$
  (Figs. 17–18). From $k_t\sim1/\lambda$ and $k_t\lesssim0.1k_c$ the authors
  derive the resolution criterion $k_c\lambda\approx10$ recorded on
  [LES grid-point requirements](/results/les-grid-point-requirements.md).

The model applies to isotropic turbulence only; the authors suggest
splitting inhomogeneous flows into statistically homogeneous subdomains,
as in Hausmann et al. (§V).

## The low-wavenumber plateau in the sources

The sources state the following on the low-wavenumber plateau.
Vicente Cruz & Lamballais (2023, §6.4) find a positive a priori plateau
in filtered DNS of the Taylor–Green vortex at $Re=40\,000$ (about 12, 2
and 0.2 times $\nu$ at three cutoffs) and conclude that it "cannot be
ignored"; Domaradzki (2024, §3.3) finds that the plateau–cusp LES-derived
viscosity agrees best with the inertial range. Rajek & Pozorski (2026, §V)
state that, "somewhat contrary" to Kraichnan, Chollet & Lesieur, Chollet
and Domaradzki, they "have postulated that the positive plateau is highly
undesirable and its existence is a strong indication of an insufficient
spatial resolution which is compensated by artificially increased energy
dissipation", and that accurate large scales in isotropic turbulence need
no viscosity at low wavenumbers; they state agreement with the
spectral-vanishing and numerical-dissipation literature they cite (Tadmor;
Karamanos & Karniadakis; Dairay et al.; Lamballais et al.); see
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
Their own a priori viscosity at $Re_\lambda\sim100$ in forced HIT is
negative, not positive, below $0.4k_c$ (§III B). The a priori estimates
of Vicente Cruz & Lamballais are from the Taylor–Green vortex at
$Re=40\,000$, those of Rajek & Pozorski from forced isotropic turbulence at
$Re_\lambda\sim100$.

## Qualifications

- **Sign of the RNG viscosity as printed.** With the minus sign inside the
  root of Hausmann et al.'s Eq. (11), the root is at most $\nu$, so
  $\nu^{\mathrm{RNG}}_t\le0$, and imaginary once the integral exceeds
  $\nu^2/C_\nu$ *(compiler check, not in the sources)*; this disagrees with
  their own text, which calls the viscosity positive, largest at small
  wavenumbers and energy-removing (§II A–B). The printed sign is recorded
  as printed.
- $9.21=0.267\times34.5$ *(compiler check, not in the sources)*: Eq. (C.3)
  of Flad & Gassner keeps only the cusp part of Eq. (C.2) and drops the
  plateau term although the model is named "plateau–cusp"; Eqs. (C.2)–(C.3)
  also print unbalanced parentheses.
- Vicente Cruz & Lamballais (2023) print the a priori estimator (Eq. 23)
  without the leading minus sign that follows from their Eqs. (18), (20)
  and (21) *(compiler check, not in the sources)*; as printed it would give
  a negative viscosity for forward transfer. The plateau values they report
  in the text (12, 2 and 0.2 times $\nu$) are positive, consistent with the
  corrected sign.
- Rajek & Pozorski (2026, §IV) introduce their Eq. (27) with "Eq. (22) can
  be rewritten in a more concise form"; Eq. (27) is the regulator Eq. (20)
  with the control operator of Eq. (26) applied to the control function,
  not a rewriting of Eq. (22) (the control function itself). Eq. (20) is
  printed without the operator. With $C_K=1.4$ the second coefficient of
  their Eq. (14) evaluates to $15.2\times1.4^{-3/2}=9.18$ against the
  printed 9.21 *(compiler check, not in the sources)*; the authors present
  $C_K=1.4$ as an approximate match.
- Rajek & Pozorski use "a priori LES" for the filtered DNS itself
  (statistics of a sharp-cutoff-filtered DNS), not for an a priori test of
  a model (§II C); see
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

# Citations

- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.2, Eqs. (16)–(23), (27)–(29); §6.3, Fig. 11; §6.4, Eq. (55), Figs. 16–19.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §3.1; §5, Fig. 8; §5.1, Fig. 10; App. C, Eqs. (C.1)–(C.5).
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §1; §2.2, Eqs. (2.24)–(2.27); §3.3, Fig. 10.
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §II A–C, Eqs. (11), (15)–(16); §IV A, Fig. 10d.
- [Rajek & Pozorski (2026)](/sources/rajek-2026.md) — §II B, Eqs. (9)–(14); §II D, Eq. (16); §III A–C, Tables II–III, Figs. 1–9; §IV, Eqs. (18)–(36), Figs. 12–18; §V.
