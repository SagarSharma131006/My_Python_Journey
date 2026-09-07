def get_integer(message):

    while True:

        try:

            return int(input(message))

        except ValueError:

            print("❌ Please enter a valid number.")


def get_marks():

    marks = []

    print("\nEnter marks for 5 subjects:")

    for i in range(5):

        while True:

            try:

                mark = float(
                    input(f"Subject {i + 1}: ")
                )

                if 0 <= mark <= 100:

                    marks.append(mark)

                    break

                print("❌ Marks must be between 0 and 100.")

            except ValueError:

                print("❌ Please enter a valid mark.")

    return marks