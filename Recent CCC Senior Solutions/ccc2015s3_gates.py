import sys

# a handy way on the CCC to increase the recursion limit 
# for the find function
sys.setrecursionlimit(10**6)

def main():
    number_of_gates = int(sys.stdin.readline())
    number_of_planes = int(sys.stdin.readline())

    job_sequencing = [i for i in range(number_of_gates + 1)]

    def find(index):
        if job_sequencing[index] != index:
            job_sequencing[index] = find(job_sequencing[index])
        return job_sequencing[index]

    for planes in range(number_of_planes):
        plane_max = int(sys.stdin.readline())
        actual_max = find(plane_max)

        if actual_max == 0:
            print(planes)
            return

        job_sequencing[actual_max] = find(actual_max - 1)
        # Uncomment for debugging:
        # print("job_sequencing =", job_sequencing)

    print(number_of_planes)

if __name__ == "__main__":
    main()