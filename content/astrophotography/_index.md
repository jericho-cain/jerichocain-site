+++

title = "Astrophotography"

draft = false

+++



![Bellatrix Observatory banner](/img/bellatrix-banner.png)


Click any image, then use **← / →** keys or on-screen arrows to navigate. Press **Esc** or click outside to close.

<div id="astro-gallery" class="gallery"></div>

<script>
  // List your filenames here (only the file names):
  const IMAGES = [
    "m31.jpg",
    "hip_106890.jpg",
    "ic_1805.jpg",
    "ic_1848.jpg",
    "m27.jpg",
    "m51.jpg",
    "m81.jpg",
    "m101.jpg",
    "ngc_281.jpg",
    "ngc_6888.jpg",
    "ngc_6960.jpg",
    "ngc_6992.jpg",
    "ngc_7000.jpg",
    "ngc_7380.jpg",
    "ngc_7635.jpg",
    "sh2_101.jpg"
  ];

  // Optional: captions (fallback to filename if missing)
  const CAPTIONS = {
  "m31.jpg": "M31 (Andromeda Galaxy) — Distance: ~2.54 million ly — Size: ~220,000 ly across — A barred spiral galaxy and the nearest major galaxy to the Milky Way, containing about one trillion stars and numerous satellite galaxies.",

  "hip_106890.jpg": "HIP 106890 (Fomalhaut) — Distance: ~25 ly — Size: ~1.8 R☉ — An A-type main sequence star with a prominent debris disk, often studied for exoplanet formation.",
  
  "ic_1805.jpg": "IC 1805 (Heart Nebula) — Distance: ~7,500 ly — Size: ~200 ly — Emission nebula rich in ionized hydrogen, powered by young massive stars in open cluster Melotte 15.",
  
  "ic_1848.jpg": "IC 1848 (Soul Nebula) — Distance: ~7,500 ly — Size: ~150 ly — Star-forming emission nebula adjacent to the Heart Nebula, containing embedded star clusters.",
  
  "m27.jpg": "M27 (Dumbbell Nebula) — Distance: ~1,360 ly — Size: ~2.5 ly — A planetary nebula formed by a dying sun-like star shedding its outer layers.",
  
  "m51.jpg": "M51 (Whirlpool Galaxy) — Distance: ~23 million ly — Size: ~76,000 ly — A grand-design spiral galaxy interacting with its companion NGC 5195, triggering star formation.",
  
  "m81.jpg": "M81 (Bode’s Galaxy) — Distance: ~12 million ly — Size: ~90,000 ly — A large spiral galaxy with an active galactic nucleus, close neighbor of M82.",
  
  "m101.jpg": "M101 (Pinwheel Galaxy) — Distance: ~21 million ly — Size: ~170,000 ly — A face-on spiral galaxy with striking spiral arms and intense star formation regions.",
  
  "ngc_281.jpg": "NGC 281 (Pacman Nebula) — Distance: ~9,200 ly — Size: ~48 ly — Emission nebula featuring dark dust lanes and active star formation.",
  
  "ngc_6888.jpg": "NGC 6888 (Crescent Nebula) — Distance: ~5,000 ly — Size: ~25 ly — Formed by fast stellar winds from the Wolf–Rayet star WR 136 colliding with earlier ejected material.",
  
  "ngc_6960.jpg": "NGC 6960 (Western Veil Nebula, Witch’s Broom) — Distance: ~2,400 ly — Size: ~35 ly — Supernova remnant filament in the Veil Nebula complex.",
  
  "ngc_6992.jpg": "NGC 6992 (Eastern Veil Nebula) — Distance: ~2,400 ly — Size: ~35 ly — Another filamentary arc of the Veil Nebula, remains of a ~20,000-year-old supernova.",
  
  "ngc_7000.jpg": "NGC 7000 (North America Nebula) — Distance: ~2,590 ly — Size: ~100 ly — Emission nebula shaped like North America, rich in hydrogen-alpha emission.",
  
  "ngc_7380.jpg": "NGC 7380 (Wizard Nebula) — Distance: ~7,200 ly — Size: ~100 ly — Nebula surrounding an open cluster, shaped by stellar winds and radiation from young stars.",
  
  "ngc_7635.jpg": "NGC 7635 (Bubble Nebula) — Distance: ~7,100 ly — Size: ~10 ly — Bubble-shaped emission nebula sculpted by the stellar wind of a massive O-type star.",
  
  "sh2_101.jpg": "Sh2-101 (Tulip Nebula) — Distance: ~6,000 ly — Size: ~70 ly — Emission nebula in Cygnus, bright in hydrogen-alpha, with striking petal-like structure."
};


  const base = "/img/astro/";
  const cont = document.getElementById("astro-gallery");

  // Build thumbnail grid
  IMAGES.forEach((fn, i) => {
    const a = document.createElement("a");
    a.href = base + fn;
    a.dataset.index = i;
    const img = document.createElement("img");
    img.src = base + fn;
    img.alt = CAPTIONS[fn] || fn;
    a.appendChild(img);
    a.addEventListener("click", (e) => { e.preventDefault(); openLightbox(i); });
    cont.appendChild(a);
  });

  // Lightbox elements
  const overlay = document.createElement("div");
  overlay.className = "lb-overlay";
  overlay.innerHTML = `
    <div class="lb-frame">
      <img class="lb-img" src="" alt="">
      <div class="lb-caption"></div>
      <button class="lb-btn lb-prev" aria-label="Previous">❮</button>
      <button class="lb-btn lb-next" aria-label="Next">❯</button>
      <button class="lb-close" aria-label="Close">✕</button>
    </div>`;
  document.body.appendChild(overlay);

  const lbImg = overlay.querySelector(".lb-img");
  const lbCap = overlay.querySelector(".lb-caption");
  const btnPrev = overlay.querySelector(".lb-prev");
  const btnNext = overlay.querySelector(".lb-next");
  const btnClose = overlay.querySelector(".lb-close");
  let idx = 0;

  function show(i) {
    idx = (i + IMAGES.length) % IMAGES.length;
    const fn = IMAGES[idx];
    lbImg.src = base + fn;
    lbImg.alt = CAPTIONS[fn] || fn;
    lbCap.textContent = CAPTIONS[fn] || fn;
  }
  function openLightbox(i) {
    show(i);
    overlay.classList.add("active");
  }
  function closeLightbox() {
    overlay.classList.remove("active");
    lbImg.src = "";
  }

  btnPrev.onclick = () => show(idx - 1);
  btnNext.onclick = () => show(idx + 1);
  btnClose.onclick = closeLightbox;
  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) closeLightbox();
  });
  document.addEventListener("keydown", (e) => {
    if (!overlay.classList.contains("active")) return;
    if (e.key === "Escape") closeLightbox();
    if (e.key === "ArrowLeft") show(idx - 1);
    if (e.key === "ArrowRight") show(idx + 1);
  });
</script>

---

## Equipment:


{{< gearset >}}

{{< gear title="Camera – ZWO ASI2600MM" >}}
Large APS-C sensor, cooled, and with a wide field of view, the ASI2600MM is one of the best value mono cameras on the market. It’s a workhorse that delivers clean data night after night.
{{< /gear >}}

{{< gear title="Mount – ZWO AM5" >}}
Exceptionally portable and easy to run with NINA, the AM5 punches above its weight for a strain-wave mount. I plan to keep it as my travel mount even if I eventually set up a heavier pier-mounted system.
{{< /gear >}}

{{< gear title="Telescope – Askar FRA400" >}}
This 72 mm quintuplet refractor is wonderfully simple because there’s no backfocus math to do. It’s sharp and portable, though I wish the manufacturer offered a fitted hard case.
{{< /gear >}}

{{< gear title="Autofocus – ZWO EAF (wired)" >}}
The wired Electronic Automatic Focuser is simple, reliable, and integrates perfectly with NINA. Once you use it, you’ll never want to go back to manual focusing.
{{< /gear >}}

{{< gear title="Calibration – DeepSkyDad FP2" >}}
Automating flats and dark flats saves me huge amounts of time at the end of a session. With NINA integration, everything is wrapped up by the time I’m packing my gear away.
{{< /gear >}}

{{< gear title="Filters – Antlia 3 nm Narrowband + LRGB" >}}
The 3 nm narrowband set delivers excellent contrast with minimal halos, while the LRGB filters give me clean color data. Together they’ve become my default filter set for most projects.
{{< /gear >}}

{{< gear title="Power – Pegasus Astro Ultimate Powerbox v3" >}}
This isn’t a small accessory — it’s the central hub that powers and manages my entire setup. With reliable power delivery and USB control, it keeps the rig organized and dependable.
{{< /gear >}}

{{< gear title="Guiding – Askar 32 mm Guidescope + ZWO ASI120MM Mini" >}}
The Askar 32 mm guidescope paired with the ASI120MM Mini keeps guiding precise and trouble-free. It’s a lightweight setup that just works.
{{< /gear >}}

{{< gear title="Dew Control – Dew Not 3\" Heater Strip" >}}
The Dew Not strip wraps around my optics to keep them dry all night. Simple, reliable, and one of those things you don’t think about until you don’t have it.
{{< /gear >}}

{{< gear title="Control Computer – Beelink S12 Mini PC" >}}
This Alder Lake-N mini PC is compact and efficient, perfect for running NINA, guiding, and image storage in the field. It’s quiet, sips power, and is more than enough for capture tasks even if it’s not built for heavy PixInsight crunching.
{{< /gear >}}

{{< gear title="Software – NINA + PixInsight" >}}
NINA opened the door to full automation for me after I outgrew ASIAIR, and it’s been rock solid. In PixInsight I lean on BlurXTerminator, NoiseXTerminator, StarXTerminator, and core tools like LHT and MLT — and though I usually compare GHS to a masked stretch, I find the masked stretch often wins.
{{< /gear >}}

{{< /gearset >}}

---

[← Back to Home](/)

