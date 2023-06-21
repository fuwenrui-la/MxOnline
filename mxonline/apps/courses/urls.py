from django.conf.urls import url
from django.urls import path

from apps.courses.views import CourseIntroduceView,CourseStandardView,CourseContentView,CourseVideoView,CourseAssignmentView,CourseExamView
#CourseListView, CourseLessonView , CourseCommentsView, CourseDetailView
# VideoView


urlpatterns = [
    # url(r'^list/$', CourseListView.as_view(), name="list"),
    url(r'^introduce/(?P<course_id>\d+)/$', CourseIntroduceView.as_view(), name="introduce"),
    url(r'^standard/(?P<course_id>\d+)/$', CourseStandardView.as_view(), name="standard"),
    url(r'^content/(?P<course_id>\d+)/$', CourseContentView.as_view(), name="content"),
    url(r'^assignment/(?P<course_id>\d+)/$', CourseAssignmentView.as_view(), name="assignment"),
    url(r'^exam/(?P<course_id>\d+)/$', CourseExamView.as_view(), name="exam"),
    url(r'^course_video/(?P<course_id>\d+)/(?P<chapter_id>\d+)/(?P<section_id>\d+)/$', CourseVideoView.as_view(), name="course_video")

    # url(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name="lesson"),
    # url(r'^(?P<course_id>\d+)/comments/$', CourseCommentsView.as_view(), name="comments"),
    # url(r'^(?P<course_id>\d+)/video/(?P<video_id>\d+)$', VideoView.as_view(), name="video"),
]






