# vector space (L5, L6, L9, L10)

## vector space basis
- definition: all vectors in a space require closure to linear operation (still in this space)
- example: $\mathbb{R^2}$ is ~, compose to a plane. $\mathbb{R^n}$ space has all n-dimension vectors, each has n scalars in $\mathbb{R}$
- zero vector: any vector scalar multiply zero is zero vector, so it must be contained in any space.
- subspace of $\mathbb{R^3}$ has:
    1. P: plane across origin(common plane)
    2. L: line across origin(common line)
    3. origin
- operation on subspace is subspace?
    - union: No. example: $P\cup L\ (L\subsetneq P)$ is not a vector space
    - intersection: Yes. example: $P\cap L\ (L\subsetneq P)$ is a vector space.
- state space
    - $x_1(t),\dots ,x_n(t)$ system state variables
    - $X=(x_1(t),\dots)$ system state vector

## rank
- obvious
    - invertable: $rank=n$
    - $A_{m\times n},0\le rank(A)\le \min\{m,n\}$
- $rank(E_1AE_2)=rank(A)$ where $E_1,E_2$ are elementary matrices.
    - $rank(A)=r$ means $A$ can be operated to row echelon form with $r$ non-zero rows.
    - equivalence: $rank(PA)=rank(AQ)=rank(PAQ)=rank(A_{m\times n})$ where $P_{m\times m},Q_{n\times n}$ are invertable.
        > proof: using elementary matrices to split $P,Q$  
        > illustration: $PAQ=\begin{bmatrix} I_r & O \\ O & O \end{bmatrix}$
- $rank(A)=rank(A^T)$ 行秩等于列秩
    > proof1: through original defination, check determinant of all sub-matrices to get maximum size is $r$. And $\det A=\det A^T$.  
    > proof2: using block matrices, $A_{m\times n}=(\alpha ^T_1,\dots ,\alpha ^T_m)=(\beta _1,\dots ,\beta _n)$ composed of independent vectors $(\alpha '^T_1,\dots ,\alpha '^T_s),(\beta '_1,\dots ,\beta '_r)$  
    > where $r$ is column rank, $s$ is row rank;  
    > so $A_{m\times n}=(\alpha ^T_1,\dots ,\alpha ^T_m)=P_{m\times s}A'_{s\times n}\to r\le s$ from the prespective of columns of $P$  
    > similarly, $A_{m\times n}=A'_{m\times r}P_{r\times n}\to s\le r$ so $r=s$.
- $rank(AB)\le \min\{rank(A), rank(B)\}$
    > proof: for $C=AB\to C$ is linear representation of $A\to rank(C)\le rank(A)$, and $rank(C)=rank(C^T)=rank(B^TA^T)\le rank(B^T)=rank(B)$
- $rank(A+B)\le rank(A)+rank(B)$
    > proof: $A=P_1\begin{bmatrix}I_{r_1\times r_1} & 0 \\ 0 & 0 \end{bmatrix}Q_1, B=P_2\begin{bmatrix}I_{r_2\times r_2} & 0 \\ 0 & 0 \end{bmatrix}Q_2, rank(A)+rank(B)=r_1+r_2=rank(\begin{bmatrix}P_1 & 0 \\ 0 & P_2\end{bmatrix}\begin{bmatrix} \begin{bmatrix}I_{r_1\times r_1} & 0 \\ 0 & 0\end{bmatrix} & 0 \\ 0 & \begin{bmatrix}I_{r_2\times r_2} & 0 \\ 0 & 0\end{bmatrix}\end{bmatrix}\begin{bmatrix}Q_1 & 0 \\ 0 & Q_2\end{bmatrix})=rank(\begin{bmatrix}A & 0 \\ 0 & B\end{bmatrix})=rank(\begin{bmatrix}A & A+B \\ 0 & B\end{bmatrix})\ge rank(A+B)$
- $AB=0\to rank(A)+rank(B)\le n$
    > proof: $AB=0\to AX=0,B$ is solutions of $Ax=0\to B$ is linear representation of $N(A)\to rank(B)\le \dim N(A)=n-rank(A)$

## linear independence / dependence
- linear representation: every column vector in $A$ is linear combination of column vectors in $B\to A$ is linear representation of $B\to A=BX$
    - judgement: $A=BX$ has solution $X\Leftrightarrow rank(A)=rank([A|B])$
- equivalence of vector set
    - $A=(a_1,\dots ,a_r),B=(b_1,\dots ,b_s)$
    - equivalence: $A=BX_1$ and $B=AX_2$
- independence: linear combination $Ax=0\to x=0$
    - independence $\Leftrightarrow N(A)=\vec{0}\Leftrightarrow rank(A)=n\Leftrightarrow \det A\ne 0$ (if $A_{n\times n}$)
    - dependence $\Leftrightarrow \dim N(A)\ge 1 \Leftrightarrow rank(A)<n\Leftrightarrow \det A=0$ (if $A_{n\times n}$)
    - $\vec{0}$ is dependent with other non-zero vectors (cofficient on $\vec{0}\ne 0$)
- dependence and dim: $\#\ge(n+1)$ vectors in $\mathbb{R^n}$ must be dependent $\Leftrightarrow A_{m\times n}(m<n), rank(C(A))=rank(A)\le m<n$
    - $\Leftrightarrow$ any independent vector set in $\mathbb{R^n}$ has no more than $\#n$ vectors.
- subset
    - any maximal linearly independent subset in a vector set is equivalent, and equivalent to the whole vector set.
    - another form of fundamental theorem of vector: if $A$ is independent and $[A|b]$ is dependent, thus $b=Ax$ for **unique** $x$.
- rank and linear representation: if independent $A_{m\times r}=B_{m\times s}X\to r\le s$
    - $\Leftrightarrow$ otherwise $r>s\to A_{m\times r}$ is dependent
    - $\Leftrightarrow$ $rank(A)\le rank(B)$ whether $A,B$ is independent or not
        > proof: check and compare maximal linearly independent subset
- basis: a maximal linearly independent subset span a space.
    - basis / coordinate transformation: $B=AT$ transform basis $A$ to $B$ through transition matrix $T$, so the vector in the space $\alpha =Ax_1=Bx_2=ATx_2\to x_1=Tx_2$

## four fundamental subspaces
- column space: $C(A)=Ax$ for all $x$
    - pivot column: independent vectors in $C(A)$
- null space: $Ax=0$ for all **solution** $x$ compose a space: $N(A)$
    > proof (using algebra):  
    > addition closure: $Av=Aw=0,A(v+w)=0$  
    > scalar multiplication closure: $Av=0\to cAv=0=A(cv)$
- elementary row operation
    - hold the row space (because linear combination results in equivalent vector set)
    - change the column space, but keep the corresponding column vectors set ($k$ columns in $A\to k$ columns in $R$) independence / dependence.
        > proof: $P$ is invertable (invertable matrices is equivalent to elementary matrices), $Ax=0\to PAx=(PA)x=0$, vice versa $(PA)x=0\to P^{-1}PAx=Ax=0$, has the same solution $x=0\text{ or }x\ne 0$, so solution is the same for sub $k$ components.
- for $r=rank(A)$, $A_{m\times n}$
    - column space $C(A)$ in $\mathbb{R^m},\dim =r$
    - null space $N(A)$ in $\mathbb{R^n},\dim =n-r$
    - row space $C(A^T)$ in $\mathbb{R^n},\dim =r$
        - $\dim C(A)=\dim C(A^T)$ because pivots look like echelon (identity) matrix
        - basis: non-zero rows in rref $R$, for the reason above.
    - left null space $N(A^T)$ in $\mathbb{R^m},\dim =m-r$
        - $A^Ty=0\to y^TA=0^T$ means left
        - basis: $[A|I]\to [R|E_{m\times m}]\to EA=R_{m\times n}, E_{(m-r)\times m}A=0_{(m-r)\times n}$ where top rows of E is $E_{r\times m}$ corresponding to pivot rows of $R$, bottom rows is $E_{(m-r)\times m}$ corresponding to zero rows in $R$, so each row of $E_{(m-r)\times m}$ is the basis.