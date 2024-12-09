########################################################################################### Exercise 1
### Replacing values in the cache using Least Recently Used (LRU) replacement strategy
access_sequence = [1,3,5,4,2,4,3,2,1,0,5,3,5,0,4,3,5,4,3,2,1,3,4,5]

cache = []
c = 0
total = 0
miss_value = 0
for i in range(len(access_sequence)):
    if len(cache) < 4:
        cache.append(access_sequence[i])
        miss_value = miss_value + 1
    elif cache[0] != access_sequence[i] and cache[1] != access_sequence[i] and cache[2] != access_sequence[i] and cache[3] != access_sequence[i]:
        cache[c] = access_sequence[i]
        miss_value = miss_value + 1
        if c < 3:
            c = c + 1
        else:
            c = 0

    total = total + 1

### Calculate hit-miss %
hit_rate = (1 - miss_value/24) * 100
print("Hit Rate =", hit_rate, "%")








