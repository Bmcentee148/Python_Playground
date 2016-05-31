from bm_math.basic_ops import add

def add_all(nums) :
    result = 0
    for num in nums :
        result = add.add(result, num)
        print result
    return result