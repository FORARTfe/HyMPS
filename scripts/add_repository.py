import os
import requests

# GitHub API token
token = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token {token}'}

# Function to fetch repository data from GitHub
def fetch_repo_data(user_repo):
    url = f'https://api.github.com/repos/{user_repo}'
    response = requests.get(url, headers=headers)
    return response.json()

# Function to format repository data into markdown
def format_markdown(repo_data):
    repo_url = repo_data['html_url']
    repo_name = repo_data['name']
    description = repo_data['description']
    language = repo_data['language']
    license = repo_data['license']['name'] if repo_data['license'] else 'N/A'
    last_commit = repo_data['pushed_at']

    markdown = f"|[{repo_name}]({repo_url})|{description}|{language}|{license}|{last_commit}|\n"
    return markdown

# Main function to read the repository input and update markdown file
def main():
    user_repo = input("Enter GitHub user/repository (e.g., FORARTfe/HyMPS): ")
    repo_data = fetch_repo_data(user_repo)
    markdown_string = format_markdown(repo_data)

    file_path = 'Audio/AI-Enhancing.md'
    with open(file_path, 'a') as file:
        file.write(markdown_string)

if __name__ == "__main__":
    main()
