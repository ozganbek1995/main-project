from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from user_model.models import User
from api.models import *
from user_model.models import *
from abconfig.settings import DOMAIN
from user_model.serializers import *

from api.api_views import *
from api.new_api_views import *



class ShopDetailView(APIView):
    def get(self, request, pk):

        response = {
            "status" : 200,
        }

        try:
            shop = Shop.objects.get(phone=pk)
            response['data'] = {
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
                }

        except Exception as e:
            print(e)
            response = {
                "status" : 200,
                "data" : None
            }

        return Response(response)

class ShopFilterView(APIView):
    def get(self, request, pk1, pk2=0):

        resp = {
            'status' : 200,
            }

        payload = []


        if pk2 != 0:
            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)

            shops = Shop.objects.filter(Q(viloyat = viloyat) and Q(tuman = tuman))
        else:
            viloyat = Viloyat.objects.get(pk=pk1)


            shops = Shop.objects.filter(viloyat=viloyat)


        for shop in shops:
            payload.append({
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
            })

        resp['data'] = payload

        return Response(resp)

class ShopsView(APIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


    def get(self, request):
        resp = {
            'status': 200

        }
        payload = []

        shops = Shop.objects.all()

        for shop in shops:
            payload.append({
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : str(DOMAIN + shop.image.url),
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
            })


        resp['data'] = payload
        return Response(resp)

    def post(self, request):
        rd = request.data

        resp = {'status' : 200}

        try:
            name = rd['name']
            description = rd['description']
            password = rd['password']

            pk1 = int(rd['viloyat'])
            pk2 = int(rd['tuman'])
            img = request.FILES['image']
            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)


            Shop.objects.create(
                name=name,
                description=description,
                password=password,
                viloyat=viloyat,
                tuman=tuman,
                image=img
            )
        except Exception as e:
            resp = {'status' : 400}


        return Response(resp)

class ShopsViewV2(APIView):
    def get(self, request):



        payload = []

        shops = Shop.objects.all()

        for shop in shops:
            payload.append({
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
            })



        return Response(payload)

    def post(self, request):
        rd = request.data

        resp = {'status' : 200}

        try:
            name = rd['name']
            description = rd['description']
            password = rd['password']

            pk1 = rd['viloyat']
            pk2 = rd['tuman']

            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)


            Shop.objects.create(
                name=name,
                description=description,
                password=password,
                viloyat=viloyat,
                tuman=tuman
            )
        except Exception as e:
            resp = {'status' : 400}


        return Response(resp)

class UserDetailView(APIView):
    def get(self, request, pk):

        response = {
            "status" : 200,
        }

        try:
            shop = Shop.objects.get(phone=pk)
            response['data'] = {
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
                }

        except Exception as e:
            print(e)
            response = {
                "status" : 200,
                "data" : None
            }

        return Response(response)

class TumanlarView(APIView):
    def get(self, request, pk):

        viloyat = Viloyat.objects.get(pk=pk)

        tumanlar = Tuman.objects.filter(viloyat=viloyat)

        response = {
            'status' : 200,
            'data' : []
        }

        data = []
        for i in tumanlar:
            data.append(
                {
                    'id' : i.id,
                    'name' : i.name,
                }
            )

        response['data'] = data


        return Response(response)






# ==============================================




# ==============================================
ShopDetailView = ShopDetailView.as_view()
ShopsView = ShopsView.as_view()
ShopFilterView = ShopFilterView.as_view()
ShopsViewV2 = ShopsViewV2.as_view()
UserDetailView =  UserDetailView.as_view()
TumanlarView = TumanlarView.as_view()