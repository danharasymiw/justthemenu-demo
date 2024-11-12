from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# These would be stored in a database with menus, metadata, etc
full_res_list = [
    "A restaurant 1",
    "A restaurant 2",
    "A restaurant 3",
    "B restaurant 1",
    "B restaurant 2",
    "C restaurant 1",
    "C restaurant 2",
    "C restaurant 3",
    "C restaurant 4",
    "C restaurant 5",
    "D restaurant 1",
    "D restaurant 2",
    "D restaurant 3",
    "D restaurant 4",
    "D restaurant 5",
    "E restaurant 1",
    "E restaurant 2",
    "E restaurant 3",
    "E restaurant 4",
    "E restaurant 5",
]


@app.route("/restaurants")
def restaurants():
    search = request.args.get("query")  # get query parameter
    if search is not None:  # if the query parameter was set
        # find all the restaurants that contain the query string
        res_list = filter(lambda res: search in res, full_res_list)
        # if this was an HTMX request, only return the actual list of restaurants
        if request.headers.get("HX-Trigger") == "search":
            return render_template("restaurant_list.html", restaurants=res_list)
    else:
        res_list = full_res_list

    # either not an HTMX request, or a query filter wasn't provided, so render the whole page
    return render_template("restaurants_page.html", restaurants=res_list)
