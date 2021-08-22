from django.conf import settings
from django.views.generic import View,TemplateView
from django.shortcuts import render,redirect
from .forms import ContactForm,SearchForm
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap
import requests
import json
import stripe
from django.views import generic
from django.http import JsonResponse
from django.urls import reverse


SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&applicationId=1041325084269081277'


def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    result = json.loads(api)
    items = []
    print(result)
    if not 'error' in result:
        items = result['Items']
    return items

def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items= [
               {
                   'price': 'price_1JR3eWBHrrkrpmkSzqI9cI0K',
                   'quantity': 1,
               },
            ],
            mode='subscription',
            success_url=request.build_absolute_uri(reverse('success.html')),
            cancel_url=request.build_absolute_uri(reverse('cancel.html')),
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error':str(e)})


class IndexView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'api/index.html', {
        })

class IndexDetailView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'api/index_detail.html', {
        })

class EbayDetailView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'api/ebay_detail.html', {
        })

class KokunaiDetailView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'api/kokunai_detail.html', {
        })

class AmazonoemDetailView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'api/amazonoem_detail.html', {
        })

class ImportDetailView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'api/import_detail.html', {
        })


class EbaycircleView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'api/ebay_circle.html', {
            'form': form
        })
    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        if form.is_valid():
            keyword = form.cleaned_data['title']
            params = {
                'keyword': keyword,
                # 'sort' : '+itemPrice',
                'hits' : 10,
                'imageFlag' : 1
            }
            items = get_api_data(params)
            product_data = []
            for i in items:
                item = i['Item']
                # print(item)
                image = item['mediumImageUrls'][0]['imageUrl']
                itemName = item['itemName']
                itemPrice = item['itemPrice']
                query = {
                    'image': image,
                    'itemName' : itemName,
                    'itemPrice' : itemPrice,
                }
                product_data.append(query)

            product_data=sorted(product_data,key=lambda x: x['itemPrice'])

            return render(request, 'api/ebay_circle_result.html', {
                'product_data': product_data[0],
                'keyword': keyword
            })

        return render(request, 'api/ebay_circle.html', {
            'form': 'form'
        })

class CourceView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'api/cource.html', {
        })


class CONTACTView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        return render(request, 'api/contact.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            content = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。
                
                {name} 様
                
                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                
                --------------------
                ■お名前
                {name}
                
                ■メールアドレス
                {email}
                
                ■メッセージ
                {message}
                --------------------
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )

            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse("無効なヘッダが検出されました。")

            return redirect('index') # 後で変更

        return render(request, 'app/contact.html', {
            'form': form
        })

class QUESTIONView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'api/question.html', {
            'form': form
        })

class PRIVACYView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'api/privacy.html', {
        })

class PaymentSuccessView(TemplateView):
    template_name = "api/success.html"

class PaymentCancelView(TemplateView):
    template_name = "api/cancel.html"

def create_checkout_session(request):
    pass
















# class PaymentView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         order = Order.objects.get(user=request.user, ordered=False)
#         user_data = CustomUser.objects.get(id=request.user.id)
#         context = {
#             'order': order,
#             'user_data': user_data
#         }
#         return render(request, 'api/payment.html', context)

#     def post(self, request, *args, **kwargs):
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         order = Order.objects.get(user=request.user, ordered=False)
#         token = request.POST.get('stripeToken')
#         amount = order.get_total()
#         order_items = order.items.all()
#         item_list = []
#         for order_item in order_items:
#             item_list.append(str(order_item.item) + '：' + str(order_item.quantity))
#         description = ' '.join(item_list)

#         charge = stripe.Charge.create(
#             amount=amount,
#             currency='jpy',
#             description=description,
#             source=token,
#         )

#         payment = Payment(user=request.user)
#         payment.stripe_charge_id = charge['id']
#         payment.amount = amount
#         payment.save()

#         order_items.update(ordered=True)
#         for item in order_items:
#             item.save()

#         order.ordered = True
#         order.payment = payment
#         order.save()
#         return redirect('thanks')