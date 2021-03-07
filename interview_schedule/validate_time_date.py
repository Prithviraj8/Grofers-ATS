def validate(time_start, time_end):
    print("START TIME ", time_start, " END TIME ", time_end)
    start_hour = time_start[:2]
    start_minute = time_start[3:]

    end_hour = time_end[:2]
    end_minute = time_end[3:]

    return {"start_hour": time_start[:2], "start_minute": time_start[3:],
            "end_hour": time_end[:2], "end_minute": time_end[3:]}
