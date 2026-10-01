# from django.shortcuts import render
# from django.http import HttpResponse 
# from django.template import loader
# import joblib
# # Create your views here.
# def home(request):
#     res = render(request,"home.html")
#     return res

# def result(request):
#     scaler = joblib.load('scalermodel.pkl')
#     mlmodel = joblib.load('glassmodel.pkl')
#     lis = []
#     lis.append(request.GET['RI'])
#     lis.append(request.GET['Na'])
#     lis.append(request.GET['Mg'])
#     lis.append(request.GET['Al'])
#     lis.append(request.GET['Si'])
#     lis.append(request.GET['K'])
#     lis.append(request.GET['Ca'])
#     lis.append(request.GET['Ba'])
#     lis.append(request.GET['Fe'])
#     scaled_input = scaler.transform([lis])
#     ans = mlmodel.predict(scaled_input)[0]

#     res = render(request,'result.html',
#     {
#         'ans': ans, 'lis':lis
#     })
#     return res

from django.shortcuts import render
import joblib

def home(request):
    res = render(request, "home.html")
    return res

def result(request):
    scaler = joblib.load('scalermodel.pkl')
    mlmodel = joblib.load('glassmodel.pkl')
    lis = []
    lis.append(float(request.GET['RI']))
    lis.append(float(request.GET['Na']))
    lis.append(float(request.GET['Mg']))
    lis.append(float(request.GET['Al']))
    lis.append(float(request.GET['Si']))
    lis.append(float(request.GET['K']))
    lis.append(float(request.GET['Ca']))
    lis.append(float(request.GET['Ba']))
    lis.append(float(request.GET['Fe']))
    scaled_input = scaler.transform([lis])
    ans = mlmodel.predict(scaled_input)[0]
    if ans == 1:
        glass_type = "Building Windows Float Processed"
    elif ans == 2:
        glass_type = "Building Windows Non-Float Processed"
    elif ans == 3:
        glass_type = "Vehicle Windows Float Processed"
    elif ans == 4:
        glass_type = "Vehicle Windows Non-Float Processed"
    elif ans == 5:
        glass_type = "Containers"
    elif ans == 6:
        glass_type = "Tableware"
    elif ans == 7:
        glass_type = "Headlamps"
    else:
        glass_type = "Unknown Glass Type"
    res = render(request,"result.html",
    {
            "ans": ans,
            "glass_type": glass_type,
            "lis": lis
        }
    )

    return res