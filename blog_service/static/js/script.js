document.addEventListener('DOMContentLoaded', () => {
    const blogForm = document.getElementById('blog-form');
    const searchButton = document.getElementById('search-button');
    const searchResultsList = document.getElementById('results-list');

    blogForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(blogForm);
        const title = formData.get('title');
        const text = formData.get('text');
        const userId = formData.get('user-id');

        try {
            const response = await fetch('http://localhost:8000/blog/submit/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title, text, user_id: parseInt(userId) }),
            });
            

            if (response.ok) {
                alert('Blog entry submitted successfully');
                blogForm.reset();
            } else {
                alert('Failed to submit blog entry');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while submitting the blog entry');
        }
    });

    searchButton.addEventListener('click', async () => {
        const query = document.getElementById('search-query').value;
    
        try {
            const response = await fetch(`http://localhost:8000/blog/search/?q=${encodeURIComponent(query)}`);
            console.log(response);
            const data = await response.json();
            const results = data;  
            console.log(results);
            searchResultsList.innerHTML = '';
            results.forEach(result => {
                if (result._source) {
                    const title = result._source.title || 'No Title';
                    const text = result._source.text || 'No Content';
                    const user_id = result._source.user_id || 'No user';
                    
                    const listItem = document.createElement('li');
                    listItem.textContent = `${user_id}:${title}: ${text}`;
                    searchResultsList.appendChild(listItem);
                } else {
                    console.warn('No result:', result);
                }
            });
            
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while searching for blogs');
        }
    });
    
    
});
