pwd = input('비밀번호?')

while pwd != '#1234*':
    pwd = input('비밀번호?')

print('문이 열렸습니다! 어서오세요.')


# 개선된 버전

pwd = ''

while pwd != '#1234*':
    pwd = input('비밀번호?')

print('문이열렸습니다! 어서오세요.')




cnt = 0

while cnt < 5:
    cnt += 1
    print(cnt)
    

msg = 'hello'

for ch in msg:
    print(f'{ch}/',end='')



    

for i in range(0, 10, 1):
    print(i, end=' ')

print()

for i in range(0, 10):
    print(i, end=' ')

print()

for i in range(10):
    print(i, end=' ')





def do_one_set(n):
    n = 15
    for cnt in range(1, n+1):
        print(cnt, end=' ')
    print()

for s in range(3):
    do_one_set(15)



#정수를 입력받아 구구단 실행 프로그

def input_positive_number(prompt):
    n = 0
    while n<=0:
        n = int(input(prompt))
        
    return n


def display_multiplication_table(n):
    for i in range(1, 10):
        print(f'{n} x {i} = {n * i:2d}') # nd는 앞에 자릿수 n칸을 지정
        
#변경된 버전  
    i = 9
    while i <= 9:
        print(f'{n} x {i} = {n * i:2d}')
        i += 1                           # i에 1을 더해줘야 구구단이 진행


    
   
n = input_positive_number('출력할 구구단을 양의 정수로 입력하세요: ')

display_multiplication_table(n)



#break문으로 가독성 있게 구성

while True:
    pwd = input('비밀번호?')

    if pwd == '#1234*':
        break
print('문이 열렸습니다! 어서오세요')
        




#유효한 나이가 입력될 때까지 반복하여 받기로 

def input_age(prompt):
    while True:
        n = int(input(prompt))
        if 0 <= n <= 120:
            return n

def is_adult(age):
    if age >= 19:
        return True
    else:
        return False

age = input_age('나이?')

if is_adult(age):
    print('당신은 성인입니다.')
else:
    print('당신은 성인이 아닙니다.')




# 윤년 여부 판별 프로그램 반복문 설계

while True:
    
    year = int(input('윤년 여부를 확인할 연도는?'))

    def chack_year(y):
        if y % 4 == 0:          #4의 배수인 경우
            if y % 100 != 0:    #100의 배수가 아닌경우 윤년
                return '윤년'
                
            elif y % 400 ==0:   #400의 배수면 무조건 윤년 처리
                return '윤년'
        return '평년'           #모두 해당 안되면 평년    
    yun = chack_year(year)

    print(f'{year}년은 {yun}입니다.')

    one_more = input('다른 연도도 확인하겠습니까?')
    if one_more != 'Y' and one_more != 'y':
        break
    print()





#정수 피라미드 나열

def display_triangle(h):
    for i in range(1, h+1):
        display_nums(i)
        print()

def display_nums(n):
    for i in range(1, n+1):
        print(i, end='')

h = int(input('높이?'))
display_triangle(h)





# 오른쪽 정렬 별찍기

def stars(h):
    for i in range(1, h+1):
        print(' '*(h-i) + '*'*i)

h = int(input('높이?'))
stars(h)







