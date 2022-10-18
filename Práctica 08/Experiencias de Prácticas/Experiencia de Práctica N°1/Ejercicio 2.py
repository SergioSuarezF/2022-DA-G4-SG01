def es_primo(n):
 if(n!=0):
        for i in range(2,n):
            if (n%i) == 0:
              return False
        return True

num = 1
while(num!=0):
    num = int(input("Ingrese un numero: "))
    print(es_primo(num))