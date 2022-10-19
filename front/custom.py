from sharitz.models import studentChoise, ws, ExamDate, Student


def WeeklyChoise(student):
    pass


def ExamChoise(student):
    pass


def Save(student):
    save = Student.objects.filter(student=student).first()
    if not save:
        save = Student.objects.create(student=student)
    return save
