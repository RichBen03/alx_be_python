# class_static_methods_demo.py

class Calculator:
    operation_count = 0  # class variable to track the number of operations

    def __init__(self, value=0):
        self.value = value

    @staticmethod
    def add(x, y):
        """Static method: performs addition and returns the result."""
        return x + y

    @classmethod
    def increment_operation_count(cls):
        """Class method: modifies class-level data."""
        cls.operation_count += 1
        return cls.operation_count

# Demonstration
if __name__ == "__main__":
    # Using static method without creating an instance
    result = Calculator.add(10, 5)
    print(f"Addition Result (using static method): {result}")

    # Using class method to increment operation count
    print("Operation count after 1st operation:", Calculator.increment_operation_count())
    print("Operation count after 2nd operation:", Calculator.increment_operation_count())

    # Showing that we don't need an instance for either
    calc = Calculator()
    print("Static method via instance (also valid):", calc.add(7, 3))
    print("Operation count after 3rd operation:", calc.increment_operation_count())
