def romano(num):
    num_r = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    romano = ''
    for i in sorted(num_r.keys(), reverse=True):
        while num >= i:
            romano += num_r[i]
            num -= i
    return romano

print(romano(12))