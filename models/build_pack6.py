"""Batch 6: rooster, seated_sahabe, vortex_swirl, kaaba, hive. v2 toolkit (rounded + linear color)."""
import numpy as np
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual import TextureVisuals

rng=np.random.default_rng(3)

def lin(c): return [(x/255.0)**2.2 for x in c[:3]]+[c[3]/255.0 if len(c)>3 else 1.0]
def M(c,alpha=None):
    bcf=lin(c)
    if alpha is not None: bcf[3]=alpha
    mat=PBRMaterial(baseColorFactor=bcf, roughnessFactor=0.9, metallicFactor=0.0)
    if alpha is not None: mat.alphaMode='BLEND'
    return TextureVisuals(material=mat)
def rbox(ex,ey,ez,c,e=0.35,subdiv=2,T=None,flat=False):
    m=trimesh.creation.icosphere(subdivisions=subdiv,radius=1.0)
    v=m.vertices; m.vertices=np.sign(v)*(np.abs(v)**e)
    m.vertices*=[ex/2,ey/2,ez/2]
    if T is not None: m.apply_transform(T)
    m.apply_translation(c)
    if flat: m.unmerge_vertices()
    return m
def ell(rx,ry,rz,c,subdiv=3,flat=False):
    m=trimesh.creation.icosphere(subdivisions=subdiv,radius=1.0)
    m.apply_scale([rx,ry,rz]); m.apply_translation(c)
    if flat: m.unmerge_vertices()
    return m
def cap(p0,p1,r,sec=14):
    p0,p1=np.array(p0,float),np.array(p1,float)
    v=p1-p0; h=np.linalg.norm(v)
    m=trimesh.creation.capsule(height=h,radius=r,count=[sec,sec])
    m.apply_transform(trimesh.geometry.align_vectors([0,0,1],v/h))
    m.apply_translation((p0+p1)/2); return m
def hexprism(r,depth,c,rot=0.0):
    m=trimesh.creation.cylinder(radius=r,height=depth,sections=6)  # axis Z
    m.apply_transform(trimesh.transformations.rotation_matrix(rot,[0,0,1]))
    m.apply_translation(c); return m
def torus_xz(rx,rz,minor,c,sec=28):
    m=trimesh.creation.torus(major_radius=1.0,minor_radius=minor,
                             major_sections=sec,minor_sections=10)
    m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
    m.apply_scale([rx,1.0,rz]); m.apply_translation(c); return m
def loft(spine,radii,wscale=1.0,vscale=1.0,ring_n=12):
    spine=np.asarray(spine,float); n=len(spine)
    ang=np.linspace(0,2*np.pi,ring_n,endpoint=False)
    up=np.array([0.,1.,0.]); verts=[];faces=[]
    for i in range(n):
        t=spine[min(i+1,n-1)]-spine[max(i-1,0)]; t/=np.linalg.norm(t)
        ref=up if abs(t@up)<0.95 else np.array([1.,0.,0.])
        u=np.cross(t,ref); u/=np.linalg.norm(u); v=np.cross(t,u)
        for a in ang:
            verts.append(spine[i]+radii[i]*(np.cos(a)*u*wscale+np.sin(a)*v*vscale))
    for i in range(n-1):
        for j in range(ring_n):
            a=i*ring_n+j; b=i*ring_n+(j+1)%ring_n
            c2=(i+1)*ring_n+(j+1)%ring_n; d=(i+1)*ring_n+j
            faces+=[[a,b,c2],[a,c2,d]]
    verts+=[spine[0],spine[-1]]; b0,t0=len(verts)-2,len(verts)-1
    for j in range(ring_n):
        faces.append([b0,(j+1)%ring_n,j])
        faces.append([t0,(n-1)*ring_n+j,(n-1)*ring_n+(j+1)%ring_n])
    m=trimesh.Trimesh(np.array(verts),np.array(faces)); m.fix_normals(); return m
def rotX(a): return trimesh.transformations.rotation_matrix(a,[1,0,0])
def rotY(a): return trimesh.transformations.rotation_matrix(a,[0,1,0])
def rotZ(a): return trimesh.transformations.rotation_matrix(a,[0,0,1])
def export(P,path,scale=1.0):
    sc=trimesh.Scene(); t=0
    for item in P:
        n,m,c=item[0],item[1],item[2]
        alpha=item[3] if len(item)>3 else None
        if scale!=1.0: m.apply_scale(scale)
        m.visual=M(c,alpha); sc.add_geometry(m,node_name=n,geom_name=n); t+=len(m.faces)
    sc.export(path); print(f'{path.split("/")[-1]:20s} {len(P):3d} parts {t:6d} tris')

SKIN=(238,196,158,255); CREAM=(243,235,214,255); GOLD=(224,186,116,255)

# ================================================== ROOSTER
def rooster(path):
    P=[]
    BODY=(243,236,218,255); ORANGE=(214,138,88,255); COMB=(206,120,96,255)
    b=ell(0.24,0.30,0.235,[0,0.46,0]); b.unmerge_vertices() if False else None
    P.append(('Body', b, BODY))
    P.append(('Chest', ell(0.205,0.245,0.19,[0,0.63,0.02]), BODY))
    P.append(('Head', ell(0.155,0.19,0.145,[0,0.82,0.03]), BODY))
    for k,(cx,h,a) in enumerate([(-0.045,0.085,0.25),(0.0,0.115,0.0),(0.045,0.085,-0.25)]):
        c=ell(0.028,h,0.045,[0,0,0],2,flat=True); c.apply_transform(rotZ(a))
        c.apply_translation([cx,1.0,0.01]); P.append((f'Comb_{k}',c,COMB))
    bk=ell(0.05,0.042,0.055,[0,0.80,0.17],1,flat=True); P.append(('Beak',bk,ORANGE))
    for s,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Eye_{nm}', ell(0.02,0.024,0.015,[s*0.07,0.845,0.13],2), (52,44,40,255)))
    for s,nm in [(1,'L'),(-1,'R')]:
        w=ell(0.045,0.11,0.14,[s*0.225,0.50,-0.02]); P.append((f'Wing_{nm}',w,(236,227,205,255)))
        P.append((f'Wing_{nm}_n', ell(0.035,0.05,0.05,[s*0.235,0.42,-0.12],2), (236,227,205,255)))
    for k,(ty,tz,a) in enumerate([(0.66,-0.22,0.55),(0.72,-0.17,0.30),(0.60,-0.25,0.80)]):
        t=ell(0.032,0.14,0.055,[0,0,0],2,flat=True); t.apply_transform(rotX(-a))
        t.apply_translation([(-0.03+0.03*k),ty,tz]); P.append((f'Tail_{k}',t,(236,224,196,255)))
    for s,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Leg_{nm}', cap([s*0.075,0.22,0.0],[s*0.075,0.05,0.0],0.028,10), GOLD))
        for k,a in enumerate([-0.5,0.0,0.5]):
            P.append((f'Toe_{nm}_{k}', cap([s*0.075,0.028,0.0],
                     [s*0.075+0.10*np.sin(a)*0.55,0.028,0.115*np.cos(a)],0.024,8), GOLD))
        P.append((f'Heel_{nm}', cap([s*0.075,0.028,0.0],[s*0.075,0.028,-0.06],0.022,8), GOLD))
    export(P,path,scale=0.5/1.06)

# ================================================== SEATED SAHABE
def seated_sahabe(path):
    P=[('Slab', rbox(0.85,0.10,0.70,[0,0.05,0.05],e=0.28,subdiv=3), (216,190,158,255))]
    ROBE=(146,144,96,255); SASH=(202,110,74,255); BEARD=(150,104,74,255)
    # seated robe: skirt dome over crossed legs + torso
    P.append(('Skirt', ell(0.34,0.24,0.30,[0,0.26,0.08]), ROBE))
    for s in (1,-1):
        P.append((f'Knee_{s}', ell(0.13,0.11,0.13,[s*0.24,0.22,0.16]), ROBE))
    P.append(('Torso', ell(0.21,0.28,0.16,[0,0.52,0.0]), ROBE))
    P.append(('Belt', torus_xz(0.185,0.15,0.035,[0,0.44,0.02]), SASH))
    P.append(('Belt_Knot', ell(0.05,0.045,0.035,[0.02,0.42,0.165],2), SASH))
    P.append(('Belt_T1', rbox(0.055,0.16,0.03,[0.0,0.32,0.19],e=0.4,T=rotZ(0.12)), SASH))
    P.append(('Belt_T2', rbox(0.05,0.13,0.028,[0.06,0.33,0.185],e=0.4,T=rotZ(-0.18)), SASH))
    # arms resting on knees
    for s,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Sleeve_{nm}', cap([s*0.185,0.66,0.02],[s*0.26,0.42,0.14],0.062), ROBE))
        h=ell(0.055,0.028,0.075,[s*0.245,0.335,0.20],2); P.append((f'Hand_{nm}',h,SKIN))
    # head + beard + calm face
    P.append(('Head', ell(0.125,0.13,0.12,[0,0.90,0.04]), SKIN))
    P.append(('Beard', ell(0.095,0.095,0.075,[0,0.80,0.10]), BEARD))
    P.append(('Beard_Tip', ell(0.05,0.06,0.04,[0,0.735,0.12],2,flat=True), BEARD))
    P.append(('Mustache', ell(0.045,0.016,0.02,[0,0.855,0.155],2), BEARD))
    for s,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Eye_{nm}', ell(0.014,0.018,0.010,[s*0.048,0.915,0.145],2), (74,50,40,255)))
        P.append((f'Brow_{nm}', cap([s*0.066,0.955,0.135],[s*0.026,0.96,0.14],0.008,8), BEARD))
    P.append(('Nose', ell(0.014,0.022,0.018,[0,0.885,0.16],2), SKIN))
    P.append(('Smile', cap([-0.014,0.856,0.152],[0.014,0.856,0.152],0.005,8), (176,110,84,255)))
    # turban + drape
    P.append(('Turban', ell(0.14,0.10,0.132,[0,0.985,0.02]), CREAM))
    tw=trimesh.creation.torus(major_radius=0.125,minor_radius=0.035,major_sections=26,minor_sections=10)
    tw.apply_transform(rotX(np.pi/2)); tw.apply_translation([0,0.945,0.03])
    P.append(('Turban_Wrap', tw, CREAM))
    for s,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Drape_{nm}', rbox(0.055,0.24,0.10,[s*0.125,0.79,0.0],e=0.35), CREAM))
    P.append(('Drape_Chest', torus_xz(0.115,0.10,0.04,[0,0.72,0.05]), CREAM))
    P.append(('Drape_Back', rbox(0.20,0.24,0.05,[0,0.79,-0.10],e=0.35), CREAM))
    export(P,path,scale=1.2/1.09)

# ================================================== VORTEX SWIRL
def vortex(path):
    P=[]
    SANDS=(226,186,132,255); STRIPE=(244,228,196,255)
    n=120; t=np.linspace(0,1,n)
    ang=t*5.2*2*np.pi
    r=0.06+0.60*t**1.25
    y=0.10+1.35*t
    spine=np.column_stack([r*np.cos(ang), y, r*np.sin(ang)])
    radii=0.030+0.085*t
    P.append(('Swirl', loft(spine,radii,vscale=0.62,ring_n=12), SANDS, 0.92))
    # cream highlight stripe following the outer edge
    sp2=np.column_stack([(r+radii*0.75)*np.cos(ang), y+radii*0.25, (r+radii*0.75)*np.sin(ang)])
    P.append(('Stripe', loft(sp2, radii*0.22+0.006, ring_n=8), STRIPE, 0.95))
    # dust puffs + pebbles at the base
    for i,(px,pz,pr) in enumerate([(-0.22,0.10,0.10),(0.20,0.05,0.085),(0.05,-0.20,0.075),
                                   (-0.05,0.22,0.065),(0.26,-0.14,0.06)]):
        P.append((f'Puff_{i}', ell(pr,pr*0.7,pr,[px,pr*0.55,pz]), (232,198,148,255)))
    for i in range(8):
        a=rng.uniform(0,2*np.pi); rr=rng.uniform(0.18,0.40)
        pr=rng.uniform(0.018,0.035)
        P.append((f'Pebble_{i}', ell(pr,pr,pr,[rr*np.cos(a),0.05+rng.uniform(0,0.25),rr*np.sin(a)],2),
                  (232,198,148,255)))
    export(P,path,scale=1.5/1.55)

# ================================================== KAABA
def kaaba(path):
    P=[]
    BLACK=(52,44,42,255); BAND=(232,196,126,255)
    P.append(('Cube', rbox(1.0,1.05,1.0,[0,0.525,0],e=0.22,subdiv=3), BLACK))
    # kiswa band around the top on all 4 sides
    bandy=0.82
    P.append(('Band_F', rbox(1.06,0.13,0.05,[0,bandy,0.50],e=0.35), BAND))
    P.append(('Band_B', rbox(1.06,0.13,0.05,[0,bandy,-0.50],e=0.35), BAND))
    P.append(('Band_L', rbox(0.05,0.13,1.06,[-0.50,bandy,0],e=0.35), BAND))
    P.append(('Band_R', rbox(0.05,0.13,1.06,[0.50,bandy,0],e=0.35), BAND))
    # band deco marks (front + right visible faces get them; do all faces lightly)
    for face,(fx,fz,ax) in {'F':(0,0.535,'x'),'B':(0,-0.535,'x'),
                            'L':(-0.535,0,'z'),'R':(0.535,0,'z')}.items():
        for k in range(3):
            off=-0.28+k*0.28
            if ax=='x': c=[off,bandy,fz]
            else: c=[fx,bandy,off]
            P.append((f'BandDeco_{face}_{k}', rbox(0.14 if ax=='x' else 0.02,0.045,
                     0.02 if ax=='x' else 0.14, c, e=0.45), (206,162,92,255)))
    # lower plaques row + diamonds
    py=0.62
    for face,(fz,ax) in {'F':(0.515,'x'),'B':(-0.515,'x')}.items():
        for k in range(3):
            off=-0.30+k*0.30
            P.append((f'Plaque_{face}_{k}', rbox(0.17,0.075,0.03,[off,py,fz],e=0.4), BAND))
        for k in range(2):
            off=-0.15+k*0.30
            d=rbox(0.05,0.075,0.03,[off,py,fz],e=0.5,T=rotZ(np.pi/4))
            P.append((f'Dia_{face}_{k}', d, BAND))
    for face,(fx,ax) in {'L':(-0.515,'z'),'R':(0.515,'z')}.items():
        for k in range(3):
            off=-0.30+k*0.30
            P.append((f'Plaque_{face}_{k}', rbox(0.03,0.075,0.17,[fx,py,off],e=0.4), BAND))
    # door on the front, offset left
    dx=-0.28
    P.append(('Door_Frame', rbox(0.20,0.52,0.045,[dx,0.42,0.515],e=0.35), BAND))
    P.append(('Door_P1', rbox(0.14,0.13,0.05,[dx,0.58,0.52],e=0.4), (214,176,106,255)))
    P.append(('Door_P2', rbox(0.14,0.10,0.05,[dx,0.44,0.52],e=0.5), (214,176,106,255)))
    P.append(('Door_P3', rbox(0.14,0.16,0.05,[dx,0.27,0.52],e=0.4), (214,176,106,255)))
    P.append(('Door_Split', rbox(0.015,0.15,0.052,[dx,0.27,0.522],e=0.5), (196,158,90,255)))
    P.append(('Door_Lock', ell(0.022,0.028,0.015,[dx,0.30,0.55],1), (186,148,84,255)))
    export(P,path,scale=1.3/1.05)

# ================================================== HIVE
def hive(path):
    P=[('Slab', rbox(0.95,0.12,0.45,[0,0.06,0.02],e=0.28,subdiv=3), (216,196,168,255))]
    BACK=(238,196,120,255); RIM1=(212,132,84,255); RIM2=(232,178,104,255)
    CELL=(178,102,58,255); HONEY=(216,150,60,255)
    P.append(('Comb_Back', ell(0.62,0.62,0.10,[0,0.72,-0.03]), BACK))
    R=0.105; sx=0.185; sy=0.162
    rows=[5,6,7,6,7,6,5]
    honey_cells={(1,4),(2,2),(4,4),(4,5)}
    idx=0
    for ri,cnt in enumerate(rows):
        yy=0.72+ (len(rows)//2 - ri)*sy
        for ci in range(cnt):
            xx=(ci-(cnt-1)/2)*sx
            idx+=1
            rim = RIM1 if (ri+ci)%2 else RIM2
            P.append((f'Cell_{ri}_{ci}', hexprism(R,0.10,[xx,yy,0.02],rot=np.pi/6), rim))
            if (ri,ci) in honey_cells:
                hn=hexprism(R*0.68,0.10,[xx,yy,0.045],rot=np.pi/6)
                P.append((f'Honey_{ri}_{ci}', hn, HONEY))
            else:
                inn=hexprism(R*0.66,0.06,[xx,yy,0.028],rot=np.pi/6)
                P.append((f'In_{ri}_{ci}', inn, CELL))
    # two tiny bees
    for bi,(bx,by,a) in enumerate([(-0.13,0.86,0.4),(0.16,0.60,-0.5)]):
        bb=ell(0.045,0.03,0.03,[0,0,0],2); bb.apply_transform(rotY(a))
        bb.apply_translation([bx,by,0.11]); P.append((f'Bee_{bi}', bb, (232,198,110,255)))
        for k in range(2):
            st=ell(0.008,0.028,0.028,[0,0,0],1); st.apply_transform(rotY(a))
            st.apply_translation([bx-0.012+k*0.022,by,0.11])
            P.append((f'Bee_{bi}_S{k}', st, (72,58,44,255)))
        for s in (1,-1):
            w=ell(0.03,0.012,0.018,[0,0,0],1,flat=True); w.apply_transform(rotZ(s*0.5)); w.apply_transform(rotY(a))
            w.apply_translation([bx,by+0.028,0.10]); P.append((f'Bee_{bi}_W{s}', w, (245,240,225,255)))
    export(P,path,scale=0.85/1.40)

O='/home/claude/'
rooster(O+'rooster.glb'); seated_sahabe(O+'seated_sahabe.glb')
vortex(O+'vortex_swirl.glb'); kaaba(O+'kaaba.glb'); hive(O+'hive.glb')
