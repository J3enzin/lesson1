def discounted(price, discount):
    if discount <= 0.0:
        raise ValueError ("Скидка на товар учитываться не будет, стоимость товара: ", price)
        #print("Скидка на товар учитываться не будет, стоимость товара: ", price)
    if discount >= 100.0:
        print("Скидка не может быть больше или равна 100%")
    else:    
        price_with_discount = price - price * discount / 100 
        print (price_with_discount)
price = float(input('Введите стоимость товара: '))
if price > 0.0:
    price = price
else: 
    print('Цена не может быть меньше, либо равна нулю') 
if price > 0.0:
    discount = float(input('Введите % скидки: '))
    discounted(price, discount)
    print()
else:
    print("Вам не повезло!")