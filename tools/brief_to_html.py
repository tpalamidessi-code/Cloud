#!/usr/bin/env python3
"""Convert a brief in briefs/YYYY-MM-DD.md to email-ready HTML.

Usage: python3 tools/brief_to_html.py briefs/2026-09-05.md > /tmp/brief.html

Deliberately dependency-free (no network installs) and scoped to exactly the
markdown the brief spec produces: h1/h2, bold, italic, links, bullets, hr.
"""
import html
import re
import sys


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',
                  r'<a href="\2" style="color:#1a5fb4;text-decoration:none">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em style="color:#555">\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code style="background:#f1f1f1;padding:1px 4px;border-radius:3px">\1</code>', text)
    return text


def convert(md: str) -> str:
    out, para, in_list = [], [], False
    style = 'body'

    STYLES = {
        'body': 'margin:0 0 14px;line-height:1.55',
        # the takeaway gets its own visual block rather than running into the item
        'sowhat': ('margin:-6px 0 14px;padding-left:10px;'
                   'border-left:3px solid #d0d0d0;line-height:1.5'),
        # the trailing source line, set smaller
        'sources': 'margin:-8px 0 20px;font-size:12px;line-height:1.5',
    }

    def flush_para():
        nonlocal style
        if para:
            out.append('<p style="%s">%s</p>' % (STYLES[style], inline(' '.join(para))))
            para.clear()
        style = 'body'

    def close_list():
        nonlocal in_list
        if in_list:
            out.append('</ul>')
            in_list = False

    for raw in md.split('\n'):
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            close_list()
        elif line.startswith('# '):
            flush_para(); close_list()
            out.append('<h1 style="font-size:21px;margin:0 0 6px;color:#111">%s</h1>' % inline(line[2:]))
        elif line.startswith('## '):
            flush_para(); close_list()
            out.append('<h2 style="font-size:15px;margin:28px 0 10px;padding-bottom:5px;'
                       'border-bottom:2px solid #e3e3e3;color:#111">%s</h2>' % inline(line[3:]))
        elif line.startswith('---'):
            flush_para(); close_list()
            out.append('<hr style="border:0;border-top:1px solid #e3e3e3;margin:26px 0">')
        elif re.match(r'^[-*] ', line) or re.match(r'^\d+\. ', line):
            flush_para()
            if not in_list:
                out.append('<ul style="margin:0 0 14px;padding-left:20px;line-height:1.55">')
                in_list = True
            out.append('<li style="margin-bottom:7px">%s</li>'
                       % inline(re.sub(r'^([-*]|\d+\.) ', '', line)))
        elif line.startswith('*So what:*'):
            # starts a new styled paragraph; wrapped continuation lines flow into it
            flush_para(); close_list()
            style = 'sowhat'
            para.append(line.strip())
        elif line.startswith('[') and '](' in line:
            flush_para(); close_list()
            style = 'sources'
            para.append(line.strip())
        else:
            if in_list:
                # continuation of the previous bullet
                out[-1] = out[-1][:-len('</li>')] + ' ' + inline(line.strip()) + '</li>'
            else:
                para.append(line.strip())

    flush_para(); close_list()

    return ('<div style="font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Helvetica,'
            'Arial,sans-serif;font-size:14px;color:#222;max-width:680px;margin:0 auto;padding:8px">'
            + '\n'.join(out) + '</div>')


if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf-8') as fh:
        sys.stdout.write(convert(fh.read()))
