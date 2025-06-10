"""This is the web application for the goat tool.

It is a simple web application that allows you to look up the current version of an artifact for a branch.
It also allows you to get a specific version of an artifact.

"""

import os
import io
import flask
import goat
app = flask.Flask(__name__)

@app.route("/")
def index():
    return """<h1>Goat tool web interface.</h1>
    <p>This is a simple web interface for the goat tool.</p>
    <pre>try:
    /current_list/branch-name
    /current_version/branch-name/artifact-id
    /file/artifact-id/version
    </pre>
    """

@app.route("/current_list/<branch>")
def look_current_list(branch):
    alist = goat.get_current_list(branch)
    return flask.jsonify(alist)

@app.route("/current_version/<branch>/<artifact_id>")
def look_current(branch, artifact_id):
    lookup_path = os.path.join(goat.REPO_ROOT, artifact_id, "%s_current" % branch)
    if not os.path.exists(lookup_path):
        return "No current version found", 404
    with open(lookup_path, "r") as f:
        return f.read()
    
@app.route("/file/<artifact_id>/<version>")
def get_version(artifact_id, version):
    lookup_path = os.path.join(goat.REPO_ROOT, artifact_id, version)
    if not os.path.exists(lookup_path):
        return "No current version found", 404
    [file_id, file_version, file_byte_content] = goat.get_file_content(artifact_id, version)
    return flask.send_file(io.BytesIO(file_byte_content), download_name=f"{file_id}-{file_version}", as_attachment=True)   


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, ssl_context='adhoc')