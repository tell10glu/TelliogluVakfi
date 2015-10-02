from django.shortcuts import render
from models import Haber,HaberKategori
# Create your views here.
def haber_ekle(request):
	if request.method == 'POST':
		#kayit etme islemi
		print(request.POST.get("hbr_resim6", ""))
	else:
		try:
			haber = Haber.objects.get(pk=request.GET.get("hid"))
		except Exception as e:
			haber = None

		haber_kategori = HaberKategori.objects.all()
	    	return render(request, 'haberekle.html', {'haber_kategori':haber_kategori,'hbr':haber})


def anasayfa(request):
	return render(request,'anasayfa.html',{})

def haberler(request):
	haberler = Haber.objects.all()
	return render(request,'haberler.html',{'haberler':haberler})

def resimgaleri(request):
	return render(request,'resimgaleri.html',{})

