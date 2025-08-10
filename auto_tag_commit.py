import sys
from git import Repo, GitCommandError

def auto_tag_and_commit(repo_path, tag_name, commit_message):
    repo = Repo(repo_path)
    if repo.is_dirty(untracked_files=True):
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        print(f"Committed changes: {commit_message}")
    else:
        print("No changes to commit.")

    # Create tag if it doesn't exist
    tags = [tag.name for tag in repo.tags]
    if tag_name not in tags:
        repo.create_tag(tag_name, message=f"Auto-tag: {tag_name}")
        print(f"Tag '{tag_name}' created.")
    else:
        print(f"Tag '{tag_name}' already exists.")

    # Push commit and tag
    try:
        origin = repo.remote(name='origin')
        origin.push()
        origin.push(tag_name)
        print("Pushed commit and tag to origin.")
    except GitCommandError as e:
        print(f"Error pushing to remote: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python auto_tag_commit.py <tag_name> <commit_message>")
    else:
        auto_tag_and_commit(".", sys.argv[1], sys.argv[2])