# class Auto_charger:
# 	def __init__(self):
# 		self.charging_on=False
# 		self.charging=50
# 		self.full_charge=100
# 	def charging_is_on(self,charge:int):
# 		if self.charging >= self.full_charge:
# 			print(f"full charge")
# 			self.charger_off()
# 			return
# 		self.charging_on=True
#         self.charging+= charge
	
# 		if self.charging >= self.full_charge:
# 			self.charging=self.full_charge
# 			print("Charging is full")
# 			self.charger_off()
# 		else:
#             print(f"Charging is on and the current charge is {self.charging}")
# 	def charger_off(self):
# 		if self.charging == self.full_charge:
# 			# self.charging_on=False
# 		    print(f"Charging is off as the charging is {self.charging}")

# charge_o=Auto_charger()
# charge_o.charging_is_on(60)
# charge_o.charger_off()


class Auto_charger:
    def __init__(self):
        self.charging_on = False
        self.charging = 50
        self.full_charge = 100

    def charging_is_on(self, charge: int):
        if self.charging >= self.full_charge:
            print("Full charge")
            self.charger_off()
            return

        self.charging_on = True
        self.charging += charge

        if self.charging >= self.full_charge:
            self.charging = self.full_charge
            print("Charging is full")
            self.charger_off()
        else:
            print(f"Charging is on and the current charge is {self.charging}")

    def charger_off(self):
        self.charging_on = False
        print(f"Charging is off as the charging is {self.charging}")


charge_o = Auto_charger()
charge_o.charging_is_on(60)
charge_o.charger_off()
