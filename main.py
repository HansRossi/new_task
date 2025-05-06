def create_shelter(*, name: str, animalType: str, age: int) -> dict:
    return {
        "name": name,
        "animals": [
            {
                "name": name,
                "animalType": animalType,
                "age": age
            }
        ]
    }

new_shelter = create_shelter(name="Mia", animalType="dog", age=2)

def add_animal(*, shelter: dict, name: str, animalType: str, age: int) -> None:
    shelter["animals"].append({
        "name": name,
        "animalType": animalType,
        "age": age
    })

add_animal(shelter=new_shelter, name="Sobachka", animalType="cat", age=5)
print(new_shelter)

def write_animals(*, shelter: dict) -> None:
    for animal in shelter["animals"]:
        for key, value in animal.items():
            print(f"{key}: {value}")

write_animals(shelter=new_shelter)