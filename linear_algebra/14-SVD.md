# singular value decomposition (L30)
- $A_{m\times n}=U_{m\times m}\Sigma _{m\times n}V_{n\times n}^T$
- prefer $A=Q\Lambda Q^{-1}$ orthonormal eigenvectors
- linear transformation
    - $r=R(A)<\min{\{m,n\}}, Av_i=\sigma _iu_i$
    - $\Sigma _{m\times n}=\mathrm{diag}(\sigma _1,\dots ,\sigma _r),\sigma _i\ge 0$ is stretching factor
        > illustration: $\sigma \ge 0\Leftarrow A^TA$ is semi-positive definite: $x^T(A^TA)x=(Ax)^T(Ax)=\| Ax\|^2\ge 0$
    - $V=(v_1,\dots ,v_r,v_{r+1},\dots ,v_n)$ is orthonormal basis
        - $v_1,\dots ,v_r\in C(A^T)\in \mathbb{R^n}\to Av=\sigma u$ is linear combination of $C(A)$
        - $v_{r+1},\dots ,v_n\in N(A)\in \mathbb{R^n}\to$ orthogonal to $C(A^T)$
    - $U=(u_1,\dots ,u_r,u_{r+1},\dots ,u_m)$ is orthonormal basis
        - $u_1,\dots ,u_r\in C(A)\in \mathbb{R^m}$
        - $u_{r+1},\dots ,u_m\in N(A^T)\in \mathbb{R^m}$
    - $AV=U\Sigma$, transform orthonormal basis to orthonormal basis in another space $\to A=U\Sigma V^{-1}=U\Sigma V^T$
- compute $U,\Sigma ,V$
    - $A^TA=V\Sigma ^TU^TU\Sigma V^T=V\Sigma ^2V^T$
    - $V$ compose eigenvectors of $A^TA$. Similarly, $U$ compose eigenvectors of $AA^T$, but use $Av_i=\sigma _iu_i$ instead for uniqueness. (remember to **normalize**)
    - $\Sigma \to \sigma _A=\sqrt{\lambda _{A^TA}}>0$

