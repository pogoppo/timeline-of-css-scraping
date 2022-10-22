import re


def clean_html(raw_html):
    """
    文字列からHTMLタグを削除（非厳密）
    """
    cleantext = re.sub(re.compile('<.*?>'), '', raw_html)
    return cleantext
