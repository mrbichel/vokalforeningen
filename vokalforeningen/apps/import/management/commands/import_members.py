import pprint
import uuid
from django.contrib.auth.models import User

__author__ = 'johan'

from django.utils.encoding import smart_str
import sys

from django.core.management.base import BaseCommand

import elementtree.ElementTree as ET

import datetime


class Command(BaseCommand):
    help = u"""
        Import members from old database xml.
    """

    args = 'infile'

    def write_out(self, message, verbosity_level=1):
        sys.stdout.write(smart_str(message))
        sys.stdout.flush()

        #if self.verbosity and self.verbosity >= verbosity_level:
        #    sys.stdout.write(smart_str(message))
        #    sys.stdout.flush()


    def handle(self, *args, **options):
        """

        """

        tree = ET.parse("/home/vokal/vokalforening_d.xml")

        for item in tree.findall("Brugere"):

            try:

                User.objects.get(username=item.find('email').text)

            except User.DoesNotExist:

                u = User(email=item.find('email').text,
                        first_name=item.find('fornavn').text,
                        last_name=item.find('efternavn').text,
                        is_active=item.find('aktiv').text == '1',
                    )

                username = uuid.uuid4().hex[:30]
                try:
                    while True:
                        User.objects.get(username=username)
                        username = uuid.uuid4().hex[:30]
                except User.DoesNotExist:
                    pass

                u.username = username


                u.set_password(item.find('password').text)
                u.save()

                p = u.get_profile()
                try:
                    p.url = item.find('hjemmeside').text
                except AttributeError:
                    pass

                try:
                    p.address = item.find('adresse').text
                except AttributeError:
                    pass

                try:
                    p.postal_code = item.find('postnr').text
                except AttributeError:
                    pass

                try:
                    p.municipality = item.find('kommune').text
                except AttributeError:
                    pass

                try:
                    p.phone_number = item.find('tlf').text
                except AttributeError:
                    pass

                try:
                    p.mobile_phone_numer = item.find('mobil').text
                except AttributeError:
                    pass

                try:
                    p.receive_email = item.find('modtagmail').text == '1'
                except AttributeError:
                    pass

                try:
                    p.birthdate = datetime.date(int(item.find('fodselsaar').text), 1, 1)
                except AttributeError:
                    pass

                try:
                    p.education = item.find('uddannelse').text
                except AttributeError:
                    pass

                try:
                    p.position = item.find('stilling').text
                except AttributeError:
                    pass

                try:
                    p.experience = item.find('brancheerfaring').text
                except AttributeError:
                    pass

                p.save()
