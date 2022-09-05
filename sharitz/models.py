from django.contrib.auth.models import User
from django.db import models


# class Student(models.Model):
#     student = models.ForeignKey(User, null=True,
#                                 on_delete=models.CASCADE,
#                                 related_name='students')


class WeeklySchedule(models.Model):
    day0 = models.IntegerField(blank=True, null=True)  # Saturday: 0 , ... , Friday: 6
    day1 = models.IntegerField(blank=True, null=True)
    startTime = models.FloatField(blank=True, null=True)
    endTime = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.day0} & {self.day1} : {self.startTime}'


class ExamDate(models.Model):
    date = models.DateField()
    startTime = models.FloatField(blank=True, null=True)
    endTime = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.date} : {self.startTime}'


class course(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                blank=True)

    weeklySchedule = models.ForeignKey(WeeklySchedule, null=True,
                                       on_delete=models.CASCADE,
                                       related_name='backWeek')

    examDate = models.ForeignKey(ExamDate, null=True,
                                 on_delete=models.CASCADE,
                                 related_name='backExam')

    title = models.CharField(blank=True, null=True, max_length=256)
    college = models.CharField(blank=True, null=True, max_length=256)
    professor = models.CharField(blank=True, null=True, max_length=256)
    group = models.IntegerField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class studentChoise(models.Model):
    student = models.ForeignKey(User, null=True,
                                on_delete=models.CASCADE,
                                related_name='choise')
    title = models.CharField(blank=True, null=True, max_length=256)
    code = models.IntegerField(blank=True, null=True)
    professor = models.CharField(blank=True, null=True, max_length=256)
    weeklySchedule = models.ForeignKey(WeeklySchedule, null=True,
                                       on_delete=models.CASCADE,
                                       related_name='frontWeek')
    examDate = models.ForeignKey(ExamDate, null=True,
                                 on_delete=models.CASCADE,
                                 related_name='frontExam')
    college = models.CharField(blank=True, null=True, max_length=256)
    group = models.IntegerField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} picked by {self.student}'

