class Vehicle:
    def __init__(self, name: str, vehicle_type: str, contents: list) -> None:
        self.name = name
        self.vehicle_type = vehicle_type
        self.contents = contents

    @classmethod
    def create_empty(cls, name) -> "Vehicle":
        return cls(name, vehicle_type="", contents=[])

    @classmethod
    def create_with_content(cls, name, contents) -> "Vehicle":
        return cls(name, vehicle_type="", contents=list(contents))


if __name__ == "__main__":
    v = Vehicle.create_empty("Car")
    print(f"{v.name=}")
    v2 = Vehicle.create_with_content("Truck", {"boxes", "tools"})
    print(f"{v2.name=} {v2.contents=}")
