def nutrition():
    dict1 ={'Apple': 130, 'Avocado': 50, 'Banana':110, 'Cantaloupe': 50, 'Grapefruit': 50,
            'Grapes': 90, 'Honeydew Melon':50, 'Kiwifruit:': 90, 'Lemon':15, 'Lime': 20, 'Nectarine':60,
            'Orange': 80, 'Peach': 60, 'Pear': 100, 'Pineapple': 50, 'Plums': 70, 'Strawberries': 50, 
            'Cherries':100, 'Tangerine':50, 'Watermelon':80}
    while True:
        k = input('Fruit: ')
        if k in dict1:
            print('Calories: ' + str(dict1[k]))
        else:
            print('', end='')