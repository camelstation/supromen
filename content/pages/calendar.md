Title: Calendar
Slug: calendar
Url: calendar/
Save_as: calendar/index.html
Status: published

<style>
.cal-list {
  list-style: none;
  margin: 16px 0 0;
  padding: 0;
  width: 100%;
  max-width: 480px;
}

.cal-entry {
  display: flex;
  gap: 16px;
  padding: 8px 0;
  border-bottom: 1px solid #222;
  align-items: flex-start;
}

.cal-date {
  min-width: 90px;
  font-size: 0.78em;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--accent);
  padding-top: 3px;
  flex-shrink: 0;
}

.cal-body {
  flex: 1;
}

.cal-title-row {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.cal-title {
  font-size: 1.1em;
  font-weight: 700;
  color: var(--text);
  letter-spacing: 0.02em;
}

.cal-tag {
  font-size: 0.7em;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 3px;
}

.cal-tag--event {
  background: #2a1a3e;
  color: #c9a0f5;
}

.cal-tag--class {
  background: #162916;
  color: #6abf69;
}

.cal-meta {
  margin-top: 4px;
  font-size: 1.1em;
  color: #888;
}

.cal-link {
  display: inline-block;
  margin-top: 6px;
  font-size: 1.1em;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: var(--accent);
  text-decoration: none;
}

.cal-link:hover {
  opacity: 0.8;
}

.cal-symbol {
  font-size: 1em;
  color: #6abf69;
  flex-shrink: 0;
}

.cal-key {
  width: 100%;
  max-width: 480px;
  margin: 0 0 16px;
  font-size: 1.1em;
  color: #888;
  line-height: 1.8;
  border: 1px solid #333;
  padding: 16px 20px;
  text-align: center;
  box-sizing: border-box;
}

.cal-key-sym {
  color: #6abf69;
}

.cal-key a {
  color: #888;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.cal-key a:hover {
  opacity: 0.7;
}
</style>

<div class="event-block" style="align-items: center;">
<h2 class="shop-heading" style="text-align: center; width: 100%; max-width: 480px;">Calendar</h2>

<div class="cal-key">
  <div><span class="cal-key-sym">◑</span> SUPR OMEN Presents (<a href="http://supromen.com/curatorial-programs">Curatorial Program</a>)</div>
  <div><span class="cal-key-sym">✎</span> Workshop / Artist Development</div>
  <div><span class="cal-key-sym">▼</span> Member Presentation</div>
  <div><span class="cal-key-sym">△</span> Partner Presentation</div>
</div>

<ul class="cal-list">

  <li class="cal-entry">
    <span class="cal-date">Mon Jun 29</span>
    <div class="cal-body">
      <div class="cal-title-row">
        <span class="cal-symbol">△</span>
        <a class="cal-title" href="https://withfriends.events/event/FlhizUfq/practice-space/" target="_blank" rel="noopener" style="color: var(--text);">Practice Space</a>
      </div>
      <div class="cal-meta">6:30pm &middot; Kris Lee</div>
    </div>
  </li>

  <li class="cal-entry">
    <span class="cal-date">Mon Jul 6</span>
    <div class="cal-body">
      <div class="cal-title-row">
        <span class="cal-symbol">△</span>
        <a class="cal-title" href="https://withfriends.events/event/FlhizUfq/practice-space/" target="_blank" rel="noopener" style="color: var(--text);">Practice Space Performance Nite</a>
      </div>
      <div class="cal-meta">6:30pm &middot; Open to public</div>
    </div>
  </li>

  <li class="cal-entry">
    <span class="cal-date">Thu Jul 23</span>
    <div class="cal-body">
      <div class="cal-title-row">
        <span class="cal-symbol">◑</span>
        <span class="cal-title">PITCH presents Tamas Marquardt &amp; Iris McCloughan</span>
      </div>
      <div class="cal-meta">8pm &middot; Curated by Isabella Thorpe-Woods and Nora Raine Thompson</div>
      <div class="cal-meta">Emerging curator program for dance and performance</div>
    </div>
  </li>

  <li class="cal-entry">
    <span class="cal-date">Fri Jul 24<br>Sat Jul 25</span>
    <div class="cal-body">
      <div class="cal-title-row">
        <span class="cal-symbol">△</span>
        <span class="cal-title">By Any Other Name</span>
      </div>
      <div class="cal-meta">8pm &middot; A new play by Alex Ford</div>
    </div>
  </li>

  <li class="cal-entry">
    <span class="cal-date">Fri Jul 31</span>
    <div class="cal-body">
      <div class="cal-title-row">
        <span class="cal-symbol">◑</span>
        <a class="cal-title" href="https://pools.events/event/htt1Fw2w/gushes-protein/" target="_blank" rel="noopener" style="color: var(--text);">DRIFT presents gushes: PROTEIN</a>
      </div>
      <div class="cal-meta">8pm &middot; Curated by Jemila MacEwan</div>
      <div class="cal-meta">Experimental live arts program</div>
    </div>
  </li>

</ul>

</div>
