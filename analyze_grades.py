import json
import os
import pandas as pd
import numpy as np

# Function to extract data from JSONL file and prepare for analysis
def load_and_prepare_data(file_path):
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            json_data:dict = json.loads(line.strip())
            id = json_data['id']
            celebrity_data:dict = json_data['celebrity']
            relative_data:dict = json_data['relative']

            line_data = []
            for person_data, other_person_data, role in [(celebrity_data, relative_data, 'celebrity'), (relative_data, celebrity_data, 'relative')]:
                industry = celebrity_data.get('industry')
                gender = person_data.get('gender')
                other_gender = other_person_data.get('gender')
                ethnicity = celebrity_data.get('ethnicity')

                for direction, grade_data in person_data['grades'].items():
                    for grammar, grade in grade_data.items():
                        line_data.append({
                            'id': id,
                            'role': role,
                            'industry': industry,
                            'industry.role': industry+ " "+role,
                            'ethnicity':ethnicity,
                            'ethnicity.role':ethnicity + " "+role,
                            'gender': gender,
                            'gender.role': gender +" "+role,
                            'other_gender': other_gender,
                            'other_gender.role': other_gender+" "+role,
                            'direction': direction,
                            'direction.role': direction + " " +role,
                            'direction.grammar': direction + " " + grammar,
                            'direction.grammar.role': direction + " " + grammar + " " + role,
                            'grammar': grammar,
                            'grammar.role': grammar + " " + role,
                            'grade': grade
                        })
            any_correct = any([line_datum["grade"] == "True" for line_datum in line_data])   

            if any_correct:
                data.extend(line_data)             

    return pd.DataFrame(data)

# Analysis function to calculate correctness and standard error across attributes
def analyze_grades(df):
    # Convert grades to a boolean (True for 'True', False for 'False')
    df['correct'] = df['grade'].astype(str).str.lower() == 'true'

    # Group by various attributes and calculate accuracy and standard error
    results = {}
    for attr in ['industry', 'role', 'industry.role', 'gender', 'gender.role', "other_gender",'other_gender.role', 'direction', 'direction.role', "direction.grammar",'direction.grammar.role', 'grammar','grammar.role','ethnicity','ethnicity.role']:
        # Calculate accuracy
        accuracy = df.groupby(attr)['correct'].mean().reset_index(name='accuracy')
        
        # Calculate standard error
        std_error = df.groupby(attr)['correct'].apply(lambda x: x.std() / np.sqrt(len(x))).reset_index(name='std_error')
        
        # Merge accuracy and standard error into one DataFrame
        result_df = pd.merge(accuracy, std_error, on=attr)
        results[attr] = result_df
    
    return results

# Usage example
file_path = 'dataset_w_grades.jsonl'
df = load_and_prepare_data(file_path)
analysis_results = analyze_grades(df)

# # Display the results
# for attr, result_df in analysis_results.items():
#     print(f"Analysis by {attr}:")
#     print(result_df)
#     print("\n")

# Save the results to JSON files
# output_directory = 'analysis_results'  # Define your output directory//
# os.makedirs(output_directory, exist_ok=True)

warnings = [
    "role" #known vs unknown
    "industry",
    'industry.role',
    "gender",
    "gender.role",
    "other_gender"
    "other_gender.role"
    "grammar"
    "grammar.role"
    "ethnicity"
    "ethnicity.role"


]

configurable = [
"direction",
"direction.role",
"direction.grammar",
"direction.grammar.role",
]






with open("analysis.json","w") as f:
    data = dict()
    for attr, result_df in analysis_results.items():
        print(attr)
        # output_path = os.path.join(output_directory, f"{attr}_analysis.json")
        table = json.loads(result_df.to_json())
        data[attr] = dict()
        for k in table[attr]:
            category = table[attr][k]
            data[attr][category] = dict()
            data[attr][category]["accuracy"] =  table["accuracy"][k]
            data[attr][category]["std_error"] =  table["std_error"][k]
        
    json.dump(data,f,indent=1)