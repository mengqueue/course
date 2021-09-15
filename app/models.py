# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Commentfeedback(models.Model):
    ucid = models.IntegerField(db_column='UCid', primary_key=True)  # Field name made lowercase.
    cflike = models.IntegerField(db_column='CFlike', blank=True, null=True)  # Field name made lowercase.
    cfunlike = models.IntegerField(db_column='CFunlike', blank=True, null=True)  # Field name made lowercase.
    cfreport = models.IntegerField(db_column='CFreport', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commentfeedback'


class Course(models.Model):
    cid = models.AutoField(db_column='Cid', primary_key=True)  # Field name made lowercase.
    cname = models.CharField(db_column='Cname', max_length=50)  # Field name made lowercase.
    cteacher = models.CharField(db_column='Cteacher', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ccredit = models.IntegerField(db_column='Ccredit', blank=True, null=True)  # Field name made lowercase.
    ctime = models.CharField(db_column='Ctime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cbookname = models.CharField(db_column='Cbookname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cbookpicture = models.CharField(db_column='Cbookpicture', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cintroduce = models.TextField(db_column='Cintroduce', blank=True, null=True)  # Field name made lowercase.
    csid = models.IntegerField(db_column='CSid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


class Feedback(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    uid = models.IntegerField(db_column='Uid')  # Field name made lowercase.
    feedback_time = models.DateTimeField()
    feedback_picture = models.CharField(max_length=1, blank=True, null=True)
    feedback_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'feedback'


class Selectedcourse(models.Model):
    scid = models.AutoField(db_column='SCid', primary_key=True)  # Field name made lowercase.
    uid = models.IntegerField(db_column='Uid')  # Field name made lowercase.
    cid = models.IntegerField(db_column='Cid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'selectedcourse'


class User(models.Model):
    uid = models.AutoField(db_column='Uid', primary_key=True)  # Field name made lowercase.
    uname = models.CharField(db_column='Uname', max_length=50)  # Field name made lowercase.
    upicture = models.CharField(db_column='Upicture', max_length=1, blank=True, null=True)  # Field name made lowercase.
    upassword = models.CharField(db_column='Upassword', max_length=50)  # Field name made lowercase.
    umajor = models.CharField(db_column='Umajor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uage = models.IntegerField(db_column='Uage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Usercomment(models.Model):
    ucid = models.AutoField(db_column='UCid', primary_key=True)  # Field name made lowercase.
    uid = models.IntegerField(db_column='Uid')  # Field name made lowercase.
    cid = models.IntegerField(db_column='Cid')  # Field name made lowercase.
    uctime = models.DateTimeField(db_column='UCtime')  # Field name made lowercase.
    ucpicture = models.CharField(db_column='UCpicture', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uctext = models.TextField(db_column='UCtext')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usercomment'


class Usercontact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    uid = models.IntegerField(db_column='Uid')  # Field name made lowercase.
    cid = models.IntegerField(db_column='Cid')  # Field name made lowercase.
    contact_time = models.DateTimeField()
    contact_picture = models.CharField(max_length=1, blank=True, null=True)
    contact_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'usercontact'
