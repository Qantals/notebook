# basic modeling techniques

## Review of circuit analysis
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
    - final solution = zero-input + zero-state response(convolution): $Y=e^{At}C+\int_0^t e^{t-\tau}BU(\tau)d\tau$ (convolution transformation ?) ($C$ is determined by initial state $Y(0)$)
- all these are analytical solution, prefer numerical , systematic solution

## Circuit equation formulation
- label nodes and branches: node voltage (potential) $e_i$, branch current $i_i$, branch voltage $v_i$
- graph theory: write a system matrix. $G=(V,E)$ where $V$ is set of vertices(顶点,nodes), $E$ is set of edges(branches)
    - spanning tree(生成树): connect all vertices without loops.
    - fundamental loop(add only one edge), cutset(set of branches, leave graph disconnected), fundamental cutset(consists of only one edge of $G$)
    - only write fundamental loops for KVL and fundamental cutset for KCL
        - KCL: 5 branches, 6 nodes: $A_{5\times 8}\vec{i}_{8\times 1}=\vec{0}$
        - KVL: $A^Te=V$ (?)
- method
    - STA = Sparse Tableau Analysis
        - $\begin{bmatrix} A & 0 & 0\\ 0 & I & -A^T\\ K_i & K_v & 0 \end{bmatrix} \begin{bmatrix} i \\ v \\ e \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ S \end{bmatrix}$
        - applied to any circuit
        - coefficient matrix is very sparse, require sophisticated programming skills and data structure
    - MNA = Modified Nodal Analysis
        - more compact than STA
        - Nodal Analysis: $i=ge$ write KCL -> use branch equations to eliminate -> use KVL to eliminate(relative potential)
            - beneficial:
                - equation can be assembled by inspection
                - $Y_n$ is sparse but smaller than STA, has non-zero diagonal entrices and is often diagonally dominant
            - drawback: can not handle:
                - floating independent voltage
                - VCVS, CCVS, CCCS
        - step: write KCL -> use branch equations to eliminate(leave current source form) -> wirte unused branch equations -> use KVL to eliminate
        - $\begin{bmatrix} Y_n & B \\ C & 0 \end{bmatrix} \begin{bmatrix} e \\ i \end{bmatrix} = MS$
        - put inductor another row, because we dont't want 1/s in frequency domain.

## Sparse matrix techniques in VLSI circuit model



