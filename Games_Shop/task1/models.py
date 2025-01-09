from django.db import models


# Create your models here.

class Buyer(models.Model):  # модель представл. покупателя
    name = models.CharField(max_length=100)  # имя покупателя (username аккаунта)
    balance = models.DecimalField(max_digits=100, decimal_places=3)  # баланс
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name


class Game(models.Model):  # модель представл. игру
    title = models.CharField(max_length=100)  # назв. игры
    cost = models.DecimalField(max_digits=100, decimal_places=3)  # цена
    size = models.DecimalField(max_digits=100, decimal_places=3)  # размер файлов игры
    description = models.TextField()  # описание
    age_limited = models.BooleanField(default=False)  # ограничение 18+
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title

'''
Домашнее задание по теме "QuerySet 
запросы в базу данных"
'''
'''-1- При помощи QuerySet запросов необходимо создать 3 записи Buyer'''
# python manage.py shell
# from task1.models import Buyer
# Buyer.objects.create(name = 'Max', balance = '3000', age = '25')
# Buyer.objects.create(name = 'Dima', balance = '2500', age = '39')
# Buyer.objects.create(name = 'Boris', balance = '500', age = '15') # только 1 Buyer <18
'''-2- При помощи QuerySet запросов необходимо создать 3 записи Game'''
# from task1.models import Game
# Game.objects.create(title = 'Need for speed', cost = '200', size = '4.5', description = 'The life of a racer',
# age_limited = '1')
# Game.objects.create(title= 'FIFA 2024', cost = '300', size = '5.7', description = 'All about football',
# age_limited = '0') # только 1 Game без огранич.возраста
# Game.objects.create(title= 'DOOM', cost = '500', size = '10.2', description = 'Blood and death', age_limited = '1')
#
'''-3- вызываем обе таблицы для связи всех объектов с полем buyer у записей Game'''
# from task1.models import *
'''-4- созд.переменные под каждого покупателя'''
# first_buyer = Buyer.objects.get(name= 'Max')
# second_buyer = Buyer.objects.get(name= 'Dima')
# third_buyer = Buyer.objects.get(name= 'Boris')
'''используем метод set(objects), который принимает коллекцию объектов'''
# Game.objects.get(id=1).buyer.set((first_buyer, second_buyer))

# Game.objects.get(id=2).buyer.set((first_buyer, third_buyer))

# Game.objects.get(id=3).buyer.set((first_buyer, second_buyer))
