def sandwich(bread,*ingredients):
    bread = bread
    other = [*ingredients]
    print('Kanapka:',f'\nRodzaj pieczywa: {bread}', f'\nDodatki: {ingredients}')

sandwich('żytnie', 'masło', 'ser', 'szynka', 'sałata', 'pomidor')