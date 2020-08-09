from django.db import models

# Create your models here.

class AnimalType(models.Model):
    type = models.CharField(max_length=256, verbose_name="Вид животного")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'

class Animal(models.Model):
    YES = "да"
    NO = "нет"
    MALE = "мальчик"
    FEMALE = "девочка"
    

    YES_NO_CHOISES = (
    (YES, 'да'),
    (NO, 'нет'),
    )

    SEX_CHOISES = (
    (MALE, "мальчик"),
    (FEMALE, "девочка"),
    )

    animal_type = models.ForeignKey("AnimalType",  on_delete=models.CASCADE, verbose_name='Вид животного')
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.CharField(max_length=100, verbose_name="Порода")
    sex = models.CharField(max_length=10, choices=SEX_CHOISES, default=MALE, verbose_name="Пол")
    age = models.SmallIntegerField(verbose_name="Возраст")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    photo = models.ImageField(upload_to='photo', blank=True)
    description = models.TextField(blank=True)
    castrated = models.CharField(max_length=3, choices=YES_NO_CHOISES, default=NO, verbose_name="Катрирован/старилизована")
    vaccinated = models.CharField(max_length=3, choices=YES_NO_CHOISES, default=NO, verbose_name="Прививки")

    
    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return self.name