def higher_version(v1, v2):
    return list(map(int, v1.split('.'))) > list(map(int, v2.split('.'))) 

if __name__ == '__main__':
    v1 = '1.10.2'
    v2 = '1.2.10'
    print(higher_version(v1, v2))
