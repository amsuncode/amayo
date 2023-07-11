from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

# Q-bank segment
# Course should reference the user
# many to many
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # User that created the course
    course_name = models.CharField(max_length=100, null=True)  # Name of the course
    description = models.TextField()  # Description of the course

    def __str__(self):
        return self.course_name
class Level(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    level_name = models.CharField(max_length=100, null=True)  # Name of the level

    def __str__(self):
        return self.level_name

class Unit(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    unit_name = models.CharField(max_length=100, null=True)  # Name of the unit

    def __str__(self):
        return self.unit_name

# Questions can be added linked to a specific topic, or a full paper
# the models are defined below
# they need to be linked to a specific course



class Topic(models.Model):
    # Course that the topic belongs to
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    topic_name = models.CharField(max_length=100, null=True)  # Name of the topic.
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic_name

class Paper(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    paper_title = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.paper_title

class MultipleChoiceQuestion(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    multiple_choice_question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.multiple_choice_question_text

class MultipleChoiceOption(models.Model):
    multiple_choice_question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE, null=True)
    multiple_choice_option_text = models.CharField(max_length=200, default=None)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.multiple_choice_option_text

class ShortAnswerQuestion(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    short_answer_question_text = models.TextField() # Text of the question
    answer = models.TextField() # Answer to the question
    discussion = models.TextField(blank=True) # Discussion or additional information about the question (optional)

    def __str__(self):
        return self.short_answer_question_text

# class Question(models.Model):
#     paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True, blank=True)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
#     question_text = models.CharField(max_length=100, null=True)
#     question_type = models.CharField(max_length=100, choices=[
#         ('MCQ', 'Multiple Choice Question'),
#         ('SAQ', 'Short Answer Question'),
#         ('IVQ', 'Image/Video Question'),
#     ])  # Type of the question (Multiple Choice, Short Answer, or Image/Video)

#     def clean(self):
#         # Ensure that a question is associated with either a paper or a topic, but not both.
#         if self.paper and self.topic:
#             raise ValidationError("A question can only be associated with either a paper or a topic, not both.")

#     def save(self, *args, **kwargs):
#         self.clean()  # Run validation before saving
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.question_text}"

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_timer_paused = models.BooleanField(default=False)

    def start_timer(self):
        self.start_time = timezone.now()
        self.save()

    def pause_timer(self):
        if self.start_time and not self.is_timer_paused:
            self.end_time = timezone.now()
            self.is_timer_paused = True
            self.save()

    def resume_timer(self):
        if self.start_time and self.is_timer_paused:
            time_paused = self.end_time - self.start_time
            self.start_time = timezone.now() - time_paused
            self.end_time = None
            self.is_timer_paused = False
            self.save()

    def stop_timer(self):
        if self.start_time:
            self.end_time = timezone.now()
            self.save()

    def get_elapsed_time(self):
        if self.start_time and not self.is_timer_paused:
            return timezone.now() - self.start_time
        return None

# class Result(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     passed = models.BooleanField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text}"
