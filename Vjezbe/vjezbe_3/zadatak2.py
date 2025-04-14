
def racunanje(N):
    broj = 5  
    for i in range(N):
        broj += 1/3  
    for i in range(N):
        broj -= 1/3  
    return broj

print(racunanje(200))
print(racunanje(2000))
print(racunanje(20000))

#Rezultat je u sva tri slučaja trebao biti 5, ali zbog nepreciznosti računala dobiju se različiti rezultati