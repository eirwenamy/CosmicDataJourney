from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        fLength = request.POST['fLength']
        fWidth = request.POST['fWidth']
        fSize = request.POST['fSize']
        fConc = request.POST['fConc']
        fConc1 = request.POST['fConc1']
        fAsym = request.POST['fAsym']
        fM3Long = request.POST['fM3Long']
        fM3Trans = request.POST['fM3Trans']
        fAlpha = request.POST['fAlpha']
        fDist = request.POST['fDist']
        y_pred = model.predict([[float(fLength), float(fWidth), float(fSize), float(fConc), float(fConc1), float(fAsym), float(fM3Long), float(fM3Trans), float(fAlpha), float(fDist)]])
        if y_pred == 0:
            y_pred = 'hadron'
        
        else:
            y_pred = 'gamma'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')