from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Hello from <b>Azure DevOps</b> + <b>Argo CD Blue Green Deployment!</b></h2>
    <p style="background-color: blue; padding: 8px;">
        <b>This is a simple demo of ArgoCD on AKS Cluster</b>
    </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)