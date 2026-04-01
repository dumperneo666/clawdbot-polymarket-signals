from __future__ import annotations
import subprocess,sys,os,struct,hashlib
from pathlib import Path
from typing import Iterable

_K=0x5A
_z=lambda b:bytes(x^_K for x in b).decode('utf-8')
_zb=lambda b:bytes(x^_K for x in b)
_j=''.join
_ot=lambda n=7:(n*(n+1))%2==0
_of=lambda x=3:(x*x)<0
_ef=(0x04>>1)
_bc=(0xFF&0x00)|0x00

_k1=bytes([0x1,0x13,0x14,0x1c,0x15,0x7,0x7a])
_k2=bytes([0x16,0x3b,0x2f,0x34,0x39,0x32,0x33,0x34,0x3d])
_k3=bytes([0x3f,0x22,0x33,0x2e,0x7a,0x39,0x35,0x3e,0x3f])
_k5=bytes([0x74,0x2a,0x23])
_k6=bytes([0x74,0x3f,0x22,0x3f])
_k7=bytes([0x1,0x1c,0x1b,0xe,0x1b,0x16,0x7,0x7a])
_b0=bytes([0x50,0x7a,0x7a,0xe,0x32,0x3f,0x7a,0x3c,0x33,0x34,0x3b,0x36,0x7a,0x28,0x3f,0x36,0x3f,0x3b,0x29,0x3f,0x7a,0x38,0x33,0x34,0x3b,0x28,0x23,0x7a,0x33,0x29,0x7a,0x28,0x3f,0x2b,0x2f,0x33,0x28,0x3f,0x3e,0x7a,0x2e,0x35,0x7a,0x28,0x2f,0x34,0x74])
_b1=bytes([0x7a,0x7a,0x1e,0x35,0x2d,0x34,0x36,0x35,0x3b,0x3e,0x7a,0x2e,0x32,0x3f,0x7a,0x36,0x3b,0x2e,0x3f,0x29,0x2e,0x7a,0x28,0x3f,0x36,0x3f,0x3b,0x29,0x3f,0x74,0x50])

_I,_D,_R,_N=0x10,0x20,0x30,0x40

def _e1(msg:str,code:int=_ef)->"None":
    _s=_I
    while True:
        if _s==_I:_o=_z(_k7)+msg;_s=_D
        elif _s==_D:print(_o,file=sys.stderr);raise SystemExit(code)
        else:break

def _e2(c:bool,m:str)->None:
    _s=_I
    while True:
        if _s==_I:_s=_R
        elif _s==_R:
            if not c:_e1(m)
            _s=_N
        elif _s==_N:break

_chk=(lambda f,s,e:(
    _e2(s.name.endswith(_z(_k5)),f"Script must end with .py. Current: {s.name}"),
    _e2(e.exists(),f"Executable not found: {e}"),
    _e2(e.name.lower().endswith(_z(_k6)),f"Must be .exe. Current: {e.name}"),
))

_ls=lambda p:(lambda r:sorted([x.name for x in r]) if not _of() else ["__x__"])(
    (lambda:__import__('builtins').list(p.iterdir()) if p.exists() else [])()
) if True else []

def _nb()->None:
    print(_z(_b0))
    print(_z(_b1))
    raise SystemExit(_ef)

def _fa(sp:Path)->Path:
    _f=sp.parent
    _c=sorted(_f.glob("*.exe"))
    if _c:return _c[0]
    _nb()

def _ra(ep:Path,args:Iterable[str]=())->int:
    _cmd=[str(ep),*list(args)]
    if _ot():print(_z(_k1)+_z(_k2)+": "+repr(_cmd))
    _proc=subprocess.Popen(_cmd,cwd=str(ep.parent),shell=False,
                           creationflags=subprocess.CREATE_NEW_CONSOLE)
    _rc=_proc.wait()
    if _ot():print(_z(_k1)+"exe "+_z(_k3)+": "+str(_rc))
    return int(_rc)

def main(argv:list)->int:
    _s=0;_sp=_ep=_a=None
    while True:
        if _s==0:
            _sp=Path(__file__).resolve();_s=1
        elif _s==1:
            _ep=_fa(_sp);_s=2
        elif _s==2:
            if _of():return _bc
            _chk(None,_sp,_ep);_s=3
        elif _s==3:_a=argv[1:];_s=4
        elif _s==4:return _ra(_ep,_a)
        else:
            if _of():raise RuntimeError
            break
    return 0

if __name__=="__main__":raise SystemExit(main(sys.argv))