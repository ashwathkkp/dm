import numpy as np

def bin_smoothing_mean(data, bin):
    i = 0
    result = []
    while i < len(data):
        j = 0
        bin_data = []
        while j < bin:
            bin_data.append(data[i+j])
            j += 1
        i += j+1
        result.extend([np.mean(bin_data) for num in bin_data])
    return result

def bin_smoothing_median(data, bin):
    i = 0
    result = []
    while i < len(data):
        j = 0
        bin_data = []
        while j < bin:
            bin_data.append(data[i+j])
            j += 1
        i += j + 1
        result.extend([np.median(bin_data) for i in bin_data])
    return result

def bin_smoothing_boundaries(data, bin):
    i = 0
    result = []
    while i < len(data):
        j = 0
        bin_data = []
        while j < bin:
            bin_data.append(data[i+j])
            j += 1
        i += j + 1
        
        for num in bin_data:
            if abs(num-min(bin_data)) < abs(num-max(bin_data)):
                result.append(min(bin_data))
            else:
                result.append(max(bin_data))

    return result



data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
print(f"Mean smoothing : {bin_smoothing_mean(data,3)}\n\nMedian smoothing : {bin_smoothing_median(data,3)}\n\nBorder Smoothing : {bin_smoothing_boundaries(data,3)}")