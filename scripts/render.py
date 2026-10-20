"""Regenerate canonical stage and weekly views after editing curriculum.json."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'curriculum.json').read_text())
def save(name,text):(R/'docs'/name).write_text(text+'\n')
def budget(w):return ', '.join(f'{k} {v:g}h' for k,v in w['allocation'].items())
rows=[]
for w in d['weekly']:
    rows.append(f"### {w['week']} · {w['module']} · {w['title']}\n\n**Deliverable:** {w['deliverable']}\n\n**Pass:** {w['acceptance']}\n\n**Resources:** {w['resources']}. **Time:** {w['hours']} hours ({budget(w)}).")
save('weekly-assignments.md','# Complete weekly assignments\n\nGenerated from `curriculum.json`. Core weeks are sequential; branch weeks are optional alternatives. Move dates after missed weeks. See resource library for assigned sections.\n\n'+'\n\n'.join(rows))
save('11-first-12-weeks.md',"# 11. First 12 weeks\n\n60 hours. Weeks 1–2 complete S0. Weeks 3–12 complete the first 50 of S1's 110 hours; week 12 is not the S1 exit. Use local synthetic program records. Materials are selected sections, not entire courses. [Resource library](07-resource-library.md).\n\n"+'\n\n'.join(rows[:12]))
parts=[]
for s in d['stages']:
    part=f"## {s['id']} — {s['name']}\n\n**Objective:** {s['objective']}\n\n**Prerequisites:** {', '.join(s['prerequisites']) or 'none'}. **Budget:** {s['hours']}h / {s['hours']/5:g} active weeks / {s['hours']/(5*d['active_weeks_per_year']):.2f} calendar years at {d['active_weeks_per_year']} active weeks/year. **Project:** {s['project']}. **Resources:** {', '.join(s['resources'])}.\n\n**Career relevance:** {s['career']}.\n\n"
    if s['id']=='S0':part+='Follow weeks 1–2 in the initial plan for diagnostic exit.\n\n'
    if s['id']=='S1':part+='First complete weeks 3–12 (50 hours), then these three modules (60 hours).\n\n'
    if s['modules']:
        part+='| Module | Implementation / increment | Hours | Acceptance |\n|---|---|---:|---|\n'
        part+='\n'.join(f"| {m['id']} — {m['name']} | {m['build']} | {m['hours']} | {m['acceptance']} |" for m in s['modules'])+'\n\n'
    part+=f"**Exit/portfolio:** all stage criteria, {s['project']} release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient."
    parts.append(part)
save('03-stage-guide.md','# 3. Multiyear curriculum\n\nGenerated from `curriculum.json`, the authority for prerequisites, estimates and module criteria. A 20-hour module has four five-hour weeks: reference implementation, application, engineering/testing, demonstration/review/repair. All reading, project and assessment time is included. See weekly assignments for deliverables and project catalog for release contracts.\n\n'+'\n\n'.join(parts))
print('Regenerated stage guide, full weekly schedule and first 12 weeks.')
