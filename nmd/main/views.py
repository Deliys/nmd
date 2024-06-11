from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import DocSorpbd ,Owner ,Autor ,SoftwareRegistrationCertificate
from django.shortcuts import render, redirect
from .forms import DocSorpbdForm 
from django.shortcuts import get_object_or_404, redirect
from .models import User
import json


def login_or_no(request):#проверка на логин
	user_data = json.loads(request.COOKIES.get('user_data', '{}'))
	print(user_data)
	if ("id" in user_data):
		return(True)
	return(False)

def login_who(request):#кто залогинин
	user_data = json.loads(request.COOKIES.get('user_data', '{}'))
	print(user_data)
	return user_data

def type_user(email):return None # заготовка под раздение полномочий


def main_page(request):
	return redirect('/a', permanent=True)
#профиль пользователя
def user_profile(request):
	return redirect("/")
#обработка удалений

def delete_doc_sorpbd(request, pk):
	doc_sorpbd = get_object_or_404(DocSorpbd, id=pk)
	if request.method == 'POST':
		doc_sorpbd.delete()
		return redirect('/a')
	return redirect('render_doc_sorpbd')
def delete_doc_soft(request, pk):
	SoftwareRegistrationCertificatea = get_object_or_404(SoftwareRegistrationCertificate, id=pk)
	if request.method == 'POST':
		SoftwareRegistrationCertificatea.delete()
		return redirect('/list_SoftwareRegistrationCertificate')
	return redirect('render_doc_sorpbd')
#отрисовка докуметов
def render_doc_sorpbd(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать

	doc_sorpbd = DocSorpbd.objects.all()
	context = {
		'docsorpbd_list': doc_sorpbd,
		"user_name":login_who(request)['email']
	}
	return render(request,"main/doc_sorpbd.html", context)

def list_SoftwareRegistrationCertificate(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать

	doc_sorpbd = SoftwareRegistrationCertificate.objects.all()
	context = {
		'add_list_SoftwareRegistrationCertificate': doc_sorpbd,
		"user_name":login_who(request)['email']
	}
	return render(request,"main/list_SoftwareRegistrationCertificate.html", context)


def get_autor(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать

	Autorr = Autor.objects.all()
	context = {
		'Autor': Autorr,
		"user_name":login_who(request)['email']
	}
	return render(request,"main/list_autor.html", context)
def get_pravo(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать


	Ownerr = Owner.objects.all()
	context = {
		'Owner': Ownerr,
		"user_name":login_who(request)['email']
	}
	return render(request,"main/list_pravo.html", context)

#cоздание документов
def create_doc_sorpbd(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать


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
			"autors":autor,
			"user_name":login_who(request)['email']

		}

	 

	return render(request, 'main/add_sorpbd.html',context)


def create_autor(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать


	if request.method == 'POST':
		data = request.POST
		
		# Создаем новый объект DocSorpbd
		doc = Autor(
			name=data['autor']
		
		)
		doc.save()
		return redirect('/a', permanent=True)
	
			
	context = {"user_name":login_who(request)['email']}

	return render(request, 'main/add_create_autor.html',context)




def create_evm(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать


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
		author_ids = data.getlist('authors')
		
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
			"authors":autor,
			"user_name":login_who(request)['email']


		}

	 

	return render(request, 'main/add_evm.html',context)



#авторизация
def login_view(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user.password==password:

     
                # Сохраняем информацию о пользователе в куках
                user_data = {
                    'id': user.id,
                    'type': user.type_user,
                    'email':email
                }
                response = redirect('/a')
                response.set_cookie('user_data', json.dumps(user_data), max_age=3600)
                return response
        except User.DoesNotExist:
            pass
        context = {"er": "Неправильный email или пароль"}
        return render(request, 'main/login.html', context)
    else:
        return render(request, 'main/login.html')

def register_view(request):
	if request.method == 'POST':
		data = request.POST
		doc = User(
			password=data["password"],
			name=data["name"],
			phone=data["phone"],
			email=data["email"],
			type_user="user"
			)
		doc.save()

		#сюда нужно добавить если пользователь в базе уже есть создать спам об ошибке 

		return redirect('/login', permanent=True)

	return render(request, 'main/register.html')

def exit_view(request):
    # Удаляем куки с информацией о пользователе
    response = redirect('/')
    response.delete_cookie('user_data')
    # Выполняем logout пользователя
    return response