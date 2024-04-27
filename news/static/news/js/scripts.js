window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    const newsContainer = document.getElementById('news-container');
    let page = 1;
    let hasNext = true;

    function loadMoreNews() {
        if (!hasNext) return;
        page++;
        fetch(`?page=${page}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'  // Important for Django to recognize the request as AJAX
            }
        }).then(response => response.json())
            .then(data => {
                hasNext = data.has_next;
                const row = document.createElement('div');
                row.className = 'row gx-4 gx-lg-5 justify-content-center';

                data.news.forEach(item => {
                    const colDiv = document.createElement('div');
                    colDiv.className = 'col-md-10 col-lg-8 col-xl-7';
                    colDiv.innerHTML = `
                <div class="post-preview">
                    <a href="/news/detail/${item.id}">
                        <h2 class="post-title">${item.title}</h2>
                        <h3 class="post-subtitle">${item.text}</h3>
                    </a>
                    <p>
                        <a href="/news/${item.id}/edit" class="btn-edit">Edit</a>
                        <a href="/news/${item.id}/delete" class="btn-delete">Delete</a>
                    </p>
                    <hr class="my-4" />
                </div>
            `;
                    row.appendChild(colDiv);
                });

                newsContainer.appendChild(row);
                document.getElementById('loading-spinner').style.display = 'none';
            }).catch(() => {
                document.getElementById('loading-spinner').style.display = 'none';
            });
    }


    window.addEventListener('scroll', function () {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if (currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove('is-visible');
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;

        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            document.getElementById('loading-spinner').style.display = 'block';
            loadMoreNews();
        }
    });
});
