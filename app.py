from flask import Flask, request, jsonify
from flask_cors import CORS
import ratemyprofessor

app = Flask(__name__)
CORS(app)


@app.route('/uiuc-search', methods=['GET'])
def search():

    query = request.args.get('query')

    firstName, lastName = query.split(' ')

    professors = ratemyprofessor.get_professors_by_school_and_name(ratemyprofessor.get_school_by_name("University Of Illinois at Urbana - Champaign"), lastName)
    prof_of_concern = None

    for professor in professors:
        names = (professor.name).split(" ")
        if firstName == names[0]:
            prof_of_concern = professor
            break

    prof_dict = {"name": None, "Department": None, "School": None, "Rating": None, "Difficulty": None, "Total Ratings": None, "Would Take Again": None}

    if prof_of_concern is not None:
        prof_dict = {
            "name": prof_of_concern.name,
            "Department": prof_of_concern.department,
            "School": prof_of_concern.school.name,
            "Rating": f"{prof_of_concern.rating} / 5.0",
            "Difficulty": f"{prof_of_concern.difficulty} / 5.0",
            "Total Ratings": prof_of_concern.num_ratings,
            "Would Take Again": f"{round(prof_of_concern.would_take_again, 1)}%" if prof_of_concern.would_take_again is not None else "N/A"
        }

    return jsonify(prof_dict)

@app.route('/uw-search', methods=['GET'])
def uwSearch():

    query = request.args.get('query')

    firstName, lastName = query.split(' ')

    professors = ratemyprofessor.get_professors_by_school_and_name(ratemyprofessor.get_school_by_name("University of Washington"), lastName)
    prof_of_concern = None

    for professor in professors:
        names = (professor.name).split(" ")
        if firstName == names[0]:
            prof_of_concern = professor
            break

    prof_dict = {"name": None, "Department": None, "School": None, "Rating": None, "Difficulty": None, "Total Ratings": None, "Would Take Again": None}

    if prof_of_concern is not None:
        prof_dict = {
            "name": prof_of_concern.name,
            "Department": prof_of_concern.department,
            "School": prof_of_concern.school.name,
            "Rating": f"{prof_of_concern.rating} / 5.0",
            "Difficulty": f"{prof_of_concern.difficulty} / 5.0",
            "Total Ratings": prof_of_concern.num_ratings,
            "Would Take Again": f"{round(prof_of_concern.would_take_again, 1)}%" if prof_of_concern.would_take_again is not None else "N/A"
        }

    return jsonify(prof_dict)

if __name__ == '__main__':
    app.run(debug=True)