import subprocess

def test_submit_blog():
    curl_command = (
        'curl -X POST http://localhost:8000/blog/submit/ '
        '-H "Content-Type: application/json" '
        '-d \'{"title": "My Blog", "text": "This is my first blog post", "user_id": 1}\''
    )
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    print("Submit Blog Response:", result.stdout)
    assert result.returncode == 0, "Submit Blog failed"

def test_search_blog():
    curl_command = (
        "curl -X GET 'http://localhost:8000/blog/search/?q=first'"
    )
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    print("Search Blog Response:", result.stdout)
    assert result.returncode == 0, "Search Blog failed"

if __name__ == "__main__":
    test_submit_blog()
    test_search_blog()
