from django.urls import path
from . import views

urlpatterns = [
    path("logoutPage/", views.logoutPage, name="logoutPage"),
    path("verifyLogin", views.verifyLogin, name="verifyLogin"),
    path("loginPage/", views.loginPage, name="login"),
    path("", views.home, name="HomePage"),
    path("placeOrder", views.placeOrder, name="Order"),
    path("displayOrder/", views.displayOrder, name="Baker"),
    path("displayIngredient", views.displayIngredient, name="ingredientDetails"),
    path("deletingIngredients/", views.deletingIngredients, name="Ingredient"),
    path("addIngredient", views.addIngredient, name="addIngredient"),
    path("deleteIngredient", views.deleteIngredient, name="deleteIngredient"),
    path("adding_ingredient/", views.adding_ingredient, name="adding_ingredient"),
    path("adding_ingredient/", views.adding_ingredient, name="adding_ingredient"),
    path("updating_ingredient/", views.updating_ingredient, name="updating_ingredient"),
    path("updateIngredient", views.updateIngredient, name="updateIngredient"),
    path("displayOrder/deleteOrder/<int:cid>", views.deleteOrder, name="deleteOrder"),

]