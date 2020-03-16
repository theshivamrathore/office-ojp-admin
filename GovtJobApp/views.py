from django.shortcuts import render
from GovtJobApp.models import *
# from GovtJobApp.filter import *
# Create your views here.
def index(request):
    return render(request,'index.html')

# Railway Jobs View starts #
def railwayview(request):
    railway_data = RailwayJobsModel.objects.all()
    context={'railway_data':railway_data}
    return render(request, 'govtapp/railway-jobs.html', context=context)

# Railway Jobs View Ends #

# Latest Notification #

def latestnotificationview(request):
    bank_data = BankModel.objects.all()
    othetfin_data = OthetGovtfinancialInstituteModel.objects.all()
    upsc_data = UpscModel.objects.all()
    ssc_data = SscModel.objects.all()
    othetAllIndia_data =OtherAllIndiaExamModel.objects.all()
    defence_data = DefenceJobsModel.objects.all()
    railways_data = RailwayModel.objects.all()
    andaman_nicobar_data = AndamanNicobarJobsModel.objects.all()
    arunachal_data = ArunachalPradeshJobsModel.objects.all()
    assam_data = AssamJobsModel.objects.all()
    bihar_data = BiharModel.objects.all()
    chhattisgarh_data = ChhattisgarhJobsModel.objects.all()
    delhi_data = DelhiJobsModel.objects.all()
    gujrat_data = GujratJobsModel.objects.all()
    haryana_data = HaryanaJobsModel.objects.all()
    himachal_data = HimachalPradeshJobsModel.objects.all()
    karnataka_data = KarnatakaModel.objects.all()
    kerala_data = KeralaJobsModel.objects.all()
    maharashtra_data = MaharashtraJobsModel.objects.all()
    odisha_data = OdishaModel.objects.all()
    punjab_data = PunjabJobsModel.objects.all()
    rajasthan_data = RajasthanJobsModel.objects.all()
    tamil_data = TamilNaduJobsModel.objects.all()
    uttarPradesh_data = UttarPradeshJobsModel.objects.all()
    westBangal_data = WestBangalJobsModel.objects.all()
    medical_data = MedicalHospitalJobsModel.objects.all()


    context = {'bank_data':bank_data,'othetfin_data':othetfin_data,'upsc_data':upsc_data,'ssc_data':ssc_data,
               'othetAllIndia_data':othetAllIndia_data,'defence_data':defence_data,'railways_data':railways_data,
               'andaman_nicobar_data':andaman_nicobar_data,'arunachal_data':arunachal_data,'assam_data':assam_data,'bihar_data':bihar_data,
               'chhattisgarh_data':chhattisgarh_data,'delhi_data':delhi_data,'gujrat_data':gujrat_data,'haryana_data':haryana_data,
               'himachal_data':himachal_data,'karnataka_data':karnataka_data,'kerala_data':kerala_data,'maharashtra_data':maharashtra_data,
               'odisha_data':odisha_data,'punjab_data':punjab_data,'rajasthan_data':rajasthan_data,'tamil_data':tamil_data,
               'uttarPradesh_data':uttarPradesh_data,'westBangal_data':westBangal_data,'medical_data':medical_data}

    return render(request,'govtapp/latest-notification.html',context=context)

# Latest Notification Ends #

# filter View Starts #

# def filter(request):
#     f = filter(request.GET,queryset=MedicalHospitalJobsModel.objects.all())
#     return render(request,'filter.html',{'f':f})
# # filter View ends #