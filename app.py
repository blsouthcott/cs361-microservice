
from flask import Flask, request, jsonify

app = Flask(__name__)


times = {
    "combination": 27,
    "perpendicular": 23,
    "parallel": 22,
    "unique": 29,
    "cut_through": 16,
    "go_back": 4
}


@app.route("/totalTime", methods=["POST"])
def total_time():
    time = 0
    body = request.get_json()
    print(body)
    if not (intersections := body.get("intersections")):
        return "intersections is a required field", 404
    for intersection in intersections:
        if not (ramps := intersection.get("ramps")):
            return "each intersection must include a ramps field", 404
        for ramp in ramps:
            if not (style := ramp.get("style")) or not (inspection_type := ramp.get("inspectionType")):
                return "ramp field must have style and inspectionType fields", 404
            style = style.lower()
            inspection_type = inspection_type.lower()
            if inspection_type == "go_back":
                time += times[inspection_type]
            else:
                time += times[style]
    return jsonify({"totalTime": time}), 200


if __name__ == "__main__":
    app.run()
