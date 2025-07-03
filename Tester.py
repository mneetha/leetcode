class Tester:
    def __init__(self, solution_instance, method_name):
        self.solution_instance = solution_instance
        self.method = getattr(solution_instance, method_name)

    def run_test(self, test_input, expected_output):
        output = self.method(test_input)

        print(f"Input: {test_input}")
        print(f"Expected output: {expected_output}")
        print(f"Actual output: {output}")

        if output == expected_output:
            print("Test Passed\n")
        else:
            print("Test Failed\n")