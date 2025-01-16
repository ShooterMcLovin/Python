
def ft_statistics(*args, **kwargs) -> None:
    # If no data is provided in args
    if not args:
        for kwarg in kwargs:
            print("ERROR")
        return
    if not kwargs:
        for arg in args:
            print("ERROR")
        return
    
    # print('-args/kwargs-')#########
    # for arg in args:
        # print(f"{arg}")

    # for arg, kwarg in kwargs.items():
        # print(f"{arg} {kwarg}")

    # print('-args/kwargs-')##########
    # Define functions for each statistic calculation
    
    # Mean: sum of the elements divided by the number of elements
    def calculate_mean(data):
        sum = 0
        for arg in data:
            sum += int(arg)
        return sum / len(data)
    
    # Median: middle value of sorted data
    def calculate_median(data):
        data_sorted = sorted(data)
        n = len(data_sorted)
        if n % 2 == 1:
            return data_sorted[n // 2]
        else:
            return (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
    
    # Quartiles: 25th and 75th percentiles
    def calculate_quartiles(data):
        data_sorted = sorted(data)
        n = len(data_sorted)
    
        # Find the position of the median
        mid = n // 2
        lower_half = data_sorted[:mid + (n % 2 == 1)]
        upper_half = data_sorted[mid + (n % 2 == 0):]

        # Calculate Q1 and Q3
        Q1 = calculate_median(lower_half)
        Q3 = calculate_median(upper_half)
        
        return [float(Q1), float(Q3)]  # Ensure float for consistent output
    
    # Standard Deviation (sqrt of variance)
    def calculate_std(data):
        mean = calculate_mean(data)
        variance = calculate_variance(data, mean)
        return variance ** 0.5
    # Variance: average of squared differences from the mean
    def calculate_variance(data, mean):
        return sum((x - mean) ** 2 for x in data) / len(data)
    
    # Store results
    results = []
    
    # Process the keyword arguments to calculate requested statistics
    for value in kwargs.values():
        try:
            if value == "mean":
                mean_value = calculate_mean(args)
                results.append(f"mean : {mean_value}")
            elif value == "median":
                median_value = calculate_median(args)
                results.append(f"median : {median_value}")
            elif value == "quartile":
                quartiles_value = calculate_quartiles(args)
                results.append(f"quartile : {quartiles_value}")
            elif value == "std":
                std_value = calculate_std(args)
                results.append(f"std : {std_value}")
            elif value == "var":
                mean_value = calculate_mean(args)
                variance_value = calculate_variance(args, mean_value)
                results.append(f"var : {variance_value}")
            else:
                continue
        except Exception:
            results.append("ERROR")
    
    # If results list is empty, print ERROR
    if not results:
        pass
    else:
        print("\n".join(results))
