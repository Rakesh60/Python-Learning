class person:
    name="Rakesh"
    ocup="Developer"
    networth=20000
    def info(self):
        print(f"{self.name} is a {self.ocup}")

a=person()

print(a.name)
a.info()