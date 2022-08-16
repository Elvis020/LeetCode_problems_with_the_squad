from curses.panel import new_panel


def max_profit(prices):
    # Solution 1
    # ans = 0
    # for index,element in enumerate(prices):
    #     if index+1 <len(prices):
    #         for j in prices[index+1:]:
    #             if j-element > ans:
    #                 ans = j-element
    # return ans

    # Solution 2
    # ans = 0
    # for index,element in enumerate(prices):
    #     if index+1< len(prices):
    #         max_el = max(prices[index+1:])
    #         min_el = min(prices[index+1:])
    #         new_ans = max(max_el-element,min_el-element)
    #         if new_ans>ans:
    #             ans=new_ans
    # return ans

    # Solution 3
    # ans = 0
    # for index, element in enumerate(prices):
    #     maxxy = max(prices[index:])
    #     if maxxy - element > ans:
    #         ans = maxxy - element
    # return ans

    # Solution 3 - Works
    max_prof = 0
    best_price = prices[0]
    for price in prices:
        if price < best_price:
            best_price = price
        elif best_price < price and (price - best_price) > max_prof:
            max_prof = price - best_price
    return max_prof






# TODO: Write unit test for the examples below
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))