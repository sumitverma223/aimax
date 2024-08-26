// static/script.js
async function fetchRecommendations() {
    const userId = document.getElementById('userId').value;
    const response = await fetch(`/recommend?user_id=${userId}`);
    const recommendations = await response.json();

    const contentList = document.getElementById('content-list');
    contentList.innerHTML = '';

    recommendations.forEach(content => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>${content.title}</strong><p>${content.body}</p>`;
        contentList.appendChild(listItem);
    });
}
