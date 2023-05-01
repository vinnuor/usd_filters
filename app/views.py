from django.shortcuts import render

# Create your views here.
def udf(request):

    d={'ud':'mallesh'}
    return render(request,'udf.html',d)