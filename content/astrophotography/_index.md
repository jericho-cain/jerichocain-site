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
  "hip_106890.png": "HIP 106890 (Fomalhaut) — Distance: ~25 ly — Size: ~1.8 R☉ — An A-type main sequence star with a prominent debris disk, often studied for exoplanet formation.",
  
  "ic_1805.png": "IC 1805 (Heart Nebula) — Distance: ~7,500 ly — Size: ~200 ly — Emission nebula rich in ionized hydrogen, powered by young massive stars in open cluster Melotte 15.",
  
  "ic_1848.png": "IC 1848 (Soul Nebula) — Distance: ~7,500 ly — Size: ~150 ly — Star-forming emission nebula adjacent to the Heart Nebula, containing embedded star clusters.",
  
  "m27.png": "M27 (Dumbbell Nebula) — Distance: ~1,360 ly — Size: ~2.5 ly — A planetary nebula formed by a dying sun-like star shedding its outer layers.",
  
  "m51.png": "M51 (Whirlpool Galaxy) — Distance: ~23 million ly — Size: ~76,000 ly — A grand-design spiral galaxy interacting with its companion NGC 5195, triggering star formation.",
  
  "m81.png": "M81 (Bode’s Galaxy) — Distance: ~12 million ly — Size: ~90,000 ly — A large spiral galaxy with an active galactic nucleus, close neighbor of M82.",
  
  "m101.png": "M101 (Pinwheel Galaxy) — Distance: ~21 million ly — Size: ~170,000 ly — A face-on spiral galaxy with striking spiral arms and intense star formation regions.",
  
  "ngc_281.png": "NGC 281 (Pacman Nebula) — Distance: ~9,200 ly — Size: ~48 ly — Emission nebula featuring dark dust lanes and active star formation.",
  
  "ngc_6888.png": "NGC 6888 (Crescent Nebula) — Distance: ~5,000 ly — Size: ~25 ly — Formed by fast stellar winds from the Wolf–Rayet star WR 136 colliding with earlier ejected material.",
  
  "ngc_6960.png": "NGC 6960 (Western Veil Nebula, Witch’s Broom) — Distance: ~2,400 ly — Size: ~35 ly — Supernova remnant filament in the Veil Nebula complex.",
  
  "ngc_6992.png": "NGC 6992 (Eastern Veil Nebula) — Distance: ~2,400 ly — Size: ~35 ly — Another filamentary arc of the Veil Nebula, remains of a ~20,000-year-old supernova.",
  
  "ngc_7000.png": "NGC 7000 (North America Nebula) — Distance: ~2,590 ly — Size: ~100 ly — Emission nebula shaped like North America, rich in hydrogen-alpha emission.",
  
  "ngc_7380.png": "NGC 7380 (Wizard Nebula) — Distance: ~7,200 ly — Size: ~100 ly — Nebula surrounding an open cluster, shaped by stellar winds and radiation from young stars.",
  
  "ngc_7635.png": "NGC 7635 (Bubble Nebula) — Distance: ~7,100 ly — Size: ~10 ly — Bubble-shaped emission nebula sculpted by the stellar wind of a massive O-type star.",
  
  "sh2_101.png": "Sh2-101 (Tulip Nebula) — Distance: ~6,000 ly — Size: ~70 ly — Emission nebula in Cygnus, bright in hydrogen-alpha, with striking petal-like structure."
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



