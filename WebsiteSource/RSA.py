""" RSA Algorithm
1. Choose secret primes p and q and compute n = pq.
2. Choose e with gcd(e, (p — l)(q - 1)) = 1.
3. Compute d with de = 1 (mod (p - l)(q — 1)).
4. Make n and e public, and keep p, q, d secret.
5. Another encrypts m^e (mod n) = c and sends c to desired party.
6.  Computig c^d (mod n) results in the decrypted message m!

p,q, and e can all be primes to simplify the process, but make sure they're all chosen at random!'
"""

def convertToNumbers(message):
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    language = {alphabet[i]:i+1 for i in range(0,len(alphabet))}
    converted = ""
    for letter in message:
        number = language[letter]
        if number < 10:
            converted += f"0{number}"
        else: 
            converted += f'{number}'
    return converted

def convertToCharacters(message):
    stringify = str(message)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    language = {i+1:alphabet[i] for i in range(0,len(alphabet))}
    converted = ""
    start = 0
    end = 2
    if len(stringify)%2 != 0:
        converted += language[int(stringify[0])]
        start +=1
        end +=1
    while start < len(stringify):
        converted += language[int(stringify[start:end])]
        start+=2
        end+=2
    return converted

def splitCheckAndSend(message,d,n): #Returns message split neccessary for mod n. Also encrypts/decrypts as the difference is just the exponent (e vs d)
    num = int(message)
    converted = []
    if num < n: return encryptDecrypt(message,d,n)
    else:
        start = 0
        end = len(str(n))-2
        new = len(str(n))-2
        while start < len(message):
            integer = int(message[start:end])
            string = str(encryptDecrypt(integer,d,n))
            converted.append(string)
            start = end
            end += new
    return converted

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def getQuotients(a,b, q=[]): #Euclidean algorithm, returns quotients for extended
    q.append(a//b)
    remainder = a-(q[-1]*b)    #r = a%b  <-- same as remainder both are fast
    if remainder == 0:
        return b
    getQuotients(b, remainder, q)
    return q

def getX(q, xs=[0,1]): #if y is needed replace [0,1] with [1,0]
        for i in range(0, len(q)-1):
            xs.append(-q[i]*xs[i+1] + xs[i])
        return xs[-1]

def xeuclideanAlgo(a,b, quotients=[]): #returns x and y s.t. ax+by = d (ideally d = 1)
    if b > a: return xeuclideanAlgo(b,a)
    if quotients != []: quotients = [] #DON'T DELETE, array doesn't reset after 1 call
    qs = getQuotients(a,b, quotients)
    x = getX(qs)
    return x  

def encryptDecrypt(a,b,n):
    squaredMod = [a]
    exponentTable = {}
    index = 1
    exponent = 2
    while exponent <= b: #saves a^2, a^4, ... up to a^b 
        result = (squaredMod[index-1]*squaredMod[index-1])%n
        #=Detects if a cycle exists, can be deleted if its faster in some different cases=
        """if result in squaredMod:
            print("cycle")
            maxIndex = index
            index = 1
            while exponent <=b:
                if index  == maxIndex:
                    index=1
                exponentTable[exponent] = index
                last = exponent-2
                last = exponent
                exponent *=2
                index +=1
            break"""
        #==============================================================
        squaredMod.append(result)
        exponentTable[exponent] = index
        index +=1
        last = exponent
        exponent *= 2
    
    b -= last
    factor = squaredMod[exponentTable[last]]
    
    while b >1: #solving a^b by getting x+y+...+z = b (x,y,...,z are stored in exponentTable)
        for key in exponentTable:
            if b >= key:
                candidate = key
            else:
                break
        b -= candidate
        factor = factor * squaredMod[exponentTable[candidate]]%n
    if b == 1: return (factor*a)%n
    if b == 0: return factor

def getD(p,q,e): #Ensures all variables are compatible and returns d
    n = p*q
    newMod = (p-1)*(q-1)
    if gcd(e,newMod) != 1:
        print("Choose another e as its gcd with (p-1)*(q-1) is not 1")
        return
    d = xeuclideanAlgo(e,newMod)
    while d < 0:
        d+= newMod
    print(f"Send e: {e} to desired party, but keep this d: {d} a secret!")
    return d
    
if __name__ == "__main__":
    print(encryptDecrypt(4,20,12))
    
    
    #Sample Data
    p = 885320963
    q = 238855417
    e = 9007
    n = p*q
    d = getD(p,q,e)
    
    exampleEncryption = convertToNumbers("MyfavoriteRpgisPhantasyStarFour")
    print(f"Converting original message {exampleEncryption}")
    
    exampleDecryption = splitCheckAndSend(exampleEncryption,e,n)
    print(f"To: {exampleDecryption}")
    
    for i in exampleDecryption:
        print(convertToCharacters(splitCheckAndSend(int(i),d,n)))
    
    l = [67359050975650272,66628823429330555,165174263993756374]
    
    for i in l:
        print(convertToCharacters(splitCheckAndSend(i,d,n)))
        print(i,d,n)