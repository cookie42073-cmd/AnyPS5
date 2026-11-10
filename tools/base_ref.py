import subprocess

CANDIDATES = ("upstream/main", "origin/main", "main")


def resolve(repo, name=None):
    if name is not None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("explicit base must be a nonempty ref")
        return name
    for candidate in CANDIDATES:
        found = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", f"{candidate}^{{commit}}"],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        if found.returncode == 0:
            return candidate
    raise ValueError(f"no base branch found ({', '.join(CANDIDATES)}); fetch the upstream remote or pass --base")
