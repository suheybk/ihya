# İhya — Olay Müdahale Rehberi (Incident Runbook)

Tek nöbetçi sensin. Bir şey bozulunca **önce buraya bak.** Bu oyun statik bir PWA'dır
(`ihya3d.html`, GitHub Pages, 3 ayna: origin/live/live2, localStorage, backend yok).

---

## Hızlı bakış — "X bozulursa önce Y'ye bak"

| Belirti | İlk bakılacak | Muhtemel sebep |
|---|---|---|
| Oyun açılmıyor / "Dünya diriltiliyor"da takılı | Tarayıcı konsolu (F12) — JS hatası var mı | Modül sözdizimi/ runtime hatası (son commit) |
| İkonlar/model kırık, eski sürüm geliyor | `sw.js` içindeki `CACHE` sürümü artırıldı mı | Bayat Service Worker cache |
| Sayfa hiç açılmıyor (404/boş) | GitHub Pages durumu + repo Settings→Pages | Deploy/Pages sorunu |
| Three.js/model yüklenmiyor | Ağ sekmesi — unpkg CDN erişimi | CDN kesintisi (self-host çözüm) |
| Kullanıcı ilerlemesi kayboldu | localStorage `ihya3d_v1` | Kullanıcı verisi client'ta; sunucu yedeği YOK |

---

## 1. Deploy / Rollback (geri alma)

**Deploy:** `main`'e push → GitHub Pages otomatik yayınlar. **Her deploy'da `sw.js` `CACHE` sürümünü artır**
(yoksa kullanıcı bayat cache alır).

**Rollback (bozuk sürümü geri al):**
```bash
git revert <bozuk_commit>            # ya da: git reset --hard <iyi_commit>  (dikkatli)
# sw.js CACHE sürümünü BİR ARTIR (yeni deploy sayılsın, cache tazelensin)
git push origin main && git push live main && git push live2 main
```
> ✅ Rollback en az bir kez **gerçekten test edilmeli** (sadece teoride değil): küçük bir zararsız
> değişiklik yap → push → revert et → push → siteyi kontrol et.

## 2. "Dünya diriltiliyor"da takılma (en sık)
Neredeyse her zaman **modül sözdizimi hatası** (bir edit'te kaçan `}` vb.). 
- Konsolda kırmızı hata satırına bak.
- Lokal: `node --check` (bkz. aşağıdaki komut) — CI de her push'ta bunu yapar.
- Son commit'i revert et, düzelt, tekrar dene.

Lokal hızlı kontrol:
```bash
node .github/scripts/check-module.mjs
```

## 3. Bayat cache / eski sürüm
- `sw.js` `CACHE` sürümü artırıldı mı? En yaygın sebep budur.
- **YAPMA:** `caches.delete` / SW unregister ile "temizleme" — kullanıcı verisini/deneyimini bozabilir;
  sürüm artırımı zaten cache'i tazeler.
- Kullanıcı tarafında: sekmeyi kapatıp aç (hard refresh) yeni sürümü çeker.

## 4. Kullanıcı verisi
- İlerleme ve Hac başvurusu (`S.hajjReg`) **yalnızca kullanıcının cihazında** (localStorage `ihya3d_v1`).
- **Sunucu yedeği yok.** Login/backend eklenene kadar bu böyle. O yüzden canlı bir kullanıcının
  save'ine test sırasında **yazma** (bkz. geliştirme notları).

## 5. Ödeme / hesap (gelecekte)
- iyzico ödemesi ve login **backend gerektirir** (secret asla client'ta olmaz). Devreye girince:
  ayrı bir runbook + secrets manager + izleme (Sentry/uptime) eklenmeli.

---

## İletişim / kaynaklar
- Sahibi: Suheyb Karaman · suheybk@gmail.com
- Repo aynaları: origin (suheybk/ihya), live (ihya-oyun), live2 (ihya-medine)
- İlgili: `YAPILACAKLAR.md`, `Kaynakca.md`, geliştirme notları (memory)

_Son güncelleme: 2026-07-09._
