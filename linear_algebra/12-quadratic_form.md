# quadratic form (L28)

## positive definite matrix
- definition
    - $\Leftrightarrow x^TAx>0 (\forall x\ne 0)$
    - $\Leftrightarrow \forall \lambda >0$
        > proof: $Ax=\lambda x\to \lambda =\frac{x^TAx}{\| x \|^2}$ depends on numerator
    - $\Leftrightarrow$ all elimination pivots $>0$ (proof: complete square)
    - $\Leftrightarrow$ all leading principal minor (expand from left upper corner) $>0$
        > wait for proof
- positive definite matrix is symmetric
    > wait for proof
- positive semidefinite 半正定: $\ge 0$
- properities
    - $A$ is positive definite $\Rightarrow A^{-1}$ is positive definite
        > proof: $\lambda _{A^{-1}}=\lambda _A^{-1}>0$
    - $A,B$ is positive definite $\Rightarrow A+B$ is positive definite 
        > proof: $x^TAx>0,x^TBx>0\to x^T(A+B)x>0, \forall x$
    - $A_{m\times n},R(A)=n\Rightarrow A^TA$ is positive definite
        > proof: $x^T(A^TA)x=(Ax)^T(Ax)=\| Ax \| ^2\ge 0,R(A)=n\to >0$

## quadratic form
- $A_{2\times 2}^T=A\to a_{12}=a_{21}$
- $f_{A}(x)=x^TAx=a_{11}x_1^2+2a_{12}x_1x_2+a_{22}x_2^2>0$
- minimum test: origin $f(0,0)=0$ is critical because $\frac{\mathrm{d}f}{\mathrm{d}x_1}=\frac{\mathrm{d}f}{\mathrm{d}x_2}=0$ is stationary point 驻点.
    - bad case: saddle point , decrease for some directions
    - good case: grows for every direction
    - judgement $(\Leftrightarrow)$: Hessian matrix
- complete square 配方: $f(x_1,x_2)=a_{11}(x_1+\frac{a_{12}}{a_{11}}x_2)^2+(a_{22}-\frac{a_{12}^2}{a_{11}})x_2^2\to$ cofficient of $x_2^2$ compared to 0 determines positive / semi / negative definite.
    - essence: elimination $A=LU$, $a_{11}, a_{22}$ is pivot and $a_{12}$ contains as multiplier in the square term.
- geometry $f_A(x)=1$, check cofficient of $x_2^2$
    - positive definite $\to$ ellipse 椭圆
    - (indefinite) saddle point $\to$ hyperbola 双曲线
- principle axis theorem
    - $A=Q\Lambda Q^T$ where $\lambda$ is length and $x$ is direction of principle axis ($f_A(x)=1$ gets an ellipsoid 椭球).

## matrices of second derivates
- Hessian matrix $\begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$ is symmetric
    - positive definite $\to (0,0)$ is minimum point
