from django.db import models

# НФ3

# Класс категории продукта
class CategoryProduct(models.Model):
    # поле с первичным ключем создается автоматически
    # Название категории товара
    name = models.CharField(max_length=128, verbose_name='имя категории товара')
    # Возможное написание категории
    alias_name = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


# Класс типа продукта
class ProductType(models.Model):
    # поле с первичным ключем создается автоматически
    # Название типа продукта
    name = models.CharField(max_length=128, verbose_name='тип продукта')
    # Возможное написание типа товара
    alias_name = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


# Класс бренда
class BrandProduct(models.Model):
    # поле с первичным ключем создается автоматически
    # Название бренда
    name = models.CharField(max_length=128, verbose_name='Имя бренда')
    # Возможное написание бренда
    alias_name = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


# Класс продуктов.
class Product(models.Model):
    # поле с первичным ключем создается автоматически (ID продукта, артикул)
    # Заголовок продукта
    title = models.CharField(max_length=255, verbose_name='имя продукта')
    # Краткое описание товара
    short_desc = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='краткое описание'
    )
    # Подробное описание товара
    description = models.TextField(verbose_name='подробно', blank=True)
    # ID бренда из class BrandProduct
    brand_id = models.ForeignKey(BrandProduct, on_delete=models.CASCADE)
    # ID типа продукта из class ProductType
    product_type_id = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE
    )
    # ID из категории товара class CategoryProduct
    category_id = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE
    )
    # стоимость продукта
    price = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name='цена',
        default=0
    )
    # картинки товара большая и 3 дополнительные
    img_big = models.ImageField(
        upload_to='big_img',
        blank=True
    )
    img_s_1 = models.ImageField(
        upload_to='small_img_1',
        blank=True
    )
    img_s_2 = models.ImageField(
        upload_to='small_img_2',
        blank=True
    )
    img_s_3 = models.ImageField(
        upload_to='small_img_3',
        blank=True
    )

    def __str__(self):
        return "{} ({})".format(self.title, self.category_id.name)


# Класс карточки заказа
# class Order(models.Model):
    # поле с первичным ключем создается автоматически
    # Имя заказчика
    # user_name = models.CharField(max_length=128, verbose_name='Имя заказчика')
    # Телефон заказчика
    # phone = models.CharField(max_length=32, verbose_name='телефон заказчика')
    # datatime =  models.DateTimeField(auto_now_add=True)


# Класс заказа товара
# class ProductOrder(models.Model):
    # order_id =  # ID заказа продукта
    # product_id =  # ID заказанного продукта
    # count =  # счет
