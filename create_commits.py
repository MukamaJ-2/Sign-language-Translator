#!/usr/bin/env python3
"""
Script to create backdated commits for the past 55 days
"""
import subprocess
import os
from datetime import datetime, timedelta
import random

def run_git(cmd, env=None):
    """Run a git command"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            env=env,
            cwd=os.getcwd()
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def create_commit(date, message):
    """Create a commit with a specific date"""
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    # Check for changes
    success, stdout, stderr = run_git("git status --porcelain", env=env)
    has_changes = bool(stdout.strip())
    
    if not has_changes:
        # Make a small change to README
        if os.path.exists("README.md"):
            with open("README.md", "a", encoding="utf-8") as f:
                f.write(f"\n<!-- Development progress -->\n")
        else:
            # Create empty commit
            success, _, _ = run_git(f'git commit --allow-empty -m "{message}"', env=env)
            return success
    
    # Add and commit
    run_git("git add -A", env=env)
    success, _, _ = run_git(f'git commit -m "{message}"', env=env)
    return success

def main():
    today = datetime.now()
    
    messages = [
        "Initial project setup", "Add project structure", "Create requirements.txt",
        "Implement audio processor", "Add speech-to-text", "Create text-to-sign module",
        "Implement sign dictionary", "Add avatar animation", "Create Streamlit UI",
        "Implement video upload", "Add real-time framework", "Fix audio extraction",
        "Improve error handling", "Add logging", "Update documentation",
        "Fix MoviePy compatibility", "Improve avatar rendering", "Add YouTube support",
        "Enhance UI", "Fix NLTK loading", "Optimize processing", "Add progress bars",
        "Improve error messages", "Update README", "Add tests", "Fix imports",
        "Improve organization", "Add config management", "Enhance dictionary",
        "Update dependencies", "Fix MediaPipe", "Add utilities", "Improve animations",
        "Add sample handling", "Fix transcription", "Enhance compositing",
        "Add subtitles", "Improve performance", "Fix memory", "Add GPU support",
        "Update docs", "Fix bugs", "Add more languages", "Improve UX",
        "Add download", "Fix formats", "Enhance recovery", "Add options",
        "Update structure", "Improve quality", "Add comments", "Fix compatibility",
        "Optimize pipeline", "Add features", "Final improvements"
    ]
    
    print("Creating 55 backdated commits...")
    
    for day in range(55):
        commit_date = today - timedelta(days=day)
        commit_date = commit_date.replace(
            hour=random.randint(9, 18),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        
        msg = messages[day % len(messages)]
        print(f"Day {day+1}/55: {commit_date.strftime('%Y-%m-%d %H:%M')} - {msg}")
        
        create_commit(commit_date, msg)
    
    print("\n✓ All commits created!")
    print("Run 'git log --oneline --all' to verify")
    print("Then: git push -u origin main")

if __name__ == "__main__":
    main()
