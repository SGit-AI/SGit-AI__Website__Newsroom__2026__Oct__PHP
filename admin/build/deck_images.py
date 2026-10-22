#!/usr/bin/env python3
"""Draws the briefing deck's model images through OpenRouter, from the briefs in admin/content/decks/images/<slug>.briefs.json.

The key is read from OPENROUTER_API_KEY and never written anywhere. Each image is saved as storyboards/<slug>/img/<slot>.webp
(the PNG the model returns, converted with Pillow), and its record (model, seconds, cost, size, the brief) goes into
admin/content/decks/images/<slug>.json with check set to 'not checked'. The build shows an image only once a person or
agent has read it against its brief and written what was checked into that field: a model can draw a number that is not
in the data. Model choice follows the newsroom's infographic bake-off of 10 October 2026.
Usage: OPENROUTER_API_KEY=... python3 admin/build/deck_images.py <slug> [slot ...]
"""
import base64, io, json, os, sys, time, urllib.request
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://openrouter.ai/api/v1'
NAMES = {'google/gemini-nano-banana-2.1': 'Nano Banana 2.1', 'google/gemini-3-pro-image': 'Gemini 3 Pro Image', 'openai/gpt-5.4-image-2': 'GPT-5.4 Image 2'}

def call(path, body=None, key=None):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode() if body is not None else None,
                                 headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json',
                                          'HTTP-Referer': 'https://php.oct.2026.newsroom.sgit.ai', 'X-Title': 'PHP October 2026, storyboard desk'})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)

def main():
    key = os.environ.get('OPENROUTER_API_KEY')
    if not key or len(sys.argv) < 2:
        sys.exit(__doc__)
    from PIL import Image
    slug, only = sys.argv[1], set(sys.argv[2:])
    bf = os.path.join(ROOT, 'admin', 'content', 'decks', 'images', slug + '.briefs.json')
    rf = os.path.join(ROOT, 'admin', 'content', 'decks', 'images', slug + '.json')
    briefs = json.load(open(bf, encoding='utf-8'), object_pairs_hook=OrderedDict)
    recs = json.load(open(rf, encoding='utf-8'), object_pairs_hook=OrderedDict) if os.path.exists(rf) else OrderedDict()
    os.makedirs(os.path.join(ROOT, 'storyboards', slug, 'img'), exist_ok=True)
    for slot, b in briefs.items():
        if only and slot not in only:
            continue
        t = time.time()
        r = call('/chat/completions', {'model': b['model'], 'modalities': ['image', 'text'], 'image_config': {'aspect_ratio': b['aspect_ratio']},
                                       'usage': {'include': True}, 'messages': [{'role': 'user', 'content': b['prompt']}]}, key)
        secs = round(time.time() - t)
        imgs = (r.get('choices') or [{}])[0].get('message', {}).get('images') or []
        if not imgs:
            print(f'{slot}: no image returned', json.dumps(r)[:400]); continue
        raw = base64.b64decode(imgs[0]['image_url']['url'].split(',', 1)[1])
        im = Image.open(io.BytesIO(raw)).convert('RGB')
        if im.width > 1600:
            im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
        out = os.path.join(ROOT, 'storyboards', slug, 'img', slot + '.webp')
        im.save(out, 'WEBP', quality=86, method=6)
        cost = (r.get('usage') or {}).get('cost')
        recs[slot] = OrderedDict([('model', b['model']), ('model_name', NAMES.get(b['model'], b['model'])), ('job', b['job']), ('aspect_ratio', b['aspect_ratio']),
                                  ('width', im.width), ('height', im.height), ('seconds', secs), ('cost_usd', f'{cost:.3f}' if isinstance(cost, (int, float)) else 'not reported'),
                                  ('generation_id', r.get('id')), ('drawn', time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())), ('prompt', b['prompt']), ('check', 'not checked')])
        json.dump(recs, open(rf, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); open(rf, 'a').write('\n')
        print(f'{slot}: {recs[slot]["model_name"]}, {secs}s, ${recs[slot]["cost_usd"]}, {im.width}x{im.height} -> {os.path.relpath(out, ROOT)}')

if __name__ == '__main__':
    main()
