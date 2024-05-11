def buy(shopping_bag):
    print('[구입]')
    item = input('상품명? ')
    if not item == '':
        item_cnt = int(input('수량은? '))
        shopping_bag[item] = item_cnt
        print(f'장바구니에 {item} {item_cnt}개가 담겼습니다.')
        print()
    else:
        return False

def show(shopping_bag):
    print(f'>>> 장바구니 보기:{shopping_bag}')

def find(shopping_bag):
    print()
    print('[검색]')
    search = input('장바구니에서 확인하고자 하는 상품은? ')

    if search not in shopping_bag:
        print(f'{search}은(는) 장바구니에 담겨있지 않습니다.')
    else:
        print(f'{search}은(는) {shopping_bag.get(search)}개 담겨 있습니다.')

shopping_bag = {}

while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)