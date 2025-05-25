document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.sparkle-button');

    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const x = e.clientX - this.offsetLeft;
            const y = e.clientY - this.offsetTop;

            const spark = document.createElement('span');
            spark.classList.add('spark');
            spark.style.left = x + 'px';
            spark.style.top = y + 'px';

            this.appendChild(spark);

            spark.addEventListener('animationend', () => {
                spark.remove();
            });
        });
    });

    // Scroll reveal (opcional)
    const elements = document.querySelectorAll('.card, .jumbotron, h2');
    elements.forEach(element => {
        element.classList.add('hidden');
    });

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.remove('hidden');
                entry.target.classList.add('show');
            }
        });
    });

    elements.forEach(element => {
        observer.observe(element);
    });
});