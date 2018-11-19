#!/usr/bin/python3.6

import copy

s = [31,56,156,167,38,240,174,248]

def f(A):
    for i in range(0,50):
        A = runde(A)
    return A

#calculates one round
def runde(A):
	return delta(gamma(beta(alpha(A))))

#calculates the alpha function
def alpha(A):
	Ap = copy.deepcopy(A)
	A[0] = copy.deepcopy(A[1])
	A[1] = copy.deepcopy(Ap[0])
	return A

#calculates the beta function
def beta(A):
	A[0][0] ^= A[1][3]
	A[0][1] ^= A[1][2]
	A[0][2] ^= A[1][1]
	A[0][3] ^= A[1][0]

	return A
#calculates the gamme function
def gamma(A):
	Ap = copy.deepcopy(A)
	A[0][3] = A[0][0]
	A[1][2] = A[0][1]
	A[1][3] = A[0][2]
	A[1][1] = A[0][3]
	A[0][1] = Ap[1][0]
	A[1][0] = Ap[1][1]
	A[0][2] = Ap[1][2]
	A[0][0] = Ap[1][3]
	return A
#calculates the delta function
def delta(A):
    A[0][0] = rotateL(A[0][0])
    A[1][0] = rotateL(A[1][0])
    A[0][2] = rotateL(A[0][2])
    A[1][2] = rotateL(A[1][2])
        
    A[0][1] = rotateR(A[0][1])
    A[1][1] = rotateR(A[1][1])
    A[0][3] = rotateR(A[0][3])
    A[1][3] = rotateR(A[1][3])       

    return A

#rotates left by one bit (There is sure also an easier way :P)
def rotateL(a):
    #firstBit = 0
    if a>>7 == 1:
        a = a<<1
        a |= 1
    else:
        a = a<<1
        a &= 0b11111110
    return (a % 256)

#rotates right by one bit (There is sure also an easier way :P)
def rotateR(a):
    #lastBit = 0
    if a % 2 ==1:
        a = a>>1
        a |= 0b10000000
    else:
        a = a>>1
        a &= 0b01111111
        
    return a

#implements the absorbing function which is dependent on the length of the input
def absorbing(w,P):
    for i in range(0,len(P)):
        for j in range(0,4):
            w[0][j] =  int(w[0][j]) ^ int(P[i][j],16)
        w = f(w)
    return w

#calculates the hash itself
def cictroHash(toHash):
        first = []
        second = []
        count = 0
        #split the state s into two lists:
        for e in s:
                if count < 4:
                    first.append(e)
                else:
                    second.append(e)
                count +=1
        w = []
        w.append(first)
        w.append(second)
        	

        hashBytes = []
        tmp = []
        count = 1
              
        #Do the split into 4 bytes
        for char in toHash:
            tmp.append(hex(ord((char))))
            if count % 4 == 0:
                hashBytes.append(tmp)
                tmp = []
            count += 1

        #do the padding
        paddingLen = 4-len(tmp)
        
        if paddingLen < 4:
            for i in range(0,paddingLen):
                tmp.append(hex(0))
            hashBytes.append(tmp)
        

        w = absorbing(w, hashBytes)

        hashVal = 0
        for i in range(0,4):
        	hashVal |= w[0][i]<<(3-i)*8
        return hashVal


def main():
        toHash = str(input())
        print(hex(cictroHash(toHash)))


if __name__ == "__main__":
	main()
