
def get_next_solution(coefficients_a: list[list[float]], coefficients_b: list[float], solution: list[float]) -> list[float]:
    n:int = len(solution)
    next_solution: list[float] = [0 for i in range(n)]
    for i in range(n):
        other_element_sum: float = sum([coefficients_a[i][j] * solution[j] for j in range(n) if j != i])
        next_solution[i] = 1 / coefficients_a[i][i] * (coefficients_b[i] - other_element_sum)
    return next_solution

def get_error(coefficients_a: list[list[float]], coefficients_b: list[float], solution: list[float]) -> list[float]:
    n: int = len(solution)
    err: list[float] = [0 for i in range(n)]
    for i in range(n):
        err[i] = coefficients_b[i] - sum([coefficients_a[i][j]*solution[j] for j in range(n)])
        err[i] = abs(err[i])
    return err

def find_solution(coefficients_a: list[list[float]], coefficients_b: list[float], solution: list[float], err: float) -> list[float]:
    next_solution:list[float] = get_next_solution(coefficients_a, coefficients_b, solution)
    while max(get_error(coefficients_a,coefficients_b,next_solution)) > err:
        next_solution = get_next_solution(coefficients_a, coefficients_b, next_solution)
    return next_solution

def test_find_root():
    coefficients_a: list[list[int]] = [[9,-4,1,2],[2,15,3,-2],[1,2,8,-4],[1,1,1,6]]
    coefficients_b: list[int] = [-3,55,27,0]
    solution_start: list[int] = [0,0,0,0]
    err: float = 0.000001

    solution = find_solution(coefficients_a, coefficients_b, solution_start, err)
    print("\n")
    for i, res in enumerate(solution):
        print("x",i,"=",res)