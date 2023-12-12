#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Some auth mechanism must be set up at this point, usually the DART_TOKEN environment variable
# Run `dart login` in the terminal for more info


from dart import replicate_space


# You can get these IDs from the space's three dot menu > 'Copy ID'
TEMPLATE_SPACE_ID_1 = "rWPeANfzSnJi"
TEMPLATE_SPACE_ID_2 = "gJLw5RsKSjw8"


# Conditionally replicate one of the template spaces, depending on the circumstances
condition = True
replicate_space(TEMPLATE_SPACE_ID_1 if condition else TEMPLATE_SPACE_ID_2)
