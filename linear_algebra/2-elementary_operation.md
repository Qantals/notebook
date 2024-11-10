# elementary operation (L2, L4)

## Gaussian elimination
- pivot: the first non-zero element of each row
    - invertable: pivot doesn't contain zero, has solution
- elementary row operations (elementary matrix):
    1. $E_{ij}$ exchange rows $i,j$ : make the pivot for each row exists.
    2. $E_{i}(c)$ multiply line $i$ with $c$ times to make the pivot be one.
    3. $E_{ij}(c)$ multiply row $i$ with $c$ times and add to row $j$ to make all elements below the pivot in the same column be zero.
    - elementary matrix (must be invertable matrix) can be obtained by doing elementary operations on a identity matrix.
    - multiply left operates row, and multiply right operates column
    - $E^{-1}$ means inverse elementary operation (1-3: $E_{ij},E_{i}(\frac{1}{c}),E_{ij}(-c)$).
    - all invertable matrices are equivalent, using elementary matrix left and right multiply it.
- result: get upper triangular matrix $U_{N\times N}$, which has $N$ pivot (unreduced row echelon form).
- computing resource: assume $A_{100\times 100}$, need $\sum_{k=1}^{100}k^2$ times element-wise addition / multiplication (first row is multiplication, others are additions)
    - estimation using calculus: $\int_{1}^{100} x^2\mathrm{d}x$

## LU decomposition
- $EA=U$, thus $A=E^{-1}U=LU$, $L$ is lower triangular matrix
- $L=E^{-1}=E_1^{-1}\dots E_n^{-1}$ is inverse transformation of getting $U$. The order is reverse (eliminate columns from left to right $\to$ right to left) so no need to concern new added elements in the left column, below the diagonals.
    > proof: property of $(AB)^{-1}=B^{-1}A^{-1}$, thus these coefficients are preserved and independent.
- more common expression: $PA=LU$ where $P$ is permutation matrix that exchanges rows.
