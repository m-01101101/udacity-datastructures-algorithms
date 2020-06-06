def smallest_positive(in_list: list) -> int:
    # input = list(sorted(in_list))
    # if max(input, default=0) < 0 or len(input) < 1:
    #     return None
    # else:
    #     for i in input:
    #         if i > 0:
    #             return i
    
    # refactor
    return min([i for i in in_list if i > 0], default=None)
