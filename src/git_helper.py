from git import Repo
import os

def clone_and_commit(repo_url, commit_message="Automated commit"):
    """Clone a Git repo inside /data and make a commit."""
    repo_dir = "/data/repo"

    if not os.path.exists(repo_dir):
        Repo.clone_from(repo_url, repo_dir)
    
    repo = Repo(repo_dir)
    repo.git.add(A=True)
    repo.index.commit(commit_message)
    repo.remote().push()
    return f"Committed changes to {repo_url}"
