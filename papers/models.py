from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Q-bank segment

class Course(models.Model):
    course_name = models.CharField(max_length=100, null=True)  # Name of the course
    description = models.TextField()  # Description of the course

    def __str__(self):
        return self.course_name

class Topic(models.Model):
    # Course that the topic belongs to
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    topic_name = models.CharField(max_length=100, null=True)  # Name of the topic
    year_of_study = models.IntegerField()
    class_unit = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name
"example"
class Paper(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    paper_title = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.paper_title

# class Question(models.Model):
#     paper = models.ForeignKey(
#         Paper, on_delete=models.CASCADE, related_name='questions')
#     question_text = models.TextField()
#     question_type = models.CharField(max_length=100, choices=[
#         ('MCQ', 'Multiple Choice Question'),
#         ('SAQ', 'Short Answer Question'),
#         ('IVQ', 'Image/Video Question'),
#     ])  # Type of the question (Multiple Choice, Short Answer, or Image/Video)

#     def __str__(self):
#         return self.question_text


# class Response(models.Model):
#     question = models.ForeignKey(
#         Question, on_delete=models.CASCADE, related_name='questions')
#     response_text = models.TextField()

#     def __str__(self):
#         return self.question_text

# Models for different types of questions


# class Question(models.Model):
#     # Course that the question belongs to
#     paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
#     question_type = models.CharField(max_length=100, choices=[
#         ('MCQ', 'Multiple Choice Question'),
#         ('SAQ', 'Short Answer Question'),
#         ('IVQ', 'Image/Video Question'),
#     ])  # Type of the question (Multiple Choice, Short Answer, or Image/Video)
#     question_text = models.TextField(null=True)  # Text of the question
#     answer = models.TextField(blank=True)  # Answer to the question (optional)
#     # File upload field for the question (optional)
#     file = models.FileField(upload_to='image_video_questions/', blank=True)

#     def __str__(self):
#         return self.question_text


# class MultipleChoiceQuestion(models.Model):
#     text = models.TextField(null=True)  # Text of the question
#     correct_answer = models.TextField(null=True)  # Correct answer to the question
#     explanation = models.TextField(null=True)  # Explanation for the correct answer
#     # Course that the question belongs to
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.text
# null=True

# class ShortAnswerQuestion(models.Model):
#     text = models.TextField(null=True)  # Text of the question
#     answer = models.TextField(null=True)  # Answer to the question
#     # Discussion or additional information about the question (optional)
#     discussion = models.TextField(blank=True)
#     # Course that the question belongs to
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.text


# class ImageVideoQuestion(models.Model):
#     text = models.TextField(null=True)  # Text of the question
#     # File upload field for the question
#     file = models.FileField(upload_to='image_video_questions/', null=True)
#     # Course that the question belongs to
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.text

# # stores the answer given by a user to a particular question


# class Answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     question = models.ForeignKey(
#         Question, on_delete=models.CASCADE, related_name='answers')
#     answer_text = models.TextField()

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text}"
# # stores the comment posted by a user to a particular question


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.TextField()

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text}"

# # store the results of a user's attempt at a question


# class Result(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     passed = models.BooleanField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text}"
