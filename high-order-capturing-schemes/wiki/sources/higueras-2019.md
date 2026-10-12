---
type: Source
title: "Higueras & Roldán (2019) — New third order low-storage SSP explicit Runge–Kutta methods"
description: "Five-stage third-order SSP Runge–Kutta methods that run in two registers while keeping u^n (2N*): shows, under an assumed coefficient structure, that the optimal SSP(5,3) methods (C ≈ 2.6506) are not 2N* in sparse Shu–Osher form, and constructs two 2N* methods with C = 2.18 and 2.15 whose observed coefficients on a Buckley–Leverett test exceed the 2N Williamson and van der Houwen methods."
resource: "doi:10.1007/s10915-019-00916-3"
source_kind: paper
authors: [Higueras I., Roldán T.]
year: 2019
venue: "J. Sci. Comput. 79:1882–1906"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2019-JSC-Higueras-101007s10915-019-00916-3.pdf"
tags: [time-discretization, ssp, low-storage, runge-kutta]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Variable-step codes need $u^n$ during the whole step, so a two-register
method must also keep it (the 2N\* class). The paper characterizes the
optimal five-stage third-order SSP methods as a five-parameter family,
under a structure inferred from RK-Opt runs, and shows that none has the
sparse 2N\* Shu–Osher form. It then optimizes inside 2N\* and obtains two
new, non-optimal methods. A single Buckley–Leverett test compares
observed SSP coefficients. Merged into
[low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md).

# Key claims

1. **SSP coefficient of a method** (§2, eqs. 9–11, 16; Defs. 1–2):
   Kraaijevanger's coefficient; the minimum ratio over one Shu–Osher form
   equals it only for an optimal representation.
2. **Known optimal methods and their storage** (§§2.2, 3): SSP($s$,1)
   $\mathcal C = s$, SSP($s$,2) $s - 1$, SSP(3,3) 1, SSP(4,3) 2, all 2N\*;
   SSP($n^2$,3) $n^2 - n$, 2N but not 2N\*.
3. **2N\*** (Def. 3, eq. 24, Algorithm 1): a 2N method that keeps $u^n$;
   the paper does not use Ketcheson's 2S/3S\* forms.
4. **Optimal SSP(5,3)** (§4.1, eqs. 25–38): $\mathcal C \approx 2.6506$,
   the real root of $x^3 - 5x^2 + 10x - 10$. The structure (31), (35) is
   observed in RK-Opt runs and then assumed ("we assume they are true").
5. **Proposition 1** (§4.2): no optimal SSP(5,3) method is 2N\* of form
   (24), conditional on that structure. The abstract and §7 state the
   result more broadly. Proposition 2: some members run in 3N.
6. **New methods** (§5.1, eqs. 49–53, 60–61): SSP53_2N\*₁,
   $\mathcal C = 2.180749177932739$, error constant $0.0278$; SSP53_2N\*₂,
   $\mathcal C = 2.1487419827223833$, error constant $0.0227$, real
   stability interval to $-7.26$ (Fig. 1).
7. **Conjecture** (§7): a smaller error constant gives a larger observed
   coefficient, within methods of equal $\mathcal C$ (hypothesis; Table 1
   does not bear it out across groups).

**Test** (§6.1, Table 1): Buckley–Leverett on 100 cells, periodic,
$t \le 1/8$, Koren-limited semi-discretization, observed coefficient by
the total-variation ratio (forward Euler TVD for $\Delta t \le 0.0025$).
Observed: 2.29 and 2.45 for the new methods; 2.72–2.96 for the optimal
SSP(5,3) members; 2.04 for SSP(4,3); 1.96–2.20 for the five-stage 2N
Williamson and van der Houwen methods. No step-size control, no
embedded pairs, no positivity or entropy content.

# Notation map

| Higueras & Roldán (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$ | $\Delta t$ | $h$ is the grid spacing |
| $f(y)$, $y_n$, $Y_i$ | $\mathcal L(u)$, $u^n$, $u^{(i-1)}$ | stages indexed from 1 |
| $\lambda_{ij}$, $\gamma_{ij}$ | $a_{i-1,j-1}$, $b_{i-1,j-1}$ | Shu–Osher, index shifted by one |
| $a_{ij}$, $b_j$, $c_i$; $\mathbb A$ | $\mathsf a_{ij}$, $\mathsf b_j$, $\mathsf c_i$ | Butcher |
| $R(\mathbb A)$, $r$ | $\mathcal C$ | $r$ is the stencil count |
| $c^{\mathrm{obs}}_{\mathbb A}$ | $\mathcal C_{\mathrm{obs}}$ | the paper calls it "effective" |
| $R(z)$ | $R_{\mathrm{st}}(z)$ | |
| $u, v, w, x$ (parameters); $\phi(\theta)$ | words | collide with registry symbols |

# Pages created or updated

* Contributed to [Low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md) and [Explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md).
* Updated [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) (coefficient of a method; optimal values), [SSP order barriers](/results/ssp-order-barriers.md) (the low-storage line in context; Proposition 1), [Total variation diminishing](/properties/total-variation-diminishing.md) (observed coefficient).
* Updated [Notation registry](/notation.md): $\mathcal C_{\mathrm{eff}}$, $\mathcal C_{\mathrm{obs}}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2019-JSC-Higueras-101007s10915-019-00916-3.pdf`.
   * **Version.** arXiv:1809.04807v1 (13 September 2018), 24 pages, not
     the typeset article.
   * **Identity.** doi:10.1007/s10915-019-00916-3, checked on Crossref:
     J. Sci. Comput. 79(3):1882–1906, 2019.
   * **How it was read.** Text extraction, all sections; Table 1, eq. 55 and
     the Buckley–Leverett set-up checked on the page images. The tableaux
     (22)–(23) and several Shu–Osher matrices are garbled in the text
     layer and not reproduced.
   * **Recorded as printed.** The §5.1 stability function of SSP53_2N\*₂
     copies that of SSP53_2N\*₁ (the appendix has the right one); equation
     labels of Table 1 and the appendix disagree; the register count of
     one method is given three ways; the Buckley–Leverett flux is printed
     with an undefined variable and is not reproduced.
   * **Reference list:** 30 entries (the published version adds Hairer,
     Nørsett & Wanner, per Crossref). The printed `shu-1988` is the SISSC
     TVD paper, merged as `shu-1988-b`.
