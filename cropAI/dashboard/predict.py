import pickle 
import datetime
from newspaper import Article
from googlesearch import search
from urllib.parse import urlparse
from  dashboard.models import CropDetails, ExtraInfo
model = pickle.load(open('models/model.pkl', 'rb'))


def fetch_data(state,district):
    season  = get_season()
    obj = CropDetails.objects.filter(State_Name=state)
    obj = obj.filter(District_Name=district)
    kharif_crops = obj.filter(Season_Label=1)
    Rabi_crops = obj.filter(Season_Label=2)
    Whole_Year_crops = obj.filter(Season_Label=4)
    if(season == "Kharif"):
        return kharif_crops
    elif(season == "Rabi"):
        return Rabi_crops
    else:
        return Whole_Year_crops
    

def predict(crop_queryset):
    crops = []
    for i in crop_queryset.iterator():
        State_Name = i.State_Name_Label
        District_Name = i.District_Name_Label
        Season = i.Season_Label
        Area = i.Area
        Production = i.Production
        ANNUAL_RAIN = i.ANNUAL_RAIN
        KHARIF_RAIN = i.KHARIF_RAIN
        RABI_RAIN = i.RABI_RAIN
        SUMMER_RAIN = i.SUMMER_RAIN
        ANNUAL_GROUNDWATER = i.ANNUAL_GROUND_WATER
        ANNUAL_GROUNDWATER_FOR_IRRIGATION = i.ANNUAL_GROUND_WATER_FOR_IRRIGATION
        crops.append(model.predict([[State_Name,District_Name,Season,Area,Production,ANNUAL_RAIN,KHARIF_RAIN,RABI_RAIN,SUMMER_RAIN,ANNUAL_GROUNDWATER,ANNUAL_GROUNDWATER_FOR_IRRIGATION]]))

    return crops

def get_crop_names(crops):
    query_list = []
    for crop in crops:
        query_list.append(CropDetails.objects.values_list('Crop',flat=True).filter(Crop_Label=crop).distinct())
    
    crop_list = []
    for crop in query_list:
        crop_list.append(crop[0])
    
    final_list = []
    for crop in crop_list:
        if crop not in final_list:
            final_list.append(crop)
             
    return final_list

def get_info(crops_list):
    info_list = []
    for crop in crops_list:
        if not ExtraInfo.objects.filter(Crop=crop).exists():
            fert_url, pest_url, seed_url, method_url = google_search(crop)
            info_model = ExtraInfo.objects.create()
            info_model.Crop = crop
            info_model.fertilzer_url = fert_url
            info_model.pesticide_url = pest_url
            info_model.seeds_url = seed_url
            info_model.method_url = method_url
            searched_data = {
                'Crop' : crop,
                'fertilizer_url' : fert_url,
                'pesticide_url' : pest_url,
                'seeds_url' : seed_url,
                'methods_url' : method_url
            }

            info_list.append(searched_data)
        
        else:
            obj = ExtraInfo.objects.filter(Crop=crop)
            fert_url = obj.fertilizer_url
            pest_url = obj.pesticide_url
            seed_url = obj.seeds_url
            method_url = obj.method_url
            retrived_data = {
                'Crop' : crop,
                'fertilizer_url' : fert_url,
                'pesticide_url' : pest_url,
                'seeds_url' : seed_url,
                'methods_url' : method_url
            }
            info_list.append(retrived_data)
    
    return info_list
            


def google_search(crop):
    fertilizer_query = "Ideal fertilizer for " + str(crop)
    for i in search(fertilizer_query, tld='com', num=1, start=1, stop=1):
        fert_url = i
    pesticide_query = "Ideal pesticides for " +str(crop)
    for i in search(pesticide_query, tld='com', num=1, start=1, stop=1):
        pest_url = i
    seed_query = "Ideal seeds for " + str(crop)
    for i in search(seed_query, tld='com', num=1, start=1, stop=1):
        seed_url = i
    method_query = "Ideal farming practice for " + str(crop)
    for i in search(method_query, tld='com', num=1, start=1, stop=1):
        method_url = i


    return fert_url, pest_url, seed_url, method_url

def get_contact(district):
    query = "KVK in " + str(district)
    for i in search(query, tld='org', num=1, start=1, stop=1):
        kvk_url = i
    return kvk_url





def get_season():
    dt = datetime.datetime.today()
    month = dt.month
    if(month>=6 and month<=11):
        Season = 'Kharif'
    elif(month>=12 and month<=3):
        Season = 'Rabi'
    else:
        Season = 'Whole Year'
    return Season



if __name__ == "__main__":
    fetch_data('ANDAMAN AND NICOBAR ISLANDS','NICOBARS')