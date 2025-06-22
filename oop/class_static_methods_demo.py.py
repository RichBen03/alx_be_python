# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method: does not use self or cls
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method: accesses class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
