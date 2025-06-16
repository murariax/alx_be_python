class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without accessing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Accesses class-level attribute and performs multiplication."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
