'''
def divide_name(nam):
    
    last_name = nam[0]
    first_name = nam[1:]
    
    print('='*12)
    print('성:\t',last_name)
    print('이름:\t',first_name)
    print('='*12)

name = input('당신의 이름은?')
divide_name(name)


n1 = int(input('첫 번째 정수는?'))
n2 = int(input('두 번째 정수는?'))

print(f'{n1}와 {n2}의 평균은 {(n1+n2) / 2}')

pi = 3.14159265

print(f'[{pi:f}]')
print(f'[{pi:.2f}]')
print(f'[{pi:^18.4f}]')
print(f'[{pi:.4g}]')


print('\'hello, {0} {2} {1}\''.format('python','script',3.6))
print('\'{0} {0} {1} {1}\''.format('python','script'))

num = input('정수를 입력하세요:')
length = len(num)
print(f'입력하신 {num}은(는) {length}자리 정수입니다')


msg = 'Python은 배우기 쉽다. Python은 강력하다.'
res = msg.replace('Python', '파이썬')
print(msg)
print(res)



def introduce(name, grage):
    first_name = name[1:]
    return f'{first_name}은(는) 내년에 {grade+1}학년입니다.'
    

name = input('이름?')
grade = int(input('학년?'))

res = introduce(name, grade)
print(res)

'''
# 6.4 연습문제
def rep_char(c, n):
    print(c*n)


# 6.5 연습문제
def draw_line_string(prompt):
    str_count = len(prompt)
    rep_char('-', str_count *2 +4)
    print(f'  {prompt}')
    rep_char('-', str_count *2 +4)

draw_line_string('안녕하세요')
draw_line_string('안녕')















