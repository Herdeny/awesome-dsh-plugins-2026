"""Read canonical catalog entries, excluding navigation and recent highlights."""
from __future__ import annotations
import re
from dataclasses import dataclass

START = '<!-- catalog:start -->'
END = '<!-- catalog:end -->'
ANCHOR_RE = re.compile(r'<a id="([\w-]+)"></a>')
ENTRY_RE = re.compile(r'^- \[(?P<name>[^\]]+)\]\((?P<url>https://github\.com/[^\s)]+)\) - (?P<description>.*?) \(⭐(?P<stars>\d+)\)(?P<tail>.*)$')
TYPE_RE = re.compile(r' · `([^`]+)`$')
TYPES = {'plugin': ('插件', 'Plugin'), 'skill': ('Skill', 'Skill'), 'mcp': ('MCP', 'MCP'), 'client': ('客户端', 'Client'), 'template': ('模板', 'Template'), 'preset': ('预设', 'Preset'), 'tool': ('工具', 'Tool'), 'directory': ('目录', 'Directory'), 'framework': ('框架', 'Framework'), 'resource': ('资源', 'Resource'), 'theme': ('主题', 'Theme'), 'integration': ('集成', 'Integration'), 'mixed': ('复合项目', 'Mixed')}
TYPE_IDS = {label: key for key, labels in TYPES.items() for label in labels}

@dataclass
class Entry:
    section: str
    name: str
    url: str
    description: str
    stars: int
    tail: str
    kind: str | None

    @property
    def key(self):
        return self.url.rstrip('/').lower()

    @property
    def score(self):
        m = re.search(r'🛡️QC:(\d+)', self.tail)
        return int(m.group(1)) if m else None

    def render(self, lang):
        if self.kind not in TYPES:
            raise ValueError(f'{self.name}: missing/unknown type; see CONTRIBUTING.md')
        return f'- [{self.name}]({self.url}) - {self.description} (⭐{self.stars}){self.tail} · `{TYPES[self.kind][lang == "en"]}`'

def catalog_bounds(text):
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError('expected one catalog:start/end pair')
    start, end = text.index(START)+len(START), text.index(END)
    if end <= start:
        raise ValueError('catalog markers are reversed')
    return start, end

def parse_entries(text):
    start, end = catalog_bounds(text)
    entries, section = [], None
    for line in text[start:end].splitlines():
        a = ANCHOR_RE.fullmatch(line)
        if a:
            section = a.group(1)
        m = ENTRY_RE.fullmatch(line)
        if m:
            if section is None:
                raise ValueError('catalog entry has no section')
            f = m.groupdict()
            tail = f['tail']
            tag = TYPE_RE.search(tail)
            kind = TYPE_IDS.get(tag.group(1)) if tag else None
            if tag:
                tail = tail[:tag.start()]
            if tail and not re.fullmatch(r' 🛡️QC:\d{1,3} [🟢🟡🟠🔴]', tail):
                raise ValueError(f'{f["name"]}: malformed QC annotation')
            score = re.search(r'QC:(\d+)', tail)
            if score and not 0 <= int(score.group(1)) <= 100:
                raise ValueError(f'{f["name"]}: score must be between 0 and 100')
            entries.append(Entry(section, f['name'], f['url'], f['description'], int(f['stars']), tail, kind))
        elif line.startswith('- ['):
            raise ValueError(f'malformed catalog entry: {line[:100]}')
    keys = [e.key for e in entries]
    if len(keys) != len(set(keys)):
        raise ValueError('duplicate repository in canonical catalog')
    return entries

def stats(text):
    entries = parse_entries(text)
    main = [e for e in entries if e.section != 'ecosystem']
    scored = sum(e.score is not None for e in main)
    return dict(projects=len(entries), main=len(main), ecosystem=len(entries)-len(main), scored=scored, unscored=len(main)-scored)

def summary(text, lang):
    s = stats(text)
    if lang == 'zh':
        return f'收录 **{s["projects"]} 个项目**：主目录 {s["main"]} 个，生态资源 {s["ecosystem"]} 个。项目类型与安装方式不同，收录不代表已通过运行测试。'
    return f'**{s["projects"]} projects**: {s["main"]} in the main catalog and {s["ecosystem"]} ecosystem resources. Entry types and install methods vary; inclusion does not imply a successful runtime test.'

def qc_summary(text, lang):
    s = stats(text)
    coverage = 100*s['scored']/s['main'] if s['main'] else 0
    scored = [e for e in parse_entries(text) if e.section != 'ecosystem' and e.score is not None]
    if lang == 'zh':
        lead = f'主目录 {s["main"]} 个项目中，**{s["scored"]} 个有历史评分记录（{coverage:.1f}%）**，{s["unscored"]} 个未标注评分；{s["ecosystem"]} 个生态资源不计入此覆盖率。'
    else:
        lead = f'Of {s["main"]} main-catalog projects, **{s["scored"]} have historical scores ({coverage:.1f}%)** and {s["unscored"]} have no score listed. The {s["ecosystem"]} ecosystem resources are outside this coverage figure.'
    buckets = [sum(lo <= e.score <= hi for e in scored) for lo, hi in [(70,100),(50,69),(30,49),(0,29)]]
    return lead+'\n\n'+'\n'.join(f'- {label}: {n}' for label,n in zip(['🟢 70-100','🟡 50-69','🟠 30-49','🔴 0-29'], buckets))

def replace_block(text, name, content):
    pattern = re.compile(r'(<!-- '+re.escape(name)+r':start -->\n).*?(\n<!-- '+re.escape(name)+r':end -->)', re.S)
    result,n = pattern.subn(lambda m:m.group(1)+content+m.group(2),text)
    if n != 1:
        raise ValueError(f'expected one {name} block, found {n}')
    return result
