#from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .apps import DeepLearningAppConfig 
import numpy as np 

import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import InputForm

import json
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#@api_view(['POST'])
#@api_view(['GET'])
@csrf_exempt

def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_data = data.get('selected_text', '')
            
            preprocessed_data = preprocess(input_data)

            prediction = DeepLearningAppConfig.model.predict(preprocessed_data)

            result = postprocess(prediction)

            #return render(request, 'deep_learning_app/output.html', {'text': result})
            return JsonResponse({'status': 'success', 'message': f'Received: {result}'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def preprocess(input_data):

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(input_data)
    sequences = tokenizer.texts_to_sequences([input_data])
    padded_sequences = pad_sequences(sequences, maxlen=20)
    
    return padded_sequences
def postprocess(prediction):

    return prediction[0][0] * 100



