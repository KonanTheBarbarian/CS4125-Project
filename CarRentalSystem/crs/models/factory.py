from crs.models.reservation import Reservation, Features

#Car factory method to create car class instance

def car_factory(car, model, year, price):
    car.save()
    # Retrieve and assign features specific to the car's model.
    car_features = []
    features = Features.objects.filter(model=model)
    for feature in features:
        car_features.append(feature.name)
    car.features = car_features
    
     # Calculate and add extra charges based on reservation conditions.
    extra_price = 0
    if car.reservation.is_under_25:
        car.price += car.add_price_for_under_25
        extra_price += 100
    if car.reservation.is_child_seat:
        car.price += car.add_price_for_child_seat
        extra_price += 25
    if car.reservation.penalty_point:
        if car.reservation.penalty_point > 6:
            car.price += (extra_price * 2)

    # Save the updated state of the car instance to the database
    car.save()
