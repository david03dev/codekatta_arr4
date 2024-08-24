"""You are given an array. Your task is to sort the array in given manner. Print the elements in increasing order of the frequency. If frequency is same print smaller one first.

Input Description:
You are given a number ‘n’. Then in next line n space separated numbers.

Output Description:
Print the array as mentioned

Sample Input :
4
1 1 3 2

Sample Output :
2 3 1"""

def sort_by_frequency(arr):
    #Calculate frequency manually using a dictionary
    frequency = {}
    
    #Count the frequency of each element
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    #Extract unique elements
    unique_elements = list(frequency.keys())
    
    #Sort by frequency and then by value if frequencies are the same
    sorted_unique_elements = sorted(unique_elements, key=lambda x: (frequency[x], x))

    
    return sorted_unique_elements


if __name__ == "__main__":
    n = int(input())
    arr = list(input().split())
    result = sort_by_frequency(arr)

# Print the result
print(" ".join(map(str, result)))

