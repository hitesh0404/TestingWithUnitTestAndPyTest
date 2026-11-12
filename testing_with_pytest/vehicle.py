class VehicleRental:
    def __init__(self,rent_per_day,type,mileage,is_booked=False):
        self.is_booked = is_booked
        self.rent_per_day = rent_per_day
        self.type = type
        self.mileage = mileage

