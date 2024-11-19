# types of matrices (L3, L4)

## diagonal matrix
- diagonal multiply diagonal: $A_{n\times n}=\mathrm{diag}(a_1,\dots ,a_n),B_{n\times n}=\mathrm{diag}(b_1,\dots ,b_n)\to AB=BA=\mathrm{diag}(a_1b_1,\dots ,a_nb_n)$
- diagonal multiply normal:
    - $A_{m\times n}=(a_1,\dots ,a_n), D_{n\times n}=\mathrm{diag}(d_1,\dots ,d_n)\to AD=(d_1a_1,\dots ,d_na_n)$
    - $A_{m\times n}=(a_1^T,\dots ,a_m^T)^T, D_{m\times m}=\mathrm{diag}(d_1,\dots ,d_m)\to DA=(d_1a_1^T,\dots ,d_ma_m^T)^T$

## inverse matrix
- $AA^{-1}=I=A^{-1}A$
    - $A^{-1}$ is unique
        > proof: $AB=I=AC\to B=IB=CAB=CI=C$
    - condition: $A_{n\times n}B_{n\times n}=I\Rightarrow \exists A^{-1},B^{-1},B=A^{-1},A=B^{-1}$, no need another condition $BA=I$
        > proof: $\det AB=\det A\det B=\det I=1\to \det A,\det B\ne 0\to \exists A^{-1}=B,B^{-1}=A$
- not invertable:
    - A is not square matrix ($A^{-1}$ in left and right is different)
    - row / column vectors of A is linear combination of other row / column vectors, w.r.t. exists non-zero vector $x$ make $Ax=0$
        > proof: assume A is invertable, thus $Ax=0\to A^{-1}Ax=Ix=0$, opposite to requirement $x\neq 0$
    - column / row of A is parallel (the same meaning to above one), thus A cannot be transformed to identity matrix.
- get inverse matrix:
    - Gauss-Jordan elimination: argumented matrix (增广矩阵) combine total identity matrix $[A|I]\to [EA|EI]=[I|E]\to E=A^{-1}$
- get $Ax=b\to x=A^{-1}B$: $[A|B]\to [I|A^{-1}B]$
- properities:
    - $\text{diag}(d_i\dots)^{-1}=\text{diag}(d_i^{-1}\dots)$
    - $(\lambda A)^{-1}=\frac{1}{\lambda}A^{-1}$
    - $(AB)^{-1}=B^{-1}A^{-1}$
        > proof: $AB(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=I$
    - $(A^T)^{-1}=(A^{-1})^T$
        > proof: $(A^{-1})^{T}A^T=(AA^{-1})^T=I$

## transpose matrix
- exchange row and column, along diagonal
- $(AB)^T=B^T A^T$
    > proof: compare element-wise.
- $(ABC)^T=C^TB^TA^T$
    > proof: $(ABC)^T=((AB)C)^T=C^T(AB)^T=C^TB^TA^T$, using mathematical induction.

## symmetric matrix
- $A=A^T$
- $A^TA$ is symmetric matrix. (also for $AA^T$)
    > proof: $(A^TA)^T=A^T(A^T)^T=A^TA$
- $A^T=A, B^T=B, AB=BA \to (AB)^T=AB$ otherwise $AB\ne BA\to (AB)^T\ne AB$
    > proof: $(AB)^T=B^TA^T=BA =\text{or}\ne AB$
- antisymmetric: $A^T=-A$. example: rotation matrix.

## block matrix
- common: diagonal, triangle, column / row vectors.
- matrix multiplication: make $AB$ that #column of $A$ equals to #row of $B$.
- transpose should transpose block and element at the same time.

## permutation matrix
- definition: a square matrix for each row and column only exists one 1, others are zero.
    - it is elementary matrix for $E_{ij}$.
    - from row / column exchange from identity matrix.
- application: exchange row / column
- property:
    - $P^{-1}=P^T$, orthogonal matrix
    - $n$ order matrices set has $n!$ permutation matrices as a group($A_n^n$)
    - Multiplication of any two matrices from this group still in this group (closure).

## relationships of matrices
- equivalence, contract and similarity have properties:
    1. reflexivity: $A\cong A$
    2. symmetry: $A\cong B\Rightarrow B\cong A$
    3. transitivity: $A\cong B,B\cong C\Rightarrow A\cong C$
- equivalence: $A_{m\times n}\cong B_{m\times n}\Leftrightarrow A=PBQ$ where $P$ and $Q$ is invertable.
    - $\Leftrightarrow R(A)=R(B)$
        > proof: equivalent means $B$ can be transformed to $A$ through elementary row and column operation $\to A,B$ has same reduced echelon form.
- contract: $A=P^TBP$ where $A,B$ are square matrices, and $P$ is invertable.
    - requires rank and positive / negative inertia index are equivalent.
- similarity: $A_{n\times n}\sim B_{n\times n}\Leftrightarrow A=P^{-1}BP$ where $A,B$ are square matrices, and $P$ is invertable.
    > prove transitivity: $B=P^{-1}AP\to C=Q^{-1}BQ=Q^{-1}P^{-1}APQ=(PQ)^{-1}A(PQ)$
    - $\Rightarrow A\cong B\Rightarrow R(A)=R(B)$
    - $\Rightarrow \lambda _{A}=\lambda _{B}$ ($\Rightarrow \det A=\det B, \text{tr}(A)=\text{tr}(B)$)
        > proof: $\det (\lambda I-B)=\det (\lambda I-P^{-1}AP)=\det (P^{-1}(\lambda I-A)P)=\det P^{-1}\det (\lambda I-A)\det P=\det (\lambda I-A)$
