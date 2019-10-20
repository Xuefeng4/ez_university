from django.db import models
from django.urls import reverse
# Create your models here.
class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.semester_name

    def get_absolute_url(self):
        return reverse('courseinfo_semester_detail_urlpattern', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('courseinfo_semester_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('courseinfo_semester_delete_urlpattern', kwargs={'pk': self.pk})


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=20)
    course_name = models.CharField(max_length=225)
    def __str__(self):
        return '%s - %s' % (self.course_number,self.course_name)

    class Meta:
        ordering = ['course_number', 'course_name']
        unique_together = (('course_number','course_name'),)

    def get_absolute_url(self):
        return reverse('courseinfo_course_detail_urlpattern',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('courseinfo_course_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('courseinfo_course_delete_urlpattern', kwargs={'pk': self.pk})

class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    def __str__(self):
        return '%s, %s' % (self.last_name,self.first_name)
    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = (('last_name', 'first_name'),)

    def get_absolute_url(self):
        return reverse('courseinfo_instructor_detail_urlpattern',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('courseinfo_instructor_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('courseinfo_instructor_delete_urlpattern', kwargs={'pk': self.pk})

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nick_name = models.CharField(max_length=45,blank=True,default='')

    def __str__(self):
        result = ''
        if self.nick_name == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.nick_name)
        return result

    class Meta:
        ordering = ['last_name','first_name', 'nick_name']
        unique_together = (('last_name','first_name','nick_name'),)

    def get_absolute_url(self):
        return reverse('courseinfo_student_detail_urlpattern',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('courseinfo_student_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('courseinfo_student_delete_urlpattern', kwargs={'pk': self.pk})


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester,related_name='sections',on_delete=models.PROTECT)
    course = models.ForeignKey(Course,related_name='sections',on_delete=models.PROTECT)
    instructor = models.ForeignKey(Instructor,related_name='sections',on_delete=models.PROTECT)

    def __str__(self):
        return '%s -%s (%s)' % (self.course.course_name, self.section_name, self.semester.semester_name)

    def get_absolute_url(self):
        return reverse('courseinfo_section_detail_urlpattern',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('courseinfo_section_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('courseinfo_section_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['course__course_number', 'section_name', 'semester__semester_name']
        unique_together = (('semester', 'course', 'instructor'),)


class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, related_name='registrations', on_delete=models.PROTECT)
    section = models.ForeignKey(Section, related_name='registrations', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.section, self.student)
        print(self.section)
        #call the sting function of the section and student modal

    class Meta:
        ordering = ['section', 'student']
        unique_together = (('section', 'student'),)

    def get_absolute_url(self):
        return reverse('courseinfo_registration_detail_urlpattern',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('courseinfo_registration_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('courseinfo_registration_delete_urlpattern', kwargs={'pk': self.pk})



