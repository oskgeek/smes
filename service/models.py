from django.db import models

class Staff(models.Model):
    i_staff = models.AutoField(primary_key=True)
    staff_username = models.CharField(
        max_length=128, verbose_name='Username')
    staff_password = models.CharField(
        max_length=128, verbose_name='Password')
   
        
    class Meta:
            db_table = 'staff'
            
    def __unicode__(self):
        '''
        Return Name as title
        '''
        return str(self.staff_username).title()
         
            
class PatientReport(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    EMERGENCY_TYPE_CHOICES = (('ha', 'Heart Attack'), ('as', 'Asthma'), 
        ('ac', 'Accident'), ('tr', 'Trauma'), ('po', 'Poisonous'),
        ('bl', 'Bleeding'), ('ch', 'Choke'), ('bt', 'Bitten'))
    i_patient_report = models.AutoField(primary_key=True)
    reported_by = models.ForeignKey(Staff)
    patient_name = models.CharField(max_length=128, verbose_name='Username')
    ic = models.CharField(max_length=128, verbose_name='Identity')
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name='Gender')
    emergency_type = models.CharField(max_length=2, choices=EMERGENCY_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)

        
    class Meta:
            db_table = 'patient_report'


    def __unicode__(self):
        '''
        Return Name as title
        '''
        return str(self.patient_name).title()
