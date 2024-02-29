words=[]
N=(input ("Введите слово"))
while N!="stop":
    words.append(N)
    N=input("Введите следующее слово")
result="".join(words)
print("Результат")
print(result)
