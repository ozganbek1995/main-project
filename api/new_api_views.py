from rest_framework.views import APIView
from rest_framework.response import Response
from user_model.models import User
from api.models import *
from user_model.models import *
from abconfig.settings import DOMAIN
from user_model.serializers import *
from api.api_views import *
from api.new_api_views import *

from geopy import distance


class GetShopsView(APIView):

    def get(self, request):
        response = {
            'status' : 200,
            'data' : []
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
                'tuman' : shop.tuman.name,
                'location' : {
                    'lat' : shop.lat,
                    'lon' : shop.lon,
                    }
            })


        response['data'] = payload
        return Response(response)

class ShopDetailView(APIView):
    def get(self, request, pk):
        response = {
            'status' : 200,
        }
        try:
            shop = Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            response['status'] = 404

        return Response(response)

class 

class PostShopsView(APIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def post(self, request):
        response = {'status' : 400}
        rd = request.data
        try:
            host = User.objects.get(pk=rd['host-id'])
            name = rd['name']
            desc = rd['description']
            password = rd['password']
            pk1 = int(rd['viloyat'])
            pk2 = int(rd['tuman'])
            img = request.FILES['image']
            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)

            lat = rd['lat']
            lon = rd['lon']

            print(lat)
            print(lon)

            new_shop = Shop.objects.create(
                host=host,
                name=name,
                description=desc,
                password=password,
                viloyat=viloyat,
                tuman=tuman,
                image=img,
                lat=lat,
                lon=lon
            )

            response['status'] = 200
            response['data'] = [
                {
                    'id' : new_shop.id,
                    'name' : new_shop.name,
                    'description' : new_shop.description,
                    'img' : str(DOMAIN + new_shop.image.url),
                    'viloyat' : new_shop.viloyat.name,
                    'tuman' : new_shop.tuman.name,
                    'location' : {
                        'lon' : new_shop.lon,
                        'lat' : new_shop.lat,
                    }
                }
            ]
        except Exception as e:
            print(e)



        return Response(response)

class AddMemberView(APIView):
    def post(self, request):
        response = {'status' : 200}
        rd = request.data

        user_id = int(rd['user-id'])
        shop_id = int(rd['shop-id'])

        shop = Shop.objects.get(pk=shop_id)
        user = User.objects.get(pk=user_id)
        shop.members.add(user)

        return Response(response)

class MembersListView(APIView):
    def get(self, request, shop_pk):
        response = {
            'status' : 200,
            'data' : []
            }

        try:
            shop = Shop.objects.get(pk=shop_pk)
            for i in shop.members.all():
                response['data'].append(
                    {
                        'id' : i.id,
                        'first_name' : i.first_name,
                        'last_name' : i.last_name,
                        'phone' : i.phone,
                        'image' : str(DOMAIN + i.img.url),
                    }
                )

        except:
            response = {
            'status' : 400,
            'data' : None
            }

        return Response(response)

class ProductsListView(APIView):
    def get(self, request, pk):
        response = {
            'status': 200,
            'data' : []
        }


        shop = Shop.objects.get(pk=pk)
        for i in Product.objects.filter(shop=shop):
            response['data'].append(
                {
                    'id' : i.id,
                    'image1' : str(DOMAIN + i.image1.url),
                    'image2' : str(DOMAIN + i.image2.url),
                    'image3' : str(DOMAIN + i.image3.url),
                    
                    'name' : i.name,
                    'description' : i.description,
                    'count' : i.count,

                    'money_type' : i.currency.name,
                    'type' : i.typee.name,

                    'entry_price' : i.entry_price,
                    'percent' : i.percent,
                    'selling_price' : i.selling_price,
                    'validity_period' : i.validity_period,
                    'enterprise' : i.enterprise,

                }
            )


        return Response(response)

class RegionsApiView(APIView):

    def get(self, request):
        viloyatlar = Viloyat.objects.all()
        


        response = {
            'status' : 200,
            'data' : []
        }

        for i in viloyatlar:
            doc = {}
            doc['id'] = i.id
            doc['name'] = i.name
            doc['data'] = []


            for x in Tuman.objects.filter(viloyat=i):
                doc['data'].append(
                    {
                        'id' : x.id,
                        'name' : x.name
                    }
                )


            response['data'].append(doc)




        return Response(response)

class GeoLocationApi(APIView):
    def get(self, request, lat, lon):
        response = {
            'status' : 200,
        }


        payload = []
        user_coordinate = (float(lat), float(lon))
        print(user_coordinate)
        minDistanse = 10

        for i in Shop.objects.all():
            model_cordinate = (float(i.lat), float(i.lon))


            if float(str(distance.distance(user_coordinate, model_cordinate))[:17]) <= minDistanse:
                payload.append(
                    {
                        'id' : i.id,
                        'name' : i.name,
                        'lat' : i.lat,
                        'lon' : i.lon,

                        'km' : str(distance.distance(user_coordinate, model_cordinate))
                    }
                )

            

        payload = sorted(payload, key=lambda v: v['km'])
        print(payload)
        response['data'] = payload

        

        return Response(response)

class GetUsersView(APIView):
    def get(self, request):
        response = {
            'status' : 200,
            'data' : []
        }
        users = User.objects.all()
        for u in users:
            response['data'].append(
                {
                    'id' : u.id,
                    'first_name' : u.first_name,
                    'last_name' : u.last_name,
                    'phone' : u.phone,
                    'img' : str(DOMAIN) + u.img.url,
                }
            )
        return Response(response)

class CreateUserView(APIView):
    def post(self, request):
        rd = request.data
        response = {'status' : 200}
        try:
            first_name = rd['first_name']
            last_name = rd['last_name']
            phone = rd['phone']
            image = request.FILES['image']

            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                image=image
            )

        except:
            response['status'] = 400

        return Response(response)

class TestUserView(APIView):
    def get(self, request, phone):
        response = {
            'status' : 200,
            'data' : []
        }

        try:
            user = User.objects.get(phone=phone)


            response['data'] = {
                "id" : user.id,
                "first_name" : user.first_name,
                "last_name" : user.last_name,
                "phone" : user.phone,
                'img' : str(DOMAIN) + user.img.url,
            }
            
        except User.DoesNotExist:
            response['data'] = None

        except Exception as e:
            print(e) 

        return Response(response)

class PostUserUpdateView(APIView):
    def post(self, request, id):
        response = {
            'status' : 200
        }
        rd = request.data

        try:
            user:User = User.objects.get(pk=id)

            first_name = rd['first_name']
            last_name = rd['last_name']
            phone = rd['phone']
            image = rd['image']

            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.img = image

            user.save()

        except User.DoesNotExist:
            response['status'] = 404
        except KeyError:
            response['status'] = 400
        except Exception as e:
            print(e)


        return Response(response)



# =================================================================================


GetShopsView = GetShopsView.as_view()
PostShopsView = PostShopsView.as_view()
AddMemberView = AddMemberView.as_view()
MembersListView = MembersListView.as_view()
ProductsListView = ProductsListView.as_view()
RegionsApiView = RegionsApiView.as_view()
GeoLocationApi = GeoLocationApi.as_view()
GetUsersView = GetUsersView.as_view()
CreateUserView = CreateUserView.as_view()
TestUserView = TestUserView.as_view() 
PostUserUpdateView = PostUserUpdateView.as_view()
ShopDetailView = ShopDetailView.as_view()