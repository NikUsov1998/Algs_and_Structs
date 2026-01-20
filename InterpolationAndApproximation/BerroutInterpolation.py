def create_Berrut_rational_function(x_value, y_value):
    def rational_function(x):
        divident_sum = 0
        divisor_sum = 0
        n = len(x_value)
        for k in range(n):
            x_product = 1
            for i in range(n):
                if i != k:
                    x_product *= (x - x_value[i])
            divident_sum += (-1) ** k * y_value[k]*x_product
            divisor_sum += (-1)**k*x_product
        return divident_sum/divisor_sum
    return rational_function

def test_Berrut_rational_function():
    x_values = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
    y_values = [0.0385, 0.0588, 0.1000, 0.2000, 0.5000, 1.0000, 0.5000, 0.2000, 0.1000, 0.0588, 0.0385]
    interpolation_function = create_Berrut_rational_function(x_values,y_values)
    print('\n')
    for x in x_values:
        print("x = {:.4f}\t y = {:4f}".format(x, interpolation_function(x)))
