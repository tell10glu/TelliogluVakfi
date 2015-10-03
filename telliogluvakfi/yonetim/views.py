from django.shortcuts import render
from models import Haber,HaberKategori
# Create your views here.
def haber_ekle(request):
	if request.method == 'POST':
		#kayit etme islemi
		hbr_baslik = request.POST.get("hbr_baslik")
		haber_kategori = request.POST.get("hbr_kategori")
		hbr_onyazi = request.POST.get("hbr_onyazi")
		hbr_yazi = request.POST.get("hbr_yazi")
		hbr_video = request.POST.get("hbr_video")
		hbr = Haber(baslik=hbr_baslik,onyazi=hbr_onyazi,anayazi=hbr_yazi,vidyo_url=hbr_video)
		hbr.save()
		print(request.POST.get("hbr_resim6", ""))
		return render(request,'haber.html',{})
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

def kategori(request):
	if request.method =='POST':
		kategoriadi = request.POST.get("kat_adi")
		hbrkat = HaberKategori(kategori_adi = kategoriadi)
		hbrkat.save()
	else:
		try:
			kategori = HaberKategori.objects.get(pk=request.GET.get("hid"))
			kategori.delete()
		except Exception as e:
			kategori = None
		tum_kategoriler = HaberKategori.objects.all()
		return render(request,'kategoriler.html',{'haber_kategori':tum_kategoriler})
