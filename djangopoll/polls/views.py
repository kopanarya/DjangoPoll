from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    """ template = loader.get_template('polls/index.html')
        output = ', '.join([q.question_text for q in latest_question_list])
        return HttpResponse(template.render(context,request))
    """
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
   
  

def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question':question}
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    
    
    """
    question = get_object_or_404(Question,pk=question_id)
    context = {'question':question}
    return render(request, 'polls/detail.html',context)
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)