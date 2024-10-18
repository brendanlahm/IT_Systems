#####################################################################

# Replacing values in the cache by querying an access sequence
access_sequence = [1,3,5,4,2,4,3,2,1,0,5,3,5,0,4,3,5,4,3,2,1,3,4,5]

cache = []
a = 0
for i in range(len(access_sequence)):
    if len(cache) < 4:
        cache.append(access_sequence[i])
    else:
        cache[0] = access_sequence[a]
        break
    a = a + 1










