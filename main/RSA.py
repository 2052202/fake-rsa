import math
def FindGCF(x,y):
  if (x % y == 0):
    return y
  else:
    return FindGCF(y, x % y)
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
# Var creation
p = 0
q = 0
e = 65337
d = 0
phi_n = 0
# Funciton to check valid values
def Checker(p,q,e,phi_n, d):
  i = True
  if (p <= 1):
    print("error, please change variables")
    i = False
  if (q <= 1):
    print("error, please change variables")
    i = False
  if (e <= 1):
    print("error, please change variables")
    i = False
  if (e >= phi_n):
    print("error, please change variables")
    i = False
  if (FindGCF(p,q) != 1):
    print("error, please change variables")
    i = False
  if (FindGCF(e,q) != 1):
    print("error, please change variables")
    i = False
  if (FindGCF(e,p) != 1):
    print("error, please change variables")
    i = False
  if (FindGCF(phi_n, e) != 1):
    print("error, please change variables")
    i = False
  if ((e * d) % phi_n != 1):
    print("Modular Operatons Failed! Error")
    i = False
  return i
def SetPQ(p1,q1):
  p = p1
  q = q1
  return True
def SetE(e1):
  e = e1
  return True
def StartRSA_var():
  phi_n = (p - 1) * (q - 1)
  d = MultModInverse(e,phi_n)
  return True
def Encrypter(Plaintext):
  return pow(Plaintext,e) % n
def Decrypter(ciphertext):
  return pow(ciphertext, d) % n