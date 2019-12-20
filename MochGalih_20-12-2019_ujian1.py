print('----No 1----\n')
def hashtag(input_str):
    list_str = input_str.split()
    for idx in range(len(list_str)):
        new_str = list_str[idx].title()    
        list_str[idx] = new_str
    hashtag_str = '#'
    for i in list_str:
        hashtag_str += i
    if len(hashtag_str) < 2 or len(hashtag_str) > 139:
        hashtag_str = False 
    return hashtag_str

print('input: \'Hello there how are you doing\'')
print('output:', hashtag('Hello there how are you doing'), '\n')

print('input: \'  Hello  World  \'')
print('output:', hashtag('  Hello  World  '), '\n')

print('input: \'\'')
print('output:', hashtag(''), '\n')

print('\n----No 2----\n')
def create_phone_num(input_list):
    str_num = ''
    for i in input_list:
        str_num += str(i)
    part_1 = '('+str_num[:3]+')'
    part_2 = ' '+str_num[3:6]
    part_3 = '-'+str_num[6:10]
    str_res = '"'+part_1+part_2+part_3+'"'
    return str_res


print('input: [1,2,3,4,5,6,7,8,9,0]')
print('output:', create_phone_num([1,2,3,4,5,6,7,8,9,0]), '\n')

print('\n----No 3----\n')
def sort_odd_even(input_list):
    odd_or_even = []
    odd_list = []
    even_list = []
    for i in input_list:
        if i%2==0:
            odd_or_even.append('even')
            even_list.append(i)
        else:
            odd_or_even.append('odd')
            odd_list.append(i) 
    
    even_list = sorted(even_list)
    even_list = even_list[::-1]
    odd_list = sorted(odd_list)
    
    res_list = []
    for i in odd_or_even:
        if i == 'even':
            res_list.append(even_list[0])
            even_list.pop(0)
        else:
            res_list.append(odd_list[0])
            odd_list.pop(0)
    return res_list

my_list = [5,3,2,8,1,4]
print('input:', str(my_list))
print('output:', sort_odd_even(my_list), '\n')

my_list_2 = []
print('input:', str(my_list_2))
print('output:', sort_odd_even(my_list_2), '\n')

print('\n----No 4----\n')
def hollowTriangle(k):
    h = k
    print('input: ', h)    
    while k > 0:
        for item in range(h-k, h-(k-1)):
            if k == h or k == 1:
                print('_'*(k-1), end='')
                print('#'*(2*(1+item)-1), end='')
                print('_'*(k-1))
            else:
                print('_'*(k-1), end='')
                print('#',end='')
                print('_'*(2*(1+item)-3),end='')
                print('#',end='')
                print('_'*(k-1))
        k -= 1
    print()

for i in range(11):
    hollowTriangle(i)