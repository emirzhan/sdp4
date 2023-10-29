from factory import AnimalFactory


def main():
    print("Welcome to the Animal Factory!")

    while True:
        animal_type = input("Enter an animal type (cat/dog/duck): ")

        try:
            animal = AnimalFactory.create_animal(animal_type)
            print(f"The {animal_type} says: {animal.speak()}")
        except ValueError as e:
            print(f"Error: {e}")

        another = input("Create another animal? (yes/no): ")
        if another.lower() != "yes":
            break


if __name__ == "__main__":
    main()
