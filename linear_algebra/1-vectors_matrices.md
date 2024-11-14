# vectors and matrices (L1)

## geometry explanation of equations
> By default $x$ means column vector.  
> binary-equations: $A_{2\times 2}x_{2\times 1}=b_{2\times 1}$  
- row picture: draw two lines and get the cross point solution
- column picture: $x_1\times a_1 + x_2\times a_2=\vec{b}$, where $a_i$ is column vector of $A$.
- column picture is better in high dimension.
- linear mapping: $Ax=y=f(x)$ see vector $x$ is mapped to $y$ through $A$.
    - see eigenvectors.
    - map a line to a line for $A_{2\times 2}$ condition.
- rotation: $A=\begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$, $y=Ax$ rotate vector $x$ to $y$ rotate counterclockwise $\theta$.

## matrix multiplication
- $Ax=b$ 右乘列
    1. $b$ is **linear combination** of column vectors of $A$, $x$ is cofficient vector.
    2. $b_i=a_ix$ is many **inner products**, where $a_i$ is row vector of $A$.
- $x^TA=b^T$ 左乘行
    1. $b^T$ is linear combination of row vectors of $A$
    2. ...
- $AB=C$
    - $Ax=b$ expand $x$ and $b$ in row direction
    - $x^TA=b^T$ expand $x^T$ and $b^T$ in column direction
    - ~ is group of linear combination results
    - ~ is group of inner product between $A$ row vector set and $B$ column vector set.
    - $C_{ij}=\sum _ka_{ik}b_{kj}$
    - ** $C=\sum _kA_{k1}B_{1k}+\dots$ is column vector multiply row vector.
