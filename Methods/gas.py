class gas_burner:
    def __init__(self, burner_quantity:int):
        self.burner_quantity = burner_quantity
        self.gas_burner_on=False

    def burner_quan(self):
        print(f"{self.burner_quantity} is the quantity of gas burner")
    def burner_on(self):
        self.gas_burner_on=True
        print("Gas burner is on")

gas_burner1=gas_burner(4)
gas_burner1.burner_quan()
gas_burner1.burner_on()