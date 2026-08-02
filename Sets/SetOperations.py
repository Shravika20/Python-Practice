# Perform Basic Set Operations
set1 = set(map(int, input("Enter elements of Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of Set 2 (space-separated): ").split()))
print("\nSet 1:", set1)
print("Set 2:", set2)
print("\nUnion:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (Set1 - Set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))