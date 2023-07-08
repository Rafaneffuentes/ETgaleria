#from django.conf.urls import url
from django.urls import path
from  . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   #path('base', views.base, name='base'),
   path('', views.home, name='home'),
   path('nosotros', views.nosotros, name='nosotros'),
   path('contacto', views.contacto, name='contacto'),
   path('obras', views.obras, name='obras'),
   
   # CRUD
   path('gestioncur', views.gestioncur, name='gestioncur'),
   path('nuevocur', views.nuevocur, name='nuevocur'),  
   path('editarcur/<codigo>', views.editarcur, name='editarcur'),
   path('borrarcur/<codigo>', views.borrarcurso, name='borrarcur'),    
   path('verobra/<codigo>', views.verobra, name='verobra'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
