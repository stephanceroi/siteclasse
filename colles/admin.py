from django.contrib import admin

# Register your models here.
from .models import creneau,colle, eleve, colleur, groupe, programme

admin.site.register(creneau)
admin.site.register(colle)
admin.site.register(eleve)
admin.site.register(colleur)
admin.site.register(groupe)
admin.site.register(programme)
