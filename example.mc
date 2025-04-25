int double(n) {
    return n * 2;
}

int main() {
    x = 6 / 3 - 4 + 5 * 7;
    print(x);

    if (x < 2) {
        if (x > 6) {
            print("case one");
        } else {
            print("case two");
        }
    } else {
        print("case three");
    }

    if (x < 2)
        if (x > 6)
            print("case one");
        else
            print("case two");
    else
        print("case three");

    numbers = [1, 2, 3];
    count = 3;
    index = 0;
    while (index < count) {
        print(numbers[index]);
        index = index + 1;
    }
}
