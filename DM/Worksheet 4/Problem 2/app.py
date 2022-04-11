def hamming_distance(X,Y):
    count = 0
    for i in range(len(X)):
        if X[i] != Y[i]:
            count += 1
    return count

def jacardian_distance(X,Y):
    return len(set(X).intersection(set(Y)))/len(set(X).union(set(Y)))

print(f"Hamming Distance\t: {hamming_distance('0101010001', '0100011000')}")
print(f"Jacardian Similarity\t: {jacardian_distance('0101010001', '0100011000')} ")
