from django.shortcuts import render_to_response
from switch.models import Vocabulary
from switch.crawler import getDefinitionsShortcut,getExamp
# Create your views here.


def boarden(request):
	vocabs = Vocabulary.objects.all()
	definitions = [getDefinitionsShortcut(v.vocab) for v in vocabs]
	examples = [getExamp(v.vocab) for v in vocabs]
	pack = zip(vocabs,definitions,examples)
	first = vocabs[0].id
	return render_to_response('board.js',locals())