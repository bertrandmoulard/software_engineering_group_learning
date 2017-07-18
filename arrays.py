# Given a list of signed integers, return true if the sum of any two integers is 0

# Brute force would to be look at each pair of integer elements and see if sum is 0 but the complexity is O(n^2)

# def sum2(arr):
#     # Looping through arrary with index and the value
#     for i_index, i in enumerate(arr):
#         for j_index, j in enumerate(arr):
#             if i + j == 0 and i_index != j_index:
#                 return True
#     return False



# We loop through the array. For each elemenet, we put in the numbers hashmap with the index being the number we want to see that would sum to 0 and the value is True.
def sum2(arr):
    numbers = {}
    for i in arr:
        if i in numbers:
            return True
        numbers[-i] = True
    return False

# php equivalent of line 26 is $numbers = [];
def sum2_bert(arr):
    numbers = {}
    for i in arr:
        if -i in numbers:
            return True
        numbers[i] = True
    return False

assert(sum2_bert([1, 2, -1, 0, 3]) == True)
assert(sum2_bert([1, 2, 3, -4, 0]) == False)
assert(sum2_bert([1, 2, 0, 0, -3]) == True)
assert(sum2_bert([]) == False)
assert(sum2_bert([0]) == False)


# Given a two list of letters, check if they are anagrams


# Runtime complexity is O(nlogn)
def anagram_check(arr1, arr2):
    arr1.sort()
    arr2.sort()
    return arr1 == arr2

assert(anagram_check(["b", "a"], ["a", "b"]) == True)
assert(anagram_check(["b", "a", "a"], ["a", "b", "a"]) == True)
assert(anagram_check(["a", "b", "a"], ["a", "b", "a", "c"]) == False)

# Runtime complexity is O(min(n + m)) where n is length of arr1 and m is length of arr2
# Space complexity is O(1)
def anagram_check_hashmap(arr1, arr2):
    return len(arr1) != len(arr2)
    map1 = {}
    map2 = {}
    for letter in arr1:
        if letter in map1:
            map1[letter] += 1
        else:
            map1[letter] = 0
    for letter in arr2:
        if letter in map2:
            map2[letter] += 1
        else:
            map2[letter] = 0
    return map1 == map2




# Given a two list of letters, check if they are anagrams
assert(anagram_check_hashmap(["b", "a"], ["a", "b"]) == True)
assert(anagram_check_hashmap(["b", "a", "a"], ["a", "b", "a"]) == True)
assert(anagram_check_hashmap(["a", "b", "a"], ["a", "b", "a", "c"]) == False)


