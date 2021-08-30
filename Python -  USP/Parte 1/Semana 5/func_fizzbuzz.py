def fizzbuzz(n):
    a = "Fizz"
    b = "Buzz"
    ab = "FizzBuzz"
    div = 1
    div = n % 3
    div2 = n % 5
    if div == 0 and div2 == 0:
        return ab
    else:
        if div == 0:
            return a
        else:
            if div2 == 0:
                return b
            else:
                return n
