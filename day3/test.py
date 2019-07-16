from collections import defaultdict

original_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 35]
price = defaultdict(int)
for i, p in enumerate(original_price):
    price[i + 1] = p

from functools import wraps
solution={}
memo_already_computed = {}
def memo(f):
    memo_already_computed = {}
    @wraps(f)
    def _wrap(arg):
        result = None

        if arg in memo_already_computed:
            result = memo_already_computed[arg]
        else:
            result = f(arg)
            memo_already_computed[arg] = result
        return result

    return _wrap

@memo
def r(n):

    max_price,max_split = max(
        [(price[0],0)] + [(r(i)+r(n-i),i) for i in range(1,n)], key=lambda x: x[0]
    )
    solution[n] = (n-max_split,max_split)
    return max_price
pr = r(38)
print(price,pr)