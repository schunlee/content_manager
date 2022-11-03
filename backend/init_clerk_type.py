#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()
from manager.models import ClerkType

clerk_types = ["zalo", "line", "fb-messenger", "whatsapp", "lulu-zalo", "lulu-fb-messenger", "lulu-line",
               "lulu-whatsapp", "外部链接"]
for _type in clerk_types:
    if not ClerkType.objects.filter(name=_type).exists():
        ClerkType.objects.create(name=_type)
