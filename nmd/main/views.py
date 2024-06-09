from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import DocSorpbd ,Owner ,Autor ,SoftwareRegistrationCertificate
from django.shortcuts import render, redirect
from .forms import DocSorpbdForm 
from django.shortcuts import get_object_or_404, redirect


def test(request):
	return redirect('/a', permanent=True)

def delete_doc_sorpbd(request, pk):

	doc_sorpbd = get_object_or_404(DocSorpbd, id=pk)

	if request.method == 'POST':

		doc_sorpbd.delete()

		return redirect('/a')

	return redirect('render_doc_sorpbd')
def render_doc_sorpbd(request):
	doc_sorpbd = DocSorpbd.objects.all()
	context = {
		'docsorpbd_list': doc_sorpbd,
	}
	return render(request,"main/doc_sorpbd.html", context)

def list_SoftwareRegistrationCertificate(request):
	doc_sorpbd = SoftwareRegistrationCertificate.objects.all()
	context = {
		'add_list_SoftwareRegistrationCertificate': doc_sorpbd,
	}
	return render(request,"main/list_SoftwareRegistrationCertificate.html", context)


def get_autor(request):
	Autorr = Autor.objects.all()
	context = {
		'Autor': Autorr,
	}
	return render(request,"main/list_autor.html", context)

def create_doc_sorpbd(request):
	if request.method == 'POST':
		data = request.POST
		
		# Создаем новый объект DocSorpbd
		doc = DocSorpbd(
			registration_certificate_number=data['n_certifacete'],
			database_name=data['name_db'],
			request_number=data['number_za'],
			requestdate=data['data_za'],
			registrationdate=data['data_reg'],
		
		)
		doc.save()
		author_ids = data.getlist('autor')  # Предполагаем, что 'autor' - это список ID авторов
		doc.authors.set(author_ids)  # Используем метод set() для установки связи       
		# # Добавляем автора
		# autor = Autor.objects.create(name=data['autor'])
		# doc.authors.add(autor)
		
		# Добавляем правообладателей
		if data['individual_owners']:
			individual_owners = data['individual_owners'].split(',')
			for owner in individual_owners:
				individual_owner, _ = Owner.objects.get_or_create(id=owner.strip())
				doc.individual_owners.add(individual_owner)
		
		if data['organization_owner']:
			organization_owners = data['organization_owner'].split(',')
			for owner in organization_owners:
				organization_owner, _ = Owner.objects.get_or_create(id=owner.strip())
				doc.organization_owners.add(organization_owner)
		
		return redirect('/a', permanent=True)
	else:

		individual_owners = Owner.objects.filter(owner_types=True)
		organization_owners = Owner.objects.filter(owner_types=False)
		autor = Autor.objects.all()


		context = {
			"individual_owners":individual_owners,
			"organization_owners":organization_owners,
			"autors":autor

		}

	 

	return render(request, 'main/add_sorpbd.html',context)


def create_autor(request):
	if request.method == 'POST':
		data = request.POST
		
		# Создаем новый объект DocSorpbd
		doc = Autor(
			name=data['autor']
		
		)
		doc.save()
		return redirect('/a', permanent=True)
	
	 

	return render(request, 'main/add_create_autor.html')


def get_pravo(request):
	Ownerr = Owner.objects.all()
	context = {
		'Owner': Ownerr,
	}
	return render(request,"main/list_pravo.html", context)


def create_evm(request):
	if request.method == 'POST':
		data = request.POST
		
		# Создаем новый объект DocSorpbd
		doc = SoftwareRegistrationCertificate(
			certificate_number=data['certificate_number'],
			software_name=data['software_name'],
			request_number=data['request_number'],
			request_date=data['request_date'],
			registration_date=data['registration_date'],
		
		)
		doc.save()
		author_ids = data.getlist('authors')  # Предполагаем, что 'autor' - это список ID авторов
		doc.authors.set(author_ids)  # Используем метод set() для установки связи       
		# # Добавляем автора
		# autor = Autor.objects.create(name=data['autor'])
		# doc.authors.add(autor)
		
		# Добавляем правообладателей
		if data['individual_owners']:
			individual_owners = data['individual_owners'].split(',')
			for owner in individual_owners:
				individual_owner, _ = Owner.objects.get_or_create(id=owner.strip())
				doc.individual_owners.add(individual_owner)
		
		if 'organization_owner' in data:
			organization_owners = data['organization_owner'].split(',')
			for owner in organization_owners:
				organization_owner, _ = Owner.objects.get_or_create(id=owner.strip())
				doc.organization_owners.add(organization_owner)

		return redirect('/list_SoftwareRegistrationCertificate', permanent=True)
	else:

		individual_owners = Owner.objects.filter(owner_types=True)
		organization_owners = Owner.objects.filter(owner_types=False)
		autor = Autor.objects.all()


		context = {
			"individual_owners":individual_owners,
			"organization_owners":organization_owners,
			"authors":autor

		}

	 

	return render(request, 'main/add_evm.html',context)