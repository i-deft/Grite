from .models import Contacts


def add_variable_to_context(request):
    if Contacts.objects.all():
        contact_info = Contacts.objects.all().latest('id')
        return {
            'contact_info': contact_info,
        }
    return {0:0}
