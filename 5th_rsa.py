
p = 17
q = 19
n = p * q
phi_n = (p-1) * (q-1)

def gcd(a,b): #유클리드 호제법 
    while b!=0:
        a,b=b, a%b
    return a

e=2 # phi_n과의 최대공약수가 1인 e 값 구하기 
while e<phi_n and gcd(e,phi_n)!=1:
    e+=1
    
d = 0
mod = 0
while True:
    d += 1
    mod = (e * d) % phi_n #%는 나머지 연산. mod를 의미 
    if mod == 1:
        break

#Encryption
#C=P^e mod n 

plain="Hello Digital Information Security Technology"
plain_list= [ord(x) for x in plain] #for x in plain:
                                    #  plain_list.append(ord(x))

cipher=[] #배열
for i in plain_list:
    x= (i**e) % n #**는 제곱을 의미
    cipher.append(int(x)) #cipher에 넣어주기 

#Decryption
#P=C^d mod n

decryted=[]
for i in cipher:
    x= (i**d) % n
    decryted.append(int(x))
    
print('Plain text',plain_list) #평문
print('Cipher text',cipher) #암호문
print('Decryted text',decryted) #해독문 

print([chr(x)for x in decryted])
decryted_text= ''.join([chr(x) for x in decryted]) #chr은 숫자를 아스키코드로 바꿔주는 함수  #join은 문자 하나하나를 붙여서 이어진 문자열로 바꿔주는 method 
print(decryted_text)
