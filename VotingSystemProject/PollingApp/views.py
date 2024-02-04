from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .models import Choice ,Question
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'PollingApp/index.html', context)

def details(request,pk):
    try: 
        question= Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse("Question Does not Exit")
    return render(request, 'PollingApp/details.html',{'question':question})

 
def results(request, pk):
    question = get_object_or_404(Question, pk = pk)
    print(question.choice_set.all,"yyyyyyyyyyyyyyyyyyyy")
    return render(request, 'PollingApp/result.html', {'question': question})


def vote(request, pk):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk = pk)
    # print(question,"kkkkkkkkkkkkkkkkkk")
    print(question,"lllllllllllllllllll")
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
        print(selected_choice,"kkkkkkkkkkkkkk")

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'PollingApp/details.html', {'question': question})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))
        
        return redirect('results',pk=question.id)
        
             
    
