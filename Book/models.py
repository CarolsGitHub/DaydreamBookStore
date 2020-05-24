from django.db import models


# Create your models here.

# 书籍分类
class Category(models.Model):
    name = models.CharField('书籍分类', max_length=100)
    index = models.IntegerField(default=1, verbose_name='分类排序')

    class Meta:
        verbose_name = '书籍分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 书籍作者表
class Author(models.Model):
    name = models.CharField('作者', max_length=100)
    index = models.IntegerField(default=1, verbose_name='作者排序')

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 出版社表
class Press(models.Model):
    name = models.CharField('出版社', max_length=100)
    index = models.IntegerField(default=1, verbose_name='出版社排序')

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 书籍图片表
class Bimg(models.Model):
    text_info = models.CharField('标题', max_length=100, default='')
    img = models.ImageField('书籍图片', upload_to='static/bimg/')
    link_url = models.URLField('图片链接', max_length=100)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 书籍标签
class Tag(models.Model):
    name = models.CharField('书籍标签', max_length=100)

    class Meta:
        verbose_name = '书籍标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐位
class Recommend(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 书籍表
class Book(models.Model):
    title = models.CharField('书籍名', max_length=100)
    img = models.ImageField(upload_to='static/bimg/%Y/%m/%d/', verbose_name='书籍图片', blank=True, null=True)
    introduction = models.TextField('摘要', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者')
    press = models.ForeignKey(Press, on_delete=models.CASCADE, verbose_name='出版社')
    time = models.DateTimeField('出版时间', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    price = models.DecimalField('售价', max_digits=8, decimal_places=2)
    recommend = models.ForeignKey(Recommend, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    bnum = models.IntegerField('库存数量')
    badv = models.BooleanField(default=False)  # 商品推荐
    bclick = models.IntegerField('点击率')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'

    def __str__(self):
        return self.title