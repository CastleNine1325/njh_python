def read_single_digit(n):
    if n == 0: return '영 '
    elif n == 1: return '일 '
    elif n == 2: return '이 '
    elif n == 3: return '삼 '
    elif n == 4: return '사 '
    elif n == 5: return '오 '
    elif n == 6: return '육 '
    elif n == 7: return '칠 '
    elif n == 8: return '팔 '
    elif n == 9: return '구 '

def read_number(num):
    if num < 10:
        return read_single_digit(num)       #한 자리 수는 바로 한글로 변환

    elif num < 100:
        n10 = num // 10                     #십의 자리 수 추출
        han10 = read_single_digit(n10)      #십의 자리 수 한글로 변환
        
        num = num % 10                      #일의 자리 수만 남김
        han1 = read_single_digit(num)

        return han10 + han1                 #한글 변환 str을 붙여서 리턴

    elif num < 1000:

        n100 = num // 100                   #백의 자리 수 추출
        han100 = read_single_digit(n100)    #백의 자리 수 한글 변환
        
        num = num % 100
        n10 = num // 10
        han10 = read_single_digit(n10)
        
        num = num % 10
        han1 = read_single_digit(num)
        
        return han100 + han10 + han1        #한글 변환 모두 호출


numbers = int(input('세 자리 정수 입력: '))
han = read_number(numbers)
print(f'{han}')
