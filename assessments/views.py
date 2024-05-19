from django.shortcuts import render
from . models import Assessment

def all_assessments(request):
    all_assess = Assessment.objects.all().order_by('-created_at')
    context =  {
        'assessments': all_assess,
    }
    return render(request, 'assesments/assessments_list.html', context)
