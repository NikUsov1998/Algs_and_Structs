def divided_differences(y_values):
    result = [y_values]
    for i in range(len(y_values)-1):
        div_diff = []
        for j in range(len(result[i])-1):
            diff = result[i][j+1] - result[i][j]
            div_diff.append(diff)
        result.append(div_diff)
    return result

def create_factorial(n):
    result = []
    for i in range(n+1):
        fact = 1
        for j in range(1, i+1):
            fact *= j
        result.append(fact)
    return result

def create_Stirling_polynomial(x_values, y_values):
    div_diff = divided_differences(y_values)
    fact = create_factorial(len(y_values))

    def stirling_polynomial(x):
        mid = len(y_values)//2
        h = x_values[1]-x_values[0]
        u = (x - x_values[mid])/h
        result = y_values[mid]

        for i in range(1, mid+1):
            mul = 1
            for j in range(1, i):
                mul *= (u*u - j*j)
            result += (1/fact[2*i-1]*u*mul *
                       (div_diff[2*i-1][-(i-1)+mid]+div_diff[2*i-1][-i+mid])/2)
            result += 1/fact[2*i]*u*u*mul*(div_diff[2*i][mid - i])
        return result
    return stirling_polynomial

def test_stirling_polynomial():
    x_values = [1,2,3,4,5,6,7]
    y_values = [2,5,10,15,20,22,24]
    polynomial = create_Stirling_polynomial(x_values,y_values)

    x=1
    print('\n')
    while(x<=8):
        print("x = {:.4f}\t y = {:4f}".format(x, polynomial(x)))
        x += 0.2

    print("f(4.3) = {:.4f}".format(polynomial(4.3)))
    expected_result = 16.6025
    assert round(polynomial(4.3),4) == expected_result

