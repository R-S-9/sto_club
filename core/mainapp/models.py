import uuid

from django.db import models
from django.utils import timezone


# Функция get_or_none для Django
class MyQuerySet(models.QuerySet):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class ServiceStation(models.Model):
    """СТО"""
    sto_name = models.CharField(
        max_length=30,
        verbose_name='Название',
        help_text='Название станции тех. обслуживания'
    )

    sto_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )

    location = models.CharField(
        max_length=150,
        verbose_name='Адрес',
        help_text='Адрес станции тех. обслуживания'
    )

    location_coordinates = models.CharField(
        max_length=150,
        verbose_name='Коордиаты адреса',
        default='',
        help_text='Координаты станции тех. обслуживания'
    )

    description_sto = models.CharField(
        max_length=150,
        verbose_name='Описание СТО',
        help_text='Описание деятельности СТО'
    )

    about_sto = models.TextField(
        max_length=3000,
        verbose_name='Описание СТО',
        help_text='Полное описание деятельности СТО',
        default=''
    )

    objects = MyQuerySet.as_manager()

    def __str__(self):
        return self.sto_name

    class Meta:
        verbose_name = 'Станция тех. обслуживания'
        verbose_name_plural = 'Станции тех. обслуживаний'


class ServiceSTO(models.Model):
    """Услуги СТО"""
    name = models.CharField(
        verbose_name='Название услуги',
        max_length=120,
    )

    service_check = models.IntegerField(
        verbose_name='Стоимость услуги',
        default=0,
        help_text='Стоимость услуги в рублях'
    )

    service = models.ForeignKey(
        ServiceStation,
        verbose_name='Услуги',
        on_delete=models.CASCADE
    )

    objects = MyQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Review(models.Model):
    """Отзывы"""
    review = models.CharField(
        max_length=1000,
        verbose_name='Отзыв',
        help_text='Оставьте отзыв о СТО'
    )

    id_service_station = models.ForeignKey(
        ServiceStation,
        verbose_name='Для какого СТО',
        on_delete=models.CASCADE,
        help_text='Выберите СТО',
        related_name='reviews'
    )

    user_name = models.CharField(
        max_length=25,
        verbose_name='Имя пользователя',
        help_text='Напишите выдуманное имя для отзыва',
    )

    stars = models.IntegerField(
        verbose_name='Оценка',
        help_text='Оценка ресторана по 5 бальной шкале'
    )

    date = models.DateTimeField(
        verbose_name='Дата',
        default=timezone.now,
        help_text='Дата создается автоматически'
    )

    order = models.IntegerField(
        verbose_name='Порядковый номер',
        default=9999,
        help_text='Порядковый номер создается автоматически'
    )

    objects = MyQuerySet.as_manager()

    def _set_order(self):
        last_order = self.__class__.objects.filter(
            id_service_station=self.id_service_station
        ).order_by('order').values_list(
            'order', flat=True
        ).last()

        if last_order:
            self.order = last_order + 1
        else:
            self.order = 1

    def save(self, *args, **kwargs):
        self._set_order()
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id_service_station} {self.review}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('id_service_station', 'order')
        ordering = ('-order',)


class Image(models.Model):
    """Изображения для СТО"""
    image_sto = models.ImageField(
        verbose_name='Изображения',
        help_text='Выберите изображение',
    )

    sto_id_image = models.ForeignKey(
        ServiceStation,
        verbose_name='Изображение СТО',
        on_delete=models.CASCADE,
        default='Станция тех. обслуживания',
        help_text='Выберите СТО',
        related_name='images'
    )

    order = models.IntegerField(
        verbose_name='Порядковый номер',
        default=1,
        help_text='Порядковый номер создается автоматически'
    )

    def __str__(self):
        return str(self.image_sto)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


def adding_endings_for_improved_search(word: str) -> str or None:
    """
        Проверка на количество слов и окончания в них
    """
    if not word:
        return None

    word = word.split()

    if len(word) > 1:
        return _split_a_sentence_for_improved_search(word)

    endings = ('и', 'ы')

    if endings in word[len(word)-1:]:
        word = word[:len(word)-1]

    return ''.join(word)


def _split_a_sentence_for_improved_search(sentence):
    """
        Если слов несколько, происходит поиск слов с длинной от 2-х, и поиском
        по ним
    """
    main_word = []
    [main_word.append(content) for content in sentence if len(content) > 2]

    for service in main_word:

        sentence = ServiceStation.objects.filter(
            servicesto__name__icontains=service
        ).distinct()

        if sentence.exists():
            return service
