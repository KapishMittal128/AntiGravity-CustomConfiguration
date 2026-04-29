import os
import json
import re

skills_dir = r'C:\Users\Kapish\.antigravity\.agents\skills'
skills = []
id_pattern = re.compile(r'^name:\s*(.+)$', re.M)
desc_pattern = re.compile(r'^description:\s*(.+)$', re.M)

for d in os.listdir(skills_dir):
    p = os.path.join(skills_dir, d)
    if os.path.isdir(p) and os.path.exists(os.path.join(p, 'SKILL.md')):
        with open(os.path.join(p, 'SKILL.md'), 'r', encoding='utf-8') as f:
            content = f.read()
            m_id = id_pattern.search(content)
            m_desc = desc_pattern.search(content)
            
            if m_id:
                skill_id = m_id.group(1).strip().strip('"').strip("'")
                name = skill_id.replace('-', ' ').title()
                desc = m_desc.group(1).strip().strip('"').strip("'") if m_desc else ''
                
                skills.append({
                    'id': skill_id,
                    'name': name,
                    'description': desc,
                    'source_reference': 'internal:antigravity-core',
                    'file_path': 'file:///' + os.path.join(p, 'SKILL.md').replace('\\', '/')
                })

with open(r'C:\Users\Kapish\.antigravity\.agents\SKILLS_REGISTRY.json', 'w', encoding='utf-8') as f:
    json.dump({'version': '3.0.0', 'total_skills': len(skills), 'skills': skills}, f, indent=4)
