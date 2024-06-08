from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import DocSorpbd ,Owner ,Autor
from django.shortcuts import render, redirect
from .forms import DocSorpbdForm 
def test(request):
	return redirect('/a', permanent=True)
def render_doc_sorpbd(request):
	doc_sorpbd = DocSorpbd.objects.all()
	context = {
		'docsorpbd_list': doc_sorpbd,
	}
	return render(request,"main/doc_sorpbd.html", context)



def create_doc_sorpbd(request):
	if request.method == 'POST':
		data = request.POST
		
		# Создаем новый объект DocSorpbd
		doc = DocSorpbd(
			registration_certificate_number=data['n_certifacete'],
			database_name=data['name_db'],
			request_number=data['number_za'],
			requestdate=data['data_za'],
			registrationdate=data['data_reg']
		)
		doc.save()
		
		# Добавляем автора
		autor = Autor.objects.create(name=data['autor'])
		doc.authors.add(autor)
		
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

		context = {
			"individual_owners":individual_owners,
			"organization_owners":organization_owners
		}

	 

	return render(request, 'main/add_sorpbd.html',context)

