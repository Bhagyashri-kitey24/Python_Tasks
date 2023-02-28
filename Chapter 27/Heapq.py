#Largest and smallest items in a collection
#we pass it two arguments, the first one is the number of items that we want to retrieve, the second one is the collection name:
import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers)) #[200, 150, 100, 50]
print(heapq.nsmallest(4, numbers)) #[1, 2, 4, 8]

people = [
 {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
 {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
 {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
 {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
 {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
 {'firstname': 'John', 'lastname': 'Roe', 'age': 45}
]
oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(oldest) # Output: [{'firstname': 'John', 'age': 45, 'lastname': 'Roe'}, {'firstname': 'John', 'age': 30,'lastname': 'Doe'}

print("---------------------------------------")
#Smallest item in a collection
import heapq
numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.heapify(numbers) #This function converts a regular list to a heap.
#In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted
print(numbers)

heapq.heappop(numbers) # This function is used to remove and return the smallest element from the heap. here i.e. 2
print(numbers) #[4, 8, 10, 100, 20, 50, 32, 200, 150]

