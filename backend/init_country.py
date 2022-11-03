#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()
from manager.models import Country

clerk_types = ["中国", "越南", "伊朗"]
for _type in clerk_types:
    if not Country.objects.filter(name=_type).exists():
        Country.objects.create(name=_type)
