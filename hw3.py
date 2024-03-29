def get_fixed_price():
    discount_rate = int(input('할인율은?'))
    

    discounted_a = int(input('A 상품의 할인된 가격은?'))
    discounted_b = int(input('B 상품의 할인된 가격은?'))

    price_a = discounted_a / (1 - discount_rate/100)
    price_b = discounted_b / (1 - discount_rate/100)
    
    print('A 상품의 정가는',price_a,'원')
    print('B 상품의 정가는',price_b,'원')

get_fixed_price()
