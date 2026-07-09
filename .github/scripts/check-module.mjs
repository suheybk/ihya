// CI syntax kontrolü: ihya3d.html içindeki son <script type="module"> bloğunu çıkarıp `node --check` eder.
// (Lokal check.sh'in CI karşılığı — her push/PR'da çalışır.)
import { readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const html = readFileSync('ihya3d.html', 'utf8');
const marker = '<script type="module">';
const i = html.lastIndexOf(marker);
if (i < 0) { console.error('HATA: <script type="module"> bulunamadı'); process.exit(1); }
const start = i + marker.length;
const end = html.indexOf('</script>', start);
if (end < 0) { console.error('HATA: kapanış </script> bulunamadı'); process.exit(1); }

const out = join(tmpdir(), 'ihya_mod.mjs');
writeFileSync(out, html.slice(start, end));
try {
  execSync(`node --check "${out}"`, { stdio: 'inherit' });
  console.log('✓ ihya3d.html modül scripti — sözdizimi OK');
} catch (e) {
  console.error('✗ Sözdizimi hatası (yukarıda)');
  process.exit(1);
}
