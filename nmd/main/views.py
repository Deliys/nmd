from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import DocSorpbd ,Owner ,Autor ,SoftwareRegistrationCertificate,Article
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
	return user_data

def type_user(email):return None # заготовка под раздение полномочий


def main_page(request):
	if login_or_no(request) == False:
		return redirect('/login')  # если пользователь не залогин, то пойдет отдыхать
	doc_sorpbd = DocSorpbd.objects.order_by('-id')[:5]
	softwareRegistrationCertificate = SoftwareRegistrationCertificate.objects.order_by('-id')[:5]
	context = {
		"doc_sorpbd": doc_sorpbd,
		"softwareRegistrationCertificate": softwareRegistrationCertificate,
		"user_name": login_who(request)['email']
	}
	return render(request, "main/main.html", context)
#профиль пользователя
def user_profile(request):
	return redirect("/")
#обработка удалений
def delete_artical_in_sbor(request,pk):
	doc_sorpbd = get_object_or_404(Article, id=pk)
	if request.method == 'POST':
		doc_sorpbd.delete()
		return redirect('/list_artical_in_sbor')
	return redirect('render_doc_sorpbd')	
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
def render_article_list(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать

	articles = Article.objects.all()
	context = {
		'article_list': articles,
		'user_name': login_who(request)['email']
	}
	return render(request, "main/article_list.html", context)
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

def DocSorp_detail(request, pk):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать
	doc = get_object_or_404(DocSorpbd, pk=pk)
	return render(request, 'main/doc_detail.html', {'doc': doc,"user_name":login_who(request)['email']})
def SoftwareRegistrationCertificate_detail(request, pk):
	if login_or_no(request) == False: return redirect('/login')  # если пользователь не залогинен, то пойдет отдыхать
	software = get_object_or_404(SoftwareRegistrationCertificate, pk=pk)
	return render(request, 'main/software_detail.html', {'software': software, "user_name": login_who(request)['email']})

#cоздание документов
def add_owner(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать
	if request.method == 'POST':
		phone_number = request.POST.get('phone_number')
		name = request.POST.get('name')
		owner_types = request.POST.get('owner_types')

		print(owner_types)

		owner_types = 0
		owner = Owner(phone_number=phone_number, name=name, owner_types=owner_types)
		owner.save()
		
		return redirect('/pravo/')  
	else:
		return render(request, 'main/add_owner.html')  
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
		# Получаем список ID авторов
		author_ids = data.getlist('autor')
		for author_id in author_ids:
			author, _ = Autor.objects.get_or_create(id=author_id.strip())
			doc.authors.set(author_ids)
		
		# Добавляем правообладателей
		if "individual_owners"in data:
			individual_owners = data['individual_owners'].split(',')
			for owner in individual_owners:
				individual_owner, _ = Owner.objects.get_or_create(id=owner.strip())
				doc.individual_owners.add(individual_owner)
		
		if "organization_owner" in data:
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
	if login_or_no(request) == False:
		return redirect('/login')  # если пользователь не залогин, то пойдет отдыхать
	if request.method == 'POST':
		data = request.POST

		dd = data.get('death_day')
		if dd=="":dd=None #на случай того что человек жив . тогда из формы приходит пустая строка
		autor = Autor(
			name=data.get('name'),
			last_name=data.get('last_name'),
			first_name=data.get('first_name'),
			code=data.get('code'),
			middle_name=data.get('middle_name'),
			birth_day=data.get('birth_day'),
			death_day=dd,
			academic_degree=data.get('academic_degree'),
			research_code=data.get('research_code'),
			phone=data.get('phone')
		)
		autor.save()
		return redirect('/autor', permanent=True)
	context = {"user_name": login_who(request)['email']}
	return render(request, 'main/add_create_autor.html', context)




def create_evm(request):
	if login_or_no(request) == False:return redirect('/login')#если пользователь не залогин , то пойдет отдыхать


	if request.method == 'POST':
		data = request.POST
		doc = SoftwareRegistrationCertificate(
			certificate_number=data['certificate_number'],
			software_name=data['software_name'],
			request_number=data['request_number'],
			request_date=data['request_date'],
			registration_date=data['registration_date'],
		)
		doc.save()

		# Получаем список ID авторов
		author_ids = data.getlist('authors')
		for author_id in author_ids:
			author, _ = Autor.objects.get_or_create(id=author_id.strip())
			doc.authors.set(author_ids)
		if "individual_owners" in data:
			# Получаем список ID индивидуальных правообладателей
			individual_owner_ids = data.getlist('individual_owners')
			for owner_id in individual_owner_ids:
				individual_owner, _ = Owner.objects.get_or_create(id=owner_id.strip())
				doc.individual_owners.add(individual_owner)
		if "organization_owners" in data:
			# Получаем список ID организационных правообладателей
			organization_owner_ids = data.getlist('organization_owners')
			for owner_id in organization_owner_ids:
				organization_owner, _ = Owner.objects.get_or_create(id=owner_id.strip())
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
def autor_get(request, pk):
	if not login_or_no(request):
		return redirect('/login')  # Redirect to login if the user is not logged in
	autor = get_object_or_404(Autor, pk=pk)

	#получение докуметов автора по базам
	doc_sorpbd = DocSorpbd.objects.filter(authors=autor)
	software_registration_certificates = SoftwareRegistrationCertificate.objects.filter(authors=autor)

	#подготовка списка для шаблона 
	documentss = []
	documentss.append({"bt":"/docSorp_detail","name_t":"Свидетельство о регистрации программы базы данных","documents":doc_sorpbd})
	documentss.append({"bt":"/softwareregistrationertificate_detail","name_t":"Свидетельств о регистрации программы для ЭВМ","documents":software_registration_certificates})


	return render(request, 'main/autor_detail.html', {
		'autor': autor,
		"user_name": login_who(request)['email'],
		'documentss': documentss
	})
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