# PromotorFinder
A search algorithm for discovery of promotor sequences

#Ambiguity codes

#Ambiquity codes are codes that mean any of the two or any of the three nucleotides. Normally, purine (R, A or G) is complemented into pyrimidine (Y, C or T) and amino (M, C or A) is complemented into keto (K, T or G). Differently, weak (W, A or T, pairs with the two hydrogen bonds) and strong (S, G or C, pairs with three hydrogen bonds) are normally not swapped during complementation, leaving the S and W codes unchanged instead. This is logical as both a nucleotide and its complement use the same number of bonds to make a complementing pair.



Code	      Nucleotides	              Complement
A	          A	                        T
G	          G	                        C
C	          C	                        G
T	          T	                        A
U   	      U	                        A
R	          A or G, purine	          Y, pyrimidine
Y	          C or T, pyrimidine	      R, purine
S	          C or G, strong pairing	  S, unchanged
W	          A or T, weak pairing	    W, unchanged
K	          G or T, keto	            M, amino
M	          A or C, amino	            K, keto
B	          C or G or T,              not A	V, not T
V	          A or C or G,              not T	B, not A
D	          A or G or T,              not C	H, not G
H	          A or C or T,              not G	D, not C
-	          gap	                      unchanged
any other	  any or unknown	          unchanged
