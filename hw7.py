shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    else:
        item_cnt = int(input('수량은? '))
        shopping_bag[item] = item_cnt
        print(f'장바구니에 {item} {item_cnt}개가 담겼습니다.')

print(f'>>> 장바구니 보기:{shopping_bag}')
print()
print('[검색]')
ser = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{ser}은(는) {shopping_bag.get(ser)}개 담겨 있습니다.')