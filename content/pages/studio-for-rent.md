Title: Studio for rent
Slug: studio-for-rent
Url: studio-for-rent/
Save_as: studio-for-rent/index.html
Status: published

<style>
.studio-slideshow {
  position: relative;
  width: 100%;
  max-width: 720px;
  height: 60vh;
  max-height: 600px;
  margin: 0 auto 2rem;
  background: #000;
  overflow: hidden;
}

.studio-slideshow img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: 1;
  transition: opacity 0.25s ease;
}

.studio-slideshow img.no-fade {
  transition: none;
}

.studio-slideshow-arrow {
  position: absolute;
  top: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  width: 15%;
  border: none;
  background: none;
  color: rgba(255, 255, 255, 0.6);
  font-size: 2rem;
  line-height: 1;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s ease, color 0.2s ease;
  z-index: 2;
  -webkit-tap-highlight-color: transparent;
}

.studio-slideshow:hover .studio-slideshow-arrow {
  opacity: 1;
}

.studio-slideshow-arrow:hover {
  color: rgba(255, 255, 255, 0.9);
}

.studio-slideshow-arrow--prev {
  left: 0;
  justify-content: flex-start;
  padding-left: 12px;
}

.studio-photo {
  display: block;
  width: 100%;
  height: auto;
  margin-top: 1rem;
}

.studio-slideshow-arrow--next {
  right: 0;
  justify-content: flex-end;
  padding-right: 12px;
}
</style>

<div class="studio-slideshow" id="studio-slideshow">
  <img id="studio-slideshow-img" src="/images/studio-for-rent/1.webp" alt="Studio for rent at SUPR OMEN">
  <button type="button" class="studio-slideshow-arrow studio-slideshow-arrow--prev" aria-label="Previous image" onclick="studioSlideshowPrev()">&#10094;</button>
  <button type="button" class="studio-slideshow-arrow studio-slideshow-arrow--next" aria-label="Next image" onclick="studioSlideshowNext()">&#10095;</button>
</div>

<script>
(function () {
  var images = (window.STUDIO_FOR_RENT_SLIDESHOW_IMAGES || []).slice();

  if (images.length === 0) {
    return;
  }

  var DISPLAY_MS = 3000;
  var idx = 0;
  var displayTimer = null;
  var pendingFadeOutHandler = null;
  var img = document.getElementById("studio-slideshow-img");

  function preload(list, done) {
    var remaining = list.length;
    if (remaining === 0) {
      done();
      return;
    }
    list.forEach(function (src) {
      var loader = new Image();
      loader.onload = loader.onerror = function () {
        remaining -= 1;
        if (remaining === 0) {
          done();
        }
      };
      loader.src = src;
    });
  }

  function clearPendingFade() {
    if (pendingFadeOutHandler) {
      img.removeEventListener("transitionend", pendingFadeOutHandler);
      pendingFadeOutHandler = null;
    }
  }

  function scheduleAdvance() {
    clearTimeout(displayTimer);
    displayTimer = setTimeout(function () {
      fadeToNext(idx + 1);
    }, DISPLAY_MS);
  }

  // Waits for the opacity:0 fade-out to visually finish (via transitionend)
  // before swapping src, so the old image is fully invisible -- never
  // painted -- underneath the new one. Images are already preloaded, so
  // the new src decodes instantly with no load delay to cause a flash.
  function fadeToNext(newIdx) {
    clearPendingFade();
    pendingFadeOutHandler = function (e) {
      if (e.propertyName !== "opacity") return;
      pendingFadeOutHandler = null;
      idx = (newIdx + images.length) % images.length;
      img.src = images[idx];
      void img.offsetWidth;
      img.style.opacity = 1;
      scheduleAdvance();
    };
    img.addEventListener("transitionend", pendingFadeOutHandler, { once: true });
    img.style.opacity = 0;
  }

  function goTo(newIdx) {
    clearTimeout(displayTimer);
    clearPendingFade();
    img.classList.add("no-fade");
    idx = (newIdx + images.length) % images.length;
    img.src = images[idx];
    img.style.opacity = 1;
    void img.offsetWidth;
    img.classList.remove("no-fade");
    scheduleAdvance();
  }

  window.studioSlideshowNext = function () {
    goTo(idx + 1);
  };
  window.studioSlideshowPrev = function () {
    goTo(idx - 1);
  };

  preload(images, function () {
    img.src = images[idx];
    img.style.opacity = 1;
    scheduleAdvance();
  });
})();
</script>

<div class="pricing-section">
  <h2 class="pricing-section__heading">Studio for rent</h2>
  <div class="pricing-text">
    <p>SUPR OMEN has a 225 sf studio for rent. The semi-private studio has a window, hardwood floors, 8 ft walls (open at the top to remain FDNY compliant) and a split system for heating and cooling. There is currently a door installed, which can be removed if you prefer a more open studio (our other studios have no doors).</p>
    <p>The 225 sf studio is $900 per month plus electricity (around $25/month). Wi-Fi and water are included. You’re welcome to share the space with a friend! Studio members also have access to a kitchenette and a bathroom.</p>
    <p>SUPR OMEN’s current studio members span dance, sculpture, new media, conceptual art and painting, and all lean into experimental performance to varying degrees. We also have rehearsal members who use the 1000 sf performance space (see photos above), where we host workshops and events several times a month. As a studio member, you can use the rehearsal space when available.</p>
    <p>Please contact <a href="mailto:info@supromen.com" style="color: var(--accent);">info@supromen.com</a> with any enquiries. Come through and say hi! Available from November 21.</p>
    <p>The photo below shows part of the studio to highlight the window, floor and wall.</p>
    <img class="studio-photo" src="/images/Studio-1.webp" alt="Studio showing window, hardwood floor and wall">
  </div>
</div>

<div class="pricing-section">
  <h2 class="pricing-section__heading">About SUPR OMEN</h2>
  <div class="pricing-text">
    <p>SUPR OMEN is an artist-run space for creation and presentation. We support interdisciplinary works that push to the edge of the edge. We were founded to give artists a space to create experimental work across performance art, dance, music, visual art, fashion & film and share it with intimate audiences.</p>
    <p>SUPR OMEN is a 1000 sf performance space adjoining 1000 sf of artist studios. We’re located two blocks from the Morgan L subway station at <a href="https://maps.app.goo.gl/A6uWQpvfiVDx9DyGA" target="_blank" rel="noopener" style="color: var(--accent);">1 Knickerbocker Ave, Brooklyn</a>. The space is up one flight of stairs (not ADA accessible).</p>
    <p>SUPR OMEN is built around an intergenerational community of artists, curators and mentors committed to experimentation, offering mid-career and emerging artists the infrastructure, support and creative permission to take real risks. We have an ongoing roster of performances through our <a href="https://supromen.com/curatorial-programs/" style="color: var(--accent);">curatorial programs</a> and occasionally invite guest curators and SUPR OMEN members to share their vision with our expanding community. We also host movement-based and conceptual workshops.</p>
  </div>
</div>
