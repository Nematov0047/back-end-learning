from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
# Create your views here.

class Books(View):
    def get(self, requests):
        books_raw = models.Books.objects.all()
        books_list = []
        for book in books_raw:
            books_list.append(model_to_dict(book))
        return JsonResponse(books_list,safe=False)
    
    @method_decorator(csrf_exempt)
    def post(self, requests):
        coming_json_data = requests.body
        coming_data = json.loads(coming_json_data)
        models.Books.objects.create(title=coming_data['title'], author=coming_data['author'], price=coming_data['price'], inventory=coming_data['inventory']).save()
        
        return JsonResponse({'message':'created'}, status=201)

class GetBook(View):
    def get(self, requests, book_id):
        try:
            book_raw = models.Books.objects.get(id=book_id)
            return JsonResponse(model_to_dict(book_raw))
        except:
            error = {
                'error':'not_found'
            }
            return JsonResponse(error)
    
    def delete(self, requests, book_id):
        models.Books.objects.get(id=book_id).delete()
        return JsonResponse({'message':'deleted'}, status=200)
    
    def put(self, requests, book_id):
        coming_data = json.loads(requests.body)
        book_update = models.Books.objects.get(id=book_id)
        update_info = {}
        if 'title' in coming_data:
            book_update.title = coming_data['title']
            update_info['title'] = 'updated'
        if 'author' in coming_data:
            book_update.author = coming_data['author']
            update_info['author'] = 'updated'
        if 'price' in coming_data:
            book_update.price = coming_data['price']
            update_info['price'] = 'updated'
        if 'inventory' in coming_data:
            book_update.inventory = coming_data['inventory']
            update_info['inventory'] = 'updated'
        
        book_update.save()
        update_info['message'] = 'updated'
        return JsonResponse(update_info)

    