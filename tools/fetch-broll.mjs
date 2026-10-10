// Usage: node tools/fetch-broll.mjs S01 "search terms" [offsetSec]   -> broll/S01.mp4 (graded later at build, trimmed to 8s) + CREDITS.txt
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
const [id, q, hitId] = process.argv.slice(2);
const key = process.env.PIXABAY_API_KEY;
if (fs.existsSync(`broll/${id}.mp4`)) { console.log(id, 'already there'); process.exit(0); }
const r = await fetch(`https://pixabay.com/api/videos/?key=${key}&${hitId ? 'id=' + hitId : 'q=' + encodeURIComponent(q)}&video_type=film&safesearch=true&per_page=20`).then((x) => x.json());
const hits = (r.hits || []).filter((h) => h.duration >= 5 && h.videos.large?.url).filter((h) => (h.videos.large.size || 0) < 60e6);
if (!hits.length) { console.log(id, 'no clip for', q); process.exit(0); }
const h = hits[0];
const v = h.videos.large.width >= 1900 ? h.videos.large : h.videos.medium;
const tmp = `broll/.${id}.raw.mp4`;
const buf = Buffer.from(await (await fetch(v.url)).arrayBuffer());
fs.writeFileSync(tmp, buf);
execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', tmp, '-t', '8', '-an', '-c:v', 'libx264', '-crf', '20', '-preset', 'fast', '-vf', 'scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30', `broll/${id}.mp4`]);
fs.rmSync(tmp);
fs.appendFileSync('broll/CREDITS.txt', `${id}\t${h.pageURL}\t${h.user}\t"${q}"\n`);
console.log(id, h.pageURL, h.user, `${h.duration}s`, h.tags.slice(0, 60));
