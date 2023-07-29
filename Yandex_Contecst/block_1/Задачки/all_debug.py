number_of_houses = int(input())
houses_map = list(map(int, input().split()))

# index_null = [i for i, hous in enumerate(houses_map) if hous == 0]
result = []
count = 0
for i in range(len(houses_map)):
    if houses_map[i] == 0:
        count += 1
        result.append(0)
        result.reverse()
        if len(houses_map[:i, -1]) < 3:

    else:
        
        if count > 1:
            
            result.append(count)
            count += 1
                
        else:
            count += 1
            result.append(1)
