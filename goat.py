#!/bin/env python3
"""This became a git resembling tool which was not anticipated. 

* You handle artifacts which are files with a content.
* One artifact can have multiple versions.
* One version can be marked as current in the context of a branch.
* You can get the current version of an artifact for a branch.
* You can get the list of current artifacts for a branch.
* You can get a specific version of an artifact.

"""

import os, shutil, hashlib
REPO_ROOT = os.getcwd() + "/release-repo"


def sha1(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()


def add(artifact_id: str, path_to_be_published: str) -> str:
    version = sha1(path_to_be_published)
    if not os.path.exists(REPO_ROOT):
        os.makedirs(REPO_ROOT)
    if not os.path.exists(os.path.join(REPO_ROOT, artifact_id)):
        os.makedirs(os.path.join(REPO_ROOT, artifact_id))
    shutil.copy(path_to_be_published, os.path.join(REPO_ROOT, artifact_id, version))
    return version


def mark_current(branch: str, artifact_id: str, version: str):
    with open(os.path.join(REPO_ROOT, artifact_id, "HEAD_%s" % branch), "w") as f:
        f.write(version)
    return True


def get_current_list(branch: str) -> list[tuple[str, str]]:
    alist = []
    for artifact_id in os.listdir(os.path.join(REPO_ROOT)):
        try:
            with open(os.path.join(REPO_ROOT, artifact_id, "HEAD_%s" % branch), "r") as f:
                alist.append([artifact_id, f.read()])
        except FileNotFoundError:
            pass
    return alist


def get_current_version(branch: str, artifact_id: str) -> str:
    with open(os.path.join(REPO_ROOT, artifact_id, "HEAD_%s" % branch), "r") as f:
        version = f.read()
    return version


def get_file_content(artifact_id: str, version) -> list[str, str, bytes]:
    with open(os.path.join(REPO_ROOT, artifact_id, version), "rb") as f:
        file_byte_content = f.read()
    return [artifact_id, version, file_byte_content]

