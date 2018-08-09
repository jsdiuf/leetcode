import pickle
import json

d = [1, 2, 3, 4]


def recur(arr, n):
    return arr[0] if n == 0 else arr[n] + recur(arr, n - 1)
print(recur(d, len(d) - 1))
