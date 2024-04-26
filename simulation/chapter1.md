# basic modeling techniques

## Review of circuit analvsis
- first order system, KVL
- second order system, KVL + KCL
- more order: linear algebra $\dot{Y}=AY+BU(\mathrm{vector}) $
- soultion: general solution + special solution
    - general solution: homogeneous system $\dot{Y}=AY \to Y=e^{At}C$,  
    Taylor expansion: $e^{At}=I+\frac{At}{1!}+\frac{A^2t^2}{2!}+\cdots$,  
    for power of A: eigen-decomposition $A^n=X\Lambda ^n X^{-1}$ so $e^{At}=Xe^{\Lambda t}X^{-1}$ (**ture for diagonal matrices!**)  
    so $Y=e^{At}C=c_1e^{\lambda_1t}X_1+\cdots$ where $X_i$ means i-th column of $X$
    - Laplace transformation: $\dot{Y}=AY \to sY(s)+Y(0)=AY(s) \to Y(s)=(sI-A)^{-1}Y(0)=(sI-X\Lambda X^{-1})^{-1}Y(0)$,  
    abbreviation $C=X^{-1}Y(0)$ so $Y(s)=X(sI-\Lambda)^{-1}X^{-1}Y(0)=X(sI-\Lambda)^{-1}C=c_1\frac{1}{s-\lambda_1}X_1+\cdots$  
    inverse Laplace transform $Y=c_1e^{\lambda_1t}X_1+\cdots$ where $\lambda_k$ are system poles.
    - final solution = zero-input + zero-response(convolution): $Y=e^{At}C+\int_0^t e^{t-\tau}BU(\tau)d\tau$ (C is determined by initial state)(boundary condition?)

## Circuit equation formulation



## Sparse matrix techniques in VLSI circuit model



