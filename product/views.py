from django.views.generic import DetailView
from .models import Product, Comment
from .forms import Commentform
from django.shortcuts import get_object_or_404, redirect
from django.views import View



class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context['comments'] = Comment.objects.filter(product=product)
        context['form'] = Commentform()
        return context
class CommentCreateView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = Commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.commenter = request.user
            comment.save()
            print("saved")
            return redirect('product:product-detail', pk=pk) 
        print("dont save")
        return redirect('product:product-detail', pk=pk) 