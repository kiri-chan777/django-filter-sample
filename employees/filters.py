from .models import Employee
from .forms import EmployeeFilterForm

class EmployeeFilter:
    def __init__(self, queryset, data=None):
        self.queryset = queryset
        self.data = data or {}
        self.form = self._get_form()
    
    def _get_form(self):
        form = EmployeeFilterForm(self.data)
        form.is_valid()  # バリデーションを実行
        return form
    
    def filter_queryset(self):
        queryset = self.queryset
        form = self.form
        
        # フォームが有効でない場合は何もフィルタしない
        if not form.is_valid():
            return queryset
        
        # 氏名フィルタ（部分一致）
        name = form.cleaned_data.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        # 部署フィルタ
        department = form.cleaned_data.get('department')
        if department:
            queryset = queryset.filter(department=department)
        
        # 在籍状況フィルタ
        status = form.cleaned_data.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # 入社日範囲フィルタ
        hire_date_from = form.cleaned_data.get('hire_date_from')
        if hire_date_from:
            queryset = queryset.filter(hire_date__gte=hire_date_from)
            
        hire_date_to = form.cleaned_data.get('hire_date_to')
        if hire_date_to:
            queryset = queryset.filter(hire_date__lte=hire_date_to)
        
        # 給与範囲フィルタ
        min_salary = form.cleaned_data.get('min_salary')
        if min_salary:
            queryset = queryset.filter(salary__gte=min_salary)
            
        max_salary = form.cleaned_data.get('max_salary')
        if max_salary:
            queryset = queryset.filter(salary__lte=max_salary)
        
        return queryset
    
    @property
    def qs(self):
        return self.filter_queryset()