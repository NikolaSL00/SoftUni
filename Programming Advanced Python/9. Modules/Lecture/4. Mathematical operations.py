from mathematical_operations_logic import perform_operation

number1, operation, number2 = input().split()
print(f"{perform_operation(float(number1), float(number2), operation):.2f}")
