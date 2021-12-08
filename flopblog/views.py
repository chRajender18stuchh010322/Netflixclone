from django.shortcuts import redirect, render

from movie.models import Flopblog as Flops

# Create your views here.



def Flopblog(request):
    Flop = Flops.objects.all()
    return render(request, 'flopblog/flop.html', {'Flop': Flop})



def create(r):

    if r.method == "POST":
        Fp = Flops()
        Fp.movie_title = r.POST.get('movietitle')
        Fp.movie_pros = r.POST.get('moviepros')
        Fp.movie_cons = r.POST.get('moviecons')
        Fp.overall_review = r.POST.get('overallreview')
        Fp.rating_by_ten = r.POST.get('rating')
        Fp.date = r.POST.get('date')
        # Fp.user = r.user
        Fp.save()
        return redirect('flop/')
    else:
        return render(r,'flopblog/create.html')

        






       
      