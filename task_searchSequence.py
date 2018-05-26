#Програма пошуку найдовшого ланцюга з одиниць
#Виконав Лисенко Артур 26.05.2018
import random
import math

#Розкоментувати для генерації вхідних даних
#file = open("input.txt", "w")
#for i in range (100):
#  file.write(str(random.randint(0,1)))
#file.close()

#Функція пошуку ланцюга
#Ідея полягає в розбитті даних по нулях недалеко від
#центру. Дані, які мають розмірність меньшу, ніж
#довжина знайденого ланцюга - не розглядаються. Тому
#на великих даних має бути гарний результат
def searchSequence(sequence, maxCount):
  #Якщо дані мають розмір менший чи такий самий, як
  #знайдена довжина ланцюга, то їх розглядати не варто
  if len(sequence) <= maxCount:
    return maxCount
  #Розбиваємо дані навпіл та шукаємо нуль справа
  for i in range(math.ceil(len(sequence)/2), len(sequence)):
    #Нуль знайдено, розбиваємо дані зліва від нуля та
    #справа від нуля
    if sequence[i] == "0":
      #Розглядаємо лише дані, які можуть містити
      #ланцюг більший, ніж вже знайдений
      #Перевіряємо ліву частину даних
      if len(sequence[0:i]) > maxCount:
        newMaxCount = searchSequence(sequence[0:i], maxCount)
        #Якщо знайдено кращий результат - запам'ятати
        if newMaxCount > maxCount:
          maxCount = newMaxCount
      #Перевіряємо праву частину даних
      if len(sequence[i+1:]) > maxCount:
        newMaxCount = searchSequence(sequence[i+1:], maxCount)
        if newMaxCount > maxCount:
          maxCount = newMaxCount
      #Розбиття показало, що нові розміри даних менші,
      #аніж вже знайдений результат. Повертаємо, що було
      return maxCount
  #Нуль справа не знайдено, шукаємо зліва
  for i in range(0, int(len(sequence)/2)):
    #Якщо знайшли, аналогічно, як вище
    if sequence[i] == "0":
      if len(sequence[0:i]) > maxCount:
        newMaxCount = searchSequence(sequence[0:i], maxCount)
        if newMaxCount > maxCount:
          maxCount = newMaxCount
      if len(sequence[i+1:]) > maxCount:
        newMaxCount = searchSequence(sequence[i+1:], maxCount)
        if newMaxCount > maxCount:
          maxCount = newMaxCount
      return maxCount
  #Послідовність складається лише з одиниць
  return len(sequence)

file = open("INPUT.TXT", "r")
data = file.read()

file.close()

file = open("OUTPUT.TXT", "w")
file.write("Шукана довжина ланцюга: " + str(searchSequence(data, 0)))

file.close()