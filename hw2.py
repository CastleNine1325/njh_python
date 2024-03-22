def exchange(money):
    first_money = money
    
    m_500 = money // 500
    money %= 500
    m_100 = money // 100
    money %= 100
    m_50 = money //50
    money %= 50
    m_10 = money //10
    print('500원 동전의 개수:',m_500)
    print('100원 동전의 개수:',m_100)
    print('50원 동전의 개수:',m_50)
    print('10원 동전의 개수:',m_10)



def get_integer(prompt):
    res = int(input(prompt))
    return res

mon = get_integer('동전으로 교환하고자 하는 금액은?: ')
answer = exchange(mon)
