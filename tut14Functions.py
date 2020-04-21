def print_letters(let):
    letter_pattern = {1:"   *   ",2:" *   * ",3:"*     *",4:"*******",5:"       ",6:"*       ",7:"      *",
                      8:" *     ",9:"     * "}
    alpha_map = {'A':[1,2,4,3,3],'N':[6,8,1,9,7]}
    for pattern in alpha_map[let]:
            print(letter_pattern[pattern])


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

#print_big('B')

print_letters('A')

#################################


def no_of_prime(num):

    prime=[2]
    x=3

    if num < 2:
        return 0

    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x+=2
                break
        else:
            prime.append(x)
            x += 2

    print(prime)
    print(len(prime))


no_of_prime(100)

def no_of_prime1(num):

    prime=[2]
    x=3

    if num < 2:
        return 0

    while x <= num:
        for y in prime:
            if x%y == 0:
                x+=2
                break
        else:
            prime.append(x)
            x += 2

    print(prime)
    print(len(prime))


no_of_prime1(100)



def vol(rad):
    return 4/3 * 3.14 * rad ** 3

print(vol(2))


def ran_check(num,low,high):
    if num > low and num < high:
        print(f" {num} is in the range between {low} and {high}")
    else:
        print(" the number is not in the range")

print(ran_check(5,2,7))

def up_low(s):
    upper = 0
    lower = 0
    for letter in s:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        else:
            pass
    print("No. of Upper case characters : {}".format(upper) )
    print("No. of Lower case characters : {}".format(lower) )

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


def unique_list(lst):
    set1 = set(lst)
    return list(set1)

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


def multiply(numbers):
    m = 1
    for n in numbers:
        m = m *n
    return m


print(multiply([1,2,3,-4]))




def palindrome(s):
    return s == s[::-1]


print(palindrome('hellehl'))



import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
