'''Условие

Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.'''

n = int(input())
my = {}
for i in range(n):
    user_input = input()
    key, value = user_input.split(" ")
    my[key] = value
    
word = input()


    
print(my)