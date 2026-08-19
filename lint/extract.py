"""Pull the article body out of a Webflow blog page as plain markdown-ish text."""
import re, html, sys

def _blocks(frag):
    """Convert an HTML fragment to line-per-block text, keeping heading level and list markers."""
    frag = re.sub(r'(?is)<(script|style|noscript|svg)\b.*?</\1>', '', frag)
    frag = re.sub(r'(?is)<br\s*/?>', '\n', frag)
    # mark block boundaries before stripping tags
    frag = re.sub(r'(?is)<h([1-6])[^>]*>', lambda m: '\n\n' + '#'*int(m.group(1)) + ' ', frag)
    frag = re.sub(r'(?is)</h[1-6]>', '\n', frag)
    frag = re.sub(r'(?is)<li[^>]*>', '\n- ', frag)
    frag = re.sub(r'(?is)<(p|div|tr|blockquote)[^>]*>', '\n\n', frag)
    frag = re.sub(r'(?is)<t[dh][^>]*>', ' | ', frag)
    # keep link targets so interlink counting works
    frag = re.sub(r'(?is)<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'\2](\1)', frag)
    frag = re.sub(r'(?is)<(strong|b)>(.*?)</\1>', r'**\2**', frag)
    frag = re.sub(r'(?s)<[^>]+>', '', frag)
    frag = html.unescape(frag)
    frag = re.sub(r'[ \t]+', ' ', frag)
    frag = re.sub(r'\n{3,}', '\n\n', frag)
    return '\n'.join(l.strip() for l in frag.split('\n')).strip()

def extract(path):
    src = open(path, encoding='utf-8', errors='replace').read()
    # Webflow rich text container, greedy to the closing of the widest match
    cands = re.findall(r'(?is)<div[^>]*class="[^"]*w-richtext[^"]*"[^>]*>(.*)', src)
    body = max(cands, key=len) if cands else src
    # cut at the footer / newsletter / related-posts furniture
    for stop in ('Before you go', 'Related Posts', 'Read the latest tips',
                 'Subscribe to', 'footer', 'Table of contents'):
        i = body.find(stop)
        if 2000 < i < len(body): body = body[:i]
    text = _blocks(body)
    title = ''
    m = re.search(r'(?is)<title>(.*?)</title>', src)
    if m: title = html.unescape(re.sub(r'(?s)<[^>]+>', '', m.group(1))).strip()
    meta = ''
    # Order-agnostic. Webflow emits content= before name=, so a name-first pattern
    # reported meta-missing on every published page. That false positive sat in
    # KNOWN-ISSUES as an open mystery about the articles; it was always this regex.
    m = (re.search(r'(?is)<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', src)
         or re.search(r'(?is)<meta[^>]+content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', src))
    if m: meta = html.unescape(m.group(1)).strip()
    return {'title': title, 'meta': meta, 'text': text}

if __name__ == '__main__':
    d = extract(sys.argv[1])
    print('TITLE:', d['title'][:90]); print('META :', d['meta'][:90])
    print('CHARS:', len(d['text']), ' LINES:', len(d['text'].splitlines()))
    print('---- first 700 ----'); print(d['text'][:700])
