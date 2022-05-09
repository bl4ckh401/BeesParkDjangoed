from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import login, authenticate, logout
from api.models import Posts, Product
from .serializers import PostSerializer, ProductSerializer, UserLogin, UserSerializer
from django.contrib.auth.models import User

# Create your views here.


class Register(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserLogin(request.data)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(
            request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'Success': 'Login SuccessFul'}, status=status.HTTP_200_OK)
        else:
            return Response({'ERROR': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)


class LogOut(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({'Success': 'Logout SuccessFul'}, status=status.HTTP_200_OK)


class NewPost(APIView):
    serializer_class = PostSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success': 'New Post Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class ShowPost(APIView):
    def get(self, request, format=None):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllProducts(APIView):

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProduct(APIView):
    serializer_class = ProductSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success': 'Product Created SuccessFully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleProduct(APIView):
    lookup_url_kwargs = 'product_slug'

    def get(self, request, format=None):
        product_slug = request.GET.get(self.lookup_url_kwargs)
        if (product_slug) is None:
            return Response({'Error': 'Bad Request. Missing Slug'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            query_set = Product.objects.filter(product_slug=product_slug)
            if query_set.exists():
                product = ProductSerializer(query_set[0]).data
                return Response(product, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'Product not Found'}, status=status.HTTP_200_OK)


class GetCSRFToken(APIView):

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})
