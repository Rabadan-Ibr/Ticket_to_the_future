from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    director = models.ForeignKey(
        'Employee',
        verbose_name='Директор',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='director_department',
    )

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=50,
        db_index=True,
    )
    patronymic = models.CharField(verbose_name='Отчество', max_length=50)
    photo = models.ImageField(
        verbose_name='Фото',
        blank=True,
        null=True,
        upload_to='company/employee/',
    )
    appointment = models.CharField(verbose_name='Должность', max_length=50)
    salary = models.DecimalField(
        verbose_name='Оклад',
        max_digits=9,
        decimal_places=3,
    )
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    department = models.ForeignKey(
        'Department',
        verbose_name='Департамент',
        on_delete=models.PROTECT,
        related_name='employees',
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = 'surname', 'name'


    def delete(self, using=None, keep_parents=False):
        self.photo.delete()
        return super().delete(using, keep_parents)

    def remove_on_update_photo(self):
        try:
            obj = self.__class__.objects.get(id=self.id)
        except self.__class__.DoesNotExist:
            return
        if obj.photo and self.photo and obj.photo != self.photo:
            obj.photo.delete()

    def save(self, *args, **kwargs):
        self.remove_on_update_photo()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
