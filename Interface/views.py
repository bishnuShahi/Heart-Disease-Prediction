from django.shortcuts import render
from django.http import HttpResponseBadRequest
import pandas as pd
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import StandardScaler
import joblib

model = joblib.load('svm_model.sav')
lambdas = np.load('lambda_values.npz')

def index(request):
    return render(request, 'index.html')

def predict(request):

    if request.method == 'POST':

        try:
            cp = int(request.POST.get('cp'))
            restecg = int(request.POST.get('restecg'))
            thal = int(request.POST.get('thal'))

            input_data = {
                'age' : [int(request.POST.get('age'))],
                'sex' : [int(request.POST.get('sex'))],
                'trestbps' : [int(request.POST.get('trestbps'))],
                'chol' : [int(request.POST.get('chol'))],
                'fbs' : [int(request.POST.get('fbs'))],
                'thalach' : [int(request.POST.get('thalach'))],
                'exang' : [int(request.POST.get('exang'))],
                'oldpeak' : [float(request.POST.get('oldpeak')) + 0.001],
                'slope' : [int(request.POST.get('slope'))],
                'ca' : [int(request.POST.get('ca'))],
                'cp_1' : [1 if cp == 1 else 0],
                'cp_2' : [1 if cp == 2 else 0],
                'cp_3' : [1 if cp == 3 else 0],
                'restecg_1' : [1 if restecg == 1 else 0],
                'restecg_2' : [1 if restecg == 2 else 0],
                'thal_1' : [1 if thal == 1 else 0],
                'thal_2' : [1 if thal == 2 else 0],
                'thal_3' : [1 if thal == 3 else 0]
            }

            data = pd.DataFrame(input_data)

            for col, lambda_val in lambdas.items():
                data[col] = boxcox(data[col], lmbda=lambda_val)

            output = model.predict(data)
            output = output.tolist()[0]

            print("Output received:", output)

            return render(request, 'index.html', {'output' : output})

                
        except TypeError as e:
            return render(request, 'index.html', {'error': True})
    return HttpResponseBadRequest("Something unexpected occurred! Please reload the page.")


