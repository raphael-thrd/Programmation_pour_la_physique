#====================================================================================
#On doit peut être pouvoir faire plus simple avec Numpy
#====================================================================================

def nombres_premiers(N):
    L = [i for i in range(2, N**2 + 1)] #liste des nombres de 0 à N²
    n = 2

    while n <= N:
        L = [x for x in L if (x == n or x%n != 0)] #on réduit la liste aux nombres qui ne sont pas des multiple de n (autre que n, car il est premier)
        
        # on cherche ici le prochain nombre dans la liste
        trouve=False
        for x in L:
            if x > n: #on prend le prochain nombre superieur à n
                n = x
                trouve=True #un nombre superieur qui n'est pas un multiple de n est trouvé
                break #on arrete la boucle
        if not trouve: #si trouve = False
            break  # aucun nouveau n trouvé, la liste n'a que des nombres premiers

    # On retourne les N² premiers nombres premiers
    return L

print(nombres_premiers(20))
