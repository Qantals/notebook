# solution of linear equation (L7, L8)

## computing null space $Ax=0$ (Ax=b的导出组)
- When doing elimination, null space won't be changed (because for equation the solution is the same) but column space will ().
- definitions:
    - rank ($r$): the amount of pivot after elimination. Then we get echelon form $U$.
    - pivot column: column with pivots variables, #=$r$
    - free column: columns except for pivot columns. Has free variables. #=$n-r$ for $A_{m \times n}$
- general solution of $Ax=0$: (MATLAB: `null()`)
    - systematically (orthonormal basis) assign free variables, then using back substitution to get pivot variables as one basis.
    - Linear combination of these basis makes up of null space.
- reduced row echelon form $R$ (MATLAB: `rref()`)
    - using Gauss-Jordan elimination so no need back substitution: zeros above pivots, pivots are 1. put pivot columns ahead compose identity matrix, and put free columns together.
    - back substitution: $R_{m\times n}=\begin{bmatrix} I_{r\times r} & F_{r\times (n-r)} \\ 0 & 0\end{bmatrix},RN=0,N=\begin{bmatrix}-F_{r\times (n-r)} \\ I_{(n-r)\times (n-r)}\end{bmatrix}$. common case without column permutation is OK.

## solve linear equation $Ax=b$
- particular solution $x_p$: set all free variables to zero. Back substitution.
- general (complete) solution: $x=x_p+x_n$ ($x_n$ is **all** general solutions of homogeneous equations)
    > proof: $Ax_p=b,Ax_n=0 \to A(x_p+x_n)=b$
- soultion circumstances w.r.t. rank
    - full column rank $r=n<m$
        - $R=\begin{bmatrix}I \\ 0\end{bmatrix}\to N(A)=\vec{0}$
        - unique solution $\to$ has 1 / no solution
    - full row rank $r=m<n$
        - $R=\begin{bmatrix}I & F\end{bmatrix}\to \dim N(A)=(n-m) \to$ can be solved by any $b$
        - has $\infty$ solutions.
    - invertable matrix $r=m=n$
        - $R=I\to N(A)=\vec{0}$  and can be solved by any $b$ 
        - unique solution $\to$ has 1 solution
    - degenerate matrix $r<m,r<n$
        - $R=\begin{bmatrix}I & F \\ 0 & 0\end{bmatrix}\to \dim N(A)=(n-r)$
        - has 0 / $\infty$ solutions.
    - conclusion
        1. $r=m$ must have solution ($b$ must be in $C(A)\Leftrightarrow \mathbf{rank([A|b])=rank(A)}$), $r<m$ depends on $b$
        3. Number of solutions depends on null space (if there is free variables)

