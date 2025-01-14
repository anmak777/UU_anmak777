data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(d_struct):
    sum_total = 0

    for elm in d_struct:
        if isinstance(elm, (int, float)):
            sum_total += elm
            #print('int', sum_total)
        elif isinstance(elm, str):
            sum_total += len(elm)
            #print('str', sum_total)
        elif isinstance(elm, (list, tuple, set)):
            sum_total += calculate_structure_sum(elm)
        elif isinstance(elm, dict):
            for items_ in elm.items():
                sum_total += calculate_structure_sum(items_)

    return sum_total

print(calculate_structure_sum(data_structure))
