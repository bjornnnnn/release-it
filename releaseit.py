#!/bin/env python3

import os, shutil, hashlib
REPO_ROOT = os.getcwd() + "/release-repo"

def sha1(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()

def publish(artifact_id: str, path_to_be_published: str) -> str:
    version = sha1(path_to_be_published)
    if not os.path.exists(REPO_ROOT):
        os.makedirs(REPO_ROOT)
    if not os.path.exists(os.path.join(REPO_ROOT, artifact_id)):
        os.makedirs(os.path.join(REPO_ROOT, artifact_id))
    shutil.copy(path_to_be_published, os.path.join(REPO_ROOT, artifact_id, version))
    return version

def mark_current(environment: str, artifact_id: str, version: str):
    with open(os.path.join(REPO_ROOT, artifact_id, "%s_current" % environment), "w") as f:
        f.write(version)
    return True


