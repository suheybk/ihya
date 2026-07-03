# 3D Model Prompt Listesi — İhya / Medine

Bu promptlar mevcut oyunun **claymorphism low-poly** stiline (Blender `ihya_world.blend`,
`models/*.glb`) uyacak şekilde yazıldı. Text-to-3D araçlarına (Meshy, Tripo, Rodin, Luma)
ya da referans görsel üretip Blender'da modellemek için kullanılabilir.

---

## 🎨 ORTAK STİL (her prompta ekle)
> **Style:** cute low-poly *claymorphism*, soft rounded beveled edges, smooth "clay finisher"
> look, matte surfaces, gentle warm lighting, friendly toy-like proportions. Flat-shade
> foliage/cloth/domes; smooth-shade bodies. Low triangle count (~60–200 tris). Solid vertex
> colors or simple materials, **no textures/text/logos**. Neutral A-pose, facing +Z.
> **Technical:** single object, origin at **base center (feet on ground)**, **Y-up**, real-world
> scale ~**1 m** tall unless noted, clean manifold mesh, export **GLB** (Draco'suz).
> **Palette:** warm sand, terracotta, olive-green, cream, muted gold — Medine/çöl-vaha hissi.

> **Adlandırma:** dosyaları koddaki `MODELS` dizisine uygun kısa isimle ver
> (ör. `sheep.glb`, `date_palm.glb`). Aşağıda her modelin önerilen dosya adı verildi.

---

## 🐑 1) Hayvanlar (çobanlık + random spawn)
Not: Hareket için gövde tek parça yeter; ama **bacaklar ayrı node** olursa (player gibi:
`legFL/legFR/legBL/legBR`) yürüme animasyonu yapabiliriz — mümkünse ayır.

1. **`sheep.glb` — Koyun**: fluffy woolly sheep, cream/off-white rounded wool body (bumpy
   low-poly wool), small dark face, tiny legs, stubby. Very cute, ~0.7 m.
2. **`goat.glb` — Keçi**: small tan/brown goat, little curved horns, short beard, slim legs,
   alert pose. ~0.7 m.
3. **`camel.glb` — Deve**: friendly one-hump (dromedary) camel, sandy-beige, long neck, calm
   expression, saddle blanket optional (muted red). ~1.8 m tall.
4. **`lamb.glb` — Kuzu** (opsiyonel): tiny baby version of sheep, softer, ~0.4 m.
5. **`chicken.glb` — Tavuk** (opsiyonel): little rounded hen, cream+red comb. ~0.35 m.

## 🌴 2) Meyve Ağaçları & Bitkiler (hasat/tekrarlanan iş)
1. **`date_palm.glb` — Hurma ağacı**: tall date palm, textured beige trunk (stacked ring
   segments), radial fan of flat-shaded green fronds at top, **clusters of golden-brown dates**
   hanging under the crown. Iconic Medine tree. ~3 m.
2. **`date_palm_bare.glb` — Hurma ağacı (hasat edilmiş)**: same palm **without date clusters**
   (topladıktan sonraki hali; tekrar büyüme için). ~3 m.
3. **`mulberry_tree.glb` — Dut ağacı**: rounded leafy tree, olive/green flat-shaded canopy
   clumps, brown trunk, **small dark-purple mulberries** dotting the canopy. ~2 m.
4. **`mulberry_tree_bare.glb` — Dut ağacı (toplanmış)**: same tree, berries removed. ~2 m.
5. **`wheat.glb` — Ekin/buğday demeti**: small golden wheat cluster/sheaf tuft on soil. ~0.5 m.
6. **`date_cluster.glb` — Hurma salkımı** (pickup): standalone hanging cluster of dates.

## 🛒 3) Medine Pazarı (Sûk)
1. **`market_stall.glb` — Pazar tezgâhı**: simple wooden market stall with striped cloth awning
   (muted red/cream), a flat counter, a couple of goods baskets on top. ~2 m.
2. **`basket.glb` — Sepet**: round woven basket (tan), optionally filled with dates/fruit. ~0.4 m.
3. **`sack.glb` — Çuval**: tied burlap grain sack, beige, slightly slumped. ~0.5 m.
4. **`scale.glb` — Terazi**: classic two-pan balance scale (muted gold/bronze) on a small
   stand — ticaret/ölçü sembolü. ~0.6 m.
5. **`jar.glb` — Testi/küp**: clay amphora/water jug, terracotta, rounded. ~0.6 m.
6. **`rug_market.glb` — Sergi kilimi** (opsiyonel): small patterned flat rug for goods display.

## 🏛️ 4) Yapılar
1. **`masjid_nabawi.glb` — Mescid-i Nebevî (sade)**: humble early mosque — **mud-brick (kerpiç)
   low walls**, **palm-trunk columns**, palm-frond flat roof, small open courtyard, NO minaret,
   NO dome (tarihe sadık, mütevazı). Warm sand tones. ~3–4 m wide. *(Mevcut `mosque.glb`'nin
   yerini alacak — daha sahih.)*
2. **`well.glb` — Kuyu**: round stone well with a small wooden frame/pulley and a bucket.
   Medine kuyuları. ~1.2 m.
3. **`suffa.glb` — Suffa (gölgelik)**: shaded low platform/bench with palm-frond canopy on
   simple posts (Ashâb-ı Suffa için). ~2 m.
4. **`tent.glb` — Çadır**: bedouin/muhâcir tent, muted striped cloth, open front. ~2 m.
5. **`palm_fence.glb` — Hurma bahçesi çiti** (opsiyonel): low woven palm-frond fence segment.

## 🧍 5) NPC Karakterler
Stil: mevcut `player.glb` ile aynı sadelik (yuvarlak, sevimli, low-poly). **Animasyon için
uzuvları ayrı node yap** (player'daki gibi `legL/legR/armL/armR/upper`).
1. **`orphan.glb` — Yetim çocuk**: small child, simple modest tunic (cream/earth tone), gentle
   sad-but-hopeful posture. ~0.7 m.
2. **`neighbor.glb` — Komşu / Ensâr**: adult in simple robe (olive/earth), welcoming pose. ~1 m.
3. **`merchant.glb` — Tüccar**: adult in slightly nicer robe + head wrap, standing behind
   goods. ~1 m.
4. **`shepherd.glb` — Çoban**: adult with a simple staff (asâ), earth-tone robe. ~1 m.
5. **`traveler.glb` — Muhâcir**: adult with a small shoulder bundle/bag, road-worn robe. ~1 m.

## 🎒 6) Toplanabilir Eşyalar & Envanter (pickup/ikon)
Küçük, tek nesne, zeminde/elde durabilir; envanterde ikon olarak da kullanılabilir.
1. **`item_date.glb` — Hurma**: a few golden-brown dates / small pile.
2. **`item_mulberry.glb` — Dut**: cluster of dark-purple mulberries.
3. **`item_milk.glb` — Süt testisi**: small clay jug with milk.
4. **`item_wool.glb` — Yün**: soft cream wool tuft/ball.
5. **`item_bread.glb` — Ekmek**: round flatbread / small loaf.
6. **`item_waterskin.glb` — Su kırbası**: leather waterskin.
7. **`seccade.glb` — Seccade**: rolled-up prayer rug **and/or** unrolled version (envanterden
   çıkarıp serme fikri için ideali: iki hali — `seccade_rolled` / `seccade_open`). Muted
   red/green with simple mihrab motif (no text). ~1.1 m açıkken.
8. **`item_coin.glb` — Dirhem/kese**: small coin purse or a few silver coins (dirhem).

---

## 📦 Öncelik Sırası (önce bunlar lazım)
1. `sheep.glb`, `camel.glb`, `goat.glb` (çobanlık)
2. `date_palm.glb` (+bare), `mulberry_tree.glb` (+bare) (hasat/tekrarlanan)
3. `item_date.glb`, `item_mulberry.glb`, `item_bread.glb` (envanter/pickup)
4. `market_stall.glb`, `basket.glb`, `scale.glb` (pazar)
5. `orphan.glb`, `neighbor.glb`, `merchant.glb` (NPC)
6. `seccade.glb`, `well.glb`, `masjid_nabawi.glb`

> Modeller hazır olunca `models/` klasörüne koy; ben `MODELS` dizisine ekleyip (base64 gömme
> dahil) mekaniği kodlayacağım. Gömme için `scratchpad/inline_world.py` akışını kullanırız.
