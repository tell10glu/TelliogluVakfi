from django.conf.urls import include, url,patterns
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.anasayfa, name='ana_sayfa'),
	url(r'^haberekle', views.haber_ekle, name='haber_ekle'),
	url(r'^haberler', views.haberler, name='haberler'),
	url(r'^resimgaleri',views.resimgaleri,name='galeri'),
	url(r'^kategoriler',views.kategori,name='kategoriler'),
)
