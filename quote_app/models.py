from django.db import models

class Quote(models.Model):
    material = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    units = models.IntegerField()
    paper_sequence = models.CharField(max_length=50)
    pages_per_book = models.IntegerField()
    printing_requirement = models.CharField(max_length=200)
    gluing_method = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calculate_price(self):
        # 这里是价格计算逻辑，你可以根据实际需求修改
        # 示例：简单的价格计算，每个参数乘以一个固定系数
        material_factor = 1.0
        size_factor = 1.0
        units_factor = 1.0
        paper_sequence_factor = 1.0
        pages_per_book_factor = 1.0
        printing_requirement_factor = 1.0
        gluing_method_factor = 1.0
        quantity_factor = 1.0

        price = self.quantity

        self.price = price
        self.save()

        return price

    def __str__(self):
        return f"Quote for {self.quantity} books"