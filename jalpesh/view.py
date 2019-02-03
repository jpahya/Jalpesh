from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,'home.html')
def count(request):
	data = request.GET['fulltextarea']
	x = data.split()
	y = len(x)
	a = {}
	for word in x:
		if word in a:
			a[word] += 1
		else:
			a[word] = 1
	s = sorted(a.items(), key = operator.itemgetter(1),reverse = True)
	
	return render(request, 'count.html',{'name':data, 'len':y,'z': s})