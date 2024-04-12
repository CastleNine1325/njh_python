### 윤년 구분 프로그램

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



### 사용자로부터 연도와 월을 입력받아 그 달의 끝날이 며칠인지 출력하는 프로그램


def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False

def month_days(y, m):
    if m==4 or m==6 or m==9 or m==11:
        return 30
    elif m==2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    else:
        return 31

year = int(input('연도?'))
month = int(input('월?'))
ndays = month_days(year, month)

print(f'{year}년 {month}월은 {ndays}일까지 있습니다.')



### 나이를 입력받아 성인여부 판별, 유효하지 않은 나이 값 오류처리

def input_age(prompt):
    n = int(input(prompt))
    if 0 <= n <= 120:
        return n
    else:
        return -1

def is_adult(age):
    if age >= 19:
        return True
    else:
        return False
    
age = input_age('나이?')


if age >= 0:
    if is_adult(age):
        print('당신은 성인입니다.')
    else:
        print('당신은 성인이 아닙니다.')
else:
    print('오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')



### 한 문자를 입력받아 문자의 종류 판별하는 프로그램

def find_char_type(ch):
    if '0' <= ch <= '9':
        return '숫자'

    elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        return '알파벳'

    elif ch == ' ':
        return '공백'

    else:
        return '기타'
    

m = input('한 문자 입력')
res = find_char_type(m)
print(f'{res}문자를 입력했습니다.')








