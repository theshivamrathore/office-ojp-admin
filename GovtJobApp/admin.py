from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from GovtJobApp.models import *
# Register your models here.

class RailwayJobsAdmin(admin.ModelAdmin):
    list_display = ['company','post_name','education','total_post','location','last_date']

class LatestNotificationAdmin(admin.ModelAdmin):
    list_display = ['post_date','bank_name','post_name','qualification','advt_no','last_date']

class OthetGovtfinancialInstituteAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class UpscAdmin(admin.ModelAdmin):
    list_display = ['post_date','exam_name','qualification','advt_no','last_date']

class SscAdmin(admin.ModelAdmin):
    list_display = ['post_date','exam_name','qualification','advt_no','last_date']

class OtherAllIndiaExam_Admin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class DefenceJob_Admin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class Railway_Admin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class AndamanNicobarJobs_Admin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class ArunachalPradeshJobs_Admin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class AssamJobs_Admin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class BiharAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class ChhattishgarhAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class DelhiAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class GujratAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class HaryanaAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class HimachalAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class KarnatakaAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class keralaAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class MaharashtraAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class OdishaAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class PunjabAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class RajasthanAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class TamilNaduAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class UttarPradeshAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class WestBangalAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

class MedicalHospitalAdmin(admin.ModelAdmin):
    list_display = ['post_date','recruitment_board','post_name','qualification','advt_no','last_date']

@admin.register(RailwayJobsModel,BankModel,OthetGovtfinancialInstituteModel,UpscModel,SscModel,
                OtherAllIndiaExamModel,DefenceJobsModel,RailwayModel,AndamanNicobarJobsModel,
                ArunachalPradeshJobsModel,AssamJobsModel,BiharModel,ChhattisgarhJobsModel,DelhiJobsModel,GujratJobsModel,
                HaryanaJobsModel,HimachalPradeshJobsModel,KarnatakaModel,KeralaJobsModel,MaharashtraJobsModel,OdishaModel,PunjabJobsModel,
                RajasthanJobsModel,TamilNaduJobsModel,UttarPradeshJobsModel,WestBangalJobsModel,MedicalHospitalJobsModel)

class view(ImportExportModelAdmin):
    pass
