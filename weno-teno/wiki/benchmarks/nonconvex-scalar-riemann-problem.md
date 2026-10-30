---
type: Benchmark
title: "Riemann problems with nonconvex scalar fluxes"
description: "Scalar Riemann problems for the quartic flux (u²−1)(u²−4)/4, with data (2,−2) giving a shock, a sonic rarefaction and a shock, and (−3,3) giving a stationary sonic shock between two rarefactions; the founding ENO and WENO papers use them to show convergence to the entropy solution."
status: established
aliases: [nonconvex Riemann problem, nonconvex flux test, quartic-flux Riemann problem, nonconvex scalar Riemann problems]
tags: [benchmark, riemann-solver, numerical-flux, weno]
timestamp: 2026-10-30T08:43:00Z
---

# Riemann problems with nonconvex scalar fluxes

For a convex flux the entropy solution of a scalar Riemann problem is a
single shock or a single rarefaction. A nonconvex flux allows compound
waves, in which a shock is attached to a rarefaction, and stationary
sonic discontinuities that a scheme can mistake for admissible jumps.
The founding papers of ENO and WENO use one quartic flux,

$$
f(u)=\tfrac14(u^2-1)(u^2-4),\qquad f'(u)=u^3-\tfrac52u,
$$

on $\partial_tu+\partial_xf(u)=0$ with Riemann data $u_{\mathrm L}$ for
$x<0$ and $u_{\mathrm R}$ for $x>0$, as the test that a high-order
scheme converges to the entropy solution, which none of them proves.
The flux changes convexity at $u=\pm\sqrt{5/6}$, where
$f''=3u^2-\tfrac52$ vanishes *(compiler check, not in the sources)*.
[Harten et al. (1987a)](/sources/harten-1987.md) choose the two data
sets so that the Riemann fan covers $x=0$, the case in which their
replacement of the exact Riemann solver by a Roe-type flux is hardest
to justify (§7 A2).

## The two data sets and their exact solutions

**Case (i), $(u_{\mathrm L},u_{\mathrm R})=(2,-2)$.** Harten et al. print
the exact solution (7.9a): $u=2$ for $x/t<-0.5281529$, a centred sonic
rarefaction $g(x/t)$ for $\lvert x\rvert/t<0.5281529$, defined by
$x/t=f'(g)$ in the concave part $\lvert u\rvert<\sqrt{5/6}$ of $f$, with
$g(\pm0.5281529)=\mp0.2152504$, and $u=-2$ beyond. Shu & Osher describe
it as "a shock followed by a rarefaction wave followed by another
shock". The two shocks are tangent to the fan: from $u=2$ to $0.2152504$
the Rankine–Hugoniot speed is $(f(2)-f(0.2152504))/(2-0.2152504)=-0.52815$,
equal to $f'(0.2152504)$, and symmetrically on the right
*(compiler check, not in the sources)*.

**Case (ii), $(u_{\mathrm L},u_{\mathrm R})=(-3,3)$.** Harten et al.'s
(7.9b) is $u=-3$ for $x/t<-19.5$, a rarefaction in the convex part
$\lvert u\rvert>\sqrt{5/6}$ for $-19.5<x/t<0$, its mirror image for
$0<x/t<19.5$, and $u=3$ beyond, with a jump at $x=0$ where the
rarefactions end at $\mp\sqrt{2.5}$; Shu & Osher call it "a stationary
shock at $x=0$". Since $f$ is even, the jump from $-\sqrt{2.5}$ to
$\sqrt{2.5}$ has Rankine–Hugoniot speed zero, and
$f'(\pm\sqrt{2.5})=0$ makes it sonic on both sides; $f'(3)=19.5$ gives
the outer edges of the fans *(compiler check, not in the sources)*.

## Runs

| Source | Scheme | Grid | Time | Reference |
|---|---|---|---|---|
| [Harten et al. (1987a)](/sources/harten-1987.md) §7 A2, Eqs. (7.7)–(7.9) | [ENO](/methods/eno-reconstruction.md) with reconstruction by deconvolution (RD), $r=1,2,4$, CFL 0.8; exact Riemann flux, or Roe flux with the crude entropy correction $\epsilon_{\mathrm R}=0.1\,\Delta x/\Delta t$ (Eq. (7.8b)) | $J=40$ cells on $[-1,1]$ (Eq. (7.4)); case (i) also $J=80$ | case (i) 80 steps (160 on $J=80$); case (ii) 20 steps | exact solution (7.9) |
| [Shu & Osher (1988)](/sources/shu-1988.md) Ex. 4, Eq. (4.4) | finite-difference ENO, 3-3-LF-ENO and 4-4-LF-ENO (third- and fourth-order Runge–Kutta and space, [Lax–Friedrichs](/methods/lax-friedrichs-flux.md) building block) | $\Delta x=1/10,1/20,1/40$ | not printed | exact solution; data "See [6]" (Harten et al.) |
| [Liu et al. (1994)](/sources/liu-1994.md) Example 3(a) | cell-average WENO, $r=3$ | $h=0.025$ (80 cells) on $[-1,1]$ | case (i) $t=1$, $\Delta t/\Delta x=0.3$; case (ii) $t=0.04$, $\Delta t/\Delta x=0.04$ | Lax–Friedrichs on a very fine grid |

Here $\epsilon_{\mathrm R}$ is page-local (Harten et al.'s $\epsilon$, as on the [Roe solver](/methods/roe-riemann-solver.md) page; the
width of the viscous fan added to the Roe flux), printed $0.1/\lambda$
with their mesh ratio $\lambda=\Delta t/\Delta x$. Shu & Osher's figures span
$x\in[-1,1]$; the report prints neither final times nor boundary
conditions for this example.

## Findings

**Exact Riemann flux.** With the exact Riemann solver in the flux, Harten
et al.'s ENO schemes develop the structure of case (i) "at the correct
rate", the computed shocks sitting at the right places, with the
first-order run showing the "dog-leg" typical of Godunov's scheme
(Fig. 5); in case (ii) the stationary shock is "perfectly resolved"
(Fig. 7).

**A crude entropy correction and the order.** With the Roe flux and
the correction $\epsilon_{\mathrm R}=0.1\,\Delta x/\Delta t$, a fan much narrower
than the exact initial fan, the case (i) solution develops the correct
structure "but not at the correct rate": the computed shocks lag the exact positions by 8,
3 and 1 cells for $r=1$, 2 and 4. On the twice finer mesh the lag in
cells stays the same, from which the authors conclude convergence to
the entropy solution, and they call the fourth-order result
"surprisingly good" (Fig. 6). In case (ii), where the fans are not
sonic, the rarefactions are as good as with the exact flux and only the
stationary shock is "somewhat smeared", the fourth-order run being
"only slightly inferior" to the exact-flux one (Fig. 8). The authors
use these runs to argue that the Riemann solver matters less as the
order grows, because for $r>1$ the smooth polynomial part of the
reconstruction carries more of the variation than its jumps (§7 A2,
p. 274). They also print a correction "more appropriate" for nonconvex
fluxes, Eq. (7.8c)–(7.8d), with which the modified Roe flux "becomes
computationally equivalent to the exact" Riemann flux; see
[Roe solver](/methods/roe-riemann-solver.md).

**Lax–Friedrichs building blocks.** Shu & Osher's finite-difference ENO
schemes "converge to the correct solutions in both cases with good
resolution" (Figs. 21–32). They state that convergence to the entropy
solution is not proved for their ENO methods and cite the nonconvex
tests of Harten et al. as numerical evidence for it.

**Weighted ENO.** Liu et al.'s WENO with $r=3$ converges "with
good resolution" to the entropy solutions of both cases against a fine
Lax–Friedrichs reference (Figs. 6–7); the same example runs the
[Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md).
They refer the details of the data to Harten et al.

## Qualifications

- Evidence is visual in all three papers; none prints an error norm on
  these problems. The only quantitative statement is Harten et al.'s
  shock lag in cells.
- Liu et al.'s case (ii) prints $\Delta t/\Delta x=0.04$ (their $\tau/h$) and $t=0.04$; with the
  maximum wave speed $f'(3)=19.5$ that ratio is a Courant number of
  about 0.78 *(compiler check, not in the sources)*.
- Harten et al. count time steps rather than a final time; with their
  CFL 0.8 and $\Delta x=0.05$ the step depends on the wave speeds of each
  case, which the paper does not convert to a time.
- The Buckley–Leverett flux is the other nonconvex flux these papers
  run; it has its own page.

# Citations

- [Harten et al. (1987a)](/sources/harten-1987.md) — §7 A2, Eqs. (7.4), (7.7)–(7.9), Figs. 5–8, pp. 271–275.
- [Shu & Osher (1988)](/sources/shu-1988.md) — §IV, Ex. 4, Eq. (4.4), Figs. 21–32 (ICASE Report 87-33).
- [Liu et al. (1994)](/sources/liu-1994.md) — §4, Example 3(a), Figs. 6–7.
