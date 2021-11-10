import time

ef_cache = {}


def expensive_function(num):
    if num in ef_cache:
        return ef_cache[num]
    print(f"computing {num}...")
    time.sleep(5)
    result = num * num
    ef_cache[num] = result
    return result


result = expensive_function(5)
print(result)
result = expensive_function(10)
print(result)
result = expensive_function(5)
print(result)
result = expensive_function(10)
print(result)
