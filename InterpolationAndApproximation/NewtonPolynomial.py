def divided_defferences(x_values, y_values, k):
    result = 0
    for j in range(k + 1):
        mul = 1
        for i in range(k + 1):
            if i != j:
                mul *= x_values[j] - x_values[i]
        result += y_values[j]/mul
    return result

def create_Newton_polynomial(x_values, y_values):
    div_diff = []
    for i in range(1, len(x_values)):
        div_diff.append(divided_defferences(x_values, y_values, i))
    def newton_polynomial(x):
        result = y_values[0]
        for k in range(1, len(y_values)):
            mul = 1
            for j in range(k):
                mul *= (x-x_values[j])
            result += div_diff[k-1]*mul
        return result
    return newton_polynomial

def test_newton_polynomial():
    x_values = [0,2,3,5]
    y_values = [0,1,3,2]

    new_pol = create_Newton_polynomial(x_values, y_values)
    print('\n')
    for x in x_values:
        print("x = {:.4f}\t y = {:4f}".format(x, new_pol(x)))

