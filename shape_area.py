cache = {}

def shapeArea(n):
    if n <= 1:
        return 1
    if n not in cache:
        cache[n] = shapeArea(n-1) + 4 * (n-1)
    return cache[n] 

if __name__ == '__main__':
    shapeArea(5)
