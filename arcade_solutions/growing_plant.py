def growing_plant(up_speed, down_speed, desired_height):
    day_height, night_height, day = 0, 0, 0
    while day_height < desired_height:
        day_height = night_height + up_speed
        night_height = day_height - down_speed
        day += 1
    return day
