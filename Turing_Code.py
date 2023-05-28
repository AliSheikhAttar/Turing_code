msg = "".join((input("enter the word: ")).split(' '))

list1 = []

for i in msg:
    a = (ord(i)-96)
    list1.append(a)



p = 23
q = 5
n = 115



def GreatestCommonDivisor(a , b):
    if (a>b):
        while True:
            Remainder = a%b
            if( Remainder==0 ):
                return b
            b = a%b
    else:
        while True:
            Remainder = b%a
            if ( Remainder==0 ):
                return a
            a = b%a



while True:
    e = int(input("import e: "))
    if( ((1 < e) and ( e < n)) and (GreatestCommonDivisor(e, ((p-1)*(q-1)))==1) and (GreatestCommonDivisor(e,n)==1)):
        break

d = 0
for i in range(1,n):
    if( (i*e) % ((p-1)*(q-1))==1 ):
        d = i
        break
print("D")
print(d)
list2 = []
for i in list1:
    c = pow(i,e)%n
    list2.append(c)
print(list2)
list3 = []
for j in list2:
    m = pow(j,d)%n
    list3.append(m)

print(list3)
list_c = []
for i in range(97,123):
    list_c.append(chr(i))

list4 =[]
for k in list3:
    list4.append(list_c[k-1])

x = ""
for t in list4:
    x+=t

    
print(x)

