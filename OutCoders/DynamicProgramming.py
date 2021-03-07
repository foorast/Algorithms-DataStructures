"""
Find the number of lattice paths from 0,0 to points m,n

Example: 2 x 2
Result: 6

input: integer N (size of lattice)
output: integer (number of unique paths)

left: y increase by 1
right: x increase by 1
                                         x, y
                                         0,0
                        /                                   \
                    0, 1                                    1, 0
                /       \                                 /       \
            0, 2        1, 1                            1, 1        2, 0
        /       \       /   \                          /    \       /       \
       base    1,2     1,2   2, 1                    1,2    2,1    2,1        base
                2,2    2,2    2,2                   2,2     2,2    2,2


create empty dictionary for cache
recursive helper function with variables i and j
    create variable key set it to x_y
    base case - if key is in cache
        return value at key in cache

    base case - if i is greater than m or j is greater than n
        return 0

    if i equals 2 and j equals 2
        return 1

    recursive case - cache[key] equals (helper i plus 1 and j) + (helper i and j plus 1)

    return key of cache

return helper function i equals 0 and j equals 0
"""


def lattice_path_memoization(m, n):
    cache = {}

    def helper(x, y):
        key = f"{x}_{y}"
        if key in cache:
            return cache[key]

        if x > m or y > n:
            return 0

        if x == m and y == n:
            return 1

        cache[key] = helper(x + 1, y) + helper(x, y + 1)
        return cache[key]

    return helper(0, 0)


def lattice_path_tabulation(m, n):
    my_list = [1 for i in range(n + 1)]

    for i in range(m):
        for j in range(1, len(my_list)):
            my_list[j] = my_list[j - 1] + my_list[j]

    return my_list[len(my_list) - 1]


"""
Find the number of combinations of coins to add up to the target number from a pool of coins. 
1 + 4 and 4 + 1 are the same same with other duplicate combinations
Example: target = 5, coins = [1, 2, 4]
Result: 1 + 1 + 1 + 1 + 1
        1 + 4
        2 + 2 + 1
        1 + 1 + 1 + 2
        return 4
        
"""


def coin_sum_memoization(coins, num):
    cache = {}

    def helper(target, current_coin):
        key = f"{target}_{current_coin}"
        if key in cache:
            return cache[key]
        if target < 0:
            return 0
        if current_coin == -1 and target != 0:
            return 0
        if current_coin == -1 and target == 0:
            return 1

        cache[key] = helper(target - coins[current_coin], current_coin) + helper(target, current_coin - 1)
        return cache[key]

    return helper(num, len(coins) - 1)


def coin_sum_tabulation(coins, num):
    my_list = [1, 0, 0, 0, 0, 0]

    for coin in range(len(coins)):
        for target in range(num + 1):
            if target - coins[coin] >= 0:
                my_list[target] += my_list[target - coins[coin]]

    return my_list[len(my_list) - 1]


if __name__ == "__main__":
    print(coin_sum_memoization([1, 2, 4], 5))
