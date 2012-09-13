# -*- coding: utf-8 -*-

"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'vokalforeningen.dashboard.CustomIndexDashboard'
"""

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append an app list module for "Applications"
        self.children.append(modules.ModelList(
            _('Indhold'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('corkboard.*','files.*','django.contrib.flatpages.*', 'django.contrib.comments.*','flatblocks.*','meetings.*'),
        ))


         # append an app list module for "Applications"
        self.children.append(modules.ModelList(
            _('Medlemmer'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('django.contrib.auth.*','profiles.*'),
        ))

        # append an app list module for "Applications"
        self.children.append(modules.ModelList(
            _('Avanceret'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('django.contrib.sites.*', 'notification.*'),
        ))

        self.children.append(
                        modules.LinkList(
                            title= _("Links og hjælp"),
                            column=2,
                            collapsible=False,
                            post_content = "<p>Kontakt support@vokalforening.dk for hjælp.</p>",
                            children=[
                                {
                                    'title': _('Se forside'),
                                    'url': '/',
                                    'external': False,
                                },
                                {
                                    'title': _('Mailchimp'),
                                    'url': 'http://www.mailchimp.com/',
                                    'external': True,
                                },
                            ]
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


