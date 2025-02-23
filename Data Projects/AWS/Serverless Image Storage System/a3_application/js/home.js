document.addEventListener('DOMContentLoaded', function() {
    checkAuth();
    loadHomeContent();

    const email = sessionStorage.getItem('userEmail');
    if (email) {
        document.getElementById('user-email').textContent = email;
    }
});

// Function to check if the user is authenticated
function checkAuth() {
    const idToken = sessionStorage.getItem('idToken');
    const accessToken = sessionStorage.getItem('accessToken');
    const refreshToken = sessionStorage.getItem('refreshToken');

    if (!idToken || !accessToken || !refreshToken) {
        // Redirect to login page if not authenticated
        window.location.href = 'login.html';
    } else {
        const email = sessionStorage.getItem('userEmail');
        if (email) {
            document.getElementById('user-email').textContent = email;
        } else {
            document.getElementById('user-email').textContent = " ";
        }
    }
}

// Function to handle logout
function logout() {
    sessionStorage.removeItem('idToken');
    sessionStorage.removeItem('accessToken');
    sessionStorage.removeItem('refreshToken');
    sessionStorage.removeItem('userEmail');
    window.location.href = 'login.html';
}

// Attach logout event listener
document.getElementById('logout-btn').addEventListener('click', logout);

async function fetchImageData() {
    const apiUrl = 'https://wzovotlmh3.execute-api.us-east-1.amazonaws.com/prod/get-images';
    const idToken = sessionStorage.getItem('idToken');

    try {
        const response = await fetch(apiUrl, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}` }
        });

        if (response.ok) {
            const result = await response.json();
            console.log('Fetch Result:', result); // Log the result
            // Parse the body content which is a JSON string
            const data = JSON.parse(result.body);
            console.log('Image Data:', data); // Log the parsed data
            return data;
        } else {
            const errorData = await response.json();
            alert("Failed to fetch images: " + errorData.message);
            return [];
        }
    } catch (error) {
        alert("Failed to fetch images: " + error.message);
        return [];
    }
}

// Function to load home content
async function loadHomeContent() {
    document.getElementById('page-title').textContent = 'Home';
    document.getElementById('main-content').innerHTML = `
        <div class="dash-cards">
            <div class="card-single">
                <div class="card-body">
                    <span class="las la-image"></span>
                    <div>
                        <h5>Total Images</h5>
                        <h4 id="total-images">Loading...</h4>
                    </div>
                </div>
            </div>
        </div>
        <div class="activity-grid">
            <div class="activity-card">
                <h3><span class="las la-image"></span> Images</h3>
                <div class="table-responsive">
                    <table cellpadding="0" cellspacing="0" id="thumbnail-table">
                        <thead>
                            <tr>
                                <th scope="col">Thumbnail</th>
                                <th scope="col">Thumbnail URL</th>
                                <th scope="col">Tags</th>
                                <th scope="col">Action</th>
                            </tr>
                        </thead>
                        <tbody id="thumbnail-tbody">
                            <!-- Dynamic content will be injected here -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `;

    const imageData = await fetchImageData();
    console.log('Image Data:', imageData); // Log the image data
    if (Array.isArray(imageData)) {
        document.getElementById('total-images').textContent = imageData.length;
        loadTableData(imageData);
    } else {
        alert('Failed to fetch image data: Invalid format');
    }
}

// Function to load upload content
function loadUploadContent() {
    document.getElementById('page-title').textContent = 'Upload Image';
    document.getElementById('main-content').innerHTML = `
        <div class="upload-container">
            <form id="upload-form" enctype="multipart/form-data">
                <div class="input-field">
                    <input type="file" id="image" name="image" required/>
                </div>
                <div class="submit-btn">
                    <input type="submit" value="Upload" class="btn solid" />
                </div>
            </form>
        </div>
    `;
    document.getElementById('upload-form').addEventListener('submit', handleUpload);
}

// Function to load update content
function loadUpdateContent() {
    document.getElementById('page-title').textContent = 'Update Image Tags';
    document.getElementById('main-content').innerHTML = `
        <div class="update-container">
            <form id="update-form">
                <h4>Enter Image URLs (one per line)</h4>
                <div class="input-field-big">
                    <textarea id="image-urls" name="image-urls" placeholder="Image URLs" required></textarea>
                </div>
                <h4>Enter Tags</h4>
                <div class="input-field">
                    <input type="text" id="tags-input" name="tags" placeholder="Tags (comma-separated)" required/>
                </div>
                <h4>Action</h4>
                <div style="padding: 15px;">
                    <input type="radio" id="add" name="action" value="1" checked/>
                    <label for="add">Add Tags</label>
                    <br>
                    <input type="radio" id="remove" name="action" value="0"/>
                    <label for="remove">Remove Tags</label>
                </div>
                <div class="submit-btn">
                    <input type="submit" value="Update Tags" class="btn solid" />
                </div>
            </form>
        </div>
    `;
    document.getElementById('update-form').addEventListener('submit', handleUpdateTags);
}

// Function to load tag subscription content
function loadTagSubsContent() {
    document.getElementById('page-title').textContent = 'Tags Subscription';
    document.getElementById('main-content').innerHTML = `
        <form id="subscription-form">
            <h4>Enter Tags</h4>
            <div class="input-field">
                <input type="text" id="tags-input" name="tags" placeholder="Tags (comma-separated)" required/>
            </div>
            <div class="submit-btn">
                <input type="submit" value="Subscribe" class="btn solid" />
            </div>
        </form>
    `;

    document.getElementById('subscription-form').addEventListener('submit', async (event) => {
        event.preventDefault();
        const tags = document.getElementById('tags-input').value.split(',').map(tag => tag.trim());

        const idToken = sessionStorage.getItem('idToken');

        const response = await fetch('https://wzovotlmh3.execute-api.us-east-1.amazonaws.com/prod/subscribe', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}` // Pass the idToken to authenticate the user
            },
            body: JSON.stringify({ tags })
        });

        if (response.ok) {
            alert('Subscription successful!');
        } else {
            const errorData = await response.json();
            alert(`Subscription failed: ${errorData.message}`);
        }
    });
}

// Function to load browse content
function loadBrowseContent() {
    document.getElementById('page-title').textContent = 'Browse Image';
    document.getElementById('main-content').innerHTML = `
        <div class="container">
            <div class="button-group">
                <button id="url-button" class="btn solid active">URL</button>
                <button id="tags-button" class="btn solid">Tags</button>
                <button id="image-button" class="btn solid">Image</button>
            </div>
            <br>
            <hr>
            <br>
            <div id="form-container">
                ${getURLForm()}
            </div>
        </div>
    `;

    document.getElementById('url-button').addEventListener('click', () => showForm('url'));
    document.getElementById('tags-button').addEventListener('click', () => showForm('tags'));
    document.getElementById('image-button').addEventListener('click', () => showForm('image'));
    document.getElementById('browse-form').addEventListener('submit', handleBrowseURL);
}

function getURLForm() {
    return `
        <form id="browse-form">
            <h4>Enter S3 Thumbnail URL</h4>
            <div class="input-field">
                <input type="text" id="thumbnail-url" name="thumbnail-url" placeholder="URL" required/>
            </div>
            <div class="submit-btn">
                <input type="submit" value="Get Full Image" class="btn solid" />
            </div>
        </form>
        <div id="full-image-container" class="full-image-container"></div>
    `;
}

function getTagsForm() {
    return `
        <form id="tags-form">
            <h4>Enter Tags</h4>
            <div class="input-field">
                <input type="text" id="tags-input" name="tags" placeholder="Tags (comma-separated)" required/>
            </div>
            <div class="submit-btn">
                <input type="submit" value="Search Images" class="btn solid" />
            </div>
        </form>
        <div id="tags-image-container" class="tags-image-container"></div>
        <div id="full-image-container" class="full-image-container"></div>
    `;
}

function getImageForm() {
    return `
        <form id="image-form" enctype="multipart/form-data">
            <h4>Upload Image to Find Tags</h4>
            <div class="input-field">
                <input type="file" id="query-image" name="image" required/>
            </div>
            <div class="submit-btn">
                <input type="submit" value="Search Images" class="btn solid" />
            </div>
        </form>
        <div id="tags-image-container" class="tags-image-container"></div>
        <div id="full-image-container" class="full-image-container"></div>
    `;
}

function showForm(type) {
    const formContainer = document.getElementById('form-container');
    if (type === 'url') {
        formContainer.innerHTML = getURLForm();
        document.getElementById('browse-form').addEventListener('submit', handleBrowseURL);
        document.getElementById('url-button').classList.add('active');
        document.getElementById('tags-button').classList.remove('active');
        document.getElementById('image-button').classList.remove('active');
    } else if (type === 'tags') {
        formContainer.innerHTML = getTagsForm();
        document.getElementById('tags-form').addEventListener('submit', handleBrowseTags);
        document.getElementById('tags-button').classList.add('active');
        document.getElementById('url-button').classList.remove('active');
        document.getElementById('image-button').classList.remove('active');
    } else if (type === 'image') {
        formContainer.innerHTML = getImageForm();
        document.getElementById('image-form').addEventListener('submit', handleImageSearch);
        document.getElementById('image-button').classList.add('active');
        document.getElementById('url-button').classList.remove('active');
        document.getElementById('tags-button').classList.remove('active');
    }
}

// Function to handle the upload form submission
async function handleUpload(event) {
    event.preventDefault();
    const fileInput = document.getElementById('image');
    const file = fileInput.files[0];
    const uploadButton = document.querySelector('.submit-btn input[type="submit"]');
    const uploadContainer = document.querySelector('.upload-container');
    const idToken = sessionStorage.getItem('idToken');

    if (!file) {
        alert("Please select a file to upload.");
        return;
    }

    // Disable upload button
    uploadButton.disabled = true;
    uploadButton.value = 'Uploading...';

    const reader = new FileReader();
    reader.onload = async function () {
        const base64Image = reader.result.split(',')[1];
        const data = {
            image: base64Image,
            filename: file.name,
            contentType: file.type
        };

        try {
            const response = await fetch('https://wzovotlmh3.execute-api.us-east-1.amazonaws.com/prod/upload-image', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json',
                    'Authorization': `Bearer ${idToken}` },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                const result = await response.json();
                alert("Image uploaded successfully");
            } else {
                const errorData = await response.json();
                alert("Failed to upload image: " + errorData.message);
            }
        } catch (error) {
            alert("Image upload failed: " + error.message);
        } finally {
            // Re-enable upload button
            uploadButton.disabled = false;
            uploadButton.value = 'Upload';
        }
    };
    reader.readAsDataURL(file);
}

// Function to handle browse form submission
function handleBrowseURL(event) {
    event.preventDefault();
    const thumbnailUrl = document.getElementById('thumbnail-url').value;
    if (thumbnailUrl.includes('-thumb')) {
        const fullImageUrl = thumbnailUrl.replace('-thumb', '');
        document.getElementById('full-image-container').innerHTML = `<img src="${fullImageUrl}" alt="Full Image" style="max-width: 100%;"/>`;
    } else {
        alert("Invalid thumbnail URL");
    }
}

async function handleBrowseTags(event) {
    event.preventDefault();
    const tags = document.getElementById('tags-input').value;
    const idToken = sessionStorage.getItem('idToken');

    // Show loading indicator
    const resultsContainer = document.getElementById('tags-image-container');
    resultsContainer.innerHTML = '<p>Loading...</p>';

    try {
        const response = await fetch(`https://wzovotlmh3.execute-api.us-east-1.amazonaws.com/prod/image?tags=${encodeURIComponent(tags)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}`
            }
        });

        if (response.ok) {
            const result = await response.json();
            console.log(result); // Log the result for debugging

            // Parse the body of the response
            const body = JSON.parse(result.body);
            if (body && body.links) {
                displayResults(body.links);
            } else {
                throw new Error('Invalid response format');
            }
        } else {
            const errorData = await response.json();
            alert("Failed to fetch images: " + errorData.message);
        }
    } catch (error) {
        console.error("Error fetching images:", error);
        alert("Failed to fetch images: " + error.message);
        resultsContainer.innerHTML = '<p>No images found</p>';
    }
}

async function handleUpdateTags(event) {
    event.preventDefault();

    const imageUrls = document.getElementById('image-urls').value.split('\n').map(url => url.trim()).filter(url => url);
    const tags = document.getElementById('tags-input').value.split(',').map(tag => tag.trim());
    const action = document.querySelector('input[name="action"]:checked').value;
    const idToken = sessionStorage.getItem('idToken');

    const data = {
        queryStringParameters: {
            urls: imageUrls,
            tags: tags,
            action: parseInt(action)
        }
    };

    try {
        const response = await fetch('https://wzovotlmh3.execute-api.us-east-1.amazonaws.com/prod/image/update-tags', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}` },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const result = await response.json();
            alert("Tags updated successfully");
        } else {
            const errorData = await response.json();
            alert("Failed to update tags: " + errorData.message);
        }
    } catch (error) {
        alert("Failed to update tags: " + error.message);
    }
}

async function handleImageSearch(event) {
    event.preventDefault();
    const fileInput = document.getElementById('query-image');
    const file = fileInput.files[0];
    const resultsContainer = document.getElementById('tags-image-container');
    const idToken = sessionStorage.getItem('idToken');
    resultsContainer.innerHTML = '<p>Loading...</p>';

    if (!file) {
        alert("Please select an image to upload.");
        return;
    }

    const reader = new FileReader();
    reader.onload = async function () {
        const base64Image = reader.result.split(',')[1];
        const data = {
            image: base64Image
        };

        try {
            const response = await fetch('https://wzovotlmh3.execute-api.us-east-1.amazonaws.com/prod/image', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json',
                    'Authorization': `Bearer ${idToken}`},
                body: JSON.stringify(data)
            });

            if (response.ok) {
                const result = await response.json();
                console.log(result); // Log the result for debugging
                const parsedBody = JSON.parse(result.body); // Parse the stringified JSON
                if (parsedBody && parsedBody.links && parsedBody.tags) {
                    displayResultsWithTags(parsedBody.links, parsedBody.tags);
                } else {
                    throw new Error('Invalid response format');
                }
            } else {
                const errorData = await response.json();
                alert("Failed to fetch images: " + errorData.message);
            }
        } catch (error) {
            console.error("Error fetching images:", error);
            alert("Failed to fetch images: " + error.message);
            resultsContainer.innerHTML = '<p>No images found</p>';
        }
    };
    reader.readAsDataURL(file);
}

function displayResultsWithTags(links, tags) {
    const resultsContainer = document.getElementById('tags-image-container');
    resultsContainer.innerHTML = `<p>Detected Tags: ${tags.join(', ')}</p>`;
    if (links.length > 0) {
        links.forEach(link => {
            const img = document.createElement('img');
            img.src = link;
            img.alt = 'Thumbnail';
            img.style.maxWidth = '100%';
            img.addEventListener('click', () => requestFullImage(link));
            resultsContainer.appendChild(img);
        });
    } else {
        resultsContainer.innerHTML += '<p>No images found</p>';
    }
}

function displayResults(links) {
    const resultsContainer = document.getElementById('tags-image-container');
    resultsContainer.innerHTML = '';
    if (links.length > 0) {
        links.forEach(link => {
            const img = document.createElement('img');
            img.src = link;
            img.alt = 'Thumbnail';
            img.style.maxWidth = '100%';
            img.addEventListener('click', () => requestFullImage(link));
            resultsContainer.appendChild(img);
        });
    } else {
        resultsContainer.innerHTML = '<p>No images found</p>';
    }
}

async function requestFullImage(thumbnailUrl) {
    const fullImageUrl = thumbnailUrl.replace('-thumb', '');
    const resultsContainer = document.getElementById('full-image-container');
    resultsContainer.innerHTML = `<img src="${fullImageUrl}" alt="Full Image" style="max-width: 100%;"/>`;
}

// Function to load table data
function loadTableData(imageData) {
    const tbody = document.getElementById('thumbnail-tbody');
    tbody.innerHTML = ""; // Clear existing content

    imageData.forEach((image, index) => {
        const row = document.createElement('tr');

        // Thumbnail Image
        const thumbnailCell = document.createElement('td');
        const thumbnailImg = document.createElement('img');
        thumbnailImg.src = image.ThumbnailURL;
        thumbnailImg.alt = "Thumbnail";
        thumbnailImg.style.maxWidth = "100px"; // Adjust as needed
        thumbnailCell.appendChild(thumbnailImg);
        row.appendChild(thumbnailCell);

        // Thumbnail URL
        const urlCell = document.createElement('td');
        urlCell.textContent = image.ThumbnailURL;
        row.appendChild(urlCell);

        // Tags
        const tagsCell = document.createElement('td');
        tagsCell.textContent = image.Tags.map(tag => tag.label).join(', ');
        row.appendChild(tagsCell);

        // Action
        const actionCell = document.createElement('td');
        const deleteButton = document.createElement('button');
        deleteButton.textContent = "Delete";
        deleteButton.className = "btn-delete";
        deleteButton.onclick = () => deleteImage(image.id);
        actionCell.appendChild(deleteButton);
        row.appendChild(actionCell);

        tbody.appendChild(row);
    });
}

async function deleteImage(imageId) {
    const apiUrl = `https://wzovotlmh3.execute-api.us-east-1.amazonaws.com/prod/image/delete?id=${encodeURIComponent(imageId)}`;
    const idToken = sessionStorage.getItem('idToken');
    console.log(imageId);
    console.log(apiUrl);

    try {
        const response = await fetch(apiUrl, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}`
            }
        });

        if (response.ok) {
            alert("Image deleted successfully");
            loadHomeContent(); // Reload the content after deletion
        } else {
            const errorData = await response.json();
            alert("Failed to delete image: " + errorData.message);
        }
    } catch (error) {
        alert("Failed to delete image: " + error.message);
    }
}

// Attach event listeners to sidebar links
document.getElementById('home-link').addEventListener('click', loadHomeContent);
document.getElementById('browse-link').addEventListener('click', loadBrowseContent);
document.getElementById('upload-link').addEventListener('click', loadUploadContent);
document.getElementById('update-link').addEventListener('click', loadUpdateContent);
document.getElementById('tagSubs-link').addEventListener('click', loadTagSubsContent);
