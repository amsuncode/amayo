from django.contrib import admin
from .models import Course, Level, Unit, Topic, Paper, MultipleChoiceQuestion, MultipleChoiceOption, ShortAnswerQuestion

class MultipleChoiceOptionInline(admin.TabularInline):
    model = MultipleChoiceOption
    extra = 3

class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    inlines = [MultipleChoiceOptionInline]
    list_display = ["multiple_choice_question_text", "paper"]

admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Unit)
admin.site.register(Topic)
admin.site.register(Paper)
admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)
admin.site.register(ShortAnswerQuestion)
