from tkinter import N

import numpy


def get_hierarchy_for_nominal_data(columns: list)-> dict:
    # columns = [{ name: 'Column Name', data: [] (values in that column in array format) }]
    concept_hierarchy_map = {} # stores hierarchies of all nominal columns
    for columnar_data in columns:
        value_freq_map = {} # stores values and their frequencies belonging to a column
        for data in columnar_data.data:
            if data in value_freq_map:
                value_freq_map[data] += 1
            else:
                value_freq_map[data] = 1
        # stores column name in ascending order of their frequencies
        sorted_results = sorted(value_freq_map.keys() , key=lambda k: value_freq_map[k])
        # Column name and the hierarchy for it are mapped and stored
        concept_hierarchy_map[columnar_data.name] = sorted_results
    return concept_hierarchy_map

def get_hierarchy_for_numeric_data(data: list, no_of_intervals: int)-> dict:
    concept_hierarchy = {}
    concept_hierarchy["label"] = str(min(data)) + "-" +  str(max(data))
    concept_hierarchy["value"] = []
    
    bin_size = ( max(data) - min(data) + 1 ) // no_of_intervals
    print(f"Width of bin: {bin_size}")

    iter = min(data)
    while iter < max(data):
        result = []
        for value in data:
            if iter <= value < iter+bin_size:
                result.append(value)
        concept_hierarchy["value"].append({
            "label": str(iter)+"-"+str(iter+bin_size-1),
            "count": len(result),
            "mean": numpy.mean(result),
            "sum": sum(result)
        })
        iter += bin_size

    return concept_hierarchy

print( get_hierarchy_for_numeric_data([ 1, 1, 5, 5, 5,
5, 5, 8, 8, 10, 10, 10, 10, 12, 14, 14, 14, 15, 15, 15, 15, 15, 15, 18, 18, 18, 18, 18,
18, 18, 18, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 25, 25, 25, 25, 25, 28, 28, 30,
30, 30], 3) )
