# Jordan form (L29)
1. similarity $\to$ same eigenvalues
2. same eigenvalues diagonalizable $\sim \Lambda$: small family of similarity: $kI\sim kI$
    > proof: $MkIM^{-1}=kMIM^{-1}=kI$
3. same eigenvalues non-diagonalizable $\sim$ Jordan form: big family of similarity
    - like $\begin{bmatrix} 4 & a \\ 0 & 4\end{bmatrix}, \begin{bmatrix} 2 & 2 \\ -2 & 6\end{bmatrix}$ where $a$ is any scalar. Fix $\lambda _1=\lambda _2=4$ by fixing determinant and trace.
    - similar to $\begin{bmatrix} 4 & 1 \\ 0 & 4\end{bmatrix}$ (Jordan form)
- Jordan block $J_i$
    - diagonal are all $\lambda _i$, upper diagonal are all 1, others are all 0.
    - means many same one eigenvalue $\lambda _i$
- Jordan theorem: $\forall A_{n\times n}\sim J=\mathrm{diag}(J_1,\dots ,J_d)$
    - #blocks ($d$) = #independent eigenvectors
        - diagonalizable $\Leftrightarrow J=\Lambda \Leftrightarrow d=n$
    - #Jordan blocks for one eigen value = $\dim (\lambda _iI-A)$ = geometry multiplicity
    - sum of order of all Jordan blocks of an eigenvalue = algebratic multiplicity
