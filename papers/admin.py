from django.contrib import admin
from .models import Course, LevelOfStudy, Unit, MultipleChoiceQuestion, MultipleChoiceOption, Topic, Paper # , ShortAnswerQuestion


class MultipleChoiceOptionInline(admin.TabularInline):
    model = MultipleChoiceOption
    extra = 1

class MultipleChoiceQuestionInline(admin.TabularInline):
    model = MultipleChoiceQuestion
    extra = 1

# class ShortAnswerQuestionInline(admin.TabularInline):
#     model = ShortAnswerQuestion
#     extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'description')

@admin.register(LevelOfStudy)
class LevelOfStudyAdmin(admin.ModelAdmin):
    list_display = ('level_name', 'course')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name', 'level_of_study')

@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    inlines = [MultipleChoiceOptionInline]
    list_display = ('multiple_choice_question_text',)

# @admin.register(ShortAnswerQuestion)
# class ShortAnswerQuestionAdmin(admin.ModelAdmin):
#     list_display = ('short_answer_question_text', 'answer')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_name', 'unit', 'created', 'updated', 'was_published_recently')
    # inlines = [MultipleChoiceQuestionInline]

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('paper_title', 'unit', 'created', 'updated', 'was_published_recently')
    inlines = [MultipleChoiceQuestionInline,]
