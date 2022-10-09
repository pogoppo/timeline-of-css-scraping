import re


def clean_html(raw_html):
    cleantext = re.sub(re.compile('<.*?>'), '', raw_html)
    return cleantext
