---
type: Definition
title: "Grad–Shafranov equation"
description: "The axisymmetric ideal-MHD force balance J×B = ∇p written as an elliptic equation for the poloidal flux per radian, Δ*ψ = −μ0R²p′(ψ) − FF′(ψ); the nonlinear MHD codes solve it on their own finite-element basis to obtain a discretely balanced initial state."
status: established
aliases: [GS equation, Grad-Shafranov, Grad–Shafranov–Schlüter equation]
tags: [equilibrium, tokamak, mhd]
timestamp: 2026-10-16T12:00:00Z
---

# Grad–Shafranov equation

In an axisymmetric plasma with
$\mathbf B=F\nabla\phi+\nabla\psi\times\nabla\phi$, where $\psi$ is the
poloidal flux per radian and $F=RB_\phi$, static ideal force balance
$\mathbf J\times\mathbf B=\nabla p$ with $\mu_0\mathbf J=\nabla\times\mathbf B$
forces $p=p(\psi)$ and $F=F(\psi)$, and the toroidal current is
$\mu_0RJ_\phi=-\Delta^*\psi$. The remaining force balance across the flux
surfaces is the Grad–Shafranov equation

$$\Delta^*\psi\equiv R^2\nabla\cdot\Big(\frac{1}{R^2}\nabla\psi\Big)=\partial_R^2\psi-\frac1R\partial_R\psi+\partial_Z^2\psi=-\mu_0R^2\frac{dp}{d\psi}-F\frac{dF}{d\psi}.$$

([Ma & Guo (2022)](/sources/ma-2022.md), Eq. 13;
[Isernia et al. (2023)](/sources/isernia-2023.md), Eq. 2;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.2, App. A.) It is
elliptic in $(R,Z)$ and nonlinear through the free functions $p(\psi)$ and
$FF'(\psi)$. The form is unchanged under $(\psi,F)\to(-\psi,-F)$, so the
sources' differing sign conventions for the field leave it intact; for
instance [Ma & Guo (2022)](/sources/ma-2022.md), Eq. 13, write
$\mathbf B=\nabla\phi\times\nabla\psi-F\nabla\phi$ and print the same
equation (compiler's check). The normalized flux is
$\psi_N=(\psi-\psi_{\rm axis})/(\psi_{\rm bnd}-\psi_{\rm axis})$.

## Role in the nonlinear codes

The equation supplies the initial state of
[visco-resistive MHD](/methods/visco-resistive-mhd-model.md) and
[reduced MHD](/methods/reduced-mhd.md) runs. A solution computed on a
different discretization is not an exact discrete equilibrium, so codes
re-solve it on their own basis:

* **JOREK** has a built-in solver on the same finite-element grid. The
  profiles $p$ (through $T$ and $\rho$) and $FF'$ are given as functions of
  $\psi_N$; the boundary flux comes from $(R,Z,\psi)$ lists (geqdsk,
  CLISTE); Picard or Newton iterations are used. The equation is solved on
  an initial grid, a flux-surface-aligned grid is built from the result, and
  the equation is solved again on that grid. A free-boundary version uses
  STARWALL with Newton iterations
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.2;
  [Bhole et al. (2023)](/sources/bhole-2023.md), p. 9, Fig. 3, polar grid
  first, then a flux-aligned multi-block grid;
  [Korving et al. (2023)](/sources/korving-2023.md), §II;
  [Bogaarts et al. (2022)](/sources/bogaarts-2022.md), where the
  built-in solver "gives discrete force balance" for imported AUG
  profiles).
* **M3D-C1** reads QSOLVER profiles and re-solves the equation on its
  finite-element basis, while **CLT** interpolates the QSOLVER solution
  directly. The two benchmark equilibria therefore differ slightly, which
  the authors propose as one reason why the nonlinear evolutions are "not
  exactly the same" ([Zhang et al. (2021)](/sources/zhang-2021.md), §2, §4;
  see [CLT–M3D-C1 benchmark](/benchmarks/clt-m3d-c1-benchmark.md)).
* **SCELT** solves the inverse problem: given $q(\psi)$ and $p(\psi)$ it
  computes the flux-coordinate geometry and obtains $F$ from the prescribed
  $q$ through a flux-surface integral of the Jacobian divided by $R$
  ([Ma & Guo (2022)](/sources/ma-2022.md), §3.2, Eqs. 13–14).

In the reduced model the equilibrium is preserved even though the
evolution uses a constant $F_0$ instead of $F(\psi)$: all $F$ terms lie in
the kernel of the momentum projectors, and the Shafranov shift is kept
through the initial $\psi$ computed with the nonzero $FF'$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.1, p. 15). In the
reduced momentum equation force balance appears as
$\mu_0^{-1}[\psi,j]+[p,R^2]$ with $j=\Delta^*\psi$ (bracket as on
[reduced MHD](/methods/reduced-mhd.md)), which vanishes when $\psi$
satisfies the equation above (same source, p. 19, in JOREK units; see
*Printed variants*). The stellarator reduced model reduces to
the tokamak one for $\chi=F_0\phi$ and then also preserves Grad–Shafranov
equilibria, whereas a full-MHD stellarator equilibrium leaves a residual
force ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II; see
[reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)).
The three-dimensional analogue is solved by
[inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md).

## Varying q at fixed pressure: Bateman scaling

Adding a constant to $F^2$ while keeping $p(\psi)$ and the toroidal current
fixed changes $q$ everywhere and keeps the Grad–Shafranov equation satisfied,
because only $FF'$ enters it. It is used to scan $q_{\min}$ for $n=1$
kink and fishbone studies of a DIII-D equilibrium. The scaling changes the
toroidal field and hence $\beta$ together with $q_{\min}$, which matters for
the strongly $\beta$-dependent $n=1$ mode; for NSTX the authors instead vary
the plasma current at fixed toroidal field, which keeps $\beta$ nearly fixed
([Liu et al. (2022b)](/sources/liu-2022-b.md), §4–5).

## Verification test: the Solov'ev solution

With $\mu_0\,dp/d\psi=-c_1$ and $F\,dF/d\psi=-c_2R_0^2$ constant, the
equation has the exact solution

$$\psi=\tfrac12\big(c_2R_0^2+c_0R^2\big)Z^2+\tfrac18(c_1-c_0)\big(R^2-R_0^2\big)^2,$$

for which $\Delta^*\psi=c_1R^2+c_2R_0^2$. SCELT's inverse solver converges
to it with an $L^1$ error of order 3.81 in the grid number, for $R_0=5$,
$c_0=0.02997$, $c_1=0.0567$, $c_2=-0.013468$ in normalized units
([Ma & Guo (2022)](/sources/ma-2022.md), §3.2, Fig. 5; the solution check
is the compiler's).

## Examples of equilibria in the sources

* NSTX discharge 139536 at 309 ms (EFIT), the
  [NSTX VDE benchmark](/benchmarks/nstx-vde-benchmarks.md) equilibrium:
  $\psi_{\rm axis}=-4.73\times10^{-2}$ Wb/rad,
  $\psi_{\rm X\text{-}point}=1.19\times10^{-2}$ Wb/rad, $q_0=2.04$,
  $q_{95}=7.32$, $\beta_N=3.83\%$
  ([Artola et al. (2021)](/sources/artola-2021.md), Fig. 1, Table).
* Circular large-aspect-ratio ($R/a=10$), $\beta\approx0$ QSOLVER
  equilibria with prescribed $q$ profiles for the $2/1$ tearing and $1/1$
  kink tests ([Zhang et al. (2021)](/sources/zhang-2021.md), Eqs. 1.7–1.8).
* A JET-like single-null equilibrium (pulse 85943) for shattered-pellet
  studies ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.1).

## Printed variants

* [Bhole et al. (2023)](/sources/bhole-2023.md), p. 9, print
  $R^2\nabla\cdot(R^{-2}\nabla\psi)=-F\,dF/d\psi-dp/d\psi$, without the factor
  $R^2$ (and $\mu_0$, which JOREK units absorb) on $dp/d\psi$.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), p. 19, write
  "$j=FF'(\psi)+R^2p'(\psi)$" with $j=\Delta^*\psi$ (JOREK units) and state
  that the two terms $[\psi,j]-[R^2,p]$ then cancel. With that sign the two
  terms add, $2p'[\psi,R^2]$; they cancel for $j=-FF'-R^2p'$, the sign of
  the equation above (compiler's check).

No contradiction between sources is recorded.

# Citations

* [Liu et al. (2022b)](/sources/liu-2022-b.md) — Bateman scaling of $q$, §4–5.
* [Bhole et al. (2023)](/sources/bhole-2023.md) — JOREK equilibrium step and its printed form.
* [Ma & Guo (2022)](/sources/ma-2022.md) — normalized equation, inverse solver, Solov'ev convergence.
* [Zhang et al. (2021)](/sources/zhang-2021.md) — re-solved versus interpolated equilibria in the CLT–M3D-C1 benchmark.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — JOREK's built-in solver and equilibrium preservation in reduced MHD.
* [Isernia et al. (2023)](/sources/isernia-2023.md) — $\Delta^*\psi=-\mu_0RJ_\phi$ in SI.
* [Artola et al. (2021)](/sources/artola-2021.md) — NSTX equilibrium data.
* [Korving et al. (2023)](/sources/korving-2023.md), [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — flux-aligned grids and discrete balance from the built-in solver.
* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — equilibrium preservation in the tokamak limit of stellarator reduced MHD.
