from django.conf import settings
from mailsnake import MailSnake

def getChimp():
    return MailSnake(settings.MAILCHIMP_API_KEY), settings.MAILCHIMP_LIST

def getStatusString(user):
    if user.is_active:
        return 'active'
    else:
        return 'inactive'

def updateProfile(user):
    ms, list = getChimp()
    profile = user.get_profile

    vars = {
        'FNAME': getattr(user,'first_name', ''),
        'LNAME': getattr(user,'last_name', ''),
        'STATUS': getStatusString(user),
        'ADDRESS': {
            'addr1': getattr(profile,'address', ''),
            'city': getattr(profile,'city',''),
            'state': '',
            'zip': getattr(profile,'postal_code', '')
            }
        }

    return ms.listSubscribe(
        id = list,
        email_address = user.email,
        merge_vars = vars,
        update_existing = True,
        double_optin = False,
    )

#def unsubscribe(user):
#    ms, list = getChimp()
