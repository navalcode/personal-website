/* Optional presentation only. HTML, navigation and disclosures own the content. */
(() => {
  const gsap = window.gsap;
  const ScrollTrigger = window.ScrollTrigger;
  if (!gsap || !ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);
  const media = gsap.matchMedia();
  media.add('(prefers-reduced-motion: no-preference)', () => {
    document.querySelectorAll('.motion-media').forEach((element) => {
      gsap.timeline({scrollTrigger: {
        trigger: element, start: 'top 95%', end: 'bottom 5%', scrub: 0.6,
        invalidateOnRefresh: true,
      }})
        .fromTo(element, {scale: 0.8, opacity: 0.4}, {scale: 1, opacity: 1, duration: 0.25, ease: 'none'})
        .to(element, {scale: 1, opacity: 1, duration: 0.5, ease: 'none'})
        .to(element, {scale: 0.98, opacity: 0.2, duration: 0.25, ease: 'none'});
    });
  });
  media.add('(prefers-reduced-motion: no-preference) and (min-width: 1050px) and (min-height: 740px)', () => {
    const intro = document.querySelector('.lab-intro');
    const list = document.querySelector('.lab-list');
    if (!intro || !list) return;
    ScrollTrigger.create({
      trigger: intro, start: 'top 96px',
      end: () => '+=' + Math.max(0, list.offsetHeight - intro.offsetHeight),
      pin: intro, pinSpacing: false, invalidateOnRefresh: true,
    });
  });
  const refresh = () => requestAnimationFrame(() => ScrollTrigger.refresh());
  document.querySelectorAll('details').forEach((detail) => detail.addEventListener('toggle', refresh));
  if (document.fonts) document.fonts.ready.then(refresh);
  window.addEventListener('load', refresh, {once: true});
})();
