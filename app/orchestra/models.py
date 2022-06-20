from django.db import models
from common.models import Base

# TODO [ ] extract class from one file and move to multiple files


class Concert(Base):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "연주회"

    def __str__(self):
        return f"{self.name}"


class Instrument(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "악기"

    def __str__(self):
        return f"{self.name}"


class User(Base):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, unique=True)
    univ = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "가입자"

    def __str__(self):
        return f"{self.name}"


class Applicant(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    motive = models.TextField()
    career = models.TextField()
    etc = models.TextField(blank=True)
    is_activate = models.BooleanField()
    is_pass = models.BooleanField()
    is_leave = models.BooleanField()

    class Meta:
        verbose_name_plural = "지원자"

    def __str__(self):
        return f"{self.user.name}"


class ApplicationForm(Base):
    name = models.CharField(max_length=50)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    instruments = models.ManyToManyField(Instrument)
    agreement = models.TextField()

    class Meta:
        verbose_name_plural = "지원서 양식"

    def __str__(self):
        return f"{self.concert.name}_{self.name}"
