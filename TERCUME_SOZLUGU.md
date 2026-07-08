# İhya — Tercüme Sözlüğü (TR → EN) · Uzman İnceleme Belgesi

Bu dosya, `ihya3d.html` içinde **İngilizce diline (EN i18n Faz 3)** çevrilen tüm içeriğin
**Türkçe aslı ↔ İngilizce karşılığı** eşleşmesini, uzman incelemesi (bir âlim/ilâhiyatçı +
anadili İngilizce olan biri) için listeler.

> ## ⚠️ ÖNEMLİ — Bu çeviriler GEÇİCİDİR
> [[Kaynakca.md]] notu gereği: **dinî metinler (âyet, hadîs, dua, zikir) serbestçe çevrilmemeli;
> hedef dildeki muteber meâl/hadîs kaynağından DOĞRUDAN alınmalıdır.** Aşağıdaki İngilizce
> karşılıklar, oyunun akıcı çalışması için **Claude tarafından yapılan geçici çevirilerdir**.
> Yayın öncesi her âyet/hadîs, muteber bir İngilizce kaynakla **teyit edilmeli ve gerekirse
> değiştirilmelidir**.
>
> **Önerilen İngilizce doğrulama kaynakları:**
> - Kur'ân: **Sahih International**, **Dr. Mustafa Khattab (The Clear Qur'an)**, veya
>   quran.com (çoklu meâl) — âyet numaraları oyunla aynıdır.
> - Hadîs: **sunnah.com** (Bukhari/Muslim/Tirmidhi/Abu Dawud/Ibn Majah — İngilizce muteber
>   tercümeler) ve DİB "Hadislerle İslam" İngilizce nüshaları.
> - Terimler (transliterasyon): "rak'ah, wudu, sajdah, tawaf, sa'y, ihram, tasbih, salawat,
>   istighfar, nisab, zakat, sadaqah, mukallaf" — yaygın akademik transliterasyon kullanıldı.
>
> **Derlenme tarihi:** 2026-07-08 (kaynak: `ihya3d.html`, EN i18n Faz 3 commit'leri).
> **Mimari:** her domain için `UI_STR.en` anahtarları + paralel EN veri tabloları
> (QUEST_EN, NAMAZ_EN, ABDEST_STEPS_EN, NAMAZ_STEPS_EN, QBANK_EN, SULH/ADALET/EMANET_CASES_EN,
> ZIKIR_EN, NPC_EN, STORY_EN, PROFILE_Q_EN, SCEN_T_EN, ISLAND_EN …) + `tU()`/accessor'lar.

---

## 1) Kur'ân-ı Kerîm Âyetleri — TR meâl ↔ EN (geçici) · **muteber meâlle değiştirilecek**

| Sûre/Âyet | TR (oyundaki kısaltma) | EN (geçici — teyit edilecek) | Oyunda yer |
|---|---|---|---|
| Bakara 2/43 | «Namazı dosdoğru kılın.» | "Establish the prayer." | Öğle namaz dersi · QBANK yok |
| Bakara 2/125 | «Makām-ı İbrâhîm'i namaz yeri edinin.» | "Take the standing-place of Abraham as a place of prayer." | Umre — tavâf namazı |
| Bakara 2/158 | «Şüphesiz Safâ ile Merve, Allah'ın nişânelerindendir.» | "Indeed, Safa and Marwah are among the symbols of Allah." | Umre — sa'y |
| Bakara 2/238 | «Namazlara ve orta namaza devam edin.» | "Guard the prayers, and the middle prayer." | İkindi namaz dersi |
| Bakara 2/261 | (İnfak — yedi başak) | (kandil hayrı ref — TR korunuyor, bkz. §7) | Hayır: kandil |
| Bakara 2/271 | (Gizli/açık sadaka) | "Giving charity in secret … is Better for you" (QBANK sadaka) | Sadaka imtihanı |
| Nisâ 4/58 | «Allah size, emanetleri ehline vermenizi emreder.» · «…adaletle hükmedin.» | "Allah commands you to render trusts to their rightful owners." · "…when you judge, judge with justice." | Emanet görevi/senaryo · Adalet (ücret) |
| Nisâ 4/135 | «Kendi aleyhinize de olsa adaleti ayakta tutan şahitler olun.» | "Be witnesses who uphold justice, even against yourselves." | Kadı — deve davası |
| Mâide 5/8 | «Adaletli olun; bu, takvâya daha yakındır.» | "Be just; that is nearer to piety." | Adalet görevi · QBANK adalet |
| A'râf 7/180 | «En güzel isimler Allah'ındır; O'na bunlarla dua edin.» | "To Allah belong the most beautiful names, so call upon Him by them." | Zikir: Esmâü'l-Hüsnâ |
| Enfâl 8/1 | «Allah'tan korkun ve aranızı düzeltin.» | "Fear Allah and set things right between yourselves." | Barıştırma — miras |
| İsrâ 17/35 | «Ölçtüğünüzde tam ölçün, doğru terazi ile tartın.» | "When you measure, give full measure, and weigh with an even balance." | Barıştırma — pazar |
| İsrâ 17/78 | «Güneşin kaymasından gecenin karanlığına kadar namaz kıl.» | "Pray from the decline of the sun until the darkness of the night." | Akşam namaz dersi |
| İsrâ 17/79 | «Gecenin bir kısmında … teheccüd kıl.» | "And in part of the night, pray tahajjud as an extra offering for you." | Gece/teheccüd dersi |
| Hucurât 49/10 | «Müminler ancak kardeştir; iki kardeşinizin arasını düzeltin.» | "The believers are but brothers, so make peace between your brothers." | Barıştırma — sınır |
| Rahmân 55/9 | «…ölçüde ve tartıda haksızlık etmeyin.» | "…do not fall short in measure and weight." | Kadı — su davası |
| Ra'd 13/28 | «Kalpler ancak Allah'ı anmakla huzura erer.» | "Hearts find rest only in the remembrance of Allah." | Dua dersi · QBANK dua |
| Duhâ 93/10 | «Dilenciyi azarlama.» | "And do not repel the beggar." | Dilenci senaryosu |
| Cum'a 62/9 | «Cuma günü namaza çağrıldığında Allah'ı anmaya koşun.» | "When the call is made for prayer on Friday, hasten to the remembrance of Allah." | Mescid — Cuma |
| Felak/Nâs | Muavvizeteyn | "Al-Falaq and An-Nas" (Mu'awwidhatayn) | QBANK dua |

---

## 2) Hadîs-i Şerîfler — TR ↔ EN (geçici) · **muteber tercümeyle değiştirilecek**

| Kaynak | TR (oyundaki kısaltma) | EN (geçici — teyit edilecek) | Yer |
|---|---|---|---|
| Buhârî, Ezân 30 | «Cemaatle namaz … 27 derece faziletlidir.» | "Prayer in congregation is twenty-seven degrees more virtuous than praying alone." | Cemaat görevi/mescid/QBANK |
| Buhârî, Hars 1 | «Müslüman ağaç diker de ondan yenirse sadaka olur.» | "If a Muslim plants a tree and a living creature eats from it, it is charity for him." | Fidan görevi · ağaç hayrı |
| Buhârî, Şirb 9 | «Susuz köpeğe su veren … bağışlandı.» | "Allah forgave a man who gave water to a thirsty dog." | Canlıya su görevi |
| Müslim, Îmân 93 | «Birbirinizi sevmedikçe cennete giremezsiniz; selamı yayın.» | "You will not enter Paradise until you love one another; spread the greeting of peace among yourselves." | Selam görevi |
| Buhârî, Edeb 28 | «Cebrâil komşu hakkını … mirasçı kılacak sandım.» | "Gabriel kept urging kindness to the neighbor so much that I thought he would make him an heir." | Komşu görevi/QBANK |
| Müslim, Birr 69 | «Sadaka maldan bir şey eksiltmez.» | "Charity does not diminish wealth." | Sadaka görevi/QBANK |
| Müslim, Zikir 38 | «İlim için yola çıkana Allah cennet yolunu kolaylaştırır.» | "Whoever takes a path to seek knowledge, Allah makes the path to Paradise easy for him." | İlim görevi/QBANK |
| Buhârî, Cihâd 102 | «Bir kişinin hidayeti kızıl develerden hayırlıdır.» | "That Allah should guide one person through you is better than red camels." | Davet görevi/QBANK |
| Taberânî | «İnsanların en hayırlısı, insanlara en faydalı olandır.» | "The best of people is the one most beneficial to people." | Hayır görevi/QBANK |
| Tirmizî, Tahâret 5 | «Tuvaletten çıkınca "Gufrâneke" derdi.» | "When the Prophet left the toilet he would say 'Ghufranaka'." | Taharet dersi/QBANK |
| Müslim, Tahâret 1 | «Temizlik imanın yarısıdır.» | "Cleanliness is half of faith." | Abdest dersi/QBANK |
| Müslim, Müsâfirîn 96 | «İki rekât sabah sünneti dünyadan hayırlıdır.» | "The two rak'ahs of the dawn sunnah are better than the world and all it contains." | Sabah namaz dersi |
| Müslim, Müsâfirîn 84 | «Kuşluğun iki rekâtı her eklem için sadakaya yeter.» | "The two rak'ahs of Duha suffice as charity for every joint of the body." | Kuşluk dersi |
| Tirmizî, Salât 188 | «Kulun ilk hesaba çekileceği amel namazdır.» | "…the first deed a servant is called to account for is the prayer." | QBANK namaz |
| Buhârî, Fedâil 21 | «En hayırlınız Kur'an'ı öğrenen ve öğretendir.» | "The best of you is the one who learns the Qur'an and teaches it." | Kur'an dersi/imam sözü/QBANK |
| Tirmizî, Fedâil 9 | (Mülk sûresi — kabir azabına siper) | "…(Al-Mulk) is a shield against the torment of the grave." | QBANK quran |
| Buhârî Tevhîd 52 / Müslim 243 | «Kur'an'ı zorlanarak okuyana iki ecir.» | "…two rewards for one who recites the Qur'an haltingly." | QBANK quran |
| Tirmizî, Deavât 66 | (Duâya hamd ve salavâtla başlama) | "…begin with praise and blessings (hamd & salawat)." | QBANK dua |
| Ebû Dâvûd, Edeb 133 | (İlk selâmı verenin fazileti) | "…the one who gives salam first is more virtuous." | QBANK selam |
| Buhârî, Edeb 29 | «Komşusu şerrinden emin olmayan … iman etmiş olmaz.» | "The one whose neighbor is not safe from his harm has not (truly) believed." | QBANK komşu |
| Buhârî, Şüf'a 3 | (İkramda en yakın komşudan başlama) | "…begin with the neighbor whose door is nearest." | QBANK komşu |
| Tirmizî, Birr 36 | «Kardeşine tebessüm sadakadır.» | "Smiling at your brother is a charity." | QBANK sadaka |
| Ebû Dâvûd, İlim 1 | «Âlimler peygamberlerin vârisleridir.» | "The scholars are the heirs of the prophets." | QBANK ilim |
| Müslim, Vasiyye 14 | «İnsan ölünce ameli kesilir; (üçü müstesnâ) faydalı ilim…» | "When a person dies their deeds cease, except… beneficial knowledge…" | QBANK ilim · ilim hayrı |
| Müslim, İmâre 133 | «Hayra vesile olan onu yapan gibidir.» | "The one who guides to good is like the one who does it." | QBANK davet/hayır |
| Buhârî, Ezân 36 | (Arş gölgesindeki yedi — âdil yönetici) | "…a just ruler (is one of the seven shaded)." | QBANK adalet |
| Buhârî, Îmân 24 | (Münafık alâmeti — emanete hıyanet) | "…(a sign of the hypocrite:) he betrays a trust." | QBANK emanet |
| Müslim, Îmân 95 | «Din nasihattir…» | "Religion is sincere counsel… to Allah, His Book, His Messenger and the Muslims." | QBANK hayır · imam sözü |
| Ebû Dâvûd (sulh) | «Sadakaların en faziletlisi, dargınların arasını düzeltmektir.» | "The most virtuous charity is reconciling those who are estranged." | Barıştırma — sınır |
| Buhârî (kardeşlik) | «Birbirinize küsüp sırt çevirmeyin; kardeş olun.» | "Do not turn your backs on one another; be brothers." | Barıştırma — miras |
| Müslim (aldatma) | «Bizi aldatan bizden değildir.» | "Whoever cheats us is not one of us." | Pazar · barıştırma |
| Beyhakî | «Beyyine (delil) davacıya düşer.» | "The burden of proof is upon the claimant." | Kadı — deve davası |
| Ebû Dâvûd (ortak haklar) | «Müslümanlar üç şeyde ortaktır: su, ot, ateş.» | "Muslims are partners in three things: water, pasture and fire." | Kadı — su davası |
| İbn Mâce | «İşçiye ücretini teri kurumadan verin.» | "Give the worker his wage before his sweat dries." | Kadı — ücret davası |
| Ahmed | «Emaneti olmayanın imanı yoktur.» | "There is no faith for the one who has no trustworthiness." | Emanet senaryosu |
| Ahmed b. Hanbel | «Kıyamet kopsa bile elinizdeki fidanı dikin.» | "Even if the Hour strikes, plant the sapling in your hand." | QBANK fidan |
| Tirmizî (gizli sadaka) | «Gizli sadaka, Rabbin öfkesini söndürür.» | "Charity given in secret extinguishes the wrath of the Lord." | Dilenci senaryosu |
| Müslim (zulüm) | «Zulümden sakının; zulüm kıyamet günü karanlıklardır.» | "Beware of injustice, for injustice will be darkness on the Day of Judgment." | Zulüm olayı |
| Buhârî (yetim) | «Ben ve yetimi gözeten cennette yan yanayız.» | "I and the one who cares for an orphan will be like this in Paradise, side by side." | NPC: yetim |
| Buhârî, Edeb 85 | «…misafirine ikram etsin.» | "…let him honor his guest." | NPC: misafir |
| Buhârî, Umre 1 | «Bir umre, diğer umreye kadar keffârettir.» | "One Umrah to the next is an expiation for the (minor) sins between them." | Umre — tamamlama |
| Buhârî, Menâkıb 3 | (Sa'd b. Rebî' — Abdurrahman b. Avf) | "Sa'd ibn Rabi' offered half his wealth…; he said 'Show me the market' — he chose lawful earning." | Muâhât |
| Müslim (salavât) | «Bana salavât getirene Allah on rahmet eder.» | "Whoever sends one blessing upon me, Allah sends ten mercies upon him." | Zikir: Salvele |
| Buhârî (iki nimet) | «İki nimet: sağlık ve boş vakit.» | "There are two blessings in which many people are deceived: health and free time." | İmam sözü |
| Buhârî (kolaylaştırın) | «Kolaylaştırın, zorlaştırmayın…» | "Make things easy, do not make them hard; give glad tidings, do not drive people away." | İmam sözü |
| Buhârî (sevdiğiyle) | «Kişi sevdiğiyle beraberdir.» | "A person is with the one he loves." | İmam sözü |
| Buhârî (müslüman) | «Müslüman, elinden ve dilinden diğerlerinin emin olduğudur.» | "The Muslim is the one from whose hand and tongue other Muslims are safe." | İmam sözü |

---

## 3) Zikir & Dualar (transliterasyon + meâl) — TR ↔ EN

| Zikir | TR meâl | EN (geçici) |
|---|---|---|
| Hamdele | «Elhamdü lillâhi Rabbil âlemîn — Hamd âlemlerin Rabbi Allah'a mahsustur.» | "Al-hamdu lillahi Rabbil-'alamin — All praise belongs to Allah, Lord of the worlds." |
| Salvele | «Allâhümme salli alâ Muhammed…» | "Allahumma salli 'ala Muhammadin wa 'ala ali Muhammad…" |
| İstiğfâr | «Estağfirullâhe'l-azîm ve etûbü ileyh…» | "Astaghfirullah al-'azim wa atubu ilayh — I seek forgiveness from Allah the Mighty and turn to Him." |
| Esmâü'l-Hüsnâ | «Yâ Rahmân, yâ Rahîm…» | "Ya Rahman, ya Rahim, ya Quddus…" |
| Tesbihât | «33 Sübhânallah · 33 Elhamdülillah · 33 Allâhü Ekber…» + Âyetü'l-Kürsî | "33 Subhanallah · 33 Alhamdulillah · 33 Allahu akbar…" + Ayat al-Kursi |
| Telbiye | «Lebbeyk Allâhümme lebbeyk» | "Labbayk Allahumma labbayk — Here I am, O Allah, here I am." |

> Not: Arapça asıllar (telbiye, âyet-i kerîme Arapça satırları) **çevrilmedi**, aynen korundu.

---

## 4) Unvanlar, Rütbeler, Yerler (dinî değil — tutarlılık için)

| TR | EN | TR | EN |
|---|---|---|---|
| Niyet / Tâlib / Gayret Ehli | Intention / Seeker / Diligent | İhyâ Yolcusu/Eri/Ustası | Ihya Wayfarer/Devotee/Master |
| Barıştırıcı / Muslih / Ara Bulan / Sulh Ustası | Reconciler / Peacemaker / Mediator / Master of Reconciliation | Hakem / Âdil Hakem / Adaletli Kadı / Adalet Ustası | Arbiter / Just Arbiter / Just Judge / Master of Justice |
| Emin / Emanet Ehli / Emanet Bekçisi / Emanet Ustası | Trustworthy / Keeper of Trust / Guardian of Trust / Master of Trust | Huzur / Huzursuz / Zulüm | Peace / Unrest / Injustice |
| Hâne / Hurma Bahçesi / Ensâr Mahallesi | Home / Date Grove / Ansar Neighborhood | Mescid / Medine / Atölye / Sadaka Bahçesi | Mosque / Medina / Workshop / Charity Garden |
| Fecir/Öğle/İkindi/Akşam/Yatsı/Kuşluk/Gece | Fajr/Dhuhr/Asr/Maghrib/Isha/Duha/Night | Sulh/Adalet/Emanet | Peace/Justice/Trust |

---

## 5) Anahtar Terim Sözlüğü (tutarlılık — çevirmen/uzman için)

| TR | EN (kullanılan) | Not |
|---|---|---|
| nûr | nur | oyun para-birimi/manevî puan; transliterasyon korundu |
| dirhem | dirham(s) | para birimi |
| kesb-i helâl | lawful earning | |
| infak / sadaka | giving / charity (sadaqah) | |
| sadaka-i câriye | ongoing charity | |
| mükellef | accountable (mukallaf) | |
| nisab | nisab | zekât eşiği |
| öşür | tithe (1/10) | |
| rekât | rak'ah | |
| abdest | ablution (wudu) | |
| secde / rükû | prostration (sajdah) / bowing (ruku) | |
| kıble | qibla | |
| tavâf / sa'y / ihrâm / tıraş | tawaf / sa'y / ihram / shave | Umre |
| emanet | trust | |
| muâhât | mu'akhat (pact of brotherhood) | |
| İmtihan Meydanı | Trial Grounds | |
| Fıkıh/Hadis/Âyet Okulu | Fiqh/Hadith/Verse School | imtihan rozetleri |
| Senaryo Defteri | Case Ledger | |
| Dağarcık | Satchel | envanter |
| Hayır Çeşmesi | Fountain of Good | |

---

## 6) İmtihan Soru Bankası (QBANK) — durum

15 konu (~35 soru) `QBANK_EN` olarak çevrildi; **şık sırası TR ile birebir korundu** (doğru cevap
indeksi `c` bozulmaz). Sorular yukarıdaki §1–§2 âyet/hadîs kaynaklarına dayanır; uzman, soru
metinlerini ve şıkları o kaynaklarla teyit etmeli. (Tam liste kaynak kodda `QBANK` ↔ `QBANK_EN`.)

## 7) Bilinçli TR bırakılan (uzman kararına) 
- **Zekât tür/ref alanları** (`ZEKAT[k].tur/ref`) ve **Hayır kalemi ref hadîsleri** (`HAYIR[].ref`):
  §7'deki hadîslerin bir kısmı (kandil/çeşme/mushaf/sebil/gölge ref'leri) henüz TR; uzman
  onayıyla EN'e alınacak. Kalem **adları** çevrildi (Plant a tree, Light a lantern…).
- Çok nadir/teknik toast'lar (su çekme animasyon ipuçları vb.) uzun kuyruğu; ihtiyaç olursa eklenir.

---

*Bu belge oyunla birlikte güncel tutulmalıdır: `ihya3d.html` içinde yeni bir `*_EN` tablosu veya
`UI_STR.en` anahtarı eklendiğinde ilgili satır buraya işlenmelidir.*

---

## 8) العربية (AR) — durum ve KRİTİK not

**AR Faz 1 (kabuk) tamam** (v1175, Faz 6.10): `UI_STR.ar` — rütbe, adalet, panel başlıkları/gövdeleri
(Dağarcık/Pazar/Senaryo), butonlar, gün/vakit/namaz adları, item adları, senaryo unvanları (`SCEN_T_AR`),
ada adları (`ISLAND_AR`). `tU()` çok-dilli yapıldı; RTL (`dir=rtl`) + saat pili dil-fix. Preview'da doğrulandı.

**⚠️ AR için dinî içerik kuralı (EN'den FARKLI):** Arapça, Kur'ân ve hadîsin **asıl dilidir**. Bu yüzden
AR'da âyet/hadîs/zikir metinleri **çevrilmeyecek; doğrudan ASIL ARAPÇA metinleri** kullanılacak
(ör. âyetin mushaf lafzı, hadîsin muteber Arapça metni — Sahîh el-Buhârî/Müslim Arapça asılları).
Bu, EN'deki "geçici çeviri" yaklaşımından farklıdır ve daha da hassastır.
Sıradaki diller (Endonezyaca/Malayca vb.) yine EN gibi "hedef dilde muteber meâl" yaklaşımıyla.

**AR Faz 2 part 1 (v1178, Faz 6.13):** görev adı/hatırlatma + adım-adım abdest/namaz öğretimi Arapça
(`QUEST_AR`, `NAMAZ_AR`, `ABDEST/NAMAZ_STEPS_AR` — MSA oyun ipuçları/fıkıh adımları).

**AR Faz 2 part 2 (v1179, Faz 6.14) — SENARYO DİYALOGLARI + ASIL ARAPÇA:** `SULH/ADALET/EMANET_CASES_AR`
+ `DILENCI_AR`. Anlatı MSA; **âyet/hadîs ref'leri ASIL ARAPÇA (mushaf lafzı)** kullanıldı:
- Hucurât 49/10 «إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ فَأَصْلِحُوا بَيْنَ أَخَوَيْكُمْ»
- Enfâl 8/1 «فَاتَّقُوا اللَّهَ وَأَصْلِحُوا ذَاتَ بَيْنِكُمْ» · İsrâ 17/35 «وَأَوْفُوا الْكَيْلَ إِذَا كِلْتُمْ...»
- Nisâ 4/135 «كُونُوا قَوَّامِينَ بِالْقِسْطِ شُهَدَاءَ لِلَّهِ...» · Nisâ 4/58 «...أَن تَحْكُمُوا بِالْعَدْلِ» / «تُؤَدُّوا الْأَمَانَاتِ إِلَىٰ أَهْلِهَا»
- Rahmân 55/9 «وَأَقِيمُوا الْوَزْنَ بِالْقِسْطِ...» · Duhâ 93/10 «وَأَمَّا السَّائِلَ فَلَا تَنْهَرْ»
> **Hadîs Arapça lafızları** (أفضل الصدقة إصلاح ذات البين / لا تدابروا... / من غشّنا فليس منّا / البيّنة على المدّعي /
> المسلمون شركاء في ثلاث / أعطوا الأجير أجره... / لا إيمان لمن لا أمانة له / صدقة السرّ تطفئ غضب الرب) **meşhur
> rivayetlerdir; uzman muteber matbu külliyattan (lafız + tam tahriç) TEYİT ETMELİ.**

**KALAN AR (sonraki):** görev sheet ref'leri (âyet/hadîs asıl Arapça), zikir metinleri, imtihan bankası
(QBANK_AR), Umre/hac, NPC/hayır/zekât ref, STORY/obligations — accessor'lar (`zikirAd`/`npcNm`/`storyEn`/
`buildExam`/`obligationsText`/`imamSoz`) hâlâ `S.lang==='en'`; AR için genelleştir + `*_AR` (âyet/hadîs ASIL Arapça).
