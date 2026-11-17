import json, html
D=json.load(open('data.json'))
esc=html.escape
from urllib.parse import urlparse
def host(u): return urlparse(u).netloc.replace('www.','')
def fd(d):
    m=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]; y,mo,dd=d.split('-'); return f"{m[int(mo)-1]} {int(dd)}"
rows_html="\n".join(
 f'<tr data-cause="{esc(r["cause"])}" data-sector="{esc(r["sector"])}" data-date="{r["date"]}" data-sev="{r["severity"]}"><td class="nw">{fd(r["date"])}</td><td>{esc(r["org"])}</td><td>{esc(r["incident"])}{" <span class=flag title=\""+esc(r["flag"])+"\">⚑</span>" if r["flag"] else ""}</td><td><span class="pill c-{r["cause"].lower().replace("-","")}">{esc(r["cause"])}</span></td><td class="num sev{r["severity"]}">{r["severity"]}</td><td><a href="{esc(r["source"])}" target="_blank" rel="noopener">{esc(host(r["source"]))}</a></td></tr>'
 for r in D)
flags_html="\n".join(f'<li><b>{fd(r["date"])} · {esc(r["org"])}</b> ({esc(r["cause"])}): {esc(r["flag"])} <a href="{esc(r["source"])}" target="_blank" rel="noopener">source</a></li>' for r in D if r["flag"])
tpl=open('template.html').read()
out=tpl.replace('%%ROWS%%',rows_html).replace('%%FLAGS%%',flags_html).replace('%%DATA%%',json.dumps(D,ensure_ascii=False).replace('</','<\\/')).replace('%%N%%',str(len(D)))
open('index.html','w').write(out)
print(len(out))
