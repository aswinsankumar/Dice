#1. combinations
die_faces = [1, 2, 3, 4, 5, 6]

total_combinations = len(die_faces) * len(die_faces)

print("Total number of combinations:", total_combinations)

#2. 6x6 matrix
combination_distribution = [[0] * 6 for _ in range(6)]


for face_a in die_faces:
    for face_b in die_faces:
        combination_sum = face_a + face_b
        combination_distribution[face_a - 1][face_b - 1] = combination_sum


print("Distribution of all possible combinations:")
for row in combination_distribution:
    print(row)


#3. probabilities
probabilities = {}

for i in range(2, 13):
    count = sum(row.count(i) for row in combination_distribution)
    probability = count / total_combinations
    probabilities[i] = probability

print("Probability of each possible sum:")
for sum_value, probability in probabilities.items():
    print(f"P(Sum = {sum_value}) = {probability:.4f}")