from django.conf import settings
from django.urls import path
from .views import AllProducts, CreateProduct, GetCSRFToken, LogOut, Login, NewPost, Register, ShowPost, SingleProduct
from django.conf.urls.static import static

urlpatterns = [
    path('/create', Register.as_view()),
    path('/login', Login.as_view()),
    path('/logout', LogOut.as_view()),
    path('/newpost', NewPost.as_view()),
    path('/posts', ShowPost.as_view()),
    path('/create-product', CreateProduct.as_view()),
    path('/product', SingleProduct.as_view()),
    path('/all-products', AllProducts.as_view()),
    path('/getcsrf', GetCSRFToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
