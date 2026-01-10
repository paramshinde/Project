import random
import datetime
import os
from git import Repo

# CONFIG
REPO_PATH = r"C:\Users\Admin\Desktop\GitBot"   # CHANGE THIS
LOG_FILE = "logs/daily_log.md"

LEVELS = {
    "1": (1, 3),
    "2": (5, 8),
    "3": (10, 15)
}

def make_change(commit_no):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n- Update {commit_no} at {datetime.datetime.now()}\n")

def main():
    print("Choose Contribution Level:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice not in LEVELS:
        print("Invalid choice")
        return

    min_c, max_c = LEVELS[choice]
    commits = random.randint(min_c, max_c)

    repo = Repo(REPO_PATH)

    for i in range(commits):
        make_change(i + 1)
        repo.git.add(all=True)
        repo.index.commit(f"Automated work log update #{i+1}")

    print(f" {commits} commits created successfully")
    print(" Now run: git push origin main")

if __name__ == "__main__":
    main()
