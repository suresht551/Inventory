from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

from Task.models import Inventory
from Task.forms import InventoryForm

# Create your views here.

class WelcomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'login.html')

class LoginView(View):
	def get(self, request):
		try:
			if request.user.is_authenticated():
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponseRedirect('/load/')
		except:
			return HttpResponseRedirect('/load/')

	def post(self, request, *args, **kwargs):
		user = authenticate(username=request.POST.get('user'), 
							password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponseRedirect('/load/')

		else:
			return HttpResponseRedirect('/load/')


class HomePageView(View):
	def get(self, request, *args, **kwargs):
		try:
			if request.user.is_authenticated():
				invs_t = Inventory.objects.filter(is_active=unicode('True'))
				invs_f = Inventory.objects.filter(is_active=unicode('False'))
				data_t = []
				data_f = []
				for inv in invs_t:
					data_t.append({'item_name': inv.item_name,
								 'item_id': inv.item_id,
								 'description': inv.description,
								 'vendor_name': inv.vendor_name.name,
								 'photo': str(inv.photo.url.split('/')[-1])})
				for inv in invs_f:
					data_f.append({'item_name': inv.item_name,
								 'item_id': inv.item_id,
								 'description': inv.description,
								 'vendor_name': inv.vendor_name.name,
								 'photo': str(inv.photo.url.split('/')[-1])})
				return render_to_response('home.html',
										  {'user': str(request.user),
										   'data_t': data_t,
										   'data_f': data_f})
			else:
				return HttpResponseRedirect('/load/')
		except:
			return HttpResponseRedirect('/load/')

class UpdateView(View):
	def get(self, request, item_id=None):
		if item_id and request.user.is_authenticated():
			try:
				inv = Inventory.objects.get(item_id=int(item_id))
				data = [{'item_name': inv.item_name,
						 'item_id': inv.item_id,
						 'description': inv.description,
						 'vendor_name': inv.vendor_name.name,
						 'is_active': inv.is_active,
						 'photo': str(inv.photo.url.split('/')[-1])}
						]
				return render(request, 'update.html',
							  {'user': str(request.user),
							   'data': data})
			except:
				return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/') 

class UpdateDataView(View):
	# @csrf_protect
	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				data = request.POST
				obj = Inventory.objects.get(item_id=int(data.get('item_id')))
				obj.item_id = data.get('item_id')
				obj.description = data.get('description')
				obj.is_active = unicode('True')
				obj.save()
				emps = Inventory.objects.all()
				data = []
				for inv in invs:
					data.append({'item_name': inv.item_name,
								 'item_id': inv.item_id,
								 'description': inv.description,
								 'vendor_name': inv.vendor_name.name,
								 'photo': str(inv.photo.url.split('/')[-1])})
				return render_to_response('home.html',
										  {'user': str(request.user),
										   'data': data})
			except:
				return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/')

class DeleteView(View):
	def get(self, request, item_id=None):
		if item_id and request.user.is_authenticated():
			try:
				inv = Inventory.objects.get(item_id=int(item_id))
				inv.is_active = unicode('False')
				inv.save()
				return HttpResponseRedirect('/home/')
			except:
				return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/')

class AddInv(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			form = InventoryForm()
			return render(request, 'add_emp.html', {'form': form})

class AddInvView(View):
	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			import pdb
			pdb.set_trace()
			form = InventoryForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect('/home/')
		else:
			return HttpResponseRedirect('/load/')
		

class LogoutView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			logout(request)
			return HttpResponseRedirect('/load/')
		else:
			return HttpResponseRedirect('/load/')