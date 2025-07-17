# Physics‑1‑Oscillations – Group Task Breakdown

Goal: Build a suite of VPython simulations (and supporting analysis) for  
1. Simple harmonic oscillators  
2. Damped oscillators  
3. Forced (impulsive) damped oscillators  
4. A full car‑suspension model  


---

A. Simple Harmonic Oscillations  
Owner: Bella Toledo  
a = –(k/m)·x  
with a single Euler or RK4 loop, animate a mass on a spring and graph x(t), v(t), a(t) vs. t.  

Requirements:
- Animate the mass‑spring (point mass OK)  
- One graph window: position, velocity, acceleration vs. time  
- One graph window: kinetic, potential, total energy vs. time  
- Color‑coded curves + legend  
- Inputs via constants at top of script:  
  - spring constant _k_  
  - equilibrium length  
  - mass _m_  
  - x₀, v₀  

---

B. Damped Oscillations  
Owner:

Tasks:  
1. Add damping term –(b/m) to your acceleration.  
2. Verify agreement with textbook solution  
   x(t) = A·e^(–b t / 2m)·cos(ωt+ϕ₀)  
   ω = √(k/m – b²/4m²)  
    
3. Plot how amplitude decays: compare numeric energy vs. E₀·e^(–tτ) for small b.  
4. Sweep b across under/critical/over‑damped regimes and observe behavior.  

---

C. Forced Damped Oscillations (Impulse)  
Owner:  

Tasks: 
1. Introduce a short, constant “bump” force F₀ for Δt at some t₁:    
   F_drive = { F₀  for  t₁ ≤ t < t₁+Δt  
             {  0  otherwise  
2. Explore with and without damping.  
3. Compare post‑bump settling for different b; discuss ride comfort.  

---

D. Design a Car Suspension  
Owner: 

Tasks:
1. Choose plausible car parameters (m, k, b)—justify estimates analytically.  
2. Adapt the previous viz: now both wheel and chassis move (two‑mass, two‑spring system).  
3. Graph only wheel and only body displacements.  
4. Test realistic scenarios: speed bump, pothole, variation of b for comfort vs. handling.  

---

> DUE JULY 22nd
