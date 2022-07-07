import math;

should_calulate = 'Y';

while should_calulate == 'Y':
    
    x = float(input('x: '));
    operators = input('operator: ');
    y = float(input('y: '));

    if operators == '+':
        print(x + y);
    elif operators == '-':
        print(x - y);
    elif operators == '/':
        print(x / y);
    elif operators == '*':
        print(x * y);
    elif operators == '**':
        print(math.pow(x, y));
    else:
        print('invalid operator selected.');
    
    should_calulate = input('Do you want to continue? Y/N ');

print('Thanks for using the Python calculator, Goodbye.');