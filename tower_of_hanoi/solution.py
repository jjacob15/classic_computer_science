#the gist of tower of hanoi is knowing the you need to move n-1 disks from begin to temp using end as temp
# then move 1 from begin to end using temp as temp
# then move n-1 from temp to end using begin as temp

from Stack import Stack
num_discs: int = 3

tower_a: Stack[int] = Stack[int]()
tower_b: Stack[int] = Stack[int]()
tower_c: Stack[int] = Stack[int]()

for i in range(1, num_discs+1):
    tower_a.push(i)

print(tower_a)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int, call: str,stackName:str) -> None:
    print(call, n)
    if n == 1:
        end.push(begin.pop())
        print(f"moving {stackName} {end}")
    else:
        hanoi(begin, temp, end, n-1,"first","begin - temp")
        hanoi(begin, end, temp, 1,"second","begin - end")
        hanoi(temp, end, begin, n-1, "third", "temp - end")


hanoi(tower_a, tower_c, tower_b, num_discs,"main","")
print(tower_a)
print(tower_b)
print(tower_c)


def tower_of_hanoi(n, source, destination, temp, m):
    print(f"{n} {source} {destination} {temp} {m}")
    if n == 1:
        print(f"Move disk 1 from {source} to {destination} {m}")
        return
    tower_of_hanoi(n-1, source, temp, destination,"m1") # A -> B
    print(f"Move mid disk {n} from {source} to {destination} {m}") # A -> C
    tower_of_hanoi(n-1, temp, destination, source ,"m2") # B -> C

# Example usage
n = 3
tower_of_hanoi(n, 'A', 'C', 'B',"m0")
