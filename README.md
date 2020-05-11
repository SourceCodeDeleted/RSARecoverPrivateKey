# RSARecoverPrivateKey
RSA private keys can be recovered if you know the two Primes (technically only one is needed) that were used for generation. 


You need to know P and Q seeds (At least one of them really) to begin the recovery process. 

To use:
Open the file and paste in your seeds in the P and Q variables and python2 run it. 

```
python2 ./decryptRSA.py
```

Additional:
This can be easily converted into use in **python 3** by changing long casts to int. 
