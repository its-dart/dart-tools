#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from dart import is_logged_in, replicate_space


# The DART_TOKEN environment variable must be set to the value from
# https://app.itsdart.com/?settings=account at this point
is_logged_in(should_raise=True)


# You can get these IDs from the space's three dot menu > 'Copy ID'
TEMPLATE_SPACE_ID_1 = "rWPeANfzSnJi"
TEMPLATE_SPACE_ID_2 = "gJLw5RsKSjw8"


# Conditionally replicate one of the template spaces, depending on the circumstances
condition = True
replicate_space(TEMPLATE_SPACE_ID_1 if condition else TEMPLATE_SPACE_ID_2)
