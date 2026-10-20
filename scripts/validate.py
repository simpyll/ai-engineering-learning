"""Validate the educational plan without third-party dependencies."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'curriculum.json').read_text())
stages={s['id']:s for s in d['stages']}
assert len(stages)==len(d['stages']), 'Duplicate stage'
resources={r['id'] for r in d['resources']}
seen=set();active=set()
def visit(k):
    assert k in stages, f'Unknown prerequisite {k}'
    assert k not in active, f'Cycle at {k}'
    if k in seen:return
    active.add(k)
    for p in stages[k]['prerequisites']:visit(p)
    active.remove(k);seen.add(k)
for k in stages:visit(k)
ids=set();by_stage={k:[] for k in stages};by_module={}
for w in d['weekly']:
    assert w['week'] not in ids, f'Duplicate week {w["week"]}'
    ids.add(w['week']);by_stage[w['stage']].append(w)
    by_module.setdefault(w['module'],[]).append(w)
    assert w['hours']==d['hours_per_week']==sum(w['allocation'].values()),w['week']
    assert w['acceptance'] and w['deliverable'], w['week']
for s in stages.values():
    assert set(s['resources'])<=resources
    assert sum(w['hours'] for w in by_stage[s['id']])==s['hours'],s['id']
    for m in s['modules']:
        assert sum(w['hours'] for w in by_module[m['id']])==m['hours'],m['id']
core=[w for w in d['weekly'] if w['stage'].startswith('S')]
assert [w['week'] for w in core]==[f'W{i:03}' for i in range(1,len(core)+1)]
first={s:min(i for i,w in enumerate(core) if w['stage']==s) for s in stages if s.startswith('S')}
last={s:max(i for i,w in enumerate(core) if w['stage']==s) for s in first}
for s in first:
    for p in stages[s]['prerequisites']:
        assert last[p]<first[s],f'{s} starts before {p} finishes'
assert len(core)==304 and sum(w['hours'] for w in core)==1520
assert sum(w['hours'] for w in core[:12])==60
print(f'PASS: {len(stages)} stages; acyclic prerequisites; {len(core)} core weeks / 1520 hours; {len(d["weekly"])-len(core)} optional branch weeks; every weekly budget = 5h.')
