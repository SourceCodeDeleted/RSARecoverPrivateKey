from Crypto.PublicKey import RSA 
import sys

# https://en.wikipedia.org/wiki/RSA_(cryptosystem) 
# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
# https://www.youtube.com/watch?v=sYCzu04ftaY

#STEPS for RSA key Generation are as follows:

"""
1. Get P and Q two large primes
2. Multiply these for N = (Q *P)
3. F (N) = (Q - 1, P - 1)
4. The most commonly chosen value for E is 216 + 1 = 65,537  - Although E can be between 1 and N ;
5. Public  key = (N , E)
6. D = E modinv(N)
6. Private key = (N, D)
"""
p = 154988316393020320653036051355151407978511939215065303333118050720790281509621039902362306813171654491364525172146615462925796358289684079702533944384287156955681423109824380925721061088494807065253265566553336319935946857972032405087524761980639739692544772054067780638327228568051348186901409994229480327061

q = 159150421979886097702368705687445947096337772554759349232509185573375413263307140569557424675090474817886359057672056550371749255108158694915631913260914976519178882226807486747046793726475675504341560550574465715042314546654829802143730548964648582702249500168383620529018656421037395428058982989168647896493

e =  65537



def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def build_key(p,q,e):
    n = p * q
    
    #Phi is the totient of n
    phi = (p-1) * (q-1)
    d = modinv(e, phi)
    
    e1 = d % (p-1)
    e2 = d % (q-1)
    c = modinv(q,p)


    print("First Large Prime Genearted\n ")
    print("p = %s \n" % p)
    print("Second Large Prime Genearted\n ")
    print("q = %s \n" % q)
    print("n is the multiplication of Q and P")
    print("n = %s \n" % n)
    print("Totient is generated which is (p-1) * (q-1) \n ")
    print("f = %d \n" % (long(p-1) * (q-1)))
    print("e a commonly known prime\n ")
    print("e = %s \n" % e)
    print("d Mod Inverse of e and f\n ")
    print("d = %s \n" % d)

    # The ONLY reason this is here is to export key as PEM

    key = RSA.construct((n, long(e), d, p , q))
    #print("u = %s \n" % key.u)

    private_key = key.exportKey("PEM")
    print(private_key)

build_key(p,q, e)


"""
Generate PKEY Python

def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    from Crypto.PublicKey import RSA 
    new_key = RSA.generate(2048, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    return private_key, public_key

"""
