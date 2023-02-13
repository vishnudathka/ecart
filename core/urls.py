from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    # product
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/create/", views.ProctCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("products/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    # feedback
    path("feedback/create", views.FeedbackCreateView.as_view(), name="feedback_create"),
    path("feedback/<int:pk>/detail/", views.FeedbackDetailView.as_view(), name="feedback_detail"),
     # Wishlist
    path("wishlists/add/product/<int:pk>/", views.AddToWishlistView.as_view(), name="add_to_wishlist"),
    path("wishlists/create/", views.WishlistCreateView.as_view(), name="wishlist_create"),
    path("wishlists/", views.WishlistListView.as_view(), name="wishlist_list"),
    #add to cart
    path("cart/add/product/<int:pk>/", views.AddToCartView.as_view(), name="add_to_cart"),
    #review
    path("reviews/product/<int:pk>/add/", views.ReviewCreatView.as_view(), name="review_create"),
    path("review/product/reviews", views.ReviewListView.as_view(), name="review_list"),
        

]
