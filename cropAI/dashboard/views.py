import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from ipstack import GeoLookup
from .models import CropDetails
from .forms import InputForm, TestForm
from dashboard.predict import fetch_data, predict, get_crop_names, get_info, get_contact
# Create your views here.

def index(request):
    return render(request, 'dashboard/landingpage.html')

def input(request):

    geo_lookup = GeoLookup("a67cb87cb66935510e58445f4625d05a")

    location = geo_lookup.get_own_location()
    print(location)

    args = {
        'region' : location['region_name'],
        'city' : location['city'],
        'lat' : location['latitude'],
        'long' : location['longitude'],
        'map_access_token' : 'pk.eyJ1Ijoic2Fua2V0NzczOCIsImEiOiJja2dmNzJpbGwwenJxMnFvNzcweGczaHk5In0.XWljmmU6UQINBGd1juYJww'
    }

    form = InputForm()
    args['form'] = form

    if request.POST:
        State_Name = request.GET['State_Name']
        District_Name = request.GET['District_Name']
        print(State_Name)
        print(District_Name)

    return render(request, 'dashboard/input.html', args)

def output(request):
    if request.method == "POST":
        print(1)
        print(request.POST)
        form = InputForm(request.POST)
        state_name = form['State_Name'].value()
        district_name = form['District_Name'].value()
        data = fetch_data(state_name,district_name)
        print(data)
        crop_list = predict(data)
        crops = get_crop_names(crop_list)
        
        data_list = get_info(crops)
        print(data_list[0]['Crop'])
       
        args = {
                'State_Name' : state_name,
                'District_Name' : district_name,
                'crops' : crops,
                'crop_list' : data_list
            }
    return render(request, 'dashboard/output.html',args)

def contact(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        district_name = form['District_Name'].value()
        kvk_url = get_contact(district_name)
        return render(request, 'dashboard/contact.html', {'kvk_url':kvk_url})
    
    return render(request, 'dashboard/contact.html')

@permission_required('admin.can_add_log_entry')
def data_upload(request):
    if request.method == "GET":
        return render(request, 'dashboard/data_upload.html')
    
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = CropDetails.objects.update_or_create(
            State_Name_Label = column[0],
            State_Name = column[1],
            District_Name_Label = column[2],
            District_Name = column[3],
            Season_Label = column[4],
            Season = column[5],
            Crop_Label = column[6],
            Crop = column[7],
            Area = column[8],
            Production = column[9],
            ANNUAL_RAIN = column[10],
            KHARIF_RAIN = column[11],
            RABI_RAIN = column[12],
            SUMMER_RAIN = column[13],
            ANNUAL_GROUND_WATER = column[14],
            ANNUAL_GROUND_WATER_FOR_IRRIGATION = column[15]
        )

    return render(request,  'dashboard/data_upload.html')
        



    