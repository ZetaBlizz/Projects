def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a, a)

def extendedEucledian(a,b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1,y1 = extendedEucledian(b%a,a)
    
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y    #returns gcd, prime, and y (i.e a*s =1 mod 94)

def affine(text,a,b,mod=94): 
        encryption = ""
        for inputs in text:
            encryption += chr((ord(inputs)*a + b)%mod +33)
        return encryption

def dAffine(text, a, b, mod=94):
    decryption = ""
    gcdPrime = extendedEucledian(a,mod)
    prime = gcdPrime[1]
    
    if gcdPrime[0] !=1:
        return "No prime exists"
    
    for i in text:
        p = (prime*(ord(i)-33-b))%mod
        if p < 33:
            p+= mod
        decryption += chr(p)
    return decryption

if __name__ == "__main__":
    s=str(affine("MyNameI!@!#$@^*:{}-+={}:';..,<>?!@#$%^&*()_+1234567890\{}''][;',./`<>?:|~-sJeff", 51,330))
    print(s)
    print(dAffine(s,51,330))
    print(dAffine(">p=*|&BvA&%%",93,1234))