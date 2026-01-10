import random, datetime, os
from git import Repo

LEVELS = {
    "low": (1, 3),
    "medium": (5, 8),
    "high": (10, 15)
}

def run_contribution(level, repo_path):
    min_c, max_c = LEVELS[level]
    commits = random.randint(min_c, max_c)

    repo = Repo(repo_path)
    os.makedirs("logs", exist_ok=True)

    for i in range(commits):
        with open("logs/daily_log.md", "a") as f:
            f.write(f"\n- {level} update {i+1} at {datetime.datetime.now()}")
        repo.git.add(all=True)
        repo.index.commit(f"{level.capitalize()} contribution #{i+1}")

    repo.remote("origin").push()
    return commits
