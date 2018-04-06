from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index, name='bookings'),
    url(r'^question/', views.post_question, name='PostQuestion'),
    url(r'^all/questions/', views.all_questions, name='AllQuestions'),
    url(r'^single/question/(\d+)', views.single_question, name='SingleQuestion'),
    url(r'^comment/(\d+)', views.post_comment, name='Comment'),
    url(r'^view/booking/', views.unbooked_session, name='ViewSessions'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
