from django.db import models

# Create your models here.

# RailwayJobsModel #
class RailwayJobsModel(models.Model):
    company = models.CharField(max_length=100,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    education = models.CharField(max_length=100,blank=True)
    total_post = models.CharField(max_length=100,blank=True)
    location = models.CharField(max_length=50,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.company

# Latest NotificationModel #

class BankModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    bank_name = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.bank_name

# class BiharModel(models.Model):
#     post_date = models.CharField(max_length=100,blank=True)
#     recruitment_board = models.CharField(max_length=200,blank=True)
#     post_name = models.CharField(max_length=300,blank=True)
#     qualification = models.CharField(max_length=200,blank=True)
#     advt_no = models.CharField(max_length=100,blank=True)
#     last_date = models.CharField(max_length=100,blank=True)

class OthetGovtfinancialInstituteModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class UpscModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    exam_name = models.CharField(max_length=200,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.exam_name

class SscModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    exam_name = models.CharField(max_length=200,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.exam_name

class OtherAllIndiaExamModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class DefenceJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class RailwayModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class AndamanNicobarJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class ArunachalPradeshJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class AssamJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class BiharModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class ChhattisgarhJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class DelhiJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class GujratJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class HaryanaJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class HimachalPradeshJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class KarnatakaModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class KeralaJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class MaharashtraJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class OdishaModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class PunjabJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class RajasthanJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class TamilNaduJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class UttarPradeshJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class WestBangalJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board

class MedicalHospitalJobsModel(models.Model):
    post_date = models.CharField(max_length=100,blank=True)
    recruitment_board = models.CharField(max_length=200,blank=True)
    post_name = models.CharField(max_length=300,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    advt_no = models.CharField(max_length=100,blank=True)
    last_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.recruitment_board
