n_th_term = int(input("Enter the nth term: "))

if(n_th_term>0):
#palindrome check
    def palin(x):
        s = str(x)
        if s==s[::-1]:
            return True
        else:
            return False
#Prime cheack
    def prime(x):
        c = 0
        for i in range(1,x+1):
            if x%i==0:
             c += 1
        if c==2:
            return True
        else:
            return False
    a = 1
    flag = 0
    while(a>0):
        if palin(a)==True:
            if prime(a)==True:
                flag +=1
        if flag==n_th_term:
            break
        a += 1
    print("Your",n_th_term,"term Primepalindrome number is",a)
    
else:
    print("put the term greater than 0")