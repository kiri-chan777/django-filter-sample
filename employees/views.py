from django.views.generic import ListView
from .models import Employee
from .filters import EmployeeFilter
from .utils import generate_excel

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = EmployeeFilter(queryset, self.request.GET)
        return self.filter.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filter.form
        return context
    
    def get(self, request, *args, **kwargs):
        # Excel出力リクエストの処理
        if 'export_excel' in request.GET:
            queryset = self.get_queryset()
            return generate_excel(queryset)
        
        return super().get(request, *args, **kwargs)