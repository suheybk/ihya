"""Batch 5 (Ihya mechanics): arg villagers, qadi, plaintiff, beggar, trust owner/pouch,
dispute item, coop, mud doorway, shade bench, public fountain. v2 toolkit."""
import numpy as np
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual import TextureVisuals

rng = np.random.default_rng(9)

def lin(c): return [(x/255.0)**2.2 for x in c[:3]]+[1.0]
def M(c): return TextureVisuals(material=PBRMaterial(baseColorFactor=lin(c),
                                roughnessFactor=0.9, metallicFactor=0.0))
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
def cyl(r,h,c,sec=20,axis='y'):
    m=trimesh.creation.cylinder(radius=r,height=h,sections=sec)
    if axis=='y': m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
    elif axis=='x': m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0]))
    m.apply_translation(c); return m
def torus_xz(rx,rz,minor,c,sec=28):
    m=trimesh.creation.torus(major_radius=1.0,minor_radius=minor,
                             major_sections=sec,minor_sections=10)
    m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
    m.apply_scale([rx,1.0,rz]); m.apply_translation(c); return m
def rotX(a): return trimesh.transformations.rotation_matrix(a,[1,0,0])
def rotY(a): return trimesh.transformations.rotation_matrix(a,[0,1,0])
def rotZ(a): return trimesh.transformations.rotation_matrix(a,[0,0,1])
def export(P,path,scale=1.0):
    sc=trimesh.Scene(); t=0
    for n,m,c in P:
        if scale!=1.0: m.apply_scale(scale)
        m.visual=M(c); sc.add_geometry(m,node_name=n,geom_name=n); t+=len(m.faces)
    sc.export(path); print(f'{path.split("/")[-1]:22s} {len(P):3d} parts {t:6d} tris')

SKIN=(233,172,120,255); CREAM=(242,233,208,255); GOLD=(206,176,104,255)
TERRA=(204,112,74,255); OLIVE=(150,148,94,255);  SAND=(236,203,150,255)
EYE=(74,50,40,255)

# ---------- shared face helpers ----------
def face(P,hy,hz,expr='calm',s=1.0):
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Eye_{nm}', ell(0.014*s,0.018*s,0.010*s,[sx*0.045*s,hy+0.005,hz+0.095*s],2), EYE))
        if expr=='angry':
            b=cap([sx*0.065*s,hy+0.055,hz+0.085*s],[sx*0.022*s,hy+0.032,hz+0.093*s],0.010*s,8)
        elif expr=='sad':
            b=cap([sx*0.062*s,hy+0.035,hz+0.085*s],[sx*0.024*s,hy+0.05,hz+0.092*s],0.008*s,8)
        else:
            b=cap([sx*0.062*s,hy+0.045,hz+0.085*s],[sx*0.024*s,hy+0.05,hz+0.09*s],0.007*s,8)
        P.append((f'Brow_{nm}', b, (120,80,58,255)))
    P.append(('Nose', ell(0.014*s,0.022*s,0.018*s,[0,hy-0.02,hz+0.105*s],2), SKIN))
    if expr=='angry':
        P.append(('Mouth', cap([-0.018*s,hy-0.075,hz+0.095*s],[0,hy-0.065,hz+0.098*s],0.007*s,8), (150,90,70,255)))
        P.append(('Mouth2', cap([0,hy-0.065,hz+0.098*s],[0.018*s,hy-0.075,hz+0.095*s],0.007*s,8), (150,90,70,255)))
    elif expr=='sad':
        P.append(('Mouth', cap([-0.014*s,hy-0.068,hz+0.095*s],[0.014*s,hy-0.068,hz+0.095*s],0.006*s,8), (170,105,80,255)))
    else:
        P.append(('Mouth', cap([-0.016*s,hy-0.07,hz+0.096*s],[0.016*s,hy-0.07,hz+0.096*s],0.006*s,8), (170,105,80,255)))

def headscarf(P,hy,col=CREAM,band=(196,164,132,255)):
    P.append(('Scarf_Top', ell(0.128,0.088,0.122,[0,hy+0.085,0.0]), col))
    P.append(('Scarf_Band', torus_xz(0.121,0.116,0.018,[0,hy+0.055,0.0]), band))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Scarf_Side_{nm}', rbox(0.05,0.28,0.095,[sx*0.118,hy-0.07,-0.02],e=0.35), col))
    P.append(('Scarf_Back', rbox(0.185,0.28,0.05,[0,hy-0.07,-0.10],e=0.35), col))

# ================================================== ARG VILLAGER A (pointing)
def villager_a(path):
    P=[('Base', cyl(0.34,0.06,[0,0.03,0],28), (238,214,178,255))]
    RED=(206,110,84,255); HOODC=(233,196,142,255)
    P.append(('Tunic', ell(0.16,0.30,0.13,[0,0.55,0]), RED))
    P.append(('Skirt', ell(0.15,0.14,0.125,[0,0.33,0]), RED))
    P.append(('Belt', torus_xz(0.15,0.125,0.032,[0,0.45,0]), OLIVE))
    P.append(('Belt_Tail', rbox(0.055,0.19,0.03,[0.07,0.33,0.115],e=0.4,T=rotZ(0.1)), OLIVE))
    P.append(('Head', ell(0.115,0.12,0.11,[0,0.99,0.02]), SKIN))
    face(P,0.99,0.02,'angry')
    # hood: dome + face-frame + drape
    P.append(('Hood_Top', ell(0.126,0.10,0.122,[0,1.06,0.0]), HOODC))
    P.append(('Hood_Band', torus_xz(0.118,0.114,0.016,[0,1.075,0.0]), OLIVE))
    fr=trimesh.creation.torus(major_radius=0.115,minor_radius=0.028,major_sections=26,minor_sections=10)
    fr.apply_translation([0,0.985,0.055])
    P.append(('Hood_Frame', fr, CREAM))
    P.append(('Hood_Drape', rbox(0.22,0.26,0.09,[0,0.85,-0.055],e=0.35), HOODC))
    # pointing right arm (his left, +x... point to -x side like image): extended arm
    P.append(('Arm_Point', cap([-0.14,0.72,0.03],[-0.40,0.78,0.06],0.045), RED if False else SKIN))
    P.append(('Sleeve_Point', cap([-0.13,0.72,0.03],[-0.24,0.755,0.045],0.055), RED))
    P.append(('Hand_Point', ell(0.042,0.038,0.05,[-0.43,0.785,0.065],2), SKIN))
    P.append(('Finger', rbox(0.09,0.022,0.022,[-0.50,0.79,0.065],e=0.4), SKIN))
    # other hand on hip
    P.append(('Sleeve_Hip', cap([0.14,0.72,0.02],[0.20,0.58,0.03],0.055), RED))
    P.append(('Arm_Hip', cap([0.20,0.58,0.03],[0.14,0.47,0.06],0.04), SKIN))
    P.append(('Hand_Hip', ell(0.04,0.045,0.04,[0.13,0.455,0.07],2), SKIN))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Leg_{nm}', cyl(0.045,0.16,[sx*0.07,0.13,0.01],14), SKIN))
        P.append((f'Sandal_{nm}', ell(0.055,0.02,0.10,[sx*0.07,0.045,0.04],2), OLIVE))
        P.append((f'Strap_{nm}', cap([sx*0.04,0.065,0.03],[sx*0.10,0.065,0.03],0.010,8), OLIVE))
    export(P,path,scale=1.7/1.16)

# ================================================== ARG VILLAGER B (arms crossed)
def villager_b(path):
    P=[('Base', rbox(0.62,0.05,0.5,[0,0.025,0.02],e=0.25), (226,200,164,255))]
    GRN=(146,144,92,255); TRIM=(240,232,204,255); HAIR=(122,88,66,255)
    P.append(('Tunic', ell(0.165,0.30,0.135,[0,0.55,0]), GRN))
    P.append(('Hem', torus_xz(0.145,0.12,0.028,[0,0.335,0]), TRIM))
    P.append(('Collar_V1', cap([-0.045,0.80,0.10],[0,0.745,0.115],0.012,8), TRIM))
    P.append(('Collar_V2', cap([0.045,0.80,0.10],[0,0.745,0.115],0.012,8), TRIM))
    P.append(('Head', ell(0.118,0.122,0.112,[0,0.99,0.02]), SKIN))
    face(P,0.99,0.02,'angry')
    P.append(('Hair', ell(0.128,0.105,0.12,[0,1.045,-0.005]), HAIR))
    for i,(hx,a) in enumerate([(-0.06,0.35),(0.0,-0.2),(0.06,0.3)]):
        h=ell(0.05,0.024,0.032,[0,0,0],2,flat=True); h.apply_transform(rotZ(a))
        h.apply_translation([hx,1.06,0.10]); P.append((f'Bang_{i}',h,HAIR))
    # crossed arms
    P.append(('Sleeve_L', cap([0.15,0.72,0.04],[0.10,0.62,0.115],0.055), GRN))
    P.append(('Cuff_L', cap([0.10,0.625,0.115],[0.08,0.61,0.125],0.056,10), TRIM))
    P.append(('Fore_L', cap([0.08,0.61,0.125],[-0.11,0.585,0.135],0.038), SKIN))
    P.append(('Hand_L', ell(0.04,0.035,0.04,[-0.13,0.60,0.135],2), SKIN))
    P.append(('Sleeve_R', cap([-0.15,0.72,0.04],[-0.10,0.60,0.11],0.055), GRN))
    P.append(('Cuff_R', cap([-0.10,0.605,0.11],[-0.08,0.59,0.12],0.056,10), TRIM))
    P.append(('Fore_R', cap([-0.08,0.565,0.12],[0.11,0.545,0.13],0.038), SKIN))
    P.append(('Hand_R', ell(0.04,0.035,0.04,[0.13,0.56,0.13],2), SKIN))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Leg_{nm}', cyl(0.048,0.17,[sx*0.07,0.135,0.01],14), SKIN))
        P.append((f'Sandal_{nm}', ell(0.056,0.02,0.10,[sx*0.07,0.045,0.04],2), GOLD))
        P.append((f'SStrap_{nm}', cap([sx*0.04,0.066,0.03],[sx*0.10,0.066,0.03],0.010,8), GOLD))
    export(P,path,scale=1.7/1.15)

# ================================================== QADI (scales in hand)
def qadi(path):
    P=[('Base', ell(0.42,0.09,0.34,[0,0.075,0]), SAND)]
    ROBE=(152,150,102,255); TRIMG=(200,172,96,255); SASH=(216,196,158,255)
    P.append(('Robe', ell(0.165,0.36,0.135,[0,0.56,0]), ROBE))
    P.append(('Robe_Low', ell(0.15,0.16,0.125,[0,0.30,0]), ROBE))
    for sx in (1,-1):
        P.append((f'Trim_{sx}', rbox(0.045,0.56,0.02,[sx*0.075,0.55,0.125],e=0.4), TRIMG))
    P.append(('Belt', torus_xz(0.145,0.12,0.024,[0,0.48,0]), SASH))
    P.append(('Belt_Knot', cap([0.02,0.47,0.12],[0.05,0.36,0.13],0.016,8), SASH))
    P.append(('Neck_Scarf', torus_xz(0.10,0.09,0.035,[0,0.83,0.01]), SASH))
    P.append(('Scarf_Tail', rbox(0.07,0.22,0.03,[0.05,0.70,0.125],e=0.4), SASH))
    P.append(('Head', ell(0.115,0.12,0.11,[0,1.0,0.02]), SKIN))
    face(P,1.0,0.02,'calm')
    # turban wrap
    P.append(('Turban', ell(0.132,0.095,0.126,[0,1.075,0.0]), (226,204,158,255)))
    tw=trimesh.creation.torus(major_radius=0.115,minor_radius=0.032,major_sections=26,minor_sections=10)
    tw.apply_transform(rotX(np.pi/2-0.15)); tw.apply_translation([0,1.03,0.02])
    P.append(('Turban_Wrap', tw, CREAM))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Side_{nm}', rbox(0.045,0.22,0.085,[sx*0.115,0.90,-0.015],e=0.35), CREAM))
    # left arm down; right arm bent holding scales
    P.append(('Sleeve_L', cap([-0.14,0.80,0.02],[-0.22,0.56,0.05],0.055), ROBE))
    P.append(('Hand_L', ell(0.042,0.05,0.042,[-0.225,0.51,0.055],2), SKIN))
    P.append(('Sleeve_R', cap([0.14,0.80,0.02],[0.26,0.66,0.09],0.055), ROBE))
    P.append(('Cuff_R', cap([0.245,0.675,0.085],[0.27,0.655,0.095],0.058,10), TRIMG))
    P.append(('Hand_R', ell(0.045,0.05,0.045,[0.30,0.64,0.10],2), SKIN))
    # handheld scales
    hx,hy,hz=0.30,0.64,0.10
    P.append(('Sc_Knob', ell(0.02,0.025,0.02,[hx,hy+0.075,hz],2), TRIMG))
    P.append(('Sc_Rod', cyl(0.011,0.10,[hx,hy+0.02,hz],10), TRIMG))
    P.append(('Sc_Beam', rbox(0.34,0.025,0.025,[hx,hy-0.035,hz],e=0.4), TRIMG))
    for sx,nm in [(1,'R'),(-1,'L')]:
        ex=hx+sx*0.155
        for k,off in enumerate([-0.05,0.05]):
            P.append((f'Str_{nm}_{k}', cap([ex,hy-0.04,hz],[ex+off*0.6,hy-0.16,hz+off],0.006,6), CREAM))
        pan=trimesh.creation.icosphere(subdivisions=2,radius=1.0)
        pan.apply_scale([0.065,0.028,0.055]); pan.apply_translation([ex,hy-0.17,hz]); pan.unmerge_vertices()
        P.append((f'Pan_{nm}', pan, TERRA))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Shoe_{nm}', ell(0.05,0.038,0.085,[sx*0.07,0.055,0.05],2), (176,96,66,255)))
    export(P,path,scale=1.8/1.23)

# ================================================== PLAINTIFF (pointing, robed)
def plaintiff(path):
    P=[]
    COAT=(198,116,82,255); INNER=(226,182,120,255); CUFF=(206,176,96,255)
    P.append(('Robe', ell(0.165,0.34,0.135,[0,0.55,0]), COAT))
    P.append(('Inner', ell(0.08,0.31,0.13,[0,0.53,0.035]), INNER))
    P.append(('Robe_Low', ell(0.15,0.15,0.125,[0,0.31,0]), INNER))
    P.append(('Belt', rbox(0.13,0.05,0.03,[0,0.50,0.13],e=0.4), CUFF))
    P.append(('Head', ell(0.115,0.12,0.11,[0,0.99,0.02]), SKIN))
    face(P,0.99,0.02,'angry')
    headscarf(P,0.99,col=CREAM,band=(210,186,150,255))
    # pointing arm (+x side, extended)
    P.append(('Sleeve_Point', cap([0.14,0.76,0.03],[0.30,0.79,0.05],0.058), COAT))
    P.append(('Cuff_Point', cap([0.285,0.788,0.048],[0.315,0.792,0.052],0.06,10), CUFF))
    P.append(('Fore_Point', cap([0.315,0.79,0.052],[0.44,0.80,0.06],0.038), SKIN))
    P.append(('Hand_Point', ell(0.05,0.035,0.045,[0.47,0.80,0.062],2), SKIN))
    P.append(('Sleeve_Dn', cap([-0.14,0.76,0.02],[-0.21,0.53,0.04],0.055), COAT))
    P.append(('Cuff_Dn', cap([-0.205,0.545,0.038],[-0.215,0.52,0.042],0.057,10), CUFF))
    P.append(('Hand_Dn', ell(0.04,0.05,0.04,[-0.215,0.48,0.045],2), SKIN))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Leg_{nm}', cyl(0.045,0.14,[sx*0.065,0.10,0.01],14), SKIN))
        P.append((f'Sandal_{nm}', ell(0.055,0.02,0.095,[sx*0.065,0.022,0.04],2), (176,120,78,255)))
    export(P,path,scale=1.7/1.14)

# ================================================== BEGGAR (seated, bowl)
def beggar(path):
    P=[]
    ROBE=(172,152,132,255); WALL=(224,164,124,255)
    P.append(('Floor', rbox(0.95,0.07,0.85,[0,0.035,0.18],e=0.25), WALL))
    P.append(('Wall', rbox(0.95,0.95,0.12,[0,0.52,-0.22],e=0.25), WALL))
    # seated body
    P.append(('Torso', ell(0.185,0.24,0.15,[0,0.42,0.05]), ROBE))
    P.append(('Sash', rbox(0.08,0.30,0.03,[0.075,0.48,0.16],e=0.4,T=rotZ(-0.45)), (160,140,120,255)))
    # crossed legs
    lg1=cap([-0.16,0.16,0.22],[0.15,0.13,0.30],0.075); P.append(('Leg_L',lg1,ROBE))
    lg2=cap([0.16,0.16,0.22],[-0.15,0.13,0.30],0.075); P.append(('Leg_R',lg2,ROBE))
    P.append(('Foot_L', ell(0.045,0.035,0.075,[0.19,0.11,0.33],2), SKIN))
    P.append(('Foot_R', ell(0.045,0.035,0.075,[-0.19,0.11,0.33],2), SKIN))
    # head + sad face
    P.append(('Head', ell(0.115,0.12,0.11,[0,0.76,0.08]), SKIN))
    face(P,0.76,0.08,'sad')
    P.append(('Scarf_Top', ell(0.126,0.085,0.12,[0,0.835,0.06]), CREAM))
    P.append(('Scarf_Band', torus_xz(0.119,0.114,0.016,[0,0.805,0.06]), GOLD))
    for i,(hx,a) in enumerate([(-0.05,0.3),(0.01,-0.15),(0.06,0.35)]):
        h=ell(0.045,0.02,0.03,[0,0,0],2,flat=True); h.apply_transform(rotZ(a))
        h.apply_translation([hx,0.845,0.155]); P.append((f'Bang_{i}',h,(196,168,132,255)))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Scarf_Side_{nm}', rbox(0.045,0.22,0.085,[sx*0.115,0.70,0.04],e=0.35), CREAM))
    # arms holding bowl
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Sleeve_{nm}', cap([sx*0.155,0.55,0.09],[sx*0.09,0.40,0.24],0.05), ROBE))
        P.append((f'Hand_{nm}', ell(0.04,0.032,0.05,[sx*0.055,0.375,0.27],2), SKIN))
    P.append(('Bowl', cyl(0.075,0.055,[0,0.40,0.27],18), GOLD))
    P.append(('Bowl_In', cyl(0.06,0.015,[0,0.425,0.27],16), (170,142,78,255)))
    export(P,path,scale=1.2/0.99)

# ================================================== TRUST OWNER (waiting)
def trust_owner(path):
    P=[('Base', ell(0.40,0.09,0.32,[0,0.075,0]), SAND)]
    COAT=(148,150,100,255); INNER=(226,186,124,255); SASH=(198,108,72,255)
    P.append(('Coat', ell(0.165,0.34,0.135,[0,0.56,0]), COAT))
    P.append(('Inner', ell(0.082,0.31,0.13,[0,0.54,0.035]), INNER))
    P.append(('Inner_Low', ell(0.145,0.15,0.12,[0,0.315,0]), INNER))
    P.append(('Sash', torus_xz(0.135,0.115,0.026,[0,0.52,0]), SASH))
    P.append(('Sash_T1', rbox(0.045,0.17,0.028,[-0.025,0.41,0.125],e=0.4), SASH))
    P.append(('Sash_T2', rbox(0.045,0.15,0.028,[0.035,0.42,0.125],e=0.4,T=rotZ(-0.08)), SASH))
    P.append(('Head', ell(0.115,0.12,0.11,[0,1.0,0.02]), SKIN))
    face(P,1.0,0.02,'calm')
    headscarf(P,1.0)
    # hands meet at the sash
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Sleeve_{nm}', cap([sx*0.145,0.80,0.02],[sx*0.13,0.60,0.10],0.055), COAT))
        P.append((f'Hand_{nm}', ell(0.045,0.04,0.05,[sx*0.075,0.52,0.145],2), SKIN))
    for sx,nm in [(1,'L'),(-1,'R')]:
        P.append((f'Leg_{nm}', cyl(0.045,0.13,[sx*0.065,0.115,0.01],14), SKIN))
        P.append((f'Sandal_{nm}', ell(0.055,0.02,0.095,[sx*0.065,0.045,0.04],2), (196,116,80,255)))
    export(P,path,scale=1.7/1.23)

# ================================================== TRUST POUCH
def trust_pouch(path):
    P=[('Mound', ell(0.42,0.10,0.34,[0,0.07,0]), (229,178,120,255))]
    for i,(lx,lz,a) in enumerate([(-0.26,0.10,2.4),(0.28,-0.06,-0.5)]):
        for j in range(5):
            lf=rbox(0.14,0.012,0.03,[0,0,0],e=0.45,T=rotY(a+j*0.35))
            lf.apply_translation([lx,0.125,lz]); P.append((f'Leaf_{i}_{j}',lf,GOLD))
    body=trimesh.creation.icosphere(subdivisions=2,radius=1.0)
    body.apply_scale([0.26,0.24,0.24]); body.apply_translation([0,0.32,0]); body.unmerge_vertices()
    P.append(('Pouch', body, (240,232,210,255)))
    P.append(('Neck', ell(0.10,0.10,0.095,[0,0.55,0]), (240,232,210,255)))
    # ruffled top
    for k in range(6):
        a=k*np.pi/3
        P.append((f'Ruffle_{k}', ell(0.05,0.055,0.04,[0.075*np.cos(a),0.635,0.07*np.sin(a)],2), (240,232,210,255)))
    P.append(('Rope1', torus_xz(0.105,0.10,0.020,[0,0.505,0]), (216,178,110,255)))
    P.append(('Rope2', torus_xz(0.102,0.098,0.018,[0,0.475,0]), (216,178,110,255)))
    P.append(('Rope_T1', cap([0.08,0.47,0.07],[0.13,0.33,0.10],0.016,8), (216,178,110,255)))
    P.append(('Rope_T2', cap([0.08,0.47,0.07],[0.05,0.32,0.12],0.016,8), (216,178,110,255)))
    # wax seal
    sl=ell(0.055,0.05,0.02,[0,0,0],2,flat=True); sl.apply_transform(rotX(0.5)); sl.apply_translation([0.09,0.50,0.085])
    P.append(('Seal', sl, (198,96,66,255)))
    P.append(('Seal_In', ell(0.028,0.026,0.012,[0.093,0.503,0.098],1), (178,84,58,255)))
    export(P,path,scale=0.3/0.68)

# ================================================== DISPUTE ITEM
def dispute_item(path):
    P=[('Mound', ell(0.50,0.11,0.40,[0,0.075,0],2,flat=True), (206,116,80,255))]
    st=rbox(0.34,0.62,0.16,[-0.10,0.42,-0.08],e=0.30,subdiv=3)
    P.append(('Boundary_Stone', st, (212,178,96,255)))
    sk=ell(0.20,0.11,0.15,[0.10,0.20,0.12],3); P.append(('Sack', sk, (240,230,204,255)))
    P.append(('Sack_Mark', rbox(0.09,0.02,0.05,[0.09,0.30,0.13],e=0.45), (226,214,184,255)))
    # fallen amphora
    am=ell(0.11,0.13,0.11,[0,0,0]); am.apply_transform(rotZ(np.pi/2*0.9)); am.apply_translation([0.33,0.20,0.11])
    P.append(('Jar_Body', am, (206,116,74,255)))
    nk=cyl(0.05,0.09,[0,0,0],14); nk.apply_transform(rotZ(np.pi/2*0.9)); nk.apply_translation([0.33,0.30,0.09])
    P.append(('Jar_Neck', nk, (206,116,74,255)))
    rm=torus_xz(0.06,0.06,0.016,[0,0,0],18); rm.apply_transform(rotZ(np.pi/2*0.9)); rm.apply_translation([0.33,0.345,0.085])
    P.append(('Jar_Rim', rm, (206,116,74,255)))
    for j in range(3):
        lf=ell(0.02,0.075,0.035,[0,0,0],2,flat=True); lf.apply_transform(rotZ(0.4*(j-1)))
        lf.apply_translation([-0.30+0.04*j,0.20,0.09]); P.append((f'Leaf_{j}',lf,OLIVE))
    export(P,path,scale=0.4/0.73)

# ================================================== COOP
def mini_chicken(P,prefix,cx,cz,yaw,peck=False,rooster=False):
    T=rotY(yaw); base=np.array([cx,0,cz])
    tilt=rotX(0.55) if peck else None
    b=ell(0.085,0.09,0.11,[0,0,0])
    if tilt is not None: b.apply_transform(tilt)
    b.apply_transform(T); b.apply_translation(base+[0,0.16,0])
    P.append((f'{prefix}_Body',b,(242,235,214,255)))
    hz=0.13 if not peck else 0.16
    hy=0.27 if not peck else 0.17
    h=ell(0.055,0.065,0.05,[0,0,0]); h.apply_transform(T); h.apply_translation(base+[0,hy,hz*np.cos(yaw)] if False else base+np.array([hz*np.sin(yaw),hy,hz*np.cos(yaw)]))
    P.append((f'{prefix}_Head',h,(242,235,214,255)))
    hp=base+np.array([hz*np.sin(yaw),hy,hz*np.cos(yaw)])
    cmb=ell(0.014,0.035 if rooster else 0.022,0.03,[0,0,0],1,flat=True)
    cmb.apply_transform(T); cmb.apply_translation(hp+[0,0.06,0])
    P.append((f'{prefix}_Comb',cmb,(216,90,80,255)))
    bk=ell(0.016,0.014,0.025,[0,0,0],1,flat=True); bk.apply_transform(T)
    bk.apply_translation(hp+np.array([0.05*np.sin(yaw),-0.005,0.05*np.cos(yaw)]))
    P.append((f'{prefix}_Beak',bk,(214,140,80,255)))
    tl=ell(0.03,0.055,0.03,[0,0,0],2,flat=True); tl.apply_transform(rotX(-0.5)); tl.apply_transform(T)
    tl.apply_translation(base+np.array([-0.10*np.sin(yaw),0.24,-0.10*np.cos(yaw)]))
    P.append((f'{prefix}_Tail',tl,(226,186,120,255) if rooster else (238,229,204,255)))

def coop(path):
    P=[('Pad', rbox(1.6,0.06,1.5,[0,0.03,0.1],e=0.25), (231,178,128,255))]
    HUT=(224,164,124,255); ROOF=(206,116,80,255); WOOD=(196,110,74,255)
    # hut on stilts
    P.append(('Hut', rbox(0.85,0.62,0.70,[0,0.62,-0.30],e=0.28), HUT))
    for i,(bx,by) in enumerate([(-0.25,0.80),(0.30,0.55),(-0.28,0.45),(0.33,0.78)]):
        P.append((f'Hut_Brick_{i}', rbox(0.15,0.055,0.03,[bx,by,0.052-0.30+0.31],e=0.4), (232,182,142,255)))
    P.append(('Lintel', rbox(0.34,0.07,0.05,[0,0.79,0.058]), GOLD))
    P.append(('Door', rbox(0.24,0.34,0.05,[0,0.60,0.055],e=0.3), (92,58,44,255)))
    for s,nm in [(1,'R'),(-1,'L')]:
        r=rbox(0.62,0.055,0.85,[0,0,0],e=0.3,T=rotZ(-s*0.62))
        r.apply_translation([s*0.245,1.06,-0.30]); P.append((f'Roof_{nm}',r,ROOF))
    P.append(('Ridge', cap([0,1.20,-0.70],[0,1.20,0.10],0.045), ROOF))
    for s in (1,-1):
        P.append((f'Stilt_{s}', rbox(0.08,0.32,0.08,[s*0.32,0.16,-0.02]), WOOD))
    # ramp with steps
    rp=rbox(0.22,0.04,0.42,[0,0,0],e=0.35,T=rotX(0.55)); rp.apply_translation([0,0.28,0.28])
    P.append(('Ramp', rp, HUT))
    for k in range(4):
        P.append((f'Step_{k}', rbox(0.20,0.02,0.045,[0,0.14+k*0.09,0.42-k*0.10],e=0.45), GOLD))
    # fence: posts + rails + lattice
    posts=[(-0.75,0.55),(-0.75,0.0),(-0.75,-0.55),(0.75,0.55),(0.75,0.0),(0.75,-0.55),
           (-0.38,0.62),(0.38,0.62)]
    for i,(px,pz) in enumerate(posts):
        P.append((f'Post_{i}', rbox(0.11,0.44,0.11,[px,0.24,pz],e=0.3), TERRA))
    rails=[((-0.75,0.55),(-0.75,-0.55)),((0.75,0.55),(0.75,-0.55)),
           ((-0.75,0.62),(-0.38,0.62)),((0.38,0.62),(0.75,0.62))]
    for i,((x1,z1),(x2,z2)) in enumerate(rails):
        P.append((f'Rail_{i}', cap([x1,0.40,z1],[x2,0.40,z2],0.028), GOLD))
        P.append((f'RailB_{i}', cap([x1,0.12,z1],[x2,0.12,z2],0.024), GOLD))
        n=4
        for k in range(n):
            t=k/(n-1) if n>1 else 0.5
            mx,mz=x1+(x2-x1)*t, z1+(z2-z1)*t
            dx,dz=(x2-x1)/n*0.9,(z2-z1)/n*0.9
            P.append((f'Lat_{i}_{k}a', cap([mx,0.13,mz],[mx+dx,0.39,mz+dz],0.012,6), GOLD))
            P.append((f'Lat_{i}_{k}b', cap([mx,0.39,mz],[mx+dx,0.13,mz+dz],0.012,6), GOLD))
    mini_chicken(P,'Hen1',-0.35,0.15,2.4,peck=True)
    mini_chicken(P,'Hen2',-0.15,0.30,0.6)
    mini_chicken(P,'Rooster',0.42,0.10,-2.2,peck=True,rooster=True)
    for i in range(5):
        P.append((f'Feed_{i}', rbox(0.05,0.012,0.018,[rng.uniform(-0.4,0.4),0.065,rng.uniform(0.0,0.5)],e=0.45,T=rotY(rng.uniform(0,3))), GOLD))
    for i,(gx,gz) in enumerate([(-0.95,0.3),(0.95,-0.2),(0.9,0.55)]):
        for j in range(3):
            g=ell(0.022,0.10,0.045,[0,0,0],2,flat=True); g.apply_transform(rotZ(0.4*(j-1)))
            g.apply_translation([gx+0.04*(j-1),0.09,gz]); P.append((f'Grass_{i}_{j}',g,OLIVE))
    export(P,path,scale=1.2/1.24)

# ================================================== MUD DOORWAY
def mud_doorway(path):
    P=[]
    FRAME=(224,148,100,255)
    for s,nm in [(1,'R'),(-1,'L')]:
        lg=rbox(0.26,1.15,0.34,[s*0.52,0.575,0],e=0.30,subdiv=3)
        P.append((f'Leg_{nm}', lg, FRAME))
    arch=trimesh.creation.torus(major_radius=0.52,minor_radius=0.155,major_sections=36,minor_sections=14)
    arch.apply_scale([1,1.05,1.10])
    arch.apply_translation([0,1.12,0])
    P.append(('Arch', arch, FRAME))
    P.append(('Interior', rbox(0.85,1.35,0.06,[0,0.75,-0.02],e=0.25), (128,62,44,255)))
    # olive curtain (gathered left) + cream curtain (right)
    for i in range(5):
        cx=-0.30+i*0.055
        w=0.09-0.008*i
        cph=ell(w,0.62-0.03*i,0.045,[0,0,0])
        cph.apply_transform(rotZ(0.12-0.05*i))
        cph.apply_translation([cx+0.05,0.72,0.06])
        P.append((f'Curtain_L_{i}', cph, (150,148,92,255)))
    P.append(('Tie', rbox(0.16,0.05,0.06,[-0.24,0.62,0.10],e=0.4,T=rotZ(0.25)), (226,182,120,255)))
    for i in range(4):
        cx=0.10+i*0.085
        P.append((f'Curtain_R_{i}', ell(0.055,0.60,0.04,[cx,0.66,0.05]), (240,232,206,255)))
    P.append(('Curtain_Top', ell(0.42,0.16,0.06,[0.0,1.28,0.03]), (150,148,92,255)))
    export(P,path,scale=1.8/1.83)

# ================================================== SHADE BENCH
def shade_bench(path):
    P=[]
    POLE=(186,172,96,255)
    for sx,nm in [(1,'R'),(-1,'L')]:
        P.append((f'Pole_{nm}', cyl(0.055,1.55,[sx*0.85,0.775,0.05],14), POLE))
        P.append((f'Brace_{nm}', cap([sx*0.85,1.30,0.05],[sx*0.45,1.52,0.0],0.035), POLE))
    P.append(('Beam_F', cap([-0.9,1.55,0.05],[0.9,1.55,0.05],0.05), POLE))
    P.append(('Canopy', rbox(1.9,0.12,1.0,[0,1.66,-0.05],e=0.3,subdiv=3), (242,234,210,255)))
    # hanging leaf thatch rows
    cols=[(150,148,94,255),(226,178,128,255),(170,162,98,255)]
    for r,zz in enumerate([0.42,0.18,-0.06,-0.30]):
        for i in range(9):
            lx=-0.85+i*0.21
            lf=ell(0.085,0.16,0.02,[0,0,0],2,flat=True)
            lf.apply_transform(rotX(0.35-0.1*r)); lf.apply_transform(rotZ(rng.uniform(-0.15,0.15)))
            lf.apply_translation([lx,1.60-0.03*r,zz])
            P.append((f'Leaf_{r}_{i}', lf, cols[(i+r)%3]))
    # block bench
    A=(214,138,104,255); B=(232,182,138,255)
    for sx,nm in [(1,'R'),(-1,'L')]:
        P.append((f'ArmLow_{nm}', rbox(0.34,0.24,0.44,[sx*0.62,0.12,0.02],e=0.3), A if sx>0 else B))
        P.append((f'ArmTop_{nm}', rbox(0.32,0.22,0.42,[sx*0.60,0.34,0.02],e=0.3), B if sx>0 else A))
    P.append(('Seat_Base1', rbox(0.50,0.20,0.40,[-0.18,0.10,0.02],e=0.3), B))
    P.append(('Seat_Base2', rbox(0.50,0.20,0.40,[0.22,0.10,0.02],e=0.3), (224,160,120,255)))
    P.append(('Seat', rbox(0.95,0.16,0.42,[0.02,0.26,0.02],e=0.3), (232,182,138,255)))
    P.append(('Back_L', rbox(0.40,0.18,0.10,[-0.22,0.42,-0.16],e=0.3), A))
    P.append(('Back_R', rbox(0.40,0.18,0.10,[0.20,0.42,-0.16],e=0.3), B))
    # small jar on the seat
    P.append(('Jar', ell(0.075,0.09,0.075,[0.42,0.42,0.02]), (206,116,74,255)))
    P.append(('Jar_Neck', cyl(0.035,0.05,[0.42,0.51,0.02],12), (206,116,74,255)))
    P.append(('Jar_Rim', torus_xz(0.042,0.042,0.012,[0.42,0.535,0.02],16), (206,116,74,255)))
    export(P,path,scale=2.0/1.9)

# ================================================== PUBLIC FOUNTAIN
def public_fountain(path):
    P=[('Ground', ell(0.85,0.10,0.70,[0,0.085,0.10],3), (236,198,138,255))]
    BODY=(230,160,112,255); WATER=(178,214,198,255)
    P.append(('Base_Ring', cyl(0.42,0.09,[0,0.10,0.22],28), (212,120,82,255)))
    P.append(('Basin', ell(0.40,0.22,0.34,[0,0.26,0.22]), BODY))
    P.append(('Basin_Rim', torus_xz(0.33,0.28,0.055,[0,0.40,0.22],28), BODY))
    P.append(('Water', cyl(0.27,0.02,[0,0.385,0.22],24), WATER))
    # back tower
    P.append(('Tower', rbox(0.55,0.85,0.30,[0,0.70,-0.10],e=0.28,subdiv=3), BODY))
    P.append(('Niche', rbox(0.30,0.48,0.06,[0,0.68,0.055],e=0.3), (212,138,96,255)))
    nr=trimesh.creation.torus(major_radius=0.15,minor_radius=0.035,major_sections=24,minor_sections=10)
    nr.apply_translation([0,0.83,0.07])
    P.append(('Niche_Arch', nr, BODY))
    # spout + water stream + bubbles
    sp=ell(0.09,0.08,0.06,[0,0.70,0.10],2,flat=True); P.append(('Spout_Boss', sp, (206,168,88,255)))
    P.append(('Spout', cyl(0.035,0.09,[0,0.665,0.145],12,axis='y') if False else cyl(0.035,0.10,[0,0.68,0.15],12), (206,168,88,255)))
    stream=cap([0,0.65,0.16],[0,0.42,0.20],0.028,10); P.append(('Stream', stream, WATER))
    for i,(bx,bz,r) in enumerate([(0.02,0.20,0.025),(-0.03,0.18,0.02),(0.05,0.16,0.015),(0.0,0.24,0.018)]):
        P.append((f'Bubble_{i}', ell(r,r,r,[bx,0.41,0.22+bz-0.20],2), WATER))
    # cap: rim + dome + finial
    P.append(('Cap_Rim', rbox(0.36,0.09,0.26,[0,1.16,-0.10],e=0.3), (212,120,82,255)))
    dm=ell(0.155,0.14,0.14,[0,1.26,-0.10]); P.append(('Dome', dm, (243,234,210,255)))
    P.append(('Finial', cap([0,1.38,-0.10],[0,1.45,-0.10],0.015,8), (206,168,88,255)))
    P.append(('Bowl_Ground', cyl(0.10,0.06,[0.48,0.045,0.52],18), OLIVE))
    P.append(('Bowl_In', cyl(0.08,0.015,[0.48,0.072,0.52],16), (128,126,76,255)))
    export(P,path,scale=1.3/1.46)

O='/home/claude/'
villager_a(O+'arg_villager_a.glb'); villager_b(O+'arg_villager_b.glb')
qadi(O+'qadi.glb'); plaintiff(O+'plaintiff.glb')
beggar(O+'beggar.glb'); trust_owner(O+'trust_owner.glb'); trust_pouch(O+'trust_pouch.glb')
dispute_item(O+'dispute_item.glb'); coop(O+'coop.glb')
mud_doorway(O+'mud_doorway.glb'); shade_bench(O+'shade_bench.glb')
public_fountain(O+'public_fountain.glb')
