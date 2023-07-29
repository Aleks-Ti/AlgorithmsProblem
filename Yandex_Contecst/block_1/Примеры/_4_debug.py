n_second = int(input())
arr = list(map(int, input().split()))
k_step = int(input())

result = []
current_sum = sum(arr[0:k_step])
result.append(current_sum / k_step)
for i in range(0, n_second - k_step):
    current_sum -= arr[i]
    current_sum += arr[i + k_step]
    current_avg = current_sum / k_step
    result.append(current_avg)

print(', '.join(result))
