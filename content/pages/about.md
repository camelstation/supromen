Title: About
Slug: about
Url: about/
Save_as: about/index.html
Status: published

<style>
.about-slideshow {
  position: relative;
  width: 100%;
  max-width: 720px;
  height: 60vh;
  max-height: 600px;
  margin: 0 auto 2rem;
  background: #000;
  overflow: hidden;
}

.about-slideshow img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: 1;
  transition: opacity 0.25s ease;
}

.about-slideshow img.no-fade {
  transition: none;
}

.about-slideshow-arrow {
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

.about-slideshow:hover .about-slideshow-arrow {
  opacity: 1;
}

.about-slideshow-arrow:hover {
  color: rgba(255, 255, 255, 0.9);
}

.about-slideshow-arrow--prev {
  left: 0;
  justify-content: flex-start;
  padding-left: 12px;
}

.about-slideshow-arrow--next {
  right: 0;
  justify-content: flex-end;
  padding-right: 12px;
}
</style>

<div class="about-slideshow" id="about-slideshow">
  <img id="about-slideshow-img" src="/images/about/1.webp" alt="About SUPR OMEN">
  <button type="button" class="about-slideshow-arrow about-slideshow-arrow--prev" aria-label="Previous image" onclick="aboutSlideshowPrev()">&#10094;</button>
  <button type="button" class="about-slideshow-arrow about-slideshow-arrow--next" aria-label="Next image" onclick="aboutSlideshowNext()">&#10095;</button>
</div>

<script>
(function () {
  var images = (window.ABOUT_SLIDESHOW_IMAGES || []).slice();

  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
    return arr;
  }

  shuffle(images);

  if (images.length === 0) {
    return;
  }

  var DISPLAY_MS = 4000;
  var FADE_MS = 250;
  var idx = 0;
  var timer = null;
  var img = document.getElementById("about-slideshow-img");

  function scheduleAdvance() {
    clearTimeout(timer);
    timer = setTimeout(function () {
      fadeToNext(idx + 1);
    }, DISPLAY_MS);
  }

  function fadeToNext(newIdx) {
    img.style.opacity = 0;
    clearTimeout(timer);
    timer = setTimeout(function () {
      idx = (newIdx + images.length) % images.length;
      img.src = images[idx];
      img.style.opacity = 1;
      scheduleAdvance();
    }, FADE_MS);
  }

  function goTo(newIdx) {
    clearTimeout(timer);
    img.classList.add("no-fade");
    idx = (newIdx + images.length) % images.length;
    img.src = images[idx];
    img.style.opacity = 1;
    void img.offsetWidth;
    img.classList.remove("no-fade");
    scheduleAdvance();
  }

  window.aboutSlideshowNext = function () {
    goTo(idx + 1);
  };
  window.aboutSlideshowPrev = function () {
    goTo(idx - 1);
  };

  img.src = images[idx];
  img.style.opacity = 1;
  scheduleAdvance();
})();
</script>

<div class="pricing-section">
  <h2 class="pricing-section__heading">About</h2>
  <div class="pricing-text">
    <p>SUPR OMEN is an artist-run space for creation and presentation. We support interdisciplinary works that push to the edge of the edge. We love experimental performance / dance / music / visual art / fashion / film.</p>
    <p>SUPR OMEN is a 1000 sf performance space adjoining 1000 sf of semi-private studios.</p>
    <p>SUPR OMEN has an ongoing roster of performances through our curatorial programs. We also occasionally host performances by members and the broader New York City arts community.</p>
    <p>SUPR OMEN is located at 1 Knickerbocker Ave, Brooklyn. We're two blocks from the Morgan L and up one flight of stairs (not ADA accessible).</p>
    <p>SUPR OMEN has rehearsal members with access to our 1000 sf rehearsal space, equipment, facilities and a calendar to make bookings directly. Full-membership $260/m for 20 hours // Half-membership $130/m for 10 hours. We occasionally accept new members: <a href="mailto:info@supromen.com">info@supromen.com</a></p>
    <p>SUPR OMEN has studio members who have access to a private studio and our 1000 sf rehearsal space. We occasionally have studios for rent: <a href="mailto:info@supromen.com">info@supromen.com</a></p>
  </div>
</div>

<div class="pricing-section">
  <h2 class="pricing-section__heading">Team</h2>
  <div class="team-list">

    <div class="team-entry">
      <p class="team-role">Founding Director</p>
      <p class="team-name">Jemila MacEwan</p>
      <p class="team-bio">Bio bio bio bio bio</p>
    </div>

    <div class="team-entry">
      <p class="team-role">Co-Founder &amp; Operations</p>
      <p class="team-name">Campbell Watson</p>
      <p class="team-bio">Campbell is an atmospheric scientist. He also hosts the occasional ping pong tournament.</p>
    </div>

    <div class="team-entry">
      <p class="team-role">Communications Director</p>
      <p class="team-name">Deena Falconetti</p>
      <p class="team-bio">Bio bio bio bio bio</p>
    </div>

    <div class="team-entry">
      <p class="team-role">Mentee</p>
      <p class="team-name">Kareena Solanki</p>
      <p class="team-bio">Bio bio bio bio bio</p>
    </div>

    <div class="team-entry">
      <p class="team-role">Bookkeeper</p>
      <p class="team-name">Noah Loiacono</p>
      <p class="team-bio">Bio bio bio bio bio</p>
    </div>

  </div>
</div>

<div class="pricing-section">
  <h2 class="pricing-section__heading">Mission</h2>
  <div class="pricing-text">
    <p>SUPR OMEN was founded to provide a space for performance artists to create experimental work and to showcase experimental work with intimate audiences. We've established art studios and a 1000 sf performance space in Bushwick, built around a community of artists, curators and mentors committed to experimentation. We exist to give emerging and mid-career artists the infrastructure, support and creative permission to take real risks in their work and the opportunities to carry that work into the wider world.</p>
  </div>
</div>

<p class="about-closing">SUPR OMEN exists because New York City artists are amazing</p>
