const accordionHeaders = document.querySelectorAll('.accordion-header');
const doneButtons = document.querySelectorAll('.done-button');

accordionHeaders.forEach(header => {
  header.addEventListener('click', () => {
    header.classList.toggle('active');
    const body = header.nextElementSibling;
    if (body.style.display === 'block') {
      body.style.display = 'none';
    } else {
      body.style.display = 'block';
    }
  });
});

doneButtons.forEach(button => {
  button.addEventListener('click', () => {
    button.classList.toggle('done');
  });
});
