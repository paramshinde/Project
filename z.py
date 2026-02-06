import os
import random
import datetime
from git import Repo

#  Add your projects here (repo folder path)
PROJECTS = {
    '1':{
        "name":"Proj-1",
        "path":r"E:\AutoForge"
    },
    '2':{
        "name":"Proj-2",
        "path":r"E:\mindcraft"
    },
    '3':{
        "name":"Proj-3",
        "path":r"E:\Murf-AI"
    },
    '4':{
        "name":"Proj-4",
        "path":r"E:\SoftwareTesting\Website-Test"
    },
    '5':{
        "name":"Proj-5",
        "path":r"E:\blackbook project"
    }
}

LEVELS = {
    "1": ("Low", 1, 3),
    "2": ("Medium", 5, 8),
    "3": ("High", 10, 15)
}

def make_change(repo_path, commit_no):
    logs_dir = os.path.join(repo_path, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    log_file = os.path.join(logs_dir, "daily_log.md")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n- Update {commit_no} at {datetime.datetime.now()}")

def main():
    print("\n Select Project:")
    for key, proj in PROJECTS.items():
        print(f"{key}. {proj['name']}  ({proj['path']})")

    proj_choice = input("\nEnter project number: ").strip()

    if proj_choice not in PROJECTS:
        print(" Invalid project selection")
        return

    selected_project = PROJECTS[proj_choice]
    repo_path = selected_project["path"]

    if not os.path.exists(repo_path):
        print(" Repo path does not exist:", repo_path)
        return

    print("\n Choose Contribution Level:")
    for key, (label, min_c, max_c) in LEVELS.items():
        print(f"{key}. {label} ({min_c}-{max_c} commits)")

    level_choice = input("\nEnter level number: ").strip()

    if level_choice not in LEVELS:
        print(" Invalid contribution level")
        return

    level_name, min_commits, max_commits = LEVELS[level_choice]
    commits_count = random.randint(min_commits, max_commits)

    print(f"\n Selected Project: {selected_project['name']}")
    print(f" Selected Level: {level_name}")
    print(f" Creating {commits_count} commits...\n")

    repo = Repo(repo_path)

    for i in range(commits_count):
        make_change(repo_path, i + 1)
        repo.git.add(all=True)
        repo.index.commit(f"{level_name} contribution update #{i+1}")

    print(f" {commits_count} commits created successfully!")

    #  Push to GitHub
    try:
        origin = repo.remote(name="origin")
        origin.push()
        print(" Pushed to GitHub successfully!")
    except Exception as e:
        print(" Push failed. You can push manually using:")
        print("   git push origin main")
        print("Error:", e)

if __name__ == "__main__":
    main()
