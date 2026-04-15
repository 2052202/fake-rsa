# Importing 
import math


class RSA_instance:
    p,q = 0 
    e = 65337
    n = 0
    phi_n = 0
    d = 0

    

    def __init__(self, p,q):
        self.p = p
        self.q = q
        n = self.p * self.q
        self.phi_n = (p - 1) - (q - 1)

    