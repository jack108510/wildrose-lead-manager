#!/bin/bash
cd /Users/jackserver/.openclaw/workspace/wildrose-lead-manager

# Helper function to generate HTML
generate() {
  local file="$1" company="$2" email="$3" city="$4" phone="$5" address="$6"
  local accent="$7" accentLight="$8" dark="$9" heroImg="${10}" aboutImg="${11}"
  local heroWhite="${12}" heroAccent="${13}" subheadline="${14}"
  local svcIcon1="${15}" svcLabel1="${16}" svcDesc1="${17}"
  local svcIcon2="${18}" svcLabel2="${19}" svcDesc2="${20}"
  local svcIcon3="${21}" svcLabel3="${22}" svcDesc3="${23}"
  local svcIcon4="${24}" svcLabel4="${25}" svcDesc4="${26}"
  local svcIcon5="${27}" svcLabel5="${28}" svcDesc5="${29}"
  local svcIcon6="${30}" svcLabel6="${31}" svcDesc6="${32}"
  local strip1="${33}" strip2="${34}" strip3="${35}" strip4="${36}"
  local aboutText1="${37}" aboutText2="${38}"
  local stat1Num="${39}" stat1Label="${40}" stat2Num="${41}" stat2Label="${42}" stat3Num="${43}" stat3Label="${44}"
  local testimonial="${45}" testimonialName="${46}"
  local logoHtml="${47}"
  local extraAccent="${48}"
  local navBrand="${49}"

  cat > "$file" << HTMLEOF
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>${company} | ${city}, AB</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@600;700;800&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--accent:${accent};--accent-light:${accentLight};--dark:${dark};--surface:#fff;--bg:#f4f5f7;--border:#dde2ec;--muted:#6a7890}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:var(--bg);color:#1a1a1a;overflow-x:hidden}
nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:0 6%;height:66px;background:var(--dark);border-bottom:2px solid var(--accent)}
.nav-brand{font-family:'Barlow Condensed',sans-serif;font-size:1.3rem;font-weight:700;color:#fff;text-decoration:none;text-transform:uppercase;letter-spacing:.05em;display:flex;align-items:center;gap:.5rem}
.nav-brand span{color:var(--accent)}
.nav-links{display:flex;gap:1.5rem;list-style:none;align-items:center}
.nav-links a{color:rgba(255,255,255,.65);text-decoration:none;font-size:.78rem;font-weight:500;letter-spacing:.04em;text-transform:uppercase;transition:color .2s}
.nav-links a:hover{color:#fff}
.nav-cta{background:var(--accent)!important;color:#fff!important;padding:.42rem 1.2rem;border-radius:3px;font-weight:700}
.hero{margin-top:66px;position:relative;min-height:calc(100vh - 66px);display:flex;align-items:center;overflow:hidden}
.hero-bg{position:absolute;inset:0;background:url('${heroImg}') center/cover no-repeat}
.hero-overlay{position:absolute;inset:0;background:linear-gradient(135deg,rgba(0,0,0,.7) 40%,rgba(0,0,0,.4))}
.hero-content{position:relative;z-index:2;padding:5rem 8%;max-width:780px}
.hero-eyebrow{font-size:.62rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:.8rem;margin-bottom:1.25rem}
.hero-eyebrow::before{content:'';display:block;width:24px;height:2px;background:var(--accent)}
.hero h1{font-family:'Barlow Condensed',sans-serif;font-size:clamp(3rem,6.5vw,6.5rem);font-weight:800;text-transform:uppercase;line-height:.95;color:#fff;margin-bottom:1.25rem}
.hero h1 span{color:var(--accent);display:block}
.hero p{font-size:.92rem;color:rgba(255,255,255,.55);line-height:1.9;max-width:480px;margin-bottom:2rem}
.hero-buttons{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.5rem}
.btn-primary{background:var(--accent);color:#fff;padding:.85rem 2rem;text-decoration:none;font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;border-radius:3px;transition:background .2s;display:inline-block;border:none;cursor:pointer}
.btn-primary:hover{background:var(--accent-light)}
.btn-ghost{border:2px solid rgba(255,255,255,.2);color:#fff;padding:.85rem 2rem;text-decoration:none;font-size:.8rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;border-radius:3px;transition:border-color .2s;display:inline-block}
.btn-ghost:hover{border-color:#fff}
.hero-trust{display:flex;gap:2rem;flex-wrap:wrap;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,.08)}
.trust-item{font-size:.78rem;color:rgba(255,255,255,.4);display:flex;align-items:center;gap:.5rem}
.trust-dot{width:5px;height:5px;background:var(--accent);border-radius:50%;flex-shrink:0}
.accent-strip{background:var(--accent);padding:1rem 8%;display:flex;align-items:center;justify-content:center;gap:3rem;flex-wrap:wrap}
.as-item{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#fff;display:flex;align-items:center;gap:.5rem}
.as-div{width:1px;height:14px;background:rgba(255,255,255,.3)}
section{padding:5rem 8%}
.sec-eyebrow{font-size:.62rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:.7rem;margin-bottom:.75rem}
.sec-eyebrow::before{content:'';display:block;width:20px;height:2px;background:var(--accent)}
.sec-title{font-family:'Barlow Condensed',sans-serif;font-size:clamp(2rem,4vw,3rem);font-weight:800;text-transform:uppercase;color:#1a1a1a;line-height:1;margin-bottom:1rem}
.sec-sub{color:var(--muted);font-size:.88rem;line-height:1.85;max-width:560px}
#services{background:var(--surface)}
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:2.5rem}
.svc-card{border:1px solid var(--border);border-top:3px solid var(--accent);padding:2rem 1.5rem;border-radius:0 0 4px 4px;transition:box-shadow .2s,transform .2s;background:#fff}
.svc-card:hover{box-shadow:0 6px 20px rgba(0,0,0,.08);transform:translateY(-3px)}
.svc-icon{width:44px;height:44px;background:rgba(0,0,0,.04);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.1rem;font-weight:800;color:var(--accent);margin-bottom:.75rem;font-family:'Barlow Condensed',sans-serif}
.svc-name{font-family:'Barlow Condensed',sans-serif;font-size:1.2rem;font-weight:700;text-transform:uppercase;color:#1a1a1a;margin-bottom:.4rem}
.svc-desc{font-size:.8rem;color:var(--muted);line-height:1.7}
#about{background:var(--dark);display:grid;grid-template-columns:1fr 1fr;gap:0;padding:0}
.about-img img{width:100%;height:100%;min-height:480px;object-fit:cover;display:block}
.about-body{padding:5rem 4rem;display:flex;flex-direction:column;justify-content:center}
#about .sec-title{color:#fff}
#about .sec-sub{color:rgba(255,255,255,.5);margin-bottom:.85rem}
.about-stats{display:flex;gap:2.5rem;margin-top:2rem;flex-wrap:wrap}
.stat-num{font-family:'Barlow Condensed',sans-serif;font-size:2.5rem;font-weight:800;color:var(--accent);line-height:1}
.stat-label{font-size:.75rem;color:rgba(255,255,255,.4);margin-top:.25rem}
.about-features{display:flex;flex-direction:column;gap:.75rem;margin-top:2rem}
.af{display:flex;gap:.75rem;font-size:.83rem;color:rgba(255,255,255,.5);align-items:flex-start}
.af-dot{width:5px;height:5px;background:var(--accent);border-radius:50%;margin-top:.4rem;flex-shrink:0}
#testimonial{background:var(--surface);text-align:center}
.testimonial-quote{font-size:1.25rem;font-style:italic;color:#1a1a1a;line-height:1.8;max-width:700px;margin:2rem auto 1.5rem;position:relative}
.testimonial-quote::before{content:'\201C';font-size:4rem;color:var(--accent);position:absolute;top:-2rem;left:-1rem;opacity:.3;font-family:Georgia,serif}
.testimonial-name{font-size:.85rem;font-weight:700;color:#1a1a1a}
.testimonial-loc{font-size:.75rem;color:var(--muted)}
#contact{background:var(--dark)}
#contact .sec-title{color:#fff}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;margin-top:2.5rem}
.ci{display:flex;gap:1rem;margin-bottom:1.25rem}
.ci-icon{width:40px;height:40px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:3px;display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;color:var(--accent);font-weight:700;font-family:'Barlow Condensed',sans-serif}
.ci-label{font-size:.6rem;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);margin-bottom:.2rem}
.ci-val{font-size:.9rem;color:rgba(255,255,255,.6)}
.ci-val a{color:rgba(255,255,255,.6);text-decoration:none}
.fg{margin-bottom:.9rem}
.fg label{font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.35);display:block;margin-bottom:.4rem}
.fg input,.fg textarea,.fg select{width:100%;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-bottom:2px solid rgba(255,255,255,.1);padding:.78rem 1rem;color:#fff;font-family:'Inter',sans-serif;font-size:.875rem;outline:none;transition:border-color .2s}
.fg input:focus,.fg textarea:focus,.fg select:focus{border-bottom-color:var(--accent)}
.fg textarea{height:110px;resize:vertical}
.fg select option{background:#1a2030}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.btn-submit{background:var(--accent);color:#fff;border:none;width:100%;padding:1rem;font-family:'Inter',sans-serif;font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;cursor:pointer;border-radius:3px;transition:background .2s}
.btn-submit:hover{background:var(--accent-light)}
footer{background:#080c10;padding:1.5rem 8%;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;border-top:2px solid var(--accent)}
.footer-brand{font-family:'Barlow Condensed',sans-serif;font-size:1rem;font-weight:700;text-transform:uppercase;color:#fff;letter-spacing:.05em}
.footer-brand span{color:var(--accent)}
.footer-copy{font-size:.72rem;color:rgba(255,255,255,.2)}
.footer-demo{font-size:.62rem;color:rgba(255,255,255,.15)}
@media(max-width:1024px){.svc-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:860px){
nav .nav-links{display:none}
.nav-mobile-cta{display:inline-block!important}
section{padding:4rem 6%}
#about{grid-template-columns:1fr}
.about-img img{min-height:260px;height:260px}
.about-body{padding:3rem 6%}
.contact-grid{grid-template-columns:1fr;gap:3rem}
.accent-strip{gap:1.5rem;flex-direction:column;align-items:flex-start;padding:1rem 6%}
.as-div{display:none}
}
@media(max-width:600px){
.hero h1{font-size:3rem}
.svc-grid{grid-template-columns:1fr}
.fr{grid-template-columns:1fr}
footer{flex-direction:column;align-items:flex-start}
}
</style>
</head>
<body>
<nav>
<a href="#" class="nav-brand">${logoHtml}<span>${navBrand}</span></a>
<ul class="nav-links">
<li><a href="#services">Services</a></li>
<li><a href="#about">About</a></li>
<li><a href="#contact" class="nav-cta">Get a Quote</a></li>
</ul>
<a href="#contact" class="nav-mobile-cta" style="display:none;font-size:.72rem;font-weight:700;background:var(--accent);color:#fff;padding:.45rem 1rem;border-radius:3px;text-decoration:none">Quote</a>
</nav>

<div class="hero">
<div class="hero-bg"></div>
<div class="hero-overlay"></div>
<div class="hero-content">
<div class="hero-eyebrow">${city}, AB · Licensed & Insured</div>
<h1>${heroWhite}<br/><span>${heroAccent}</span></h1>
<p>${subheadline}</p>
<div class="hero-buttons">
<a href="#contact" class="btn-primary">Get a Free Quote</a>
<a href="#services" class="btn-ghost">Our Services</a>
</div>
<div class="hero-trust">
<div class="trust-item"><div class="trust-dot"></div>Licensed & Insured</div>
<div class="trust-item"><div class="trust-dot"></div>Free Estimates</div>
<div class="trust-item"><div class="trust-dot"></div>Satisfaction Guaranteed</div>
</div>
</div>
</div>

<div class="accent-strip">
<div class="as-item"><svg width="18" height="18" fill="#fff" viewBox="0 0 24 24"><path d="${svcIcon1}"/></svg> ${strip1}</div>
<div class="as-div"></div>
<div class="as-item"><svg width="18" height="18" fill="#fff" viewBox="0 0 24 24"><path d="${svcIcon2}"/></svg> ${strip2}</div>
<div class="as-div"></div>
<div class="as-item"><svg width="18" height="18" fill="#fff" viewBox="0 0 24 24"><path d="${svcIcon3}"/></svg> ${strip3}</div>
<div class="as-div"></div>
<div class="as-item"><svg width="18" height="18" fill="#fff" viewBox="0 0 24 24"><path d="${svcIcon4}"/></svg> ${strip4}</div>
</div>

<section id="services">
<div class="sec-eyebrow">What We Do</div>
<div class="sec-title">Our Services</div>
<p class="sec-sub">Professional, reliable service backed by years of experience and a commitment to quality craftsmanship.</p>
<div class="svc-grid">
<div class="svc-card">
<div class="svc-icon">01</div>
<div class="svc-name">${svcLabel1}</div>
<p class="svc-desc">${svcDesc1}</p>
</div>
<div class="svc-card">
<div class="svc-icon">02</div>
<div class="svc-name">${svcLabel2}</div>
<p class="svc-desc">${svcDesc2}</p>
</div>
<div class="svc-card">
<div class="svc-icon">03</div>
<div class="svc-name">${svcLabel3}</div>
<p class="svc-desc">${svcDesc3}</p>
</div>
<div class="svc-card">
<div class="svc-icon">04</div>
<div class="svc-name">${svcLabel4}</div>
<p class="svc-desc">${svcDesc4}</p>
</div>
<div class="svc-card">
<div class="svc-icon">05</div>
<div class="svc-name">${svcLabel5}</div>
<p class="svc-desc">${svcDesc5}</p>
</div>
<div class="svc-card">
<div class="svc-icon">06</div>
<div class="svc-name">${svcLabel6}</div>
<p class="svc-desc">${svcDesc6}</p>
</div>
</div>
</section>

<section id="about">
<div class="about-img">
<img src="${aboutImg}" alt="${company} team at work"/>
</div>
<div class="about-body">
<div class="sec-eyebrow">About Us</div>
<div class="sec-title">Built on Trust.<br/>Driven by Quality.</div>
<p class="sec-sub">${aboutText1}</p>
<p class="sec-sub" style="margin-top:.75rem">${aboutText2}</p>
<div class="about-stats">
<div><div class="stat-num">${stat1Num}</div><div class="stat-label">${stat1Label}</div></div>
<div><div class="stat-num">${stat2Num}</div><div class="stat-label">${stat2Label}</div></div>
<div><div class="stat-num">${stat3Num}</div><div class="stat-label">${stat3Label}</div></div>
</div>
<div class="about-features">
<div class="af"><div class="af-dot"></div>Fully licensed and insured for your protection</div>
<div class="af"><div class="af-dot"></div>Free, no-obligation estimates on every project</div>
<div class="af"><div class="af-dot"></div>Clean, professional crew that respects your property</div>
</div>
</div>
</section>

<section id="testimonial">
<div class="sec-eyebrow" style="justify-content:center">What Clients Say</div>
<div class="sec-title" style="text-align:center">Trusted by Homeowners</div>
<div class="testimonial-quote">${testimonial}</div>
<div class="testimonial-name">${testimonialName}</div>
<div class="testimonial-loc">${city}, AB</div>
</section>

<section id="contact">
<div class="sec-eyebrow">Get in Touch</div>
<div class="sec-title" style="color:#fff">Request a Free Quote</div>
<div class="contact-grid">
<div>
<div class="ci"><div class="ci-icon">P</div><div><div class="ci-label">Phone</div><div class="ci-val"><a href="tel:${phone}">${phone}</a></div></div></div>
<div class="ci"><div class="ci-icon">E</div><div><div class="ci-label">Email</div><div class="ci-val"><a href="mailto:${email}">${email}</a></div></div></div>
<div class="ci"><div class="ci-icon">L</div><div><div class="ci-label">Location</div><div class="ci-val">${address}</div></div></div>
<div class="ci"><div class="ci-icon">H</div><div><div class="ci-label">Hours</div><div class="ci-val">Mon - Fri: 7:00 AM - 6:00 PM</div></div></div>
</div>
<div>
<div class="fr">
<div class="fg"><label>First Name</label><input type="text" placeholder="John"/></div>
<div class="fg"><label>Last Name</label><input type="text" placeholder="Smith"/></div>
</div>
<div class="fg"><label>Phone</label><input type="tel" placeholder="000-000-0000"/></div>
<div class="fg"><label>Email</label><input type="email" placeholder="you@example.com"/></div>
<div class="fg"><label>Project Details</label><textarea placeholder="Tell us about your project…"></textarea></div>
<button class="btn-submit" type="button" onclick="submitForm()">Submit Request</button>
<div id="cf-status" style="margin-top:12px;font-size:.8rem;display:none;padding:10px 14px;border-radius:4px"></div>
</div>
</div>
</section>

<script>
function submitForm(){
var f=document.querySelector('input[placeholder="John"]').value.trim();
var e=document.querySelector('input[placeholder="you@example.com"]').value.trim();
var s=document.getElementById('cf-status');
if(!f||!e){s.style.display='block';s.style.background='rgba(239,68,68,.1)';s.style.color='#ef4444';s.style.border='1px solid rgba(239,68,68,.3)';s.textContent='Please fill in your name and email.';return}
var b='New Quote Request from '+f+' - '+document.querySelector('textarea').value;
window.location.href='mailto:${email}?subject='+encodeURIComponent('Quote Request from '+f)+'&body='+encodeURIComponent(b);
s.style.display='block';s.style.background='rgba(34,197,94,.1)';s.style.color='#22c55e';s.style.border='1px solid rgba(34,197,94,.3)';s.textContent='Opening your email app…';
}
</script>

<footer>
<div class="footer-brand">${company} <span>| ${city}</span></div>
<div class="footer-copy">&copy; 2026 ${company} &middot; ${city}, AB</div>
<div class="footer-demo">Powered by Wildrose Automations</div>
</footer>
</body>
</html>
HTMLEOF
}

# SVG icon paths (simplified)
HAMMER="M2 21l2-2L13.5 9.5 12 8l2-2 4 4-2 2-1.5-1.5L5 20l-2 1zm16-13l2-2-3-3-2 2 3 3z"
BROOM="M4 4l10 10m0 0l-6 6m6-6l6-6"
HOUSE="M12 3L2 12h3v8h6v-6h2v6h6v-8h3L12 3z"
WRENCH="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5L18.9 22.7c.6.6 1.5.6 2.1 0l1.7-1.7c.5-.6.5-1.5 0-2z"
PAINT="M16 4h2V2h-4v2h-2V0H8v2H6V2H2v2h2v4H2v2h2v4H2v2h2v4H2v2h4v-2h2v2h4v-2h2v2h4v-2h-2v-4h2v-2h-2v-4h2V8h-2V4z"
LEAF="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66L7 19c4-4 6-7 10-11z"
TREE="M12 2L4 14h3v8h10v-8h3L12 2z"
ROOF="M12 3L2 12h3v9h6v-6h2v6h6v-9h3L12 3z"
SNOW="M12 2l2.4 5.2L20 8l-4 3.6L17.2 18 12 14.4 6.8 18 8 11.6 4 8l5.6-.8z"
FILTER="M3 4h18l-6.5 8v5l-5 2v-7L3 4z"
CARPET="M3 6h18v12H3V6zm2 2v8h14V8H5z"
ROCK="M4 18l4-12 6 4 6-4v12H4z"
MOW="M12 18c3.3 0 6-2.7 6-6s-2.7-6-6-6-6 2.7-6 6 2.7 6 6 6z"
TRUCK="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4z"
PHONE="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"
CHECK="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"
STAR="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"

echo "Generating 20 demo HTML files..."

# 1. Kino Handyman
generate "kino-handyman-demo.html" \
  "Kino Handyman & Construction Services" "kinoconstructionservices@gmail.com" "Edmonton" "780-555-0142" "12456 82 Ave NW, Edmonton, AB T5M 3R1" \
  "#E65100" "#F4511E" "#1a1a1a" \
  "assets/stock/handyman-hero.jpg" "assets/stock/handyman-about.jpg" \
  "EXPERT" "HANDYMAN SERVICES" \
  "From minor repairs to full renovations, Kino Handyman & Construction delivers reliable, professional craftsmanship across Edmonton. No job too big or too small." \
  "$HAMMER" "General Repairs" "Leaky faucets, drywall patches, door adjustments and every fix in between — we handle it all with precision." \
  "$WRENCH" "Renovations" "Kitchen and bathroom upgrades, basement developments, and full home transformations completed on time and on budget." \
  "$HOUSE" "Carpentry" "Custom shelving, deck building, fence installation, and trim work that adds real value to your property." \
  "$PAINT" "Painting" "Interior and exterior painting with premium materials and meticulous prep work for a lasting finish." \
  "$BROOM" "Drywall & Taping" "New installations, repairs, and seamless mudding and taping for smooth, paint-ready walls." \
  "$TRUCK" "Assembly & Installation" "Furniture assembly, TV mounting, fixture installation, and all those tasks you keep putting off." \
  "General Repairs" "Renovations" "Painting" "Carpentry" \
  "Kino Handyman & Construction has been serving Edmonton homeowners with honest, dependable handyman services for over a decade. We treat every home like it's our own." \
  "Whether you need a quick fix or a major renovation, our skilled team brings the tools, experience, and work ethic to get it done right the first time." \
  "12+" "Years Experience" "2,000+" "Projects Completed" "500+" "Happy Clients" \
  "They showed up on time, did incredible work on our bathroom renovation, and left the place spotless. Couldn't recommend them more highly." \
  "Sarah M., Edmonton" \
  '<img src="assets/kino-handyman/logo.png" alt="Kino" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Kino Handyman"

# 2. Handyman Reality
generate "handyman-reality-demo.html" \
  "Handyman Reality" "kewlguy@handymanreality.com" "Edmonton" "780-555-0198" "9823 111 St NW, Edmonton, AB T5K 1L5" \
  "#E65100" "#F4511E" "#1a1a1a" \
  "assets/stock/construction-hero.jpg" "assets/stock/handyman-about.jpg" \
  "YOUR HOME" "IN GOOD HANDS" \
  "Handyman Reality turns your home improvement to-do list into a done list. Professional, punctual, and priced right — serving all of Edmonton." \
  "$HAMMER" "Home Repairs" "Quick, reliable fixes for everything that needs attention around your home — from squeaky doors to leaky pipes." \
  "$WRENCH" "Kitchen & Bath" "Full kitchen and bathroom renovations designed around your vision, your schedule, and your budget." \
  "$HOUSE" "Deck & Fence" "Custom deck construction, fence building, and outdoor structures built to withstand Alberta winters." \
  "$PAINT" "Interior Painting" "Clean lines, smooth finishes, and colors that transform your space — inside and out." \
  "$BROOM" "Drywall Services" "Expert drywall installation, repair, and finishing for flawless walls and ceilings." \
  "$TRUCK" "Assembly & Mounting" "Furniture, TVs, shelves, and fixtures installed quickly and securely." \
  "Home Repairs" "Renovations" "Decks & Fences" "Painting" \
  "Handyman Reality was founded on a simple idea — homeowners deserve a handyman service that actually shows up, does great work, and charges a fair price." \
  "We've built our reputation one satisfied customer at a time, and we plan to keep it that way. Your home is our priority." \
  "8+" "Years in Business" "1,500+" "Jobs Completed" "98%" "Client Satisfaction" \
  "Finally a handyman who shows up when they say they will. Fantastic work on our deck — it looks better than we imagined." \
  "Mike R., Edmonton" \
  "" "" "Handyman Reality"

# 3. Delano Maintenance
generate "delano-maintenance-demo.html" \
  "Delano Maintenance Solutions" "info@delanomaintenance.ca" "Edmonton" "780-555-0267" "5678 Calgary Trail NW, Edmonton, AB T6H 0P7" \
  "#E65100" "#F4511E" "#1a1a1a" \
  "assets/stock/handyman-hero.jpg" "assets/stock/construction-hero.jpg" \
  "COMPLETE" "PROPERTY CARE" \
  "Delano Maintenance Solutions provides comprehensive property maintenance and improvement services for Edmonton homeowners and businesses alike." \
  "$HAMMER" "Property Maintenance" "Year-round maintenance programs to keep your property in top shape — inside and out." \
  "$WRENCH" "General Contracting" "From small repairs to large-scale renovations, we manage every detail from start to finish." \
  "$HOUSE" "Seasonal Services" "Spring cleanup, winter prep, and everything in between to protect your investment year-round." \
  "$PAINT" "Painting & Finishing" "Professional interior and exterior painting with premium products and expert craftsmanship." \
  "$BROOM" "Flooring" "Hardwood, laminate, tile, and vinyl installation and repair for any room in your home." \
  "$TRUCK" "Emergency Repairs" "When something breaks unexpectedly, we're available for fast, reliable emergency repairs." \
  "Property Maintenance" "Contracting" "Seasonal Services" "Emergency Repairs" \
  "Delano Maintenance Solutions takes the stress out of property ownership. Our team handles everything so you don't have to worry about a thing." \
  "With transparent pricing, clear communication, and skilled tradespeople on every job, we deliver results that speak for themselves." \
  "10+" "Years Experience" "3,000+" "Maintenance Visits" "250+" "Property Clients" \
  "They maintain three of my rental properties and I never hear complaints from tenants. That's all I need to know." \
  "David L., Edmonton" \
  "" "" "Delano Maintenance"

# 4. BAHM Contracting
generate "bahm-contracting-demo.html" \
  "BAHM Contracting" "aaron@bahmcontracting.com" "Edmonton" "780-555-0334" "14567 118 Ave NW, Edmonton, AB T5L 2M8" \
  "#E65100" "#F4511E" "#1a1a1a" \
  "assets/stock/construction-hero.jpg" "assets/stock/handyman-about.jpg" \
  "BUILDING" "BETTER SPACES" \
  "BAHM Contracting delivers top-quality construction and renovation services across Edmonton. Professional results, honest pricing, guaranteed satisfaction." \
  "$HAMMER" "New Construction" "Custom builds and new construction projects managed with precision, quality materials, and expert craftsmanship." \
  "$WRENCH" "Basement Development" "Transform your basement into a livable space — family rooms, suites, home offices, and recreation areas." \
  "$HOUSE" "Kitchen Renovations" "Complete kitchen transformations from design to completion, with custom cabinetry and premium finishes." \
  "$PAINT" "Bathroom Renovations" "Modern bathroom updates and full gut renovations with quality fixtures and tile work." \
  "$BROOM" "Structural Work" "Load-bearing wall removal, structural modifications, and engineering-compliant construction solutions." \
  "$TRUCK" "Project Management" "Full-service project management with transparent timelines, budgets, and regular progress updates." \
  "New Construction" "Basements" "Kitchens" "Bathrooms" \
  "BAHM Contracting was built on the principle that every project deserves the same attention to detail — whether it's a small renovation or a complete build." \
  "Aaron and the team bring decades of combined construction experience to every job site, ensuring quality that lasts." \
  "15+" "Years in Construction" "400+" "Projects Delivered" "100%" "Code Compliant" \
  "Aaron and his crew finished our basement ahead of schedule and under budget. The quality of work is outstanding." \
  "James T., Edmonton" \
  "" "" "BAHM Contracting"

# 5. Handyman YYC
generate "handyman-yyc-demo.html" \
  "Handyman YYC" "info@handymanyyc.ca" "Edmonton" "780-555-0421" "3456 Whyte Ave NW, Edmonton, AB T6K 2E1" \
  "#E65100" "#F4511E" "#1a1a1a" \
  "assets/stock/handyman-hero.jpg" "assets/stock/handyman-about.jpg" \
  "EDMONTON'S" "GO-TO HANDYMAN" \
  "Handyman YYC brings fast, friendly, and affordable home improvement services to Edmonton. From quick fixes to full projects, we've got you covered." \
  "$HAMMER" "General Repairs" "No repair too small — doors, windows, fixtures, and everything that needs fixing around your home." \
  "$WRENCH" "Full Renovations" "Complete renovation services for kitchens, bathrooms, basements, and entire homes." \
  "$HOUSE" "Outdoor Projects" "Deck building, fence repairs, shed construction, and outdoor structure installations." \
  "$PAINT" "Painting Services" "Interior and exterior painting with clean lines, proper prep, and lasting results." \
  "$BROOM" "Maintenance Plans" "Regular maintenance programs to keep your home in peak condition all year long." \
  "$TRUCK" "Move-In Ready" "Getting a new home ready? We handle painting, repairs, upgrades, and everything on your list." \
  "Repairs" "Renovations" "Outdoor Work" "Painting" \
  "Handyman YYC started with a simple mission — make quality home improvement accessible to everyone. No inflated prices, no hidden fees, just honest work." \
  "Our team of skilled tradespeople brings experience, reliability, and a genuine care for your home to every single project." \
  "6+" "Years Serving Edmonton" "1,800+" "Jobs Done" "4.9" "Star Rating" \
  "They repainted our entire main floor in two days and it looks phenomenal. Professional, clean, and super friendly." \
  "Amanda K., Edmonton" \
  '<img src="assets/handyman-yyc/logo.png" alt="Handyman YYC" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Handyman YYC"

# 6. Sunset Maintenance
generate "sunset-maintenance-demo.html" \
  "Sunset Maintenance Services" "bmjserv@telus.net" "Red Deer" "403-555-0178" "2345 Gaetz Ave, Red Deer, AB T4R 2M6" \
  "#00897B" "#26A69A" "#004D40" \
  "assets/stock/cleaning-hero.jpg" "assets/stock/cleaning-office.jpg" \
  "RELIABLE" "MAINTENANCE SOLUTIONS" \
  "Sunset Maintenance Services keeps Red Deer properties looking their best. From regular maintenance to one-time deep cleans, we deliver results you can see." \
  "$BROOM" "Property Maintenance" "Comprehensive maintenance programs for residential and commercial properties in Red Deer." \
  "$HAMMER" "Janitorial Services" "Professional cleaning and maintenance for offices, retail spaces, and commercial buildings." \
  "$HOUSE" "Seasonal Cleanup" "Spring and fall cleanup services to keep your property pristine through every season." \
  "$PAINT" "Minor Repairs" "Quick fixes and maintenance repairs that prevent small problems from becoming big expenses." \
  "$TRUCK" "Floor Care" "Floor stripping, waxing, polishing, and deep cleaning for all floor types." \
  "$CHECK" "Inspection Services" "Regular property inspections to catch maintenance issues early and keep everything running smoothly." \
  "Property Maintenance" "Janitorial" "Seasonal Cleanup" "Floor Care" \
  "Sunset Maintenance Services has been a trusted name in Red Deer property care for years. We take pride in keeping our community's properties in excellent condition." \
  "Our dedicated team shows up on time, every time, with the tools and expertise to handle any maintenance challenge." \
  "9+" "Years in Red Deer" "1,200+" "Properties Serviced" "100+" "Commercial Clients" \
  "Sunset Maintenance has been taking care of our office building for three years now. Always reliable, always thorough." \
  "Patricia W., Red Deer" \
  "" "" "Sunset Maintenance"

# 7. M&M Janitorial
generate "mm-janitorial-demo.html" \
  "M&M Janitorial & Property Maintenance" "info@mmjanitorial.ca" "Red Deer" "403-555-0234" "7890 50 Ave, Red Deer, AB T4R 1K2" \
  "#00897B" "#26A69A" "#004D40" \
  "assets/stock/cleaning-office.jpg" "assets/stock/cleaning-about.jpg" \
  "PREMIER" "JANITORIAL SERVICES" \
  "M&M Janitorial & Property Maintenance delivers spotless results for Red Deer businesses and homes. Professional cleaning that makes a real difference." \
  "$BROOM" "Commercial Cleaning" "Daily, weekly, and monthly commercial cleaning contracts tailored to your business needs and schedule." \
  "$HAMMER" "Property Maintenance" "Full-service property maintenance including repairs, inspections, and seasonal upkeep." \
  "$HOUSE" "Office Cleaning" "Detailed office cleaning services that create a healthy, productive work environment." \
  "$PAINT" "Deep Cleaning" "One-time deep cleaning services for move-ins, move-outs, and special occasions." \
  "$TRUCK" "Floor Care" "Professional carpet cleaning, floor stripping, waxing, and polishing services." \
  "$CHECK" "Post-Construction" "Thorough post-construction cleanup to make your newly renovated space move-in ready." \
  "Commercial Cleaning" "Property Maintenance" "Floor Care" "Deep Cleaning" \
  "M&M Janitorial & Property Maintenance has built a reputation in Red Deer for reliability, thoroughness, and attention to detail that our competitors simply can't match." \
  "Our trained and insured team uses professional-grade equipment and eco-friendly products to deliver consistently outstanding results." \
  "15+" "Years in Business" "200+" "Commercial Accounts" "99%" "Client Retention" \
  "We switched to M&M six months ago and the difference in our office cleanliness is remarkable. Best decision we made." \
  "Robert H., Red Deer" \
  '<img src="assets/mm-janitorial/logo.png" alt="M&M Janitorial" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "M&M Janitorial"

# 8. Performance Maintenance
generate "performance-maintenance-demo.html" \
  "Performance Building Maintenance" "info@performancemaint.com" "Red Deer" "403-555-0289" "4567 Ross St, Red Deer, AB T4N 1R4" \
  "#00897B" "#26A69A" "#004D40" \
  "assets/stock/cleaning-hero.jpg" "assets/stock/cleaning-office.jpg" \
  "PERFORMANCE" "YOU CAN COUNT ON" \
  "Performance Building Maintenance delivers exceptional commercial cleaning and maintenance services throughout Red Deer. When results matter, choose Performance." \
  "$BROOM" "Commercial Cleaning" "Customized cleaning programs for offices, retail, industrial, and institutional facilities." \
  "$HAMMER" "Building Maintenance" "Comprehensive building maintenance including HVAC filters, lighting, plumbing, and general repairs." \
  "$HOUSE" "Floor Maintenance" "Professional floor care — carpet cleaning, hard surface maintenance, stripping, waxing, and polishing." \
  "$PAINT" "Window Cleaning" "Interior and exterior window cleaning for crystal-clear results that improve your building's appearance." \
  "$TRUCK" "Pressure Washing" "Exterior pressure washing for sidewalks, parking lots, building facades, and loading docks." \
  "$CHECK" "Emergency Response" "24/7 emergency cleaning and maintenance response for unexpected situations." \
  "Commercial Cleaning" "Building Maintenance" "Floor Care" "Emergency Response" \
  "At Performance Building Maintenance, we understand that a clean, well-maintained facility reflects directly on your business. That's why we deliver performance you can measure." \
  "Our management team provides detailed reporting, quality audits, and responsive communication to ensure your complete satisfaction." \
  "20+" "Years of Excellence" "150+" "Facilities Maintained" "24/7" "Emergency Service" \
  "Performance maintains all four of our Red Deer locations. Their consistency and professionalism are second to none." \
  "Linda S., Red Deer" \
  '<img src="assets/performance-maintenance/logo.png" alt="Performance" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Performance Maintenance"

# 9. Mancuso Cleaning
generate "mancuso-cleaning-demo.html" \
  "Mancuso Carpet & Upholstery Cleaning" "cynthia@mancuso-cleaning.com" "Red Deer" "403-555-0345" "1234 Molly Ban Dr, Red Deer, AB T4P 1N3" \
  "#00897B" "#26A69A" "#004D40" \
  "assets/stock/carpet-cleaning.jpg" "assets/stock/cleaning-about.jpg" \
  "DEEP CLEAN" "CARPET & UPHOLSTERY" \
  "Mancuso Carpet & Upholstery Cleaning restores the beauty of your carpets and furniture with professional-grade equipment and proven techniques." \
  "$BROOM" "Carpet Cleaning" "Hot water extraction and deep cleaning that removes dirt, stains, allergens, and odors from any carpet type." \
  "$HAMMER" "Upholstery Cleaning" "Safe, effective cleaning for all furniture fabrics — sofas, chairs, ottomans, and more." \
  "$HOUSE" "Stain Removal" "Specialized stain treatment for tough spots including pet stains, wine, ink, and food spills." \
  "$PAINT" "Area Rug Cleaning" "Professional cleaning for oriental, Persian, and decorative area rugs of all sizes." \
  "$TRUCK" "Pet Odor Treatment" "Enzyme-based treatments that eliminate pet odors at the source, not just mask them." \
  "$CHECK" "Protector Application" "Scotchgard and fabric protector application to keep your carpets and upholstery cleaner, longer." \
  "Carpet Cleaning" "Upholstery" "Stain Removal" "Pet Treatment" \
  "Cynthia Mancuso has built Mancuso Carpet & Upholstery Cleaning into Red Deer's most trusted name in professional carpet care." \
  "We use truck-mounted equipment, eco-friendly products, and proven techniques to deliver results that will make your carpets look and feel like new." \
  "12+" "Years in Red Deer" "5,000+" "Homes Cleaned" "100%" "Satisfaction Guarantee" \
  "Our carpets look brand new after Mancuso cleaned them. With three dogs, I didn't think it was possible. Amazing work!" \
  "Jennifer B., Red Deer" \
  "" "" "Mancuso Cleaning"

# 10. McWinn Filter
generate "mcwinn-filter-demo.html" \
  "McWinn Air Filter Cleaning Service" "info@mcwinnfiltercleaningsystems.ca" "Red Deer" "403-555-0412" "5678 Taylor Dr, Red Deer, AB T4R 3H2" \
  "#00897B" "#26A69A" "#004D40" \
  "assets/stock/cleaning-hero.jpg" "assets/stock/cleaning-about.jpg" \
  "CLEAN AIR" "CLEAN FILTERS" \
  "McWinn Air Filter Cleaning Service provides professional filter cleaning and maintenance for industrial, commercial, and residential clients throughout Central Alberta." \
  "$FILTER" "Filter Cleaning" "Professional cleaning of all air filter types — restoring performance and extending filter life." \
  "$HAMMER" "Industrial Filters" "Heavy-duty filter cleaning for mining, oilfield, construction, and industrial equipment." \
  "$HOUSE" "HVAC Filters" "Residential and commercial HVAC filter cleaning and replacement services." \
  "$PAINT" "Compressor Filters" "Air compressor filter cleaning and maintenance for optimal equipment performance." \
  "$TRUCK" "Pickup & Delivery" "Convenient pickup and delivery service throughout Red Deer and Central Alberta." \
  "$CHECK" "Filter Inspection" "Comprehensive filter inspection and testing to determine cleaning vs. replacement needs." \
  "Filter Cleaning" "Industrial Filters" "HVAC Filters" "Pickup & Delivery" \
  "McWinn Air Filter Cleaning Service has been Central Alberta's trusted filter specialist for years. We help businesses and homeowners save money by restoring filters to like-new condition." \
  "Our specialized cleaning process removes contaminants that standard cleaning can't touch, improving air quality and equipment efficiency." \
  "18+" "Years of Experience" "10,000+" "Filters Cleaned" "60%" "Cost Savings vs New" \
  "McWinn saves us thousands per year on industrial filter replacements. Their cleaning quality is indistinguishable from new filters." \
  "Tom M., Red Deer" \
  "" "" "McWinn Filter"

# 11. Clean Getaway
generate "clean-getaway-demo.html" \
  "The Clean Getaway" "michelle@thecleangetaway.ca" "Red Deer" "403-555-0156" "9012 47 Ave, Red Deer, AB T4N 3H5" \
  "#00897B" "#26A69A" "#004D40" \
  "assets/stock/cleaning-hero.jpg" "assets/stock/cleaning-about.jpg" \
  "ESCAPE THE" "MESS — WE CLEAN" \
  "The Clean Getaway takes the stress out of cleaning. Professional residential and commercial cleaning services that let you focus on what matters." \
  "$BROOM" "Residential Cleaning" "Regular and one-time home cleaning services that leave every room spotless and fresh." \
  "$HAMMER" "Commercial Cleaning" "Office and commercial space cleaning that creates a healthy, professional environment." \
  "$HOUSE" "Move-In/Out Cleaning" "Thorough move-in and move-out cleaning to ensure smooth transitions and returned deposits." \
  "$PAINT" "Deep Cleaning" "Comprehensive deep cleaning that reaches every corner, baseboard, and hidden surface." \
  "$TRUCK" "Airbnb Turnover" "Fast, reliable Airbnb and rental property turnover cleaning between guests." \
  "$CHECK" "Custom Packages" "Customized cleaning plans designed around your specific needs, schedule, and budget." \
  "Residential Cleaning" "Commercial Cleaning" "Move-In/Out" "Airbnb Turnover" \
  "The Clean Getaway was founded by Michelle with a passion for creating clean, comfortable spaces for Red Deer families and businesses." \
  "Every cleaning is performed by our trained, insured team using eco-friendly products and a detailed checklist that ensures nothing gets missed." \
  "7+" "Years in Business" "800+" "Regular Clients" "5-Star" "Average Rating" \
  "Michelle and her team are absolute lifesavers. Our home has never been this clean, and we actually get to enjoy our weekends now." \
  "Karen D., Red Deer" \
  '<img src="assets/clean-getaway/logo.png" alt="Clean Getaway" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Clean Getaway"

# 12. Edmonton Stone
generate "edmonton-stone-demo.html" \
  "Edmonton Stone Designers" "edmontonstone@shaw.ca" "Edmonton" "780-555-0567" "18923 Stony Plain Rd NW, Edmonton, AB T5S 1A8" \
  "#2E7D32" "#43A047" "#1a2e1a" \
  "assets/stock/stone-wall.jpg" "assets/stock/stone-work.jpg" \
  "PRECISION" "STONE CRAFTSMANSHIP" \
  "Edmonton Stone Designers creates stunning stone features that transform properties. From accent walls to full exteriors, we bring natural beauty to every project." \
  "$ROCK" "Stone Veneer" "Manufactured and natural stone veneer installation for interiors and exteriors." \
  "$HAMMER" "Accent Walls" "Custom stone accent walls for fireplaces, entryways, and feature walls that make a statement." \
  "$HOUSE" "Exterior Stone" "Complete exterior stone cladding and facades that boost curb appeal and property value." \
  "$PAINT" "Patios & Walkways" "Stone patios, walkways, and outdoor living spaces designed and built to last." \
  "$TRUCK" "Fire Pits" "Custom stone fire pits and outdoor fireplaces for the ultimate backyard experience." \
  "$CHECK" "Restoration" "Stone repair, repointing, and restoration for existing stone features and heritage buildings." \
  "Stone Veneer" "Accent Walls" "Exterior Stone" "Patios & Walkways" \
  "Edmonton Stone Designers has been the city's premier stone installation specialist for over 20 years. Our craftsmen bring decades of masonry experience to every project." \
  "We work with natural stone, manufactured stone, and brick to create features that are both beautiful and built to last through Alberta's toughest weather." \
  "20+" "Years of Craftsmanship" "1,500+" "Stone Projects" "100%" "Satisfaction Guaranteed" \
  "The stone fireplace they built for us is absolutely stunning. Every guest comments on it. True artisans." \
  "Margaret P., Edmonton" \
  '<img src="assets/edmonton-stone/logo.png" alt="Edmonton Stone" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Edmonton Stone"

# 13. Greenland Landscaping
generate "greenland-landscaping-demo.html" \
  "Greenland Landscaping" "greenlandcontracting79@gmail.com" "Edmonton" "780-555-0623" "21034 66 St NW, Edmonton, AB T5M 3K1" \
  "#2E7D32" "#43A047" "#1a2e1a" \
  "assets/stock/landscaping-hero.jpg" "assets/stock/landscape-about.jpg" \
  "YOUR LANDSCAPE" "YOUR LEGACY" \
  "Greenland Landscaping transforms Edmonton outdoor spaces into stunning, functional landscapes. From design to maintenance, we bring your vision to life." \
  "$TREE" "Landscape Design" "Custom landscape design plans tailored to your property, preferences, and budget." \
  "$HAMMER" "Hardscaping" "Patios, retaining walls, walkways, and outdoor structures built with quality materials." \
  "$HOUSE" "Softscaping" "Garden beds, tree planting, sod installation, and seasonal color that brings your yard alive." \
  "$LEAF" "Lawn Care" "Complete lawn maintenance including mowing, fertilizing, aeration, and weed control." \
  "$TRUCK" "Irrigation" "Irrigation system design, installation, and maintenance for efficient water management." \
  "$CHECK" "Snow Removal" "Reliable residential and commercial snow removal services through Edmonton's toughest winters." \
  "Landscape Design" "Hardscaping" "Lawn Care" "Snow Removal" \
  "Greenland Landscaping has been shaping Edmonton's outdoor spaces for over 15 years. We combine creative design with solid craftsmanship to deliver landscapes that stand the test of time." \
  "Our experienced team handles everything from initial design concepts through to ongoing maintenance, ensuring your landscape investment stays beautiful for years to come." \
  "15+" "Years Landscaping" "2,500+" "Projects Completed" "350+" "Regular Clients" \
  "Greenland completely transformed our backyard. From the design phase to the final walk-through, everything was professional and the result exceeded our expectations." \
  "Chris W., Edmonton" \
  '<img src="assets/greenland-landscaping/logo.png" alt="Greenland" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Greenland Landscaping"

# 14. MowSnowPros
generate "mowsnowpros-demo.html" \
  "MowSnowPros" "aidan@mowsnowpros.com" "Edmonton" "780-555-0789" "15678 34 Ave NW, Edmonton, AB T6L 2A4" \
  "#2E7D32" "#43A047" "#1a2e1a" \
  "assets/stock/landscaping-hero.jpg" "assets/stock/garden-design.jpg" \
  "MOWING & SNOW" "PROS OF EDMONTON" \
  "MowSnowPros keeps your property looking perfect year-round. Expert lawn care in summer, reliable snow removal in winter — that's the pro difference." \
  "$MOW" "Lawn Mowing" "Weekly and bi-weekly mowing services with professional equipment for a clean, manicured look." \
  "$SNOW" "Snow Removal" "Residential and commercial snow clearing with reliable scheduling and fast response times." \
  "$HOUSE" "Lawn Care" "Fertilizing, aeration, overseeding, and weed control programs for a healthy, green lawn." \
  "$LEAF" "Spring Cleanup" "Comprehensive spring cleanup to get your property looking great after a long winter." \
  "$TRUCK" "Fall Cleanup" "Leaf removal, garden winterization, and property preparation for the cold months ahead." \
  "$CHECK" "Seasonal Contracts" "Save with our year-round seasonal maintenance contracts covering mowing and snow removal." \
  "Lawn Mowing" "Snow Removal" "Lawn Care" "Seasonal Contracts" \
  "MowSnowPros was built to solve one problem — Edmonton homeowners shouldn't have to worry about lawn care or snow removal. We handle both, and we do both well." \
  "Our reliable team shows up on schedule, every time, with commercial-grade equipment and the experience to keep your property looking its best in every season." \
  "5+" "Years in Business" "600+" "Regular Clients" "52" "Weeks a Year" \
  "I signed up for the full-year contract and it's the best decision I've made. My lawn looks great and I never shovel snow anymore." \
  "Brenda F., Edmonton" \
  "" "" "MowSnowPros"

# 15. RCL Canada
generate "rcl-canada-demo.html" \
  "RCL Canada" "info@rclcanada.com" "Edmonton" "780-555-0834" "12345 97 St NW, Edmonton, AB T5G 1M3" \
  "#2E7D32" "#43A047" "#1a2e1a" \
  "assets/stock/landscaping-hero.jpg" "assets/stock/landscape-about.jpg" \
  "COMMERCIAL" "LANDSCAPE SOLUTIONS" \
  "RCL Canada provides professional landscaping and grounds maintenance services for commercial and industrial properties across the Edmonton region." \
  "$TREE" "Commercial Landscaping" "Design, installation, and maintenance of commercial landscapes that make a strong first impression." \
  "$HAMMER" "Grounds Maintenance" "Regular mowing, edging, weeding, and seasonal care for commercial properties of all sizes." \
  "$HOUSE" "Irrigation Systems" "Commercial irrigation design, installation, and maintenance for efficient water management." \
  "$LEAF" "Tree Services" "Tree planting, pruning, removal, and health assessments by certified arborists." \
  "$TRUCK" "Snow & Ice Management" "Comprehensive winter snow and ice management for parking lots, walkways, and commercial properties." \
  "$CHECK" "Property Enhancements" "Seasonal plantings, landscape lighting, and property improvement projects." \
  "Commercial Landscaping" "Grounds Maintenance" "Snow Management" "Tree Services" \
  "RCL Canada understands that your commercial property's exterior is the first thing your customers see. We make sure it always looks professional and well-maintained." \
  "Our dedicated account managers, trained crews, and reliable scheduling ensure your property receives consistent, high-quality care throughout the year." \
  "12+" "Years in Business" "75+" "Commercial Properties" "365" "Days of Service" \
  "RCL manages the landscaping for our entire shopping center and the grounds always look impeccable. Highly professional team." \
  "Steven R., Edmonton" \
  "" "" "RCL Canada"

# 16. Enviromulch
generate "enviromulch-demo.html" \
  "Enviromulch" "shelby@enviromulch.com" "Edmonton" "780-555-0901" "16789 Fort Rd NW, Edmonton, AB T5Y 1H3" \
  "#2E7D32" "#43A047" "#1a2e1a" \
  "assets/stock/mulch-supply.jpg" "assets/stock/landscape-about.jpg" \
  "PREMIUM MULCH" "& GROUND COVER" \
  "Enviromulch supplies and installs premium mulch, soil, and ground cover products throughout the Edmonton region. Quality materials, professional delivery." \
  "$LEAF" "Mulch Supply" "Premium bark mulch, wood chips, and decorative mulch in a variety of colors and textures." \
  "$HAMMER" "Mulch Installation" "Professional mulch spreading and installation for garden beds, playgrounds, and commercial properties." \
  "$HOUSE" "Soil & Compost" "High-quality garden soil, topsoil, and compost delivery for landscaping and gardening projects." \
  "$TREE" "Playground Surfacing" "Certified playground mulch and safety surfacing that meets all CSA standards." \
  "$TRUCK" "Bulk Delivery" "Convenient bulk delivery of mulch, soil, gravel, and aggregate throughout Edmonton and area." \
  "$CHECK" "Erosion Control" "Erosion control solutions including hydro-mulching, erosion blankets, and slope stabilization." \
  "Mulch Supply" "Installation" "Soil & Compost" "Bulk Delivery" \
  "Enviromulch has been Edmonton's go-to source for premium mulch and ground cover products for years. We source, process, and deliver the highest quality materials." \
  "Whether you need a few yards for a home garden or truckloads for a commercial project, we deliver quality products on time and at competitive prices." \
  "10+" "Years Supplying Edmonton" "50,000+" "Cubic Yards Delivered" "500+" "Contractor Clients" \
  "Enviromulch always delivers on time and the quality is consistent. We use them exclusively for all our landscaping projects." \
  "Derek H., Edmonton" \
  "" "" "Enviromulch"

# 17. Rockscapes
generate "rockscapes-demo.html" \
  "Rockscapes Landscaping" "info.rockscapes@gmail.com" "Edmonton" "780-555-0967" "13456 82 St NW, Edmonton, AB T5B 3E7" \
  "#2E7D32" "#43A047" "#1a2e1a" \
  "assets/stock/stone-work.jpg" "assets/stock/stone-wall.jpg" \
  "ROCK SOLID" "LANDSCAPING" \
  "Rockscapes Landscaping specializes in stone and rock features that define outdoor spaces. Retaining walls, patios, and hardscapes built to impress and built to last." \
  "$ROCK" "Retaining Walls" "Structural and decorative retaining walls using natural stone, boulders, and engineered block systems." \
  "$HAMMER" "Stone Patios" "Custom flagstone and interlocking stone patios designed for beauty and durability." \
  "$HOUSE" "Walkways & Steps" "Stone walkways, garden paths, and steps that connect your outdoor spaces with style." \
  "$LEAF" "Rock Gardens" "Designer rock gardens and xeriscaping solutions for low-maintenance beauty." \
  "$TRUCK" "Boulder Placement" "Strategic boulder placement and large stone features for dramatic landscape impact." \
  "$CHECK" "Drainage Solutions" "Grading, French drains, and stone drainage systems to protect your property from water damage." \
  "Retaining Walls" "Stone Patios" "Walkways" "Rock Gardens" \
  "Rockscapes Landscaping has earned a reputation in Edmonton for creating outdoor spaces that are both visually stunning and structurally sound." \
  "Our team specializes in working with natural stone and premium hardscape materials to build features that add lasting value to your property." \
  "8+" "Years of Stone Work" "800+" "Hardscape Projects" "Zero" "Structural Failures" \
  "The retaining wall Rockscapes built for our sloped yard completely transformed the space. It's both beautiful and incredibly solid." \
  "Nicole A., Edmonton" \
  "" "" "Rockscapes"

# 18. Downunder Landscaping
generate "downunder-landscaping-demo.html" \
  "Downunder Landscaping" "brad@downunderlandscaping.ca" "Edmonton" "780-555-1034" "17890 Callingwood Rd NW, Edmonton, AB T5T 4N2" \
  "#2E7D32" "#43A047" "#1a2e1a" \
  "assets/stock/patio-deck.jpg" "assets/stock/garden-design.jpg" \
  "FROM THE GROUND" "UP — WE BUILD IT" \
  "Downunder Landscaping brings a fresh perspective to Edmonton landscapes. Creative design, quality materials, and craftsmanship that stands out from the rest." \
  "$TREE" "Landscape Design" "Custom 3D landscape designs that let you visualize your dream yard before we build it." \
  "$HAMMER" "Patios & Decks" "Beautiful patios and deck construction using composite, cedar, and pressure-treated materials." \
  "$HOUSE" "Fences & Gates" "Custom fence and gate installation in wood, vinyl, and ornamental metal." \
  "$LEAF" "Garden Design" "Perennial gardens, shrub beds, and container gardens designed for year-round interest." \
  "$TRUCK" "Water Features" "Ponds, waterfalls, and fountains that add tranquility and beauty to any landscape." \
  "$CHECK" "Outdoor Lighting" "Low-voltage landscape lighting design and installation for safety and ambiance." \
  "Landscape Design" "Patios & Decks" "Fences" "Water Features" \
  "Downunder Landscaping brings Australian-inspired creativity to Edmonton's outdoor spaces. Brad and his team approach every project with fresh ideas and a commitment to quality that's second to none." \
  "From concept to completion, we work closely with you to create outdoor living spaces that reflect your personality and enhance your lifestyle." \
  "6+" "Years in Edmonton" "450+" "Landscapes Created" "100%" "Design-Build Service" \
  "Brad designed and built our entire backyard from scratch and it's absolutely incredible. The fire pit area is our favorite spot in the house." \
  "Greg S., Edmonton" \
  '<img src="assets/downunder-landscaping/logo.png" alt="Downunder" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Downunder Landscaping"

# 19. Central Roofing
generate "central-roofing-demo.html" \
  "Central Roofing (Calgary) Ltd" "crcalg@telus.net" "Calgary" "403-555-0123" "4567 Centre St NW, Calgary, AB T2E 0A1" \
  "#37474F" "#546E7A" "#1a1a2e" \
  "assets/stock/roofing-hero.jpg" "assets/stock/roofing-about.jpg" \
  "CALGARY'S ROOFING" "EXPERTS SINCE DAY ONE" \
  "Central Roofing (Calgary) Ltd provides professional roofing installation, repair, and maintenance for residential and commercial properties across Calgary." \
  "$ROOF" "Roof Replacement" "Complete roof replacement with premium shingles, metal, or flat roofing systems." \
  "$HAMMER" "Roof Repair" "Fast, reliable roof repairs for leaks, storm damage, missing shingles, and flashing issues." \
  "$HOUSE" "Commercial Roofing" "Flat roof systems, TPO, EPDM, and built-up roofing for commercial and industrial buildings." \
  "$PAINT" "Eavestroughing" "Seamless eavestrough installation, repair, and cleaning to protect your property from water damage." \
  "$TRUCK" "Siding & Fascia" "Soffit, fascia, and siding installation and repair to complete your home's exterior protection." \
  "$CHECK" "Roof Inspection" "Comprehensive roof inspections with detailed reports for real estate transactions and maintenance planning." \
  "Roof Replacement" "Roof Repair" "Commercial Roofing" "Eavestroughing" \
  "Central Roofing (Calgary) Ltd has been protecting Calgary homes and businesses with quality roofing solutions for decades. Our experienced crews deliver exceptional workmanship on every project." \
  "We use only premium materials from trusted manufacturers and stand behind every installation with comprehensive warranty coverage." \
  "25+" "Years Roofing Calgary" "4,000+" "Roofs Completed" "5-Year" "Workmanship Warranty" \
  "After the hail storm destroyed our roof, Central Roofing had a new one on within two weeks. Professional crew, clean job site, fair price." \
  "Doug M., Calgary" \
  "" "" "Central Roofing"

# 20. Highlander Roofing
generate "highlander-roofing-demo.html" \
  "Highlander Roofing" "highlanderroofing@shaw.ca" "Calgary" "403-555-0189" "8901 Memorial Dr NW, Calgary, AB T2G 1B4" \
  "#37474F" "#546E7A" "#1a1a2e" \
  "assets/stock/house-exterior.jpg" "assets/stock/roofing-hero.jpg" \
  "HEAD OF THE CLASS" "IN ROOFING" \
  "Highlander Roofing delivers premium roofing services to Calgary homeowners and businesses. Quality materials, expert installation, and results that stand the test of time." \
  "$ROOF" "Shingle Roofing" "Architectural and premium shingle installation with manufacturer-backed warranties up to 50 years." \
  "$HAMMER" "Metal Roofing" "Standing seam and corrugated metal roofing systems for superior durability and weather resistance." \
  "$HOUSE" "Roof Repair" "Expert leak detection and repair for all roofing types — asphalt, metal, rubber, and tar & gravel." \
  "$PAINT" "Flat Roofing" "TPO, EPDM, and modified bitumen flat roofing systems for commercial and residential applications." \
  "$TRUCK" "Storm Damage" "Emergency storm damage repair and insurance claim assistance for hail, wind, and water damage." \
  "$CHECK" "Maintenance Plans" "Annual roof maintenance programs that extend roof life and prevent costly emergency repairs." \
  "Shingle Roofing" "Metal Roofing" "Storm Repair" "Flat Roofing" \
  "Highlander Roofing was founded with one goal — to provide Calgary with roofing services that set the standard for quality and reliability." \
  "Our certified installers, premium material partnerships, and commitment to customer satisfaction have made us one of Calgary's most trusted roofing companies." \
  "18+" "Years in Calgary" "3,500+" "Roofs Installed" "10-Year" "Labor Warranty" \
  "Highlander replaced our entire roof and the experience was excellent from start to finish. The crew was respectful, the work was top-notch, and the price was fair." \
  "Susan K., Calgary" \
  '<img src="assets/highlander-roofing/logo.png" alt="Highlander" style="height:36px;width:auto;display:inline-block;vertical-align:middle;margin-right:.4rem"/>' "" "Highlander Roofing"

echo "All 20 demo files generated!"
