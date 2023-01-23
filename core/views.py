from django.shortcuts import render,redirect
from django.views import generic as views
from core import models
from django.urls import reverse_lazy
from core import forms


class HomeView(views.TemplateView):
    template_name = "core/home.html"
    extra_context = {
        "products": models.ProductModel.objects.all(),
    }

# this is exagiration of templateview    

# class HomeView(views.View):
#     template_name = "core/home.html"
#     def get(self, request, *args):
#         context={
#            "project_name" :"Ecart"

#         }
#         return render(request,self.template_name,context)





class AboutView(views.TemplateView):
    template_name = "core/about.html"



# class ProductListView(views.ListView):
#     template_name = "core/products/product_list.html"
#     model = models.ProductModel
#     context_object_name = "products"


# this is exagiration of Listview  


class ProductListView(views.View):
    template_name = "core/products/product_list.html"
    model = models.ProductModel
    context_object_name = "products"
    def get(self, request, *args):
        products = self.model.objects.all()
        context ={
            "products" : products,
            "project_name" :"Ecart",
            "page_name" :"ProductList"
        }
        return render(request,self.template_name,context)


class ProctCreateView(views.CreateView):
    template_name = "core/products/product_create.html"
    model =models.ProductModel
    form_class = forms.ProductForm
    success_url =reverse_lazy("core:product_list")


# class ProductDetailView(views.DetailView):
#     template_name = "core/products/product_detail.html"
#     model =models.ProductModel
#     context_object_name ="product"  


class ProductDetailView(views.View):
    template_name = "core/products/product_detail.html"
    model =models.ProductModel
    context_object_name ="product" 
    def get(self,request,pk):
        product = self.model.objects.get(id=pk)
        context = {
            self.context_object_name:product
        }     
        return render(request,self.template_name,context)


# class ProductUpdateView(views.UpdateView):
#     template_name = "core/products/product_update.html"
#     form_class = forms.ProductForm
#     model = models.ProductModel
#     success_url = reverse_lazy("core:product_list")


class ProductUpdateView(views.View):
    template_name ="core/products/product_update.html"
    model =models.ProductModel
    form_class =forms.ProductForm

    def get(self,request,pk):
        product =self.model.objects.get(id=pk)
        context ={
            'form' :self.form_class(instance=product)
        }
        return render(request,self.template_name,context)
    def post(self,request,pk):
        product =self.model.objects.get(id=pk)
        form =self.form_class(request.POST,request.FILES,instance=product) 
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
    def form_valid(self,form):
        obj=form.save()
        return redirect (reverse_lazy("core:product_detail",args=(obj.id,)))
    def form_invalid(self,form):
        return render(self.request,self.template_name,{"form":form})              


# class ProductDeleteView(views.DeleteView):
#     template_name = "core/products/product_delete.html"
#     model = models.ProductModel
#     success_url = reverse_lazy("core:product_list")  


class ProductDeleteView(views.View):
    template_name ="core/products/product_delete.html"  
    model =models.ProductModel
    success_url = reverse_lazy("core:product_list")

    def get(self,request,pk)    :
        product =self.model.objects.get(id=pk)
        cotext ={
            "product" :product
        }
        return render(request,self.template_name,cotext)
    def post(self,request,pk):
        product = self.model.objects.get(id=pk)
        product.delete()
        # product.status=False
        # product.save()    
        return redirect(self.success_url)



    
# Create your views here.
