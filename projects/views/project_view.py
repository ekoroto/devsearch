from django.views import View


class ProjectView(View):
    def get(self, request):
        return '<h1>Hello<h1>'