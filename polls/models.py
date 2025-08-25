from django.db import models

# Create your models here.
class Memo (models.Model) :
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    is_important = models.BooleanField('중요도', default=False)
    created_at =  models.DateTimeField('만들어진 날', auto_now_add=True)
    updated_at = models.DateTimeField('수정된 날', auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글들 "