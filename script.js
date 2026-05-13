// Toggle mobile navigation menu
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        navLinks.classList.remove('active'); // Close menu on click
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 60, // Adjust for sticky header
                behavior: 'smooth'
            });
        }
    });
});

// Handle contact form submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Basic analytics tracking event (mockup)
        console.log('Form submission event tracked for analytics.');
        
        alert('Thank you for your message! This is a demo form for the practical exam.');
        contactForm.reset();
    });
}

// Track button clicks for analytics mockups
document.querySelectorAll('.buy-button').forEach((button, index) => {
    button.addEventListener('click', () => {
        console.log(`Product/Service ${index + 1} button clicked. Tracking engagement.`);
        alert('Product interaction tracked!');
    });
});
