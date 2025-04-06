from django.core.management.base import BaseCommand
from employees.models import Department, Employee
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'テスト用のデータを作成します'

    def handle(self, *args, **kwargs):
        # 部署の作成
        departments = [
            '営業部',
            '技術部',
            '人事部',
            '経理部',
            'マーケティング部',
            '研究開発部',
            'カスタマーサポート部',
        ]
        
        department_objects = []
        for dept_name in departments:
            dept, created = Department.objects.get_or_create(name=dept_name)
            department_objects.append(dept)
            if created:
                self.stdout.write(self.style.SUCCESS(f'部署を作成しました: {dept_name}'))
        
        # 従業員の作成
        first_names = ['太郎', '花子', '一郎', '恵子', '次郎', '直子', '三郎', '京子', '四郎', '美香']
        last_names = ['佐藤', '鈴木', '高橋', '田中', '伊藤', '渡辺', '山本', '中村', '小林', '加藤']
        
        # すでに存在する社員IDを取得
        existing_ids = set(Employee.objects.values_list('employee_id', flat=True))
        
        # 従業員100名を作成
        for i in range(100):
            # ユニークな社員IDを生成
            while True:
                employee_id = f'EMP{random.randint(1000, 9999)}'
                if employee_id not in existing_ids:
                    existing_ids.add(employee_id)
                    break
            
            name = f'{random.choice(last_names)} {random.choice(first_names)}'
            department = random.choice(department_objects)
            gender = random.choice(['M', 'F', 'O'])
            
            # 生年月日（25〜60歳）
            age = random.randint(25, 60)
            date_of_birth = timezone.now().date() - timedelta(days=365 * age)
            
            # 入社日（0〜20年前）
            years_employed = random.randint(0, 20)
            hire_date = timezone.now().date() - timedelta(days=365 * years_employed)
            
            # 在籍状況
            status = random.choices(
                ['active', 'inactive', 'leave'],
                weights=[0.8, 0.15, 0.05],
                k=1
            )[0]
            
            # 給与（300万〜1500万）
            salary = random.randint(3000000, 15000000)
            
            # メールアドレス
            email = f'{employee_id.lower()}@example.com'
            
            # 従業員を作成
            Employee.objects.create(
                name=name,
                employee_id=employee_id,
                department=department,
                gender=gender,
                date_of_birth=date_of_birth,
                hire_date=hire_date,
                status=status,
                email=email,
                salary=salary
            )
        
        self.stdout.write(self.style.SUCCESS('100名の従業員データを作成しました'))