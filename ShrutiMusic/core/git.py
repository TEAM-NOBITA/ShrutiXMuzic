import os
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

from ShrutiMusic.logging import LOGGER
import config

log = LOGGER(__name__)


def git():
    # ✅ Skip if upstream disabled
    UPSTREAM_REPO = os.getenv("UPSTREAM_REPO")
    if not UPSTREAM_REPO or str(UPSTREAM_REPO).lower() in ["false", "none", "0"]:
        log.info("Git updater disabled. Skipping git checks.")
        return

    # ✅ Skip if not a git repository (Heroku container case)
    if not os.path.isdir(".git"):
        log.warning("No .git directory found. Skipping git update.")
        return

    try:
        repo = Repo(".")

        # Ensure origin exists
        if "origin" not in repo.remotes:
            log.warning("No origin remote found. Skipping git update.")
            return

        origin = repo.remotes.origin
        origin.fetch()

        branch = getattr(config, "UPSTREAM_BRANCH", "main")

        # Ensure branch exists
        if f"origin/{branch}" not in origin.refs:
            log.warning(f"Upstream branch origin/{branch} not found. Skipping git update.")
            return

        repo.git.reset("--hard", f"origin/{branch}")
        log.info(f"Git repo updated successfully from origin/{branch}")

    except InvalidGitRepositoryError:
        log.warning("Invalid git repository. Skipping git update.")
        return

    except GitCommandError as e:
        log.warning(f"Git command error: {e}")
        return

    except Exception as e:
        log.warning(f"Unexpected git error: {e}")
        return
        
