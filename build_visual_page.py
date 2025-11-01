# build_visual_page.py
# usage: python build_visual_page.py T_Bank_hotels_and_flights_V009.ipynb
import sys, os, re, base64, nbformat
from pathlib import Path

INP = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not INP or not INP.exists():
    print("Укажи путь к .ipynb: python build_visual_page.py <notebook.ipynb>")
    sys.exit(1)

OUT_DIR = Path("images"); OUT_DIR.mkdir(exist_ok=True)

def clean(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^#+\s*", "", s)        # убрать заголовочные решётки
    s = re.sub(r"\*\*|__", "", s)       # убрать жирное/подчёркнутое
    s = re.sub(r"\s+", " ", s)
    return s

SECTIONS = [
    ("Сезонность и недельные паттерны", r"(сезон|месяц|месяч|недел|день|daily|weekly|monthly)", re.I),
    ("Ключевые метрики",             r"(средн(ий|его)\s*чек|количеств|доля|SUC|успешн|конверси)", re.I),
    ("Структура заказов и география",r"(распределен|страна|город|тип(ы)?\s*заказ|product|статус|оператор)", re.I),
    ("Премиальные заказы и выручка", r"(1%|топ|дорогих|вклад|оборот|выручк)", re.I),
    ("Коммуникации и контакты",     r"(email|sms|коммуникац|bounce|валидн|доставк)", re.I),
]
def pick_section(text: str) -> str:
    for name, pat, flags in SECTIONS:
        if re.search(pat, text or "", flags):
            return name
    return "Прочее"

nb = nbformat.read(str(INP), as_version=4)

items = []
for i, cell in enumerate(nb.cells):
    if cell.get("cell_type") != "code": 
        continue
    for j, out in enumerate(cell.get("outputs", []) or []):
        data = out.get("data") or {}
        if "image/png" not in data:
            continue
        b64 = data["image/png"]
        if isinstance(b64, list): b64 = "".join(b64)
        png = base64.b64decode(b64 if isinstance(b64, (bytes, bytearray)) else b64.encode("ascii"))
        fname = f"plot_{i:03d}_{j:02d}.png"
        (OUT_DIR / fname).write_bytes(png)

        # ближайшие markdown для названия/описания
        prev, nxt = "", ""
        k = i-1
        while k >= 0:
            c = nb.cells[k]
            if c.get("cell_type")=="markdown":
                prev = c.get("source","").strip(); break
            if c.get("cell_type")=="code" and c.get("outputs"): break
            k -= 1
        k = i+1
        while k < len(nb.cells):
            c = nb.cells[k]
            if c.get("cell_type")=="markdown":
                nxt = c.get("source","").strip(); break
            if c.get("cell_type")=="code" and c.get("outputs"): break
            k += 1

        title = ""
        if prev:
            for ln in prev.splitlines():
                ln = ln.strip()
                if ln:
                    title = clean(ln); break
        if not title:
            title = f"График {len(items)+1}"
        desc = ""
        if nxt:
            paras = [p.strip() for p in re.split(r"\n\s*\n", nxt) if p.strip()]
            if paras: desc = clean(paras[0])
        section = pick_section((title + " " + desc).lower())
        items.append({"file": fname, "title": title, "desc": desc, "section": section})

# собрать visual_analysis.md
order = [s for s,_,_ in SECTIONS] + ["Прочее"]
lines = ["# Визуализация и ключевые графики",
         "",
         f"Источник: `{INP.name}`. Все изображения выгружены автоматически из ячеек с выводами."]

for sec in order:
    grp = [x for x in items if x["section"]==sec]
    if not grp: 
        continue
    lines += ["", f"## {sec}", ""]
    for x in grp:
        lines += [f"### {x['title']}",
                  f"![{x['title']}](./images/{x['file']})"]
        if x["desc"]:
            lines += [f"_{x['desc']}_"]
        lines += [""]

Path("visual_analysis.md").write_text("\n".join(lines), encoding="utf-8")
print(f"OK: {len(items)} картинок → папка images/, страница visual_analysis.md")
