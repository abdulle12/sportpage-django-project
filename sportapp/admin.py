from django.contrib import admin

# Register your models here.
from .models import Homepage
from .models import Homepage1
from .models import Homepage2
from .models import Homepage3
from .models import Newspage1
from .models import Newspage2
from .models import Newspage3
from .models import Newspage4
from .models import Transfepage1
from .models import Transfepage2
from .models import Transfepage3
from .models import Transfepage4
from .models import Livescore
from .models import League, Match
from .models import Home_article_1, Paragraph,Home_article_2, Paragraph2,Home_article_3, Paragraph3
from .models import Home_article_4, Paragraph4,Paragraph5,Home_article_5,Paragraph6,Home_article_6
from .models import Home_article_7, Paragraph7,Home_article_8, Paragraph8,Home_article_9, Paragraph9
from .models import News_article_1, Paragraph1a,News_article_2, Paragraph1b,News_article_3, Paragraph1c
from .models import News_article_4, Paragraph1d,News_article_5, Paragraph1e,News_article_6, Paragraph1f
from .models import News_article_7, Paragraph1g,News_article_8, Paragraph1h,News_article_9, Paragraph1i
from .models import Transfer_article_1, Paragraph11,Transfer_article_2, Paragraph12,Transfer_article_3,Paragraph13
from .models import Transfer_article_4, Paragraph14,Transfer_article_5, Paragraph15,Transfer_article_6, Paragraph16


#homepage models
admin.site.register(Homepage)
admin.site.register(Homepage1)
admin.site.register(Homepage2)
admin.site.register(Homepage3)

#newspage models
admin.site.register(Newspage1)
admin.site.register(Newspage2)
admin.site.register(Newspage3)
admin.site.register(Newspage4)
#tranferpage models
admin.site.register(Transfepage1)
admin.site.register(Transfepage2)
admin.site.register(Transfepage3)
admin.site.register(Transfepage4)
#livescore models
admin.site.register(Livescore)
admin.site.register(League)
admin.site.register(Match)
#Article models
class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1

class HomeArticle1Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_1, HomeArticle1Admin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph2
    extra = 1

class HomeArticle2Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_2, HomeArticle2Admin)




class ParagraphInline(admin.TabularInline):
    model = Paragraph3
    extra = 1

class HomeArticle3Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_3, HomeArticle3Admin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph4
    extra = 1

class HomeArticle4Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_4, HomeArticle4Admin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph5
    extra = 1

class HomeArticle5Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_5, HomeArticle5Admin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph6
    extra = 1

class HomeArticle6Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_6, HomeArticle6Admin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph7
    extra = 1

class HomeArticle7Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_7, HomeArticle7Admin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph8
    extra = 1

class HomeArticle8Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_8, HomeArticle8Admin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph9
    extra = 1

class HomeArticle9Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Home_article_9, HomeArticle9Admin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph1a
    extra = 1

class NewsArticle1aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_1, NewsArticle1aAdmin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph1b
    extra = 1

class NewsArticle2aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_2, NewsArticle2aAdmin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph1c
    extra = 1

class NewsArticle3aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_3, NewsArticle3aAdmin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph1d
    extra = 1

class NewsArticle4aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_4, NewsArticle4aAdmin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph1e
    extra = 1

class NewsArticle5aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_5, NewsArticle5aAdmin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph1f
    extra = 1

class NewsArticle6aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_6, NewsArticle6aAdmin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph1g
    extra = 1

class NewsArticle7aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_7, NewsArticle7aAdmin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph1h
    extra = 1

class NewsArticle8aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_8, NewsArticle8aAdmin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph1i
    extra = 1

class NewsArticle9aAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(News_article_9, NewsArticle9aAdmin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph11
    extra = 1

class TransferArticle1Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Transfer_article_1, TransferArticle1Admin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph12
    extra = 1

class TransferArticle2Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Transfer_article_2, TransferArticle2Admin)


class ParagraphInline(admin.TabularInline):
    model = Paragraph13
    extra = 1

class TransferArticle3Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Transfer_article_3, TransferArticle3Admin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph14
    extra = 1

class TransferArticle4Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Transfer_article_4, TransferArticle4Admin)



class ParagraphInline(admin.TabularInline):
    model = Paragraph15
    extra = 1

class TransferArticle5Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Transfer_article_5, TransferArticle5Admin)




class ParagraphInline(admin.TabularInline):
    model = Paragraph16
    extra = 1

class TransferArticle6Admin(admin.ModelAdmin):
    inlines = [ParagraphInline]

admin.site.register(Transfer_article_6, TransferArticle6Admin)