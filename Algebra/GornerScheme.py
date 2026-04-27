def gorner_scheme(poly_coff: list[int], x: int):
    result: int = poly_coff[0]
    for i in range(len(poly_coff) - 1):
        result: int = result * x + poly_coff[i + 1]
    return result

def test_gorner_sceme():
    x: int = 2
    poly_coff: list[int] = [5,1,-3,2,5]
    print('\n', gorner_scheme(poly_coff, x))