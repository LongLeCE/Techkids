def k_mer_count(dna, k):
    count = {}
    for i in range(len(dna)-k+1):
        x = (dna[i:k+i])
        if x not in count:
            count[x] = 0
        count[x] += 1
    print(count)


k_mer_count(input("DNA string: "), int(input("k: ")))
