# Importing 
import math


class RSA_instance:
    p,q = 0 
    e = 65337
    n = 0
    phi_n = 0
    d = 0

    def MultModInverse(a,n):
        t1 =  0
        t2 = 0
        t3 = 1
        a1 = a
        n1 = n
        r = 5
        q = 0
        # Inital Step
        while True:
            r = n1 % a1
            q = math.floor(n1/a1)
            t1 = t2
            t2 = t3
            t3 = t1 - q * t2
            n1 = a1
            a1 = r
                if (r == 0):
                    return t2 % n
    

    def __init__(self, p,q):
        self.p = p
        self.q = q
        n = self.p * self.q
        self.phi_n = (p - 1) * (q - 1)
        self.d = self.MultModInverse(e,phi_n)
    def Encrypter(self, Plaintext):
        return pow(Plaintext,self.e) % self.n
    def Decrypter(self, ciphertext):
        return pow(ciphertext, self.d) % self.n


def Encrypter(e,n,text):
    return pow(text,e) % n
def Decrypter(d,n,text):
    return pow(text,d) % n