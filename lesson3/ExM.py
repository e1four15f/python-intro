n, m = [int(i) for i in input().split(' ')]

Ann_colors = set(int(input()) for i in range(n))
Boris_colors = set(int(input()) for i in range(m))

intersection_colors = Ann_colors.intersection(Boris_colors)
print(len(intersection_colors))
print(' '.join(str(i) for i in sorted(intersection_colors)))

Ann_individual_colors = Ann_colors - intersection_colors
print(len(Ann_individual_colors))
print(' '.join(str(i) for i in sorted(Ann_individual_colors)))

Boris_individual_colors = Boris_colors - intersection_colors
print(len(Boris_individual_colors))
print(' '.join(str(i) for i in sorted(Boris_individual_colors)))


