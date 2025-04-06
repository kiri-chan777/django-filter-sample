from django.db import models

class Department(models.Model):
    name = models.CharField('部署名', max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '部署'
        verbose_name_plural = '部署一覧'

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', '男性'),
        ('F', '女性'),
        ('O', 'その他'),
    )
    
    STATUS_CHOICES = (
        ('active', '在籍中'),
        ('inactive', '退職'),
        ('leave', '休職中'),
    )
    
    name = models.CharField('氏名', max_length=100)
    employee_id = models.CharField('社員ID', max_length=20, unique=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.PROTECT,
        related_name='employees',
        verbose_name='所属部署'
    )
    gender = models.CharField('性別', max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField('生年月日')
    hire_date = models.DateField('入社日')
    status = models.CharField('在籍状況', max_length=10, choices=STATUS_CHOICES, default='active')
    email = models.EmailField('メールアドレス', max_length=255)
    salary = models.IntegerField('給与')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.employee_id})"
    
    class Meta:
        verbose_name = '従業員'
        verbose_name_plural = '従業員一覧'
        ordering = ['-hire_date']