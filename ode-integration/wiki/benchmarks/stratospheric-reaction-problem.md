---
type: Benchmark
title: "Stratospheric reaction problem"
description: "Sandu's six-species oxygen–nitrogen stratospheric chemistry with diurnal photolysis, two linear invariants and concentrations spanning sixteen orders of magnitude; the sources use two variants that differ in one reaction, one rate factor and the initial nitrogen oxides, to test positivity-preserving integrators."
status: established
aliases: [stratospheric chemistry problem, stratospheric chemistry model, Sandu stratospheric problem]
tags: [stiff, positivity, verification, structure-preserving]
timestamp: 2026-10-20T08:00:00Z
---

# Stratospheric reaction problem

The **stratospheric reaction problem**, attributed by both sources to Sandu (2001), evolves
the concentrations $y=(O(^1D),O,O_3,O_2,NO,NO_2)$ (molecules per cm³) under photochemical
reactions whose photolysis rates follow the sun. With $T=(t/3600)\bmod24$ hours,
$T_r=4.5$, $T_s=19.5$ and $x=(2T-T_r-T_s)/(T_s-T_r)$ (page-local), the diurnal factor is

$$\sigma(t)=\begin{cases}\tfrac12+\tfrac12\cos\bigl(\pi\,\lvert x\rvert\,x\bigr),&T_r\le T\le T_s,\\0,&\text{otherwise},\end{cases}$$

and the photolysis rates are $k_1=2.643\times10^{-10}\sigma^3$,
$k_3=6.120\times10^{-4}\sigma$, $k_5=1.070\times10^{-3}\sigma^2$,
$k_{10}=1.289\times10^{-2}\sigma$ (page-local $\sigma$, $k_l$). The thermal rates are
$k_2=8.018\times10^{-17}$, $k_6=7.110\times10^{-11}$, $k_7=1.200\times10^{-10}$,
$k_8=6.062\times10^{-15}$, $k_9=1.069\times10^{-11}$, and $k_4$ (below)
([Nüßlein et al. 2021](/sources/nusslein-2021.md), §5.4, Eqs. (5.8)–(5.11);
[Nurkhametova et al. 2026](/sources/nurkhametova-2026.md), §4.1.3, Eq. (41)). The run starts
at noon, $t_0=12$ h, and covers three days in Nüßlein et al. ($t\in[12,84]$ h) and one or
three days in Nurkhametova et al. Oxygen and nitrogen atom counts,
$w_O=(1,1,3,2,1,2)$ and $w_N=(0,0,0,0,1,1)$, are linear invariants. The initial
concentrations range from about $10^2$ ($O(^1D)$) to $1.7\times10^{16}$ ($O_2$), the rates
switch on and off at sunrise and sunset, and $O(^1D)$ and $O$ fall towards zero at night,
which is what makes the problem a positivity test.

## Reactions and the two variants

Nüßlein et al. write eleven reactions with rates $r_1=k_1O_2$, $r_2=k_2O\,O_2$,
$r_3=k_3O_3$, $r_4=k_4O_3O$, $r_5=k_5O_3$, $r_6=k_6\mathcal M\,O(^1D)$, $r_7=k_7O(^1D)O_3$,
$r_8=k_8O_3NO$, $r_9=k_9NO_2O$, $r_{10}=k_{10}NO_2$, $r_{11}=k_{11}NO\,O$, with
$\mathcal M=8.120\times10^{16}$ (page-local) and

$$\begin{aligned}
O(^1D)'&=r_5-r_6-r_7, & O'&=2r_1-r_2+r_3-r_4+r_6-r_9+r_{10}-r_{11},\\
O_3'&=r_2-r_3-r_4-r_5-r_7-r_8, & O_2'&=-r_1-r_2+r_3+2r_4+r_5+2r_7+r_8+r_9,\\
NO'&=-r_8+r_9+r_{10}-r_{11}, & NO_2'&=r_8-r_9-r_{10}+r_{11}.
\end{aligned}$$

Nurkhametova et al. print the same species, invariants, diurnal factor, start time and the
nine rate constants $k_1$–$k_3$, $k_5$–$k_{10}$ with identical values, but the systems are
**not the same**:

| | Nüßlein et al. (2021) | Nurkhametova et al. (2026) |
|---|---|---|
| reaction $NO+O\to NO_2$ ($r_{11}$, $k_{11}=1.0\times10^{-8}$) | present | absent |
| quenching of $O(^1D)$ | $k_6\mathcal M\,O(^1D)$ | $k_6\,O(^1D)$ (no factor $\mathcal M$) |
| $k_4$ | $1.567\times10^{-15}$ | $1.576\times10^{-15}$ |
| initial $NO$, $NO_2$ | $4.000\times10^6$, $1.093\times10^9$ | $8.725\times10^8$, $2.240\times10^8$ |

The other initial values agree: $O(^1D)=9.906\times10^1$, $O=6.624\times10^8$,
$O_3=5.326\times10^{11}$, $O_2=1.697\times10^{16}$ (Nüßlein et al., Eq. (5.12); Nurkhametova
et al., §4.1.3; comparison by the compiler from the printed equations, PDF pp. 17–18 and
24–25). Whether the differences are deliberate variants or transcription differences cannot
be decided from the two papers; results are not comparable across them.

As a [production–destruction system](/definitions/production-destruction-system.md) in
graph Laplacian form, Nurkhametova et al. print a factorization $y'=\mathbb G(t,y)y$ for
which $w_N$ is a left null vector and $w_O$ is not, so only the nitrogen count is preserved
structurally and the oxygen count only to high accuracy; they state that no single
factorization preserves both (§4.1.3, after Blanes, Iserles and Macnamara).

## Results

- **Adaptive-weight Runge–Kutta** (Nüßlein et al. 2021, §5.4, Figs. 10–11). Third-order
  backward-Euler extrapolation with free weight adaptation and step-size control, internal
  normalization so that every component starts at 1: 249 steps, two rejected for the error
  bound; 25 steps had negative values, almost all very close to zero, the smallest value of
  the solution being $-1.59\times10^{-11}$; both invariants kept to roundoff. See
  [adaptive-weight Runge–Kutta methods](/methods/adaptive-weight-runge-kutta.md).
- **Patankar predictor–corrector** (Nurkhametova et al. 2026, §5). Uncorrected SDIRK21 gives
  negative $O(^1D)$ and $O$ over one day; final-stage and all-stage corrections remove them
  (Figs. 5–7). Rejecting steps with negative entries and halving $h$ drives the step to the
  minimum allowed (Fig. 8). Invariant errors over one day: oxygen $4.89\times10^{-14}$
  (baseline and final-stage) and $1.49\times10^{-12}$ (all stages), nitrogen about
  $7\times10^{-15}$ (Table 3). Observed orders with the final-stage correction 2.07, 4.27 and
  4.70 for SDIRK21, SDIRK32 and SDIRK43 on $t\in[19,29]$ h (Table 4). Over three days with
  SDIRK43 at tolerance $10^{-7}$ the correction raises the wall-clock time from 30.2 s to
  110.5 s, $+266\%$ (Table 6). See
  [modified Patankar methods](/methods/modified-patankar-methods.md).

## Qualifications

- **Printed slip in Nurkhametova et al.** The printed equation for $O_3$ in (41) lacks the
  term $-k_5y_3$, so $w_O^\top y'=3k_5y_3\ne0$ for the system as printed; the printed
  factorization $\mathbb G$ contains $k_5$ in its $O_3$ diagonal entry, so the term is
  presumably only missing from the displayed ODE *(compiler check, not in the sources)*.
  The text also calls the run "one-day" while saying the integration is typically three days
  (§4.1.3, §5.1.3).
- The nightly rates vanish exactly, so the Jacobian changes structure twice a day; Nüßlein
  et al. attribute the sudden step-size changes to this explicit time dependence (§5.4).

# Citations

- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §5.4 (Eqs. (5.6)–(5.12), Figs. 10–11); arXiv v2.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §4.1.3 (Eq. (41), factorization, invariants), §5.1.3, §5.2.3 (Table 3), §5.3 (Table 4), §5.4 (Table 6), Figs. 5–8.
