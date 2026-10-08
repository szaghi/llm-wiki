---
type: Benchmark
title: "High-Mach-number astrophysical jet (Mach 80 and Mach 2000)"
description: "A supersonic jet injected into ambient gas, with kinetic energy so dominant that the pressure easily turns negative; the Mach 2000 case is the standard stress test of positivity-preserving schemes."
status: established
aliases: [Mach 2000 jet, Mach 80 jet, astrophysical jet]
tags: [benchmark, euler, positivity, 2d, high-mach]
timestamp: 2026-10-08T00:00:00Z
---

# High-Mach-number astrophysical jet

**Set-up** (Ha et al.'s model without radiative cooling). $\gamma = 5/3$;
ambient state $(\rho, u, v, p) = (\rho_a, 0, 0, 0.4127)$; a jet
$(5, u_j, 0, 0.4127)$ enters at the left for $\vert y\vert < 0.05$; the
other boundaries are outflow.
* Mach 80: $u_j = 30$, $\rho_a = 5$, domain $[0,2]\times[-0.5,0.5]$,
  $t = 0.07$, $448\times224$
  ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.4).
* Mach 2000 ($u_j = 800$, about Mach 2100 relative to the jet sound
  speed): domain $[0,1]\times[-0.25,0.25]$, $t = 0.001$. The ambient density
  is $\rho_a = 5$ in [Zhang & Shu (2010)](/sources/zhang-2010.md) ($640\times320$)
  and $\rho_a = 0.5$ in [Zhang & Shu (2012)](/sources/zhang-2012.md)
  (Example 5.4, $800\times400$) and
  [Hu, Adams & Shu (2013)](/sources/hu-2013.md) (§3.2, half domain with a
  reflecting lower boundary, CFL 0.25).

**Results.** Without positivity preservation even state-of-the-art
schemes produce negative pressure. RKDG with the
[scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
(TVB $M = 10^4$ for Mach 80, $10^7$ for Mach 2000), FD WENO5 with the
same limiter, and WENO5 with the
[cut-off flux limiter](/methods/positivity-preserving-flux-limiter.md)
all complete the run. The results agree with each other at equal
resolution.

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.4.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.4.
3. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.2.
