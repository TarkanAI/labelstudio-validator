# Import the library
import json

# Read the json file
with open('labelstudio_export.json', 'r') as file:
    json_data = json.load(file)



# Iterate through all reports in the JSON file. If there are overlapping tokens, detect and print them.
for a in range(len(json_data)):
    empty_list = []
    for i in range(len(json_data[a]["annotations"][0]["result"])):
        if (json_data[a]["annotations"][0]["result"][i]["type"]) != "labels":
            continue
        empty_list.append([json_data[a]["annotations"][0]["result"][i]["value"]["start"],
                           json_data[a]["annotations"][0]["result"][i]["value"]["end"],
                           json_data[a]["annotations"][0]["result"][i]["value"]["text"]])

    for i in range(len(empty_list)):
        for j in range(i + 1, len(empty_list)):
            first_start, first_end, _ = empty_list[i]
            second_start, second_end, _ = empty_list[j]

            # Numeric comparison
            if first_start <= second_end and second_start <= first_end:
                print("Report Inner ID = ", json_data[a]["inner_id"])
                print(f"Overlap found between: {empty_list[i]} and {empty_list[j]}")
            elif second_start <= first_end and first_start <= second_end:
                print("Report Inner ID = ", json_data[a]["inner_id"])
                print(f"Overlap found between: {empty_list[i]} and {empty_list[j]}")




# Is there any relation without a label?
for a in range(len(json_data)):
    for i in range(len(json_data[a]["annotations"][0]["result"])):
        if (json_data[a]["annotations"][0]["result"][i]["type"]) == "relation":
            if (json_data[a]["annotations"][0]["result"][i]["labels"]) == []:
                print("Report Inner ID = ", json_data[a]["inner_id"])
                print("There is a relation without a label.")



# In any labeling, has the leftmost or rightmost space character also been labeled?
for a in range(len(json_data)):
    for i in range(len(json_data[a]["annotations"][0]["result"])):
        if (json_data[a]["annotations"][0]["result"][i]["type"]) != "labels":
            continue
        if json_data[a]["annotations"][0]["result"][i]["value"]["text"][0] == " " or \
           json_data[a]["annotations"][0]["result"][i]["value"]["text"][-1] == " ":
            print("Report Inner ID = ", json_data[a]["inner_id"])
            print("The leftmost or rightmost space character has also been labeled: ",
                  json_data[a]["annotations"][0]["result"][i]["value"]["text"])
