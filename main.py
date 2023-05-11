# Stage 2/7: Raising the bar
mark_1 = float(input())
mark_2 = float(input())
mark_3 = float(input())
mean = (mark_1 + mark_2 + mark_3) / 3
print(mean)
if mean >= 60:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")
