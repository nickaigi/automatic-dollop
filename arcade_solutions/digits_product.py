def digits_product(number):
    if product > 1:
        for i in range(2, number):
            if product % i == 0:
                # number is not prime
                pass
                break
        else:
            # number is prime
            return -1
