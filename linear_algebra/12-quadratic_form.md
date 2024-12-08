# quadratic form (L28)

## quadratic form
- symmetric $A_{n\times n}=A^T$: to unify different $A\to A$ is unique for one quadratic form (they express the same in quadratic form).
- $f_{A_{2\times 2}}(x)=x^TAx=a_{11}x_1^2+2a_{12}x_1x_2+a_{22}x_2^2$
- complete square 配方: $f(x_1,x_2)=a_{11}(x_1+\frac{a_{12}}{a_{11}}x_2)^2+(a_{22}-\frac{a_{12}^2}{a_{11}})x_2^2\to$ cofficient of $x_2^2$ compared to 0 determines positive / semi / negative definite.
    - essence: elimination $A=LU$, $a_{11}, a_{22}$ is pivot and $a_{12}$ contains as multiplier in the square term.
- invertable linear transformation (complete square): $x=Cy\to f(x)=x^TAx=(Cy)^TA(Cy)=y^T(C^TAC)y=y^TBy$ is congruence
    - purpose: transform to canonical form / normal form
    - $x=Cy$ is basis transformation, $B=C^TAC$ is coordinate transformation
    - $C$ is invertable $\to R(A)=R(B)$
    - $C$ is orthonormal
        - keep the geometric shape
            > proof: $x=A\alpha,y=A\beta$ transforms two vectors but keep inner product $\to$ keep modulus and angle:  
            > $(x,y)=(A\alpha,A\beta)=(A\alpha)^T(A\beta)=\alpha ^TA^TA\beta=(\alpha,\beta)$
        - $A$ is symmetric $\Rightarrow \Lambda =B=C^TAC=C^{-1}AC$, coefficients are eigenvalues
        - this canonical form is unique regardless order of $\lambda$ in $\Lambda$
- canonical form 标准型: only contains square term
    - unique when $\Lambda =C^TAC$
- normal form 规范型: cofficients of canonical form are $\pm 1$
    - unique
    - rank: $R(A)=r$ is #nonzero terms (proof: $\Lambda =C^TAC$ invertable linear transformation)
    -  positive index of inertia: $p$ is #positive cofficient terms
    - negative index of inertia: $r-p$ is #negative cofficient terms
    - signature 符号差: $p-(r-p)=2p-r$
- positive definite minimum test: origin $f(0,0)=0$ is critical because $\frac{\mathrm{d}f}{\mathrm{d}x_1}=\frac{\mathrm{d}f}{\mathrm{d}x_2}=0$ is stationary point 驻点.
    - bad case: saddle point , decrease for some directions
    - good case: grows for every direction
    - judgement $(\Leftrightarrow)$: Hessian matrix
- geometry $f_A(x)=1$, check cofficient of $x_2^2$
    - positive definite $\to$ ellipse 椭圆
    - (indefinite) saddle point $\to$ hyperbola 双曲线
- principle axis theorem
    - $A=Q\Lambda Q^T$ where $\lambda$ is length and $x$ is direction of principle axis ($f_A(x)=1$ gets an ellipsoid 椭球).

## matrices of second derivates
- Hessian matrix $\begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$ is symmetric
    - positive definite $\to (0,0)$ is minimum point

## positive definite matrix
- definition
    - $\Leftrightarrow x^TAx>0 (\forall x\ne 0)$
        > proof: see canonical form / normal form
    - $\Leftrightarrow \forall \lambda >0 \Leftrightarrow p=r \Leftrightarrow A$ is congruent with $I$
        > proof: $Ax=\lambda x\to \lambda =\frac{x^TAx}{\| x \|^2}$ depends on numerator  
        > normal form: all cofficients are 1
    - $\Leftrightarrow$ all elimination pivots $>0$
        > proof: complete square: elimination $x^TAx=y^TC^TACy$, $C$ is invertable (see as elementary matrix)
    - $\Leftrightarrow$ all leading principal minor (expand from left upper corner) $P_k>0$
        > proof: eigenvalues of leading principal minor is proportion of eigenvalues of original matrix
- positive definite matrix is symmetric (definition)
- positive semidefinite 半正定: $\ge 0$, like negative definite, negative semidefinite, others are indefinite
    - negative definite $\Leftrightarrow$ all leading principle minor meets $(-1)^kP_k>0$
- properities
    - $A$ is positive definite $\Rightarrow A^{-1}$ is positive definite
        > proof: $\lambda _{A^{-1}}=\lambda _A^{-1}>0$
    - $A,B$ is positive definite $\Rightarrow A+B$ is positive definite 
        > proof: $x^TAx>0,x^TBx>0\to x^T(A+B)x>0, \forall x$
    - $A_{m\times n},R(A)=n\Rightarrow A^TA$ is positive definite
        > proof: $x^T(A^TA)x=(Ax)^T(Ax)=\| Ax \| ^2\ge 0,R(A)=n\to >0$