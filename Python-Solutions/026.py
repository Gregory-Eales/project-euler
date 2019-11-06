



def get_recurring_digits(n):

    div = 1.00/n
    div = str('%.16f' % div)
    div = div.split('.')[1]
    for i in range(1, int(len(div)/2)):
            if div[0:i] == div[i:2*i]:
                return div[0:i]
    return False

def get_longest_repeat(n):
    longest = 0
    length = 0
    for i in range(1, n):
        d = get_recurring_digits(i)
        if d != False:
            if len(d) > length:
                longest = i
                length = len(d)
    return longest, length
    
print(get_longest_repeat(100))
