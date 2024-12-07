# pseudo inverses (L34)

## left / right inverses
- 2-sided inverse $AA^{-1}=I=A^{-1}A,R(A)=r=m=n$
    - $\dim N(A)=\dim N(A^T)=0$
    - projection $P=I$ (**the relation with $A^+$**: $AA^+A=I,AP=I|PA=A\to$ need $P$ close to $I$)
- left inverse: full column rank $r=n<m\to (A^TA)_{n\times n}$ is invertable
    - $\dim N(A)=0$, has 0 / 1 solution
    - $(A^TA)^{-1}A^TA=I_{n\times n}=A^{-1}_{\mathrm{left}-n\times m}A_{m\times n}\to A^{-1}_{\mathrm{left}}=(A^TA)^{-1}A^T$
- right inverse: full row rank $r=m<n\to (AA^T)_{m\times m}$ is invertable
    - $\dim N(A^T)=0,\dim N(A)=n-m$ has $\infty$ solutions
    - $AA^T(AA^T)^{-1}=I_{m\times m}=A_{m\times n}A^{-1}_{\mathrm{right}-n\times m}\to A^{-1}_{\mathrm{right}}=A^T(AA^T)^{-1}$

## pseudo-inverses
- pseudo inverse: no full rank $r<m,r<n, P$ projection matrix is invertable
    - $\dim N(A),\dim N(A^T)\ne 0$
    - left inverse (if exists): $A(A^TA)^{-1}A^T=P_{m\times m}\to PA=A$ is projection onto column space, $P\to I$
    - right inverse (if exists): $A^T(AA^T)^{-1}A=P_{n\times n}\to AP=A$ is projection onto row space, $P\to I$
    - usage: least square (normal equation: $A^TAx=A^Tb$ obtains $x$ using pseudo inverse $A^+$ by $P$)
- suppose $Ax=b$ is **one-to-one** linear mapping $x\in C(A^T)\to C(A)$, including $x\in N(A)\to \{\vec{0}\}$ includes all $x\in \mathbb{R^n}$
    - if $x\ne y\in C(A^T)\to Ax\ne Ay$
        > proof: suppose $Ax=Ay\in C(A)\to A(x-y)=0\to (x-y)\in N(A)$  
        > $(x-y)\in C(A^T)\perp N(A)\to (x-y)=0\to x=y$ so assumption is bad: $Ax\ne Ay$
    - result: $Ax$ doesn't map $C(A^T)$ to $N(A^T)$ and $A^+(Ax)$ doesn't map $C(A)$ to $N(A)\to $ pseudo inverse
- compute $A^+$: SVD $A=U\Sigma V^T$
    - $\Sigma _{m\times n}=\mathrm{diag}(\sigma _1,\dots ,\sigma _r,0,\dots)\to \Sigma ^+_{n\times m}=\mathrm{diag}(\sigma ^{-1}_1,\dots ,\sigma ^{-1}_r,0,\dots)$
    - $\Sigma \Sigma ^+=\mathrm{diag}(1,\dots ,1,0,\dots)_{m\times m}$ is projection $C(A^T)\to C(A)$
    - $\Sigma ^+ \Sigma =\mathrm{diag}(1,\dots ,1,0,\dots)_{n\times n}$ is projection $C(A)\to C(A^T)$
    - $\Rightarrow A^+=V\Sigma ^+U^T$

