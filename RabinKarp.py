import time
#impliment basic formula for RM.
def RabinKarp(string,searchedString,Q):
    
    M=len(searchedString)
    N=len(string)
    R=10
    RM=(R**(M-1)) % Q#Formula to obtain the number sets' hash after i+M
    p=0#hash for searchedstring
    t=0#hash for string

    for i in range(0,M):#to obtain the initial hashes
        print("[p] i: "+str(i)+" char: "+searchedString[i]+" ascii: "+str(ord(searchedString[i])))
        p=( R * p + ord(searchedString[i]))%Q 
        print("p: "+str(p))
        print("[t] i: "+str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        t=( R * t + ord(string[i]))%Q
        print("t: "+str(t))

    print("\np: "+str(p))
    print("t: "+str(t)+"\n")    
    if p==t:#if the first M chars(up until the [M-1]th index) are equal
        return "found at index 0"

    for i in range(M,N):#start searching from the Mth element
        print("[t] i: "+str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        t = t - ord(string[i-M])*RM#to obtain hash values that do not conntain the leading digit of the past number
        t = ( R * t + ord(string[i])) % Q
        print("t: "+str(t))
        if p==t:
            return "found at index "+ str(i-M+1)

givenString = "algorithmisfun"
searchedString = "ib"
Q=997#divide by modulo to prevent very large hash values
start =time.time()
index=RabinKarp(givenString,searchedString,Q)
end=time.time()
print("\n"+str(index)+" with the running time of "+ str(end-start))