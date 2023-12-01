#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from dart import is_logged_in, login, replicate_space


# You can get these IDs from the space's three dot menu > 'Copy ID'
TEMPLATE_SPACE_ID_1 = "rWPeANfzSnJi"
TEMPLATE_SPACE_ID_2 = "gJLw5RsKSjw8"


# Login based on information stored in environment variables, but only if needed
if not is_logged_in():
    login(email=os.environ["DART_EMAIL"], password=os.environ["DART_PASSWORD"])


# Conditionally replicate one of the template spaces, depending on the circumstances
condition = True
replicate_space(TEMPLATE_SPACE_ID_1 if condition else TEMPLATE_SPACE_ID_2)
