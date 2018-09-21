from django.generic import TemplateView

# GET - name (name of the user chatting)
def telegram_bot(self, request):
    message = request.GET['message']
