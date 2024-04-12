import exchange_money as em

rate = int(input('$1에 대한 오늘의 환율은?'))
em.set_rate(rate)

dollar = int(input('원화로 변환할 달러화 액수는?'))
print(dollar,'달러는',em.to_won(dollar),'원입니다.')

won = int(input('달러화로 변환할 원화 액수는?'))
print(won,'원은', em.to_dollar(won),'달러입니다.')

