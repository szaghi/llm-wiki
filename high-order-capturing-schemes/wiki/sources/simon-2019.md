---
type: Source
title: "Simon & Mandal (2019) — A simple cure for numerical shock instability in the HLLC Riemann solver"
description: "Writes HLLC as HLL plus an anti-diffusive term and widens the HLL wave speeds only inside the dissipation, with an eigenvalue or pressure sensor (HLLC-SWM): contacts and shear survive, a saw-tooth analysis and a matrix stability analysis of a steady shock fix the coefficient at 3.5, and the carbuncle, odd–even decoupling and kinked Mach stem disappear in first- and second-order tests."
resource: "doi:10.1016/j.jcp.2018.11.022"
source_kind: paper
authors: [Simon S., Mandal J.C.]
year: 2019
venue: "J. Comput. Phys. 378:477-496"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2019-JCP-Simon-101016jjcp201811022.pdf"
tags: [riemann-solver, shock-instability, hllc]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

HLLC resolves contacts and shear exactly, but it is "highly susceptible"
to [numerical shock instability](/definitions/numerical-shock-instability.md).
The paper writes HLLC as the HLL flux plus an anti-diffusive term and
enlarges $S_L$ and $S_R$ only in the HLL dissipation vector. The contact
speed and the anti-diffusion stay as they are, which the authors call
"selective wave modification" (SWM). The increment is the largest
entropy-fix quantity over the faces transverse to the face (variant E),
optionally switched by a pressure-ratio sensor (variant P). The tuning
coefficient 3.5 comes from a matrix stability analysis of a steady normal
shock. The tests are mostly first-order finite volume on structured
quadrilaterals; two are second order. There is no WENO. Merged into
[cures for numerical shock instability](/methods/shock-instability-cures.md),
the new instability, benchmark and Riemann-solver pages, and four
existing benchmarks.

# Key claims

1. **HLLC as HLL plus anti-diffusion** (§5, eqs. 13–16, from the page
   images): $\hat f^{\mathrm{HLLC}} = \hat f^{\mathrm{HLL}} + S_L(u^{\mathrm{HLLC}}_{*L} - u^{\mathrm{HLL}}_*)$
   for $S_L \le 0 \le S_M$, and with $R$ for $S_M \le 0 \le S_R$. The HLL
   flux is written as central plus $\mathbf d^{\mathrm{HLL}}$, with
   coefficients $(\vert S_R\vert - \vert S_L\vert)/(2(S_R - S_L))$ on the
   flux jump and $(\vert S_L\vert S_R - \vert S_R\vert S_L)/(2(S_R - S_L))$
   on the state jump.
2. **The modification** (eqs. 17–18). Only $\vert S_L\vert$ and
   $\vert S_R\vert$ in the numerators become
   $\vert S^{\mathrm w}_{L,R}\vert = \vert S_{L,R} \mp \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}\vert$.
   Denominators and outer factors keep the original speeds, so this "is
   not" HLL with wider speeds, and the authors stress that only this form
   works (p. 12). With equal increments on a subsonic face, the change
   adds $\tfrac12\alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}(u^- - u^+)$
   (§5.1, eqs. 20–22).
3. **Linear saw-tooth analysis** (§6, eqs. 23–27). For plain HLLC the
   amplification factors of density, normal velocity and pressure are
   $(1, 1, 1 - 2\nu_y)$, with $0 < \nu_y < 1$. Pressure feeds density
   through a $-2\nu_y/\gamma$ coupling, and the scheme is "marginally
   stable". With SWM the diagonal becomes
   $1 - 2\nu_y\alpha\epsilon/\sqrt\gamma$ (twice) and
   $1 - 2\nu_y(1 + \alpha\epsilon/\sqrt\gamma)$, damping all three under
   $\nu_y < 1/(1 + \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}/\sqrt\gamma)$.
4. **Sensors** (§7, eqs. 28–32).
   * Variant E: $\epsilon_{\mathrm{SWM}}$ is the maximum over the four
     transverse faces of $\tfrac12\max_p\vert\lambda^{(p)}(u^+) - \lambda^{(p)}(u^-)\vert$.
     The face itself is excluded, after Pandolfi & D'Ambrosio, to spare
     boundary layers.
   * Variant P multiplies this by $1 - \omega_{\mathrm p}$, with
     $\omega_{\mathrm p}$ the minimum of $\min(p^+/p^-, p^-/p^+)^5$ over
     the same stencil.
5. **Choice of the coefficient** (§8). The matrix stability analysis
   (Dumbser–Moschetta–Gressier) of a Mach 7 steady shock on $11\times11$
   gives the largest real part of the spectrum: $+8.15562$ at coefficient
   0 (plain HLLC), $+0.55869$ at 1, $-0.11959$ at 1.5, $-0.66053$ at 3.5
   (Fig. 4a). In a nonlinear run to $t = 20$ the shock is stable only for
   a coefficient of at least 2.5. Growth rates rise with Mach number (3, 7,
   10, 20). 3.5 is chosen for both variants. At 3.5, variant P has a
   largest real part of $-0.59317$ (Fig. 7).
6. **Low-Mach switch for variant E** (§9.9, eqs. 33–34): the increment is
   multiplied by $\sin\left(\tfrac{\pi}{2}\,\mathrm{Ma}/0.3\right)$ for
   $\mathrm{Ma} \le 0.3$.
7. **Claims from tests only**:
   * positivity and contact preservation are kept (§§9.1, 9.8);
   * variant P "suggests that it is possible to circumvent" the
     Gressier–Moschetta conjecture that exact contact resolution implies
     shock instability (§10).

**Tests** (§9, coefficient 3.5 throughout):
* the Einfeldt double rarefaction and a sheared variant on $100\times50$;
* Quirk's odd–even test (grid size not given);
* the inclined stationary shock;
* the Mach 20 blunt body on $320\times20$;
* the double Mach reflection on $480\times120$, end time printed as
  $t = 0.02$;
* shock diffraction at a 90° corner on $400\times400$, second order;
* the forward-facing step on $120\times40$, second order;
* a supersonic shear layer, where HLLE smears the contact and SWM does not;
* a Blasius flat plate at Mach 0.1.

# Notation map

| Simon & Mandal (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$; $\mathbf F$, $\mathbf G$ | $u$; components of $\mathbf f$ | |
| $\mathbf U_L, \mathbf U_R$; $\mathbf F_L, \mathbf F_R$ | $u^-, u^+$; $f(u^-), f(u^+)$ | |
| $\mathbf U^{HLL}_*$, $\mathbf U^{HLLC}_{*L/R}$ | $u^{\mathrm{HLL}}_*$, $u^{\mathrm{HLLC}}_{*L}$, $u^{\mathrm{HLLC}}_{*R}$ | |
| $\mathbf D_{HLL}$, $\overline{\mathbf D}_{HLL}$ | $\mathbf d^{\mathrm{HLL}}$ and its modified form | |
| $\overline{S_L}$, $\overline{S_R}$ | $S^{\mathrm w}_L$, $S^{\mathrm w}_R$ | the overbar would read as a cell average |
| $\alpha$, $\epsilon^{L,R}$ | $\alpha_{\mathrm{SWM}}$, $\epsilon_{\mathrm{SWM}}$ | collide with $\alpha$ and $\varepsilon$ |
| $\omega$, $f_k$, $\beta$ | $\omega_{\mathrm p}$; pressure-ratio factors; exponent 5 | collide with $\omega_k$, $f$, $\beta_k$ |
| $\lambda = \sqrt\gamma\,\Delta t/\Delta y$ | $\nu_y$ | collides with $\lambda^{(p)}$ |
| $\lambda_p$ | $\lambda^{(p)}$ | |
| $a$, $u_n$, $u_t$ | $c$, $v_n$, $v_t$ | |
| $M$ | $M_s$ (shock) or $\mathrm{Ma}$ (local) | collides with the TVB $M$ |
| $\theta$ (stability eigenvalues) | words | collides with the limiter $\theta$ |

# Pages created or updated

* Created [Numerical shock instability](/definitions/numerical-shock-instability.md), [Cures for numerical shock instability](/methods/shock-instability-cures.md), [Quirk's odd–even decoupling test](/benchmarks/quirk-odd-even-test.md), [Hypersonic blunt-body carbuncle test](/benchmarks/hypersonic-blunt-body.md), [Stationary normal shock test](/benchmarks/stationary-normal-shock.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (HLLC as HLL plus anti-diffusion; `Contradictions` on HLLE), [Low-Mach-number fluxes](/methods/low-mach-number-fluxes.md), [Double Mach reflection](/benchmarks/double-mach-reflection.md), [Forward-facing step](/benchmarks/forward-facing-step.md), [Shock diffraction](/benchmarks/shock-diffraction.md), [Double rarefaction](/benchmarks/double-rarefaction.md), [Supersonic cylinder flow](/benchmarks/supersonic-cylinder-flow.md).
* Updated [Notation registry](/notation.md): $u^{\mathrm{HLL}}_*$, $\mathbf d^{\mathrm{HLL}}$, $S^{\mathrm w}_{L,R}$, $\alpha_{\mathrm{SWM}}$, $\epsilon_{\mathrm{SWM}}$, $\omega_{\mathrm p}$, $\nu_y$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2019-JCP-Simon-101016jjcp201811022.pdf`.
   * **Version.** arXiv:1803.04922v1 (13 March 2018, "Preprint submitted
     to Journal of Computational Physics"), the only arXiv version, 47
     pages. It is not the typeset article. The published title adds "the".
   * **Identity.** doi:10.1016/j.jcp.2018.11.022, checked on Crossref:
     J. Comput. Phys. 378:477–496, February 2019.
   * **How it was read.** Text extraction, all sections. The equations
     used here (eqs. 13–34) and Figs. 3–4 were read from the page images.
     Contour figures were read from the text.
   * **Defects in the preprint.** A broken section reference (p. 5).
     §7.2 says "HLLEM-SWM" where it means HLLC. The Fig. 9 caption gives
     $t = 0.1$ against $t = 0.11$ in the text. The double Mach reflection
     end time is $t = 0.02$.
   * **Reference list:** 45 entries.
