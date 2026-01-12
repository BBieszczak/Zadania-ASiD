def power(a, n):
    match(n):
        case 0:
            return 1
        case 1:
            return a
        case 2:
            return a*a
        case _:
            if n%2 == 0:
                return power(power(a, n/2), 2)
            else:
                return a*power(a, n-1)

def stairs(n, memo={}):
    if n in memo:
        return memo[n]
    match(n):
        case 1:
            return 1
        case 2:
            return 2
        case _:
            memo[n] = stairs(n-1, memo) + stairs(n-2, memo)
            return memo[n]

def sub_arr_max(arr):
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, arr[start:end + 1]

def longest_increasing_substring(arr):
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def coin_exchange(n, final_coins = {}):
    while n > 0:

        if n >= 25:
            n -= 25
            final_coins.append(25)

        if n >= 10 and n < 25:
            n -= 10
            final_coins.append(10)

        if n >= 5 and n < 10:
            n -= 5
            final_coins.append(5)

        if n >= 1 and n < 5:
            n -= 1
            final_coins.append(1)

    return final_coins, len(final_coins)

def edit_distance(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) < len(s2):
        s1 += '@'*(len(s2)-len(s1))

    operations = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            temp = s1[i]
            s1[i] = s2[i]
            s2[i] = temp
            operations += 1

    while s2[len(s2) - 1] == '@':
        s2 = s2[0:len(s2)-1]

    return ''.join(s1), ''.join(s2), operations

