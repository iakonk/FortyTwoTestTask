from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    """
    https://trac.42cc.co/agiloprojects/42-test-iakonk/ticket/1#comment:16
    Model represent Project main contact
    """
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField('First Name', max_length=10)
    surname = models.CharField('Surname', max_length=15)
    birth_date = models.DateField('Date of Birth', auto_now=False, auto_now_add=False)
    email = models.EmailField('Email address', max_length=255)
    phone_number = models.CharField('Contact phone number', max_length=15, validators=[phone_regex], blank=True)
    skype = models.CharField('Skype contact', max_length=25, blank=True)
    biography = models.TextField('Biography', max_length=500)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)

    class Meta:
        ordering = ['surname']
        db_table = 'contacts_list'

