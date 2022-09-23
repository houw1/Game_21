print('Добро пожаловать в игру "21"')
import random
pl1=random.randint(6,10)
pl2=random.randint(6,10)
pl3=random.randint(6, 10)
diler=random.randint(12,21)

print('Вы взяли 2 карты и вам выпали числа: '+str(pl1),'и '+str(pl2))
print('Ваша сумма числ равна: '+str(pl1+pl2))
print('Если вы хотите взять ещё одну карту то напишите да, если хотите оставить то напишите нет')
print('НО! будьте осторожны, если сумма ваших чисел будет больше 21, то вы проиграете')
pl4=(input('Хочешь ещё 1 карту?: '))

if pl4==('да'):
    print('Вам выпало число: '+str(pl3))
    print('Ваша сумма числ равна: '+str(pl1+pl2+pl3))
    if pl1 + pl2 + pl3 > 21:
        print('ПОРАЖЕНИЕ')
        exit()
    print('У дилер сумма карт равна: ' + str(diler))
    if 21-(pl1+pl2+pl3)>21-diler:
        print('ПОРАЖЕНИЕ')
    if 21-(pl1+pl2+pl3)==21-diler:
        print('НИЧЬЯ')
    if 21-(pl1+pl2+pl3)<21-diler:
        print('ПОБЕДА')
if pl4==('нет'):
    print('Ваша сумма числ равна: '+str(pl1+pl2))
    print('У дилера сумма карт равна: ' + str(diler))
    if 21-(pl1+pl2)>21-diler:
        print('ПОРАЖЕНИЕ')
    if 21-(pl1+pl2)==21-diler:
        print('НИЧЬЯ')
    if 21-(pl1+pl2)<21-diler:
        print('ПОБЕДА')
        exit()




















































