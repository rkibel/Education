The "secret formula" encrypts an integer in the sense that it scrambles it into another number that is not parseable unless the encryption technique is known. Strictly speaking, it takes an integer m, calculates m^7, and returns the modulus of the first two arguments (x,y) multiplied by one another. Interestingly, removing after applying the secret formula of an integer m will return m mod xy (in the case when xy=33, this is not necessarily true with other values of xy) which explains why the array 1 2 3 4 5 6 7 8 9 10 remains the same after applying and removing the formula. This is helpful because to decrypt the integer (remove the "secret formula") x and y must be known (so that we know what we take the modulus of), so unless you have the "key" to obtaining the original integer you cannot determine it.

(i)
u = [3, 5, 1]
t = [7, 3, 15]
c = secret_formula_apply(u) = [9, 14, 1]
f = secret_formula_apply(t) = [28, 9, 27]
u*t = [21, 15, 15]
c*f = [252, 126, 27]
secret_formula_remove(c*f) = [21, 15, 15]

yes, u[i]*t[i] = secret_formula_remove(c[i]*f[i]) clearly holds for all entries in both arrays

(ii)
u = [3, 5, 1]
t = [7, 3, 15]
c = secret_formula_apply(u) = [9, 14, 1]
f = secret_formula_apply(t) = [28, 9, 27]
u+t = [10, 8, 16]
c+f = [37, 23, 28]
secret_formula_remove(c+f) = [31, 23, 8]

No, u[i]+t[i] ≠ secret_formula_remove(c[i]+f[i]), it does not hold for all entries in both arrays
