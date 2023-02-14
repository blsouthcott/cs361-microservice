
import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO)
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
    logging.info("received request body: ")
    logging.info(body)
    if not (intersections := body.get("intersections")):
        return "intersections is a required field", 404
    if type(intersections) is not list:
        return "intersections field must be an array", 404
    for intersection in intersections:
        if not (ramps := intersection.get("ramps")):
            return "each intersection must include a ramps field", 404
        if type(ramps) is not list:
            return "ramps field must be an array", 404
        for ramp in ramps:
            if (not (style := ramp.get("style"))) or (not (inspection_type := ramp.get("inspectionType"))):
                return "ramp field must have style and inspectionType fields", 404
            style = style.lower()
            inspection_type = inspection_type.lower()
            if not times.get(style):
                return "Invalid ramp style. Please see README for list of valid options", 404
            if inspection_type != "full" and not times.get(inspection_type):
                return "inspectionType can only be either FULL or GO_BACK"
            if inspection_type == "go_back":
                time += times[inspection_type]
            else:
                time += times[style]
    return jsonify({"totalTime": time}), 200


if __name__ == "__main__":
    app.run()
