from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Change:
    path:str
    before:tuple[int,int]
    after:tuple[int,int]

def snapshot(root:str)->dict[str,tuple[int,int]]:
    base=Path(root)
    if not base.is_dir(): raise ValueError("root must be a directory")
    return {str(p.relative_to(base)):(p.stat().st_size,p.stat().st_mtime_ns) for p in base.rglob("*") if p.is_file()}

def diff(old,new):
    changes=[]
    for path in sorted(set(old)|set(new)):
        if old.get(path)!=new.get(path): changes.append(Change(path,old.get(path,(0,0)),new.get(path,(0,0))))
    return changes
