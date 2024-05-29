class calculations:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

    def factorial(self):
        return self.cal_factorial(self.b)

    def cal_factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.cal_factorial(n - 1)


if __name__ == "__main__":
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))

    numbers = calculations(a, b, c)

    print("Sum of a, b, and c:", numbers.sum())
    print("Factorial of b:", numbers.factorial())
