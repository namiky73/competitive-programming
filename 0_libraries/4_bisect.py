# binary search
from bisect import bisect_left, bisect_right

al = [-9,-7,-4,0,3,3,6,6,7,10]
# al = []
N = len(al)
b = 6
print(f'N : {N}')
print(f'al: {al}')
print(f'b : {b}')
print()

# b以下の要素の個数
cnt = bisect_right(al, b)
print(f'count ( a <= b ):  {cnt}')

# b未満の要素の個数
cnt = bisect_left(al, b)
print(f'count ( a < b ) :  {cnt}')

# b以上の要素の個数
cnt = N - bisect_left(al, b)
print(f'count ( a >= b ):  {cnt}')

# bより大きい要素の個数
cnt = N - bisect_right(al, b)
print(f'count ( a > b ) :  {cnt}')

print('--------------------')

# b以下の最大要素のindex/value
ind = bisect_right(al, b) - 1
ind = ind if 0 <= ind < N else None
val = al[ind] if ind is not None else None
print(f'max index/value ( a <= b ): {ind}/{val}')

# b未満の最大要素のindex/value
ind = bisect_left(al, b) - 1
ind = ind if 0 <= ind < N else None
val = al[ind] if ind is not None else None
print(f'max index/value ( a < b ) : {ind}/{val}')

# b以上の最小要素のindex/value
ind = bisect_left(al, b)
ind = ind if 0 <= ind < N else None
val = al[ind] if ind is not None else None
print(f'min index/value ( a >= b ): {ind}/{val}')

# bより大きい最小要素のindex/value
ind = bisect_right(al, b)
ind = ind if 0 <= ind < N else None
val = al[ind] if ind is not None else None
print(f'min index/value ( a > b ) : {ind}/{val}')


# -------- 最も近い要素 ----------
# 1. b以下の最大要素のindex/value（複数の場合は、最も右の要素）
ind1 = bisect_right(al, b) - 1
ind1 = ind1 if 0 <= ind1 < N else None        # -> 7
val1 = al[ind1] if ind1 is not None else None  # -> 6

# 2. b未満の最大要素のindex/value（複数の場合は、最も右の要素）
ind2 = bisect_left(al, b) - 1
ind2 = ind2 if 0 <= ind2 < N else None        # -> 5
val2 = al[ind2] if ind2 is not None else None # -> 3

# 3. b以上の最小要素のindex/value（複数の場合は、最も左の要素）
ind3 = bisect_left(al, b)
ind3 = ind3 if 0 <= ind3 < N else None        # -> 6
val3 = al[ind3] if ind3 is not None else None # -> 6

# 4. bより大きい最小要素のindex/value（複数の場合は、最も左の要素）
ind4 = bisect_right(al, b)
ind4 = ind4 if 0 <= ind4 < N else None        # -> 8
val4 = al[ind4] if ind4 is not None else None # -> 7

# 5. bに最も近い要素のindex/value -> 1. と 3. を組み合わせてコネコネ


# print('--------------------')


# # bに最も近い要素のindex/value
# ## 大きい側で最も近い要素
# ind_large = bisect_right(al, b)
# ind_large = ind_large if 0 <= ind_large < N else None
# val_large = al[ind_large] if ind_large is not None else None

# ## 小さい側で最も近い要素
# ind_small = ind_large - 1
# ind_small = ind_small if 0 <= ind_small < N else None
# val_smallind_small = al[ind_small] if ind_small is not None else None

# if 

# print(f'max index/value ( a <= b ): {ind}/{val}')