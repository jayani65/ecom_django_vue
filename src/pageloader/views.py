from django.shortcuts import render
from django.views import View
from products.models import Category
import os

# Create your views here.
class BaseLoader(View):
    # this class is used to find all catagorys in the database bring them
    # in, and check if a catagory is selected and load things accordingly
    def __init__(self):
        self.all_categories = Category.update_sub_category_lists()
        self.categories = Category.find_main_categories(self.all_categories)
        path = os.getcwd() + '\src\pageloader\\navigationString.txt'
        try:
            f= open(path,"w+")
        except:
            path = os.getcwd() + '\pageloader\\navigationString.txt'
            f= open(path,"w+")
        for cat in self.categories:
            Category.generate_navigation_code(cat, f)
        f.close()

        with open(path, 'r') as file:
            self.massive_string = file.read().replace('\n', '')
            f.close()
        
        
    def get(self, request):
    # this should be to load the homepage, so give featured products and catalog data
        return render(request, 'pageloader/home.html', {'categories':self.categories, 'all_categories':self.all_categories, 'massive_string':self.massive_string})