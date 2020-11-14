from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
def index(request):
	return render(request, 'app/index.html')

def feedback(request):
	if request.method == 'POST':
		f = FeedbackForm(request.POST)
		if f.is_valid():
			f.save()
			messages.add_message(request, messages.INFO, 'Feedback Submitted')
			return redirect('feedback')

	else:
		f = FeedbackForm()
	return render(request, 'app/index.html', {'form':f})