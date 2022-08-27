import re
import math 

class Calculator(object):
    def __init__(self):
        self.operators = ["*", "+", "/", "-"]

    def _perform_operation(self, operation, num1, num2):
        if operation == "*":
            return num1 * num2
        elif operation == "+":
            return num1 + num2
        elif operation == "/":
            return num1 // num2
        elif operation == "-":
            return num1 - num2

    def _concatenate_lists(self, operands, operators):
        result = [None]*(len(operands)+len(operators))
        result[::2] = operands
        result[1::2] = operators
        return result

    def _run_calulation(self, operands, operators):
        calculation_started = False

        joined_list = self._concatenate_lists(operands, operators)
        
        for index in range(0, len(joined_list)): 
            if joined_list[index] in self.operators:
                if not calculation_started:
                    # Perform operation on operation, num1, num2
                    final_result = self._perform_operation(joined_list[index], joined_list[index-1], joined_list[index+1])
                    calculation_started = True
                else:
                    # If we've already started calculating, then we use the current running total
                    final_result = self._perform_operation(joined_list[index], final_result, joined_list[index+1])

        return final_result

class UI(Calculator):
    def __init__(self):
        Calculator.__init__(self)
        self.run()
    
    def _validate_input_contains_operand(self, user_input):
        validation = False
        for i in self.operators: 
            if i in user_input:
                validation = True
        return validation

    # The regex checker will handle if the the first and last are nums
    def _check_first_last_value_is_number(self, user_input):
        return user_input[0] not in self.operators \
                    and user_input[-1] not in self.operators

    def _check_for_error_chars_in_string(self, input_string):
        return True if re.fullmatch(r"[0-9*/-/+]", input_string) is None else False

    def _check_no_operators_next_to_eachother(self, input_string):
        operation_indices = [i for i, x in enumerate(input_string) if x in self.operators]
        value_together = False

        for index in range(len(operation_indices)):
            for sub_index in range(index + 1, len(operation_indices)):
                if math.abs(operation_indices[index] - operation_indices[sub_index]) <= 1:
                    value_together = True 

        return not value_together


    def _parse_input_string(self, input_string):
        operators_in_string = []
        operands_in_string = []
        
        input_string = input_string.replace(" ", "")
        input_string = [*input_string]

        index = 0
        
        while index < len(input_string):
            if input_string[index] not in self.operators:
                num_str = ""
                while index < len(input_string) and input_string[index] not in self.operators:
                    num_str += input_string[index] 
                    index += 1
                operands_in_string.append(int(num_str))
            else: 
                operators_in_string.append(input_string[index])
                index += 1

        return operands_in_string, operators_in_string

    def _perform_calculation(self, user_input):
        operands, operators = self._parse_input_string(user_input)
        return self._run_calulation(operands, operators)

    def _valid_input(self, user_input):
        return self._validate_input_contains_operand(user_input) \
                and self._check_first_last_value_is_number(user_input) \
                and self._check_for_error_chars_in_string(user_input)

    def _menu(self):
        print("Accepted characters - numbers, *, +, /, -")
        user_input = input("Enter a Calculation \n")
        while not self._valid_input(user_input):
            user_input = input("Enter a Calculation \n")

        result_string = self._perform_calculation(user_input)
        print(result_string)

    def run(self): 
        while True:
            self._menu()


if __name__ == "__main__":
    UI()







