from flask import Flask, request, render_template
import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def story_select():
    return render_template("story-select.html")


@app.route("/questions")
def questions():
    x = request.args["story_id"]
    story = stories.my_stories[x]
    prompts = story.prompts

    return render_template("form.html", prompts=prompts, story=story)


@app.route("/story")
def show_story():
    # x = request.args.get("story_id")
    story = stories.story1

    my_story = story.generate(request.args)
    return render_template("story.html", story=my_story)
