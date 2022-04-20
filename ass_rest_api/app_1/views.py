
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken    
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegister(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request ,format=None):
        serializer = Seri_user(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            token = get_tokens_for_user(user)
            return JsonResponse({
             "data":serializer.data ,
            "access":token
             })
        else:
            return JsonResponse(serializer.errors)

class HomeUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        seri = Item_seri(data=request.data)
        if seri.is_valid():
            seri.save()
            return JsonResponse({'data':'save'})
        else:
            return JsonResponse({'data':seri.errors})

    def get(self ,request  ):

        items = Items.objects.all()
        data = Item_seri(items ,  many=True )
        i_data = data.data
        return JsonResponse({"data":i_data})

 
class HomeEdit(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request ,pk):
        id = Items.objects.get(pk=pk)
        data = Item_seri(instance=id, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse({'data':'edit now'})
        else:
            return JsonResponse({'data':data.errors})
    def delete(self ,request, pk):
        id = Items.objects.get(pk=pk)
        # data = Item_seri(nstance=id )
        id.delete()
        return JsonResponse({'data':'delete now'})

   

