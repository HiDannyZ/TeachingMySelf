#Check if there exists a permutation

def permutationCheck(a, b):
    dictionary = {}
    dictionary2 = {}

    # Assuming that
    a = a.lower()
    b = b.lower()

    for i in range(len(a)):
        if a[i] in dictionary:
            dictionary[a[i]] += 1
        else:
            dictionary[a[i]] = 1
    for j in range(len(b)):
        if b[j] in dictionary2:
            dictionary2[b[j]] += 1
        else:
            dictionary2[b[j]] = 1

    for k,v in dictionary.items():
        print(k,v)

    # Differences if False
    set_1 = set(dictionary.items())
    set_2 = set(dictionary2.items())

    value = set_2 - set_1
    print("Differences from set_1 to set_2 is ",value)

    if value == set():
        return True

    #if dictionary == dictionary2:
    #    return True

    return False





if __name__ == '__main__':

    print(permutationCheck("Hello", "Olleh"))
