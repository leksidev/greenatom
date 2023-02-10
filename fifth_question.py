""" Напиши функцию на Python, выполняющую сравнение версий. Условия: 
Return -1 if version A is older than version B 
Return 0 if versions A and B are equivalent 
Return 1 if version A is newer than version B 
Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1. """


def compare_versions(A: str, B:str) -> int:
    A = [int(number) for number in A.split('.')]
    B = [int(number) for number in B.split('.')]

    zipped_values = zip(A, B)
    for pair in zipped_values:
        if pair[0] < pair[1]:
            return -1
        elif pair [0] > pair[-1]:
            return 1
    else:
        if len(A) == len(B):
            return 0
        else:
            return 1 if len(A) > len(B) else -1


assert compare_versions('1.10', '1.1') == 1
assert compare_versions('1.10', '1.11') == -1
assert compare_versions('1.1', '1.1') == 0
assert compare_versions('1.1', '1.1.1') == -1
