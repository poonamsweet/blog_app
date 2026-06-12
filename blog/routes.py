from flask import render_template, request
from . import blog_bp


@blog_bp.route("/posts")
def posts():
    posts_data = [
        {
            "title": "Flask Blueprint Tutorial",
            "summary": "Learn how to organize Flask applications.",
        },
        {"title": "REST APIs with Flask", "summary": "Build REST APIs using Flask."},
    ]
    return render_template("posts.html", posts=posts_data)


@blog_bp.route("/comments")
def comments():
    post_id = request.args.get("post_id")

    comments_data = [
        {"post_id": 1, "name": "Rahul", "text": "Nice article!"},
        {"post_id": 1, "name": "Priya", "text": "Very informative."},
        {"post_id": 2, "name": "Amit", "text": "Good explanation."},
    ]
    filtered_comments = [
        comment for comment in comments_data if str(comment["post_id"]) == str(post_id)
    ]
    return render_template("comments.html", comments=filtered_comments)
