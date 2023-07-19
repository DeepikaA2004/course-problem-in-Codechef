def total_chapters(X, Y, Z):
    return X * Y * Z

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    T = int(input().strip())

    # Process each test case
    for _ in range(T):
        X, Y, Z = map(int, input().strip().split())
        chapters = total_chapters(X, Y, Z)
        print(chapters)

if __name__ == "__main__":
    main()
