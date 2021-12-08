from django.contrib import admin

from movie.models import Movie,MovieLinks,Flopblog


# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieLinks)
admin.site.register(Flopblog)
