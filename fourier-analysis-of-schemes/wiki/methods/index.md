# Methods

Algorithms and schemes.

* [Forward Euler method](/methods/forward-euler-method.md) — The one-step recurrence y^{n+1} = y^n + Delta t F(t^n, y^n) from the forward difference; on the decay equation dy/dt = -y it multiplies the solution by G = 1 - Delta t per step, and the source states |G| < 1, i.e. 0 < Delta t < 2, as a necessary condition for non-divergence that does not ensure accuracy, with oscillation for Delta t > 1 and divergence for Delta t > 2.
* [Milne's central-difference method](/methods/milne-central-difference-method.md) — The two-step recurrence y^{n+1} = y^{n-1} + 2 Delta t F(t^n, y^n) from the central difference, needing a second starting value; on the decay equation with Delta t = 0.5 and exact starting values it is more accurate early but soon oscillates with growing amplitude, which the source attributes to rounding errors exciting the growing solution exp(+t).
